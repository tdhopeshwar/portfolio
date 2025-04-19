import streamlit as st
import streamlit.components.v1 as components
from PIL import Image
from io import BytesIO
import base64
import time

st.set_page_config(layout="wide")

# Custom CSS
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(to right, #f0f2f5, #ffffff);
    }
    .circle-img {
        border-radius: 50%;
        width: 150px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
    h1 {
        font-family: 'Georgia', serif;
        font-size: 3em;
        color: #1f4e79;
    }
    h2, h3, h4 {
        font-family: 'Verdana', sans-serif;
        color: #2e4053;
    }
</style>
""", unsafe_allow_html=True)

# Tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs(["🏠 Home", "📊 Projects", "💼 Experience", "🎥 Content", "📬 Contact"])

# Helper function
def image_to_base64(image):
    buffered = BytesIO()
    image.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    return img_str

with tab1:
    st.title('Tanisha Dhopeshwar')
    st.write('''Aspiring Data Scientist''')
    st.header('About Me')

    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown('''"I'm Tanisha Dhopeshwar, a data analyst and machine learning practitioner currently pursuing a Master's in Data Analytics at San Jose State University. With hands-on machine learning experience from my roles at Vodafone and Incognetics Technologies, I've honed my skills in predictive modeling and AI-driven analysis. My aim is to merge technical analysis with business savvy to craft data-driven strategies that enact meaningful change."''')
    with col2:
        image = Image.open('Profile_pic.JPG')
        st.markdown(f'<img src="data:image/jpeg;base64,{image_to_base64(image)}" class="circle-img">', unsafe_allow_html=True)

with tab2:
    st.header('Projects')

    def project_card(title, desc, link=None):
        st.markdown(f'''
        <div style="background-color:#f9f9f9; padding:15px; border-radius:10px; box-shadow: 2px 2px 12px #aaa; margin-bottom: 15px;">
            <h4>{title}</h4>
            <p>{desc}</p>
            {'<a href="' + link + '" target="_blank">🔗 View Project</a>' if link else ''}
        </div>
        ''', unsafe_allow_html=True)

    subtab1, subtab2, subtab3, subtab4, subtab5 = st.tabs(["🖼️ Computer Vision", "🎯 Recommendation Systems", "🧠 Deep Learning", "📊 Data Science & Analytics", "📚 Others"])

    with subtab1:
        project_card("Image Captioning Using Deep Learning",
        "Presented at the 2021 International Conference on Computational Performance Evaluation. Used CNN-RNN architecture to caption images with a BLEU score of 51.77.",
        "https://ieeexplore.ieee.org/abstract/document/9751818")

    with subtab2:
        project_card("Influencer Project",
        "ML model to predict more influential social media user between two influencers based on their metrics.",
        "https://github.com/tdhopeshwar/Influencer-Project")

    with subtab3:
        project_card("Geographic Origin Of Music",
        "Used regression to predict the geographical origin of a music track using audio features.",
        "https://github.com/tdhopeshwar/GrographicOriginOfMusic")

    with subtab4:
        project_card("Harmony Hits Analysis",
        "An analysis of Spotify's top 200 songs to understand popularity trends, artist diversity, and social media influence. Created for a Data Visualization course at San Jose State University.",
        "https://public.tableau.com/views/SpotifyTrendAnalysis_TanishaDhopeshwar/SpotifyTrendAnalysis")

    with subtab5:
        st.write("Add any miscellaneous or future projects here.")

with tab3:
    st.header('Experience')

    st.markdown("""
    <div style="background-color:#f9f9f9; padding:15px; border-radius:10px; box-shadow: 2px 2px 12px #aaa; margin-bottom: 15px;">
    <h4>Data Analyst | Vodafone Intelligent Solutions (Aug 2021 – Mar 2023)</h4>
    <p>
    Orchestrated end-to-end data pipelines from on-prem to BigQuery. Led marketing campaigns using AI models with 20% revenue increase. Automated 30 hours/month tasks with Shell scripts. Safeguarded data systems against €50,000 in risks.
    </p>
    </div>
    <div style="background-color:#f9f9f9; padding:15px; border-radius:10px; box-shadow: 2px 2px 12px #aaa; margin-bottom: 15px;">
    <h4>Research Assistant | MIT World Peace University (Nov 2020 – Jun 2021)</h4>
    <p>
    Designed an image captioning architecture with CNN-RNN and attention. Published at ComPE 2021 with a BLEU score of 51.77.
    </p>
    </div>
    <div style="background-color:#f9f9f9; padding:15px; border-radius:10px; box-shadow: 2px 2px 12px #aaa; margin-bottom: 15px;">
    <h4>Machine Learning Intern | Incognetics Technologies (Jun 2020 – Oct 2020)</h4>
    <p>
    Developed LSTM-based contract summarizer, improving efficiency by 30%. Applied NLP and ML for real-world legal document insights.
    </p>
    </div>
    """, unsafe_allow_html=True)

with tab4:
    st.header('Content Creation')

    st.subheader('📺 YouTube Channel')
    st.write("Lifestyle, travel and tech explained! [Visit Channel](https://www.youtube.com/channel/UCXH9s5XakB22syX3Vnawl7w)")
    st.video('https://youtu.be/dP0TV5FCIAc?si=c3yjnQXmCP2u9INd')

    st.subheader('📸 Instagram')
    st.write("Follow me on Instagram [@toulouuseee__](https://www.instagram.com/toulouuseee__/) for travel and behind-the-scenes content.")

with tab5:
    st.header('Contact Me')
    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submitted = st.form_submit_button("Send")
        if submitted:
            st.success("Thanks for reaching out! I'll get back to you soon.")

    st.write("📧 tanisha.dhopeshwar@sjsu.edu")
    st.write("🔗 [LinkedIn](https://www.linkedin.com/in/tdhopeshwar/)")
