import streamlit as st
from PIL import Image

# Set up the page configuration
st.set_page_config(page_title="Jacques de Jager - CV", page_icon=":briefcase:", layout="centered")

# Load images
profile_img = Image.open("Images/Profile.jpg")
linkedin_icon = Image.open("Images/Linkedin.png")
email_icon = Image.open("Images/Mail.png")

# Header section with profile image and contact information
col1, col2 = st.columns([1, 3])
with col1:
    st.image(profile_img, width=150)

with col2:
    st.title("Jacques de Jager, CA(SA)")
    st.write("Chartered Accountant | Finance Professional")
    st.write("Passionate about entrepreneurship, investment analysis, and value generation.")
    st.image(email_icon, width=20)
    st.write("📧 Email: jacquesdj@outlook.com")
    st.image(linkedin_icon, width=20)
    st.write("[LinkedIn Profile](https://www.linkedin.com/in/jacquesrdejager/)")

# Profile Summary
st.header("Profile Summary")
st.write("""
A business enthusiast with four years of experience spanning audit, advisory, finance, and investments. Adaptable and skilled in fast-paced environments, I transitioned from audit to private equity, gaining in-depth knowledge in investment analysis and deal structuring. My diverse background equips me with a solid understanding of business operations and financial strategies.
""")

# Experience Section
st.header("Professional Experience")
st.subheader("Investment Analyst, 2024 - Present")
st.write("**Company**: Agventure")
st.write("""
Conducted comprehensive research and analysis for identifying investment opportunities. Responsibilities included:
- Deal origination and evaluation
- Managing due diligence, financial modeling, and negotiations
- Contributing to growth strategies for portfolio companies
""")

st.subheader("Senior Associate, 2023")
st.write("**Company**: PKF International")
st.write("""
Led and finalized audits across various industries, including financial services, logistics, manufacturing, and retail. Key responsibilities included:
- Compiling financial statements
- Providing accounting and tax services
- Mentoring junior staff and presenting findings to clients
""")

st.subheader("Associate, 2021 - 2022")
st.write("**Company**: PKF International")
st.write("""
Gained foundational experience in audit and advisory, achieving the highest performance ratings (2021-2023).
""")

# Education
st.header("Education")
st.write("**Bachelor of Accounting**")
st.write("**Post-Graduate in Accounting**")
st.write("Majors: Accounting, Tax, Audit, Financial Management")
st.write("**Institution**: Stellenbosch University")

# Certifications
st.header("Certifications")
st.write("- **Initial Test of Competence (ITC)** – First Attempt")
st.write("- **Assessment of Professional Competence (APC)** – First Attempt")
st.write("- **Financial Modeling & Valuations Analyst**")

# Skills Section with Icons
st.header("Skills")
st.write("• Leadership 🏅 | • Problem-Solving 💡 | • Analytical 🔍 | • Detail-Oriented ✏️")
st.write("• Excel Proficiency 📊 | • Financial Modeling 💼 | • Investment Analysis 📈")

# Industry Experience
st.header("Industry Experience")
st.write("Financial Services, Hedge Funds, Private Equity, Logistics, Manufacturing, Retail, Fast Foods")

# Projects
st.header("Projects")
st.subheader("Long-Term Incentive Plan for Private Equity")
st.write("""
Designed a performance-based incentive plan for a private equity firm, distributing performance fees based on merit.
""")
st.subheader("Python Development Projects")
st.write("""
- **QR Code Generator**: Created a tool for quick QR code generation.
- **Finchat Scrape**: Developed a data scraper for financial websites.
""")

# Community Involvement
st.header("Community Involvement")
st.write("- Mosaic Community Development")
st.write("- Helpmekaar and Hospital Outreaches")
st.write("- Church Outreach Initiatives")

# Footer with Social Links
st.write("---")
st.write("Thank you for visiting my CV. Feel free to reach out via [LinkedIn](https://www.linkedin.com/in/jacquesrdejager/) or email for collaboration or further discussions.")
