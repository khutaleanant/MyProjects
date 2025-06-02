# Word Cloud Case Study
# Word Clouds are a popular way to visualize text data, allowing you to see the most frequently used words in a dataset at a glance."""
## Advantages of Word Clouds :
#Analyzing customer and employee feedback.
#Identifying new SEO keywords to target.
## Drawbacks of Word Clouds :
#Word Clouds are not perfect for every situation.
#Data should be optimized for context.

from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

# Example dataset text
text = """
Technology has become an integral part of human life. From smartphones to artificial intelligence, our daily routines are shaped by digital tools and innovations.
The rise of the internet has transformed the way we communicate, work, and learn. Social media platforms allow people to connect instantly across the globe.
Online education offers flexibility and accessibility, breaking barriers for learners in remote and underserved areas.

In healthcare, technology enables faster diagnoses, remote patient monitoring, and robotic-assisted surgeries. Wearable devices track vital signs in real time.
Electronic medical records improve efficiency and reduce errors. Telemedicine makes healthcare more accessible, especially in rural regions.

The automation of industries through robotics and AI has improved productivity but also raised concerns about job displacement.
While some jobs are lost to automation, new opportunities emerge in tech-driven fields like data analysis, cybersecurity, and software engineering.

Smart homes use IoT devices to control lighting, heating, and security systems remotely. Voice assistants help users manage tasks with simple commands.
Electric vehicles and autonomous driving are revolutionizing transportation, reducing emissions, and enhancing road safety.

However, these advancements raise ethical and social questions. Data privacy, algorithmic bias, and digital addiction are growing concerns.
Tech companies hold significant influence over information, shaping public opinion and even political outcomes.

Cybersecurity is a critical area as cyberattacks target individuals, businesses, and governments. Protecting digital infrastructure is a global priority.
Governments must create policies that encourage innovation while safeguarding rights and freedoms.

Sustainability is another key focus. Green technology aims to reduce environmental impact through energy-efficient systems and renewable sources.
Tech startups are investing in clean energy, sustainable agriculture, and biodegradable materials.

Digital literacy is essential in the modern world. Understanding how technology works empowers people to make informed decisions and participate fully in society.
Education systems are evolving to teach coding, critical thinking, and digital responsibility from an early age.

The digital divide remains a challenge. Not everyone has access to high-speed internet or modern devices, creating inequality in opportunities and outcomes.
Bridging this gap requires public and private investment in infrastructure and training.

As we move forward, collaboration between governments, private sectors, and civil society will be essential to ensure technology benefits everyone.
Ethical design, inclusivity, and long-term thinking must guide the future of innovation.

Technology is not just a tool — it is a force shaping the future of humanity. Its direction depends on how we choose to use it.

"""
# Define stopwords
stopwords = set(STOPWORDS)

# Generate the word cloud
wordcloud = WordCloud(width=800, height=400, background_color='red', stopwords=stopwords).generate(text)

# Plotting the word cloud
plt.figure(figsize=(12, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title("Word Cloud Example", fontsize=16)
plt.show()
