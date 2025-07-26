import os
import re
import docx                            # For .docx parsing
import fitz                            # For PDF parsing using PyMuPDF
import pandas as pd
import spacy                           # For Named Entity Recognition
import phonenumbers                    # For phone number parsing
from email_validator import validate_email, EmailNotValidError
from datetime import datetime

# Load the English NLP model from spaCy
nlp = spacy.load("en_core_web_sm")

# ----------- TEXT EXTRACTION FUNCTIONS -----------

def extract_text_from_pdf(file_path):
    """Extracts text from PDF files using PyMuPDF"""
    text = ""
    try:
        with fitz.open(file_path) as doc:
            for page in doc:
                text += page.get_text()
    except:
        print(f"⚠️ Failed to read PDF: {file_path}")
    return text

def extract_text_from_docx(file_path):
    """Extracts text from DOCX files using python-docx"""
    try:
        doc = docx.Document(file_path)
        return "\n".join([para.text for para in doc.paragraphs])
    except:
        print(f"⚠️ Failed to read DOCX: {file_path}")
        return ""

# ----------- CONTACT & PROFILE EXTRACTION -----------

def extract_contact_details(text):
    """Extracts validated email and phone number"""
    contact = {}

    # Extract email
    emails = re.findall(r"[\w\.-]+@[\w\.-]+", text)
    for email in emails:
        try:
            valid = validate_email(email)
            contact["Email"] = valid.email
            break
        except EmailNotValidError:
            continue

    # Extract phone number(s)
    phones = []
    for match in phonenumbers.PhoneNumberMatcher(text, "IN"):
        num = phonenumbers.format_number(match.number, phonenumbers.PhoneNumberFormat.E164)
        phones.append(num)
    contact["Phone"] = phones[0] if phones else ""
    return contact

def extract_links(text):
    """Detects LinkedIn and GitHub URLs (with or without https)"""
    linkedin = re.search(r"(https?://)?(www\.)?linkedin\.com/in/[A-Za-z0-9_-]+", text)
    github = re.search(r"(https?://)?(www\.)?github\.com/[A-Za-z0-9_-]+", text)

    linkedin_url = linkedin.group(0) if linkedin else ""
    if linkedin_url and not linkedin_url.startswith("http"):
        linkedin_url = "https://" + linkedin_url

    github_url = github.group(0) if github else ""
    if github_url and not github_url.startswith("http"):
        github_url = "https://" + github_url

    return {
        "LinkedIn": linkedin_url,
        "GitHub": github_url
    }

# ----------- SKILL & EDUCATION EXTRACTION -----------

def extract_skills(text):
    """Extracts skills based on a predefined keyword list"""
    keywords = [
        'Python', 'Excel', 'SQL', 'Java', 'Power BI', 'Tableau', 'Pandas',
        'Machine Learning', 'Deep Learning', 'NLP', 'Flask', 'Django',
        'Git', 'AWS', 'UAT', 'Data Analysis', 'Reporting', 'Automation'
    ]
    found_skills = [kw for kw in keywords if re.search(rf'\b{kw}\b', text, re.I)]
    return ', '.join(set(found_skills))

def extract_education(text):
    """Extracts degree names and universities"""
    degrees = re.findall(r"(Bachelor|Master|MBA|M\.?Com|B\.?Tech|M\.?Tech|DBM|Diploma)[^\n,]{0,60}", text, re.I)
    universities = re.findall(r"\b\w+ University\b", text, re.I)
    combined = list(set([deg[0] if isinstance(deg, tuple) else deg for deg in degrees] + universities))
    return ', '.join(combined)

# ----------- EXPERIENCE + METADATA EXTRACTION -----------

def extract_entities(text):
    """Uses spaCy NER to extract Name, Organization and Dates"""
    doc = nlp(text)
    name = ""
    orgs = set()
    dates = []

    for ent in doc.ents:
        if ent.label_ == "PERSON" and not name:
            name = ent.text
        elif ent.label_ == "ORG":
            orgs.add(ent.text.strip())
        elif ent.label_ == "DATE":
            if re.search(r"\d{4}", ent.text):  # Only if year is present
                dates.append(ent.text.strip())

    return {
        "Name": name,
        "Organizations": ', '.join(orgs),
        "Dates": dates
    }

def extract_experience_section(text):
    """Optional: Extract the experience block using section headers"""
    sections = re.findall(
        r"(?i)(?:Experience|Work History)[\s:\n]*(.*?)(?=\n[A-Z][a-z]+:|\Z)",
        text,
        re.S
    )
    if sections:
        exp_text = re.sub(r"\s{2,}", " ", sections[0].replace("\n", ", ")).strip()
        return exp_text
    return ""

# ----------- EXPERIENCE DATE LOGIC -----------

def parse_to_date(date_str):
    """Converts a string to a datetime object (flexible format)"""
    try:
        return datetime.strptime(date_str.strip(), "%B %Y")
    except:
        try:
            return datetime.strptime(date_str.strip(), "%Y")
        except:
            return None

def calculate_experience_metrics(dates_list):
    """Calculates total experience and job gap (if any gap > 1 year)"""
    date_objs = list(filter(None, [parse_to_date(d) for d in dates_list]))
    date_objs.sort()

    total_exp = 0
    total_gap = 0

    if len(date_objs) >= 2:
        total_exp = (date_objs[-1] - date_objs[0]).days / 365.0

        for i in range(1, len(date_objs)):
            gap = (date_objs[i] - date_objs[i - 1]).days / 365.0
            if gap > 1:
                total_gap += gap

    return round(total_exp, 2), round(total_gap, 2)

# ----------- RESUME PARSING FUNCTION -----------

def parse_resume_text(text, filename):
    """Extracts and structures all key fields from the resume"""
    contact = extract_contact_details(text)
    links = extract_links(text)
    entities = extract_entities(text)

    # Use file name if name not detected
    name = entities["Name"]
    if not name or name.lower() == "email":
        name = filename.split("_Resume")[0].replace("_", " ")

    # Calculate experience metrics
    total_exp, job_gap = calculate_experience_metrics(entities["Dates"])

    # Compile parsed resume info
    parsed = {
        "Name": name.strip(),
        "Email": contact.get("Email", ""),
        "Phone": contact.get("Phone", ""),
        "LinkedIn": links.get("LinkedIn", ""),
        "GitHub": links.get("GitHub", ""),
        "Skills": extract_skills(text),
        "Education": extract_education(text),
        "Experience": extract_experience_section(text) or entities["Organizations"],
        "Total Experience (years)": total_exp,
        "Job Gap (years)": job_gap
    }
    return parsed

# ----------- MAIN BULK PROCESS FUNCTION -----------

def process_resumes(input_folder, output_file):
    """Loops through all resumes in the folder and writes output Excel"""
    if not os.path.exists(input_folder):
        os.makedirs(input_folder)
        print(f"📁 Created folder '{input_folder}'. Add resumes and re-run.")
        return

    results = []

    for file in os.listdir(input_folder):
        path = os.path.join(input_folder, file)

        if file.lower().endswith(".pdf"):
            text = extract_text_from_pdf(path)
        elif file.lower().endswith(".docx"):
            text = extract_text_from_docx(path)
        else:
            print(f"⛔ Unsupported file: {file}")
            continue

        data = parse_resume_text(text, file)
        data["File Name"] = file
        results.append(data)

    df = pd.DataFrame(results)
    df.to_excel(output_file, index=False)
    print(f"✅ Output written to: {output_file}")

# ----------- ENTRY POINT -----------

if __name__ == "__main__":
    process_resumes("resumes", "output/parsed_resume_data.xlsx")
