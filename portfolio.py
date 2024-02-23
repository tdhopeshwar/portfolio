import streamlit as st
import streamlit.components.v1 as components
from PIL import Image
import base64
from io import BytesIO
st.set_page_config(layout="wide")

def image_to_base64(image):
    import base64
    from io import BytesIO

    buffered = BytesIO()
    image.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    return img_str
# Custom CSS to make the image circular
st.markdown(
    """
    <style>
    .circle-img {
        border-radius: 50%;
        width: auto;
        max-width: 150px;  # You can adjust the size as needed
        height: auto;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
st.title('Tanisha Dhopeshwar')

st.write('''
Aspiring Data Scientist''')
# About Me section integrated directly into the homepage
st.header('About Me')

# Use columns for layout
col1, col2 = st.columns([3, 1])  # Adjust the ratio as needed

with col1:  # This column is for your text
    st.write('''
    "I'm Tanisha Dhopeshwar, a data analyst and machine learning practitioner currently pursuing a Master's in Data Analytics at San Jose State University. My academic journey is fueled by a passion for uncovering insights through data, supported by a solid foundation in technical skills, including SQL, Python, and advanced analytics tools. With hands-on machine learning experience from my roles at Vodafone and Incognetics Technologies, I've honed my skills in predictive modeling and AI-driven analysis. My passion is to unlock the stories that data reveals—be it predicting market trends or uncovering the narratives behind music popularity. I bring a mix of rigorous analysis and creative problem-solving to the table, eager to tackle the next data challenge.

    My aim is to merge technical analysis with business savvy to craft data-driven strategies that enact meaningful change. Whether it's cutting operational costs or boosting customer engagement through targeted marketing, my focus is on transforming complex data into actionable insights."
    ''')

with col2:  # This column is for your image
    image = Image.open('Profile_pic.JPG')
    # Display the image using HTML to apply the custom CSS for circular crop
    st.markdown(
        f'<img src="data:image/jpeg;base64,{image_to_base64(image)}" class="circle-img">', 
        unsafe_allow_html=True
    )



if st.sidebar.button('Projects'):
    st.header('Projects')
    st.write('Here are some of my projects...')
    with st.expander("Harmony Hits Analysis"):
         st.subheader('Harmony Hits Analysis')
         st.write('''
         **Introduction**: The Harmony Hits Analysis aims to unravel trends in music popularity, explore artist dynamics, 
         and understand the influence of social media trends on Spotify rankings. In a rapidly evolving music landscape, 
         these insights are crucial for artists, music companies, and streaming platforms. This project was created as a part of the Data Visualization Course  work at San Jose State University under Professor Andrew Bond.''')

         st.write('''
         **1.1 Background**:
         
         We frequently listen to songs online in the music industry. Spotify is a popular music application.  
         The title of the project is "HarmonyHits: Exploring Top 200 Spotify Songs."
         The goal of this project is to help people understand these top 200 songs using pictures and graphs. 
         A timeline that shows how songs go up and down in popularity.
         ''')
     
         st.write('''
         **1.2 Objectives**:
         - Analyze trends in music popularity over time.
         - Investigate the global reach and popularity of Harmony Hits.
         - Explore the relationship between artist popularity and diversity.
         - Integrate social media trends to understand correlations with Spotify rankings.
         ''')
         # Embed Tableau visualization within the Projects section
         tableau_url = "https://public.tableau.com/views/SpotifyTrendAnalysis_TanishaDhopeshwar/SpotifyTrendAnalysis?:language=en-US&publish=yes&:sid=&:display_count=n&:origin=viz_share_link"
         tableau_iframe_html = f'''
         <iframe src="{tableau_url}" width="100%" height="1000" frameborder="0"></iframe>
         '''
         components.html(tableau_iframe_html, height=1300)
         
         # Additional projects can be added here
         # st.image, st.video, st.markdown, etc., to showcase other projects
    with st.expander("Image Captioning Using Deep Learning"):
        st.write("This project explores the intersection of computer vision and natural language processing by developing a deep learning model for image captioning. Presented at the 2021 International Conference on Computational Performance Evaluation, our work leverages advanced neural networks to generate descriptive text for images, pushing the boundaries of AI's ability to understand and interpret visual content.")
        st.write('''
        **Publication**:
        
        Y. S. Jain, T. Dhopeshwar, S. K. Chadha and V. Pagire, "Image Captioning using Deep Learning," 2021 International Conference on Computational Performance Evaluation (ComPE), Shillong, India, 2021, pp. 040-044, doi: 10.1109/ComPE53109.2021.9751818. keywords: {Deep learning;Performance evaluation;Image recognition;Social networking (online);Surveillance;Object detection;Real-time systems;Image Caption;Attention;CNN;RNN},

        ''')
        st.write('''
For more details, you can refer to the publication [Image Captioning Using Deep Learning](https://ieeexplore.ieee.org/abstract/document/9751818). ''')

    
            
if st.sidebar.button('Experience'):
    st.header('Experience')

    with st.expander("Data Analyst | Vodafone Intelligent Solutions (Aug 2021 – Mar 2023)"):
        st.write("""
        -As a Data Analyst at Vodafone Intelligent Solutions, I spearheaded pivotal initiatives aimed at optimizing data management processes and leveraging advanced analytics for business enhancement. Key responsibilities included:

-Data Pipeline Creation and Implementation: Orchestrated the development and deployment of robust data pipelines, facilitating seamless migration of data from On-Premise Databases to Google BigQuery. This initiative led to a notable 30% reduction in operational costs.

-Data Transformation and Cleansing: Transformed raw data into refined, structured formats conducive to in-depth analysis. By ensuring the scalability, reliability, and efficiency of data pipelines, downtime was reduced by 25%.

-AI-Driven Marketing Campaigns: Utilized AI-based models within Pega to execute real-time marketing campaigns, harnessing customer data for targeted outreach. The implementation resulted in a remarkable 20% increase in revenue and a 30% enhancement in customer engagement metrics.

-Automation with Shell Scripts: Developed and deployed Shell Scripts for automating routine operational tasks, including Server Health Monitoring and Housekeeping. This initiative not only bolstered server performance but also yielded substantial monthly savings equivalent to 30 hours of manual labor.

-Database Issue Resolution: Addressed critical data issues within Teradata and Oracle Databases, safeguarding data integrity and averting potential disruptions. These efforts mitigated downtime risks, preventing an estimated loss of €50,000 in revenue.
        """)

    with st.expander("Research Assistant | MIT World Peace University (Nov 2020 – Jun 2021)"):
        st.write("""
-As a Research Assistant at MIT World Peace University, I played a pivotal role in advancing the field of computer vision and natural language processing. Key responsibilities included:

-Architecture Development: Constructed an innovative architecture featuring a dense attention model with a CNN Encoder and RNN Decoder. This architecture seamlessly integrated object detection and text generation algorithms to automate the generation of image descriptions.

-Publication Achievement: Published a paper titled "Image Captioning using Deep Learning" at the esteemed 2021 International Conference on Computational Performance Evaluation. The paper achieved an impressive average BLEU score of 51.77, highlighting the effectiveness and significance of the proposed methodology.
        """)

    with st.expander("Machine Learning Intern | Incognetics Technologies (Jun 2020 – Oct 2020)"):
        st.write("""
        During my internship at Incognetics Technologies in 2020, I spearheaded the development of a contract summarization model leveraging LSTM networks and NLP techniques. This innovative project resulted in a significant 30% increase in operational efficiency, thereby enhancing overall productivity and contributing to streamlined operations within the organization. Through this endeavor, I gained valuable hands-on experience in applying cutting-edge machine learning and natural language processing methodologies to real-world business challenges.
        """)         

        
if st.sidebar.button('Content Creation'):
    st.header('Content Creation')

    # Information about YouTube Channel
    st.subheader('YouTube Channel')
    st.write('Here is a brief overview of my YouTube channel where I share Lifestyle, Travel and Informational Videos. Check out my channel [here](https://www.youtube.com/channel/UCXH9s5XakB22syX3Vnawl7w).')
    
    # Embedding a YouTube video
    st.video('https://youtu.be/dP0TV5FCIAc?si=c3yjnQXmCP2u9INd')

    # Information about Instagram Handle
    st.subheader('Instagram')
    st.write('Follow me on Instagram [@toulouuseee__](https://www.instagram.com/toulouuseee__/) for more updates and insights.')

            
            
if st.sidebar.button('Contact'):
    st.header('Contact Me')
    st.write('You can contact me via email at tanisha.dhopeshwar@sjsu.edu you can also reach out to me on LinkedIn "https://www.linkedin.com/in/tdhopeshwar/"')


