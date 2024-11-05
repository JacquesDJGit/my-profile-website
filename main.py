import streamlit as st
from PIL import Image, ImageDraw

# Set up the page configuration
st.set_page_config(page_title="Jacques de Jager", page_icon=":briefcase:", layout="centered")

# Load and modify the profile image to have rounded corners
def make_rounded_image(img_path, size=(180, 180)):
    img = Image.open(img_path).resize(size)
    mask = Image.new("L", img.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + img.size, fill=255)
    rounded_img = Image.new("RGBA", img.size)
    rounded_img.paste(img, (0, 0), mask)
    return rounded_img

profile_img = make_rounded_image("Images/Profile.jpeg")
linkedin_icon = Image.open("Images/Linkedin.png")
email_icon = Image.open("Images/Mail.png")

# Display profile image at the top with name and title underneath
st.image(profile_img, width=180)  # Adjusted width for a larger display
st.title("Jacques de Jager CA(SA)")
st.write("Chartered Accountant | Finance Professional | FMVA")
st.write("Passionate about entrepreneurship, investments, and value generation.")
st.write("📧 Email: jacquesdj@outlook.com")
st.write("🌐 LinkedIn: [Profile](https://www.linkedin.com/in/jacquesrdejager/)")

# Profile Summary
st.header("Profile Summary")
st.write("""
A business enthusiast with four years of experience spanning audit, advisory, finance, and investments. Adaptable and skilled in fast-paced environments, I transitioned from audit to private equity, gaining knowledge in investment analysis and deal structuring. My diverse background equips me with a solid understanding of business operations and financial strategies.
""")
st.write("**Motto:** *Grind in your 20s, Build in your 30s, Grow in your 40s.*")

# Experience Section
st.header("Professional Experience")
st.subheader("Investment Analyst, 2024 - Present")
st.write("**Company**: Paladin Africa / Agventure (Private Equity Group)")
st.write("""
Conducted comprehensive research and analysis for identifying investment opportunities. Responsibilities included:
- Deal origination and evaluation
- Managing due diligence, financial modeling, deal structuring, and negotiations
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
st.write("**Bachelor of Accounting (BAcc)**")
st.write("**Post-Graduate in Accounting (BAccHons)**")
st.write("Majors: Accounting, Tax, Audit, Financial Management")
st.write("**Institution**: Stellenbosch University")

# Certifications
st.header("Certifications")
st.write("- **Initial Test of Competence (ITC)** – First Attempt")
st.write("- **Assessment of Professional Competence (APC)** – First Attempt")
st.write("- **Financial Modeling & Valuations Analyst (FMVA)**")

# Skills Section with Icons
st.header("Skills")
st.write("• Leadership 🏅 | • Problem-Solving 💡 | • Analytical 🔍 | • Detail-Oriented ✏️")
st.write("• Excel, Word, and PowerPoint Proficiency 📊 | • Financial Modeling 💼 | • Limited Python Knowledge 🐍")

# Industry Experience
st.header("Industry Experience")
st.write("Financial Services, Hedge Funds, Private Equity, Logistics, Manufacturing, Retail, Fast Foods, Agriculture, SaaS.")

# Languages
st.header("Languages")
st.write("**English**: Fully proficient")
st.write("**Afrikaans**: Fully proficient")

# Investment Approach
st.header("Investment Philosophy")
st.write("I take a long-term view on investments and value creation, aiming to generate sustainable growth over time.")

# Community Involvement
st.header("Community Involvement")
st.write("- Mosaic Community Development")
st.write("- Helpmekaar and Hospital Outreaches")
st.write("- Church Outreach Initiatives")

# Footer with Social Links
st.write("---")
st.write("Thank you for visiting my website. Feel free to reach out via [LinkedIn](https://www.linkedin.com/in/jacquesrdejager/) or email for collaboration or further discussions.")
