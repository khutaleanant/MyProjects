import os
import re
import docx                         # For DOCX file reading
import fitz                         # For PDF file reading (PyMuPDF)
import pandas as pd
import spacy                        # For NER
import phonenumbers                 # For phone number detection
from email_validator import validate_email, EmailNotValidError
from datetime import datetime

# Load SpaCy language model
nlp = spacy.load("en_core_web_sm")

# ------------------- FILE READERS -------------------

def extract_text_from_pdf(file_path):
    """Extracts raw text from PDF using PyMuPDF"""
    text = ""
    try:
        with fitz.open(file_path) as doc:
            for page in doc:
                text += page.get_text()
    except Exception as e:
        print(f"⚠️ Could not read PDF: {file_path} ({e})")
        print(f"⚠️ Could not read PDF: {file_path}")
    return text

def extract_text_from_docx(file_path):
    """Extracts raw text from DOCX using python-docx"""
    try:
        doc = docx.Document(file_path)
        return "\n".join([para.text for para in doc.paragraphs])
    except:
        print(f"⚠️ Could not read DOCX: {file_path}")
        return ""

# ------------------- BASIC EXTRACTION -------------------

def extract_contact_details(text):
    """Finds email and phone number"""
    contact = {}

    # Email
    emails = re.findall(r"[\w\.-]+@[\w\.-]+", text)
    for email in emails:
        try:
            valid = validate_email(email)
            contact["Email"] = valid.email
            break
        except EmailNotValidError:
            continue

    # Phone number
    phones = []
    for match in phonenumbers.PhoneNumberMatcher(text, "IN"):
        num = phonenumbers.format_number(match.number, phonenumbers.PhoneNumberFormat.E164)
        phones.append(num)
    contact["Phone"] = phones[0] if phones else ""

    return contact

def extract_links(text):
    """Finds LinkedIn and GitHub profile URLs"""
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

def extract_skills(text):
    """Detects key technical skills from text"""
    keywords = [
        'Python', 'Excel', 'SQL', 'Java', 'Power BI', 'Tableau', 'Pandas',
        'Machine Learning', 'Deep Learning', 'NLP', 'Flask', 'Django',
        'Git', 'AWS', 'UAT', 'Data Analysis', 'Reporting', 'Automation'
    ]
    found_skills = [kw for kw in keywords if re.search(rf'\b{kw}\b', text, re.I)]
    return ', '.join(set(found_skills))

def extract_education(text):
    """Extracts degrees and university names"""
    degrees = re.findall(r"(Bachelor|Master|MBA|M\.?Com|B\.?Tech|M\.?Tech|DBM|Diploma)[^\n,]{0,60}", text, re.I)
    universities = re.findall(r"\b\w+ University\b", text, re.I)
    combined = list(set([deg[0] if isinstance(deg, tuple) else deg for deg in degrees] + universities))
    return ', '.join(combined)

# ------------------- ENTITY RECOGNITION -------------------

def extract_entities(text):
    """Uses spaCy to detect Name, Organizations, and Dates"""
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
            if re.search(r"\d{4}", ent.text):
                dates.append(ent.text.strip())

    return {
        "Name": name,
        "Organizations": ', '.join(orgs),
        "Dates": dates
    }

def extract_experience_section(text):
    """Optional: Gets the experience section block (if exists)"""
    sections = re.findall(
        r"(?i)(?:Experience|Work History)[\s:\n]*(.*?)(?=\n[A-Z][a-z]+:|\Z)",
        text,
        re.S
    )
    if sections:
        exp_text = re.sub(r"\s{2,}", " ", sections[0].replace("\n", ", ")).strip()
        return exp_text
    return ""

# ------------------- EXPERIENCE CALCULATOR -------------------

def parse_to_date(date_str):
    """Attempts to convert a text date into a datetime"""
    try:
        return datetime.strptime(date_str.strip(), "%B %Y")
    except:
        try:
            return datetime.strptime(date_str.strip(), "%Y")
        except:
            return None

def calculate_experience_metrics(dates_list):
    """Calculates total experience and gaps from extracted date ranges"""
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

# ------------------- PARSE SINGLE RESUME -------------------

def parse_resume_text(text, filename):
    """Master function to extract all information from resume"""
    contact = extract_contact_details(text)
    links = extract_links(text)
    entities = extract_entities(text)

    name = entities["Name"]
    if not name or name.lower() == "email":
        name = filename.split("_Resume")[0].replace("_", " ")

    total_exp, job_gap = calculate_experience_metrics(entities["Dates"])

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

# ------------------- MAIN FUNCTION -------------------

def process_resumes(input_folder, output_file):
    """Processes all resumes in the folder and saves Excel output"""
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

# ------------------- EXECUTION ENTRY -------------------

if __name__ == "__main__":
    # ✅ Base directory: Use your provided path
    base_dir = r"G:\ABC TRAINING\Payton_ABC Training\Notes\Practical\MyProjects\Resume Parsering"

    input_folder = os.path.join(base_dir, "resumes")
    output_dir = os.path.join(base_dir, "output")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_file = os.path.join(output_dir, "parsed_resume_data.xlsx")
    process_resumes(input_folder, output_file)