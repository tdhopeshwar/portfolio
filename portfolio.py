
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
    st.markdown("<h3 style='color: #5a5a5a; margin-top: -20px;'>Machine Learning Engineer | Data Scientist</h3>", unsafe_allow_html=True)
    st.header('About Me')

    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown('''"I'm Tanisha Dhopeshwar, a passionate Machine Learning Engineer and Data Scientist currently pursuing my Master's in Data Analytics at San Jose State University. I thrive at the intersection of data, creativity, and impact—harnessing the power of AI to uncover patterns, tell stories, and drive innovation. With hands-on experience from Vodafone, Incognetics, and current research in Generative AI and computer vision, I’ve designed and deployed real-world models that solve problems in healthcare, marketing, and content personalization. I aim to bridge technical depth with user-centered insights to build solutions that are not only smart but also meaningful."''')
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

    subtab1, subtab2, subtab3, subtab4 = st.tabs(["🖼️ Computer Vision", "🎯 Recommendation Systems", "🧠 Deep Learning", "📊 Data Science & Analytics"])

    with subtab1:
        project_card("Image Captioning Using Deep Learning",
        "Presented at the 2021 International Conference on Computational Performance Evaluation. Used CNN-RNN architecture to caption images with a BLEU score of 51.77.",
        "https://ieeexplore.ieee.org/abstract/document/9751818")

        project_card(
        "Real-Time Height Detection Model",
        "Developed a real-time height detection system using YOLOv5 and MiDaS for object detection and depth estimation.",
        "https://github.com/tdhopeshwar/Height-Detection" )

        project_card(
        "Road Sign Detection using YOLOv8",
        "Trained YOLOv8 on a custom 25-class dataset to detect and classify road signs with 86% accuracy.",
        "https://github.com/tdhopeshwar/Deep-Learning-Projects/blob/main/YOLO_Object_Detection_Training.ipynb.ipynb")

        project_card(
        "Cat Breed Classification with CNN",
        "Implemented a convolutional neural network to classify cat images into breeds, achieving high accuracy through image preprocessing and model tuning.",
        "https://github.com/tdhopeshwar/Deep-Learning-Projects/blob/main/Cat_Breed_Classification.ipynb")

    with subtab2:
        project_card("Anime Recommendation using ANN",
        "Developed a neural network-based recommendation system that learns user preferences and anime features to suggest titles users are likely to enjoy.",
        "https://github.com/tdhopeshwar/Anime-Recommendation")

        project_card("Kdrama Recommendation using LLM",
        "Built a recommendation tool using a large language model (LLM) to generate Kdrama suggestions based on plot descriptions, user queries, and viewing history.",
        "https://github.com/tdhopeshwar/kdrama-Recommendation-using-LLM")


    with subtab3:
        project_card("Fashion MNIST GAN",
        "Used a Generative Adversarial Network (GAN) to generate realistic fashion item images by learning from the Fashion MNIST dataset.",
        "https://github.com/tdhopeshwar/Deep-Learning-Projects/blob/main/Fashion_MNIST_GAN_Basics.ipynb")

        project_card("Deep Learning Project Suite",
        "A collection of foundational deep learning projects covering CNNs, RNNs, and GANs, built to strengthen understanding of model architectures, training workflows, and real-world applications in image generation, classification, and sequence modeling.",
        "https://github.com/tdhopeshwar/Deep-Learning-Projects")

        project_card("Anime Recommendation using ANN",
        "Developed a neural network-based recommendation system that learns user preferences and anime features to suggest titles users are likely to enjoy.",
        "https://github.com/tdhopeshwar/Anime-Recommendation")

        project_card("Kdrama Recommendation using LLM",
        "Built a recommendation tool using a large language model (LLM) to generate Kdrama suggestions based on plot descriptions, user queries, and viewing history.",
        "https://github.com/tdhopeshwar/kdrama-Recommendation-using-LLM")



    with subtab4:
        project_card("Harmony Hits Analysis",
        "An analysis of Spotify's top 200 songs to understand popularity trends, artist diversity, and social media influence. Created for a Data Visualization course at San Jose State University.",
        "https://public.tableau.com/views/SpotifyTrendAnalysis_TanishaDhopeshwar/SpotifyTrendAnalysis")

        project_card("Geographic Origin Of Music",
        "Used regression to predict the geographical origin of a music track using audio features.",
        "https://github.com/tdhopeshwar/GrographicOriginOfMusic")

        project_card("Influencer Comparison Model",
        "ML model to predict more influential social media user between two influencers based on their metrics.",
        "https://github.com/tdhopeshwar/Influencer-Project")

        project_card("Myocardial Infarction Analysis",
        "Analyzed complications post-myocardial infarction using patient clinical data to predict outcomes and identify key risk factors through machine learning models.",
        "https://github.com/tdhopeshwar/Myocardial_Infarction_Analysis")

        

with tab3:
    st.header('Experience')

    st.markdown("""
    <div style="background-color:#f9f9f9; padding:15px; border-radius:10px; box-shadow: 2px 2px 12px #aaa; margin-bottom: 15px;">
    <h4>Machine Learning Scientist | Entrevita (Apr 2024 – Present)</h4>
    <p>
    Leading the development of AI-powered precision health tools by integrating biometric data with fine-tuned large language models (LLMs). Engineered a smart nutrition advisor that generates personalized meal and supplement plans using QLoRA-tuned models deployed via Azure OpenAI. Additionally, built a real-time height detection pipeline using YOLOv5 and MiDaS to assist with contextual health assessments. Contributing to Entrevita's mission to democratize health by delivering actionable insights from individual biopsychosocial data.
    </p>
    </div>
    <div style="background-color:#f9f9f9; padding:15px; border-radius:10px; box-shadow: 2px 2px 12px #aaa; margin-bottom: 15px;">
    <h4>Data Analyst | Vodafone Intelligent Solutions (Aug 2021 – Mar 2023)</h4>
<p>
Led development of predictive marketing models using TensorFlow and BigQuery on GCP, boosting customer engagement by 27%. Automated data cleaning and transformation with Pandas and Scikit-learn, improving data quality by 37%. Resolved critical integrity issues in Teradata and Oracle databases using ML-based anomaly detection, preventing disruptions and averting potential €47,000 revenue loss.
</p>
</div>
    <div style="background-color:#f9f9f9; padding:15px; border-radius:10px; box-shadow: 2px 2px 12px #aaa; margin-bottom: 15px;">
    <h4>Research Assistant | MIT World Peace University (Nov 2020 – Jun 2021)</h4>
<p>
Designed an automated image captioning architecture using CNN and RNN with attention mechanism, achieving a 51.77 BLEU score. Focused on enhancing object detection and natural language generation for real-time captioning applications.
</p>
</div>
    <div style="background-color:#f9f9f9; padding:15px; border-radius:10px; box-shadow: 2px 2px 12px #aaa; margin-bottom: 15px;">
    <h4>Machine Learning Intern | Incognetics Technologies (Jun 2020 – Oct 2020)</h4>
<p>
Developed a contract summarization model using LSTM networks, increasing operational efficiency by 33%. Applied NLP techniques to extract and summarize key legal clauses, streamlining internal workflows.
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
