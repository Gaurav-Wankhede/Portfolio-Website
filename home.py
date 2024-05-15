import requests
import streamlit as st
from streamlit_option_menu import option_menu
import base64
from streamlit_lottie import st_lottie
import os

# Path to your resume
resume_path = "assets/resume.pdf"

st.set_page_config(layout='wide')
def render_svg(svg_path, width=16, height=16):
    with open(svg_path, 'rb') as f:
        svg_bytes = f.read()
    b64 = base64.b64encode(svg_bytes).decode()
    html = f'<img src="data:image/svg+xml;base64,{b64}" width="{width}" height="{height}"/>'
    return html

def render_gif(gif_path, width=16, height=16):
    with open(gif_path, 'rb') as f:
        gif_bytes = f.read()
    b64 = base64.b64encode(gif_bytes).decode()
    html = f'<img src="data:image/gif;base64,{b64}" width="{width}" height="{height}"/>'
    return html

def render_png(png_path, width=50, height=50):
    with open(png_path, 'rb') as f:
        png_bytes = f.read()
    b64 = base64.b64encode(png_bytes).decode()
    file_name = os.path.splitext(os.path.basename(png_path))[0]  # Get the file name without the .png extension
    html = f'<div class="logo-container" style="text-align: center; color: white;">'  # Center the text and set its color to white
    html += f'<img class="logo" src="data:image/png;base64,{b64}" width="{width}" height="{height}"/>'
    html += f'<p class="logo-text">{file_name}</p>'  # Display the file name
    html += '</div>'
    return html


def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def load_lottie_file(file_path):
    with open(file_path, 'rb') as file:
        lottie_bytes = file.read()
    base64_str = base64.b64encode(lottie_bytes).decode()
    return f"data:application/json;base64,{base64_str}"


def home():

    # CSS styles file
    with open("styles/main.css") as f:
        st.write(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    # Profile image file
    with open("assets/profile.png", "rb") as img_file:
        img = "data:image/png;base64," + base64.b64encode(img_file.read()).decode()

    # PDF CV file
    with open("assets/resume.pdf", "rb") as pdf_file:
        pdf_bytes = pdf_file.read()

    st.subheader("Hey Guys :wave:")
    # Custom HTML and CSS using st.markdown
    st.markdown(
        """
        <h1 style='color: white;'><i><font size="4">I am </font></i> <font color="Goldenrod">G</font>aurav <font color="Goldenrod">W</font>ankhede</font></h1>
        """,
        unsafe_allow_html=True
    )

    st.write(f"""
        <div class="container" style="display: flex; justify-content: center;">
            <div class="box">
                <div class="spin-container">
                    <div class="shape">
                        <div class="bd">
                            <img src="{img}" alt="Gaurav Wankhede">
                        </div>
                    </div>
                </div>
            </div>
        </div>
        """,
             unsafe_allow_html=True)

    # Load GIF URLs
    linkedin_gif_url = "assets/linkedin.gif"
    github_gif_url = "assets/github.gif"
    instagram_gif_url = "assets/instagram.gif"


    # Use the render_gif function to get the HTML for the GIFs
    linkedin_gif_html = render_gif(linkedin_gif_url, width=50, height=50)
    github_gif_html = render_gif(github_gif_url, width=50, height=50)
    instagram_gif_html = render_gif(instagram_gif_url, width=50, height=50)

    # Define the HTML code to display GIFs and their respective links horizontally
    html_code = f"""
        <div style="display: flex; align-items: center; justify-content: center;">
            <a href="https://www.linkedin.com/in/gaurav-wankhede-5244101b8/" target="_blank" style="margin-right: 20px;">
                {linkedin_gif_html}
            </a>
            <a href="https://github.com/Gaurav-Wankhede" target="_blank" style="margin-right: 20px;">
                {github_gif_html}
            </a>
            <a href="https://github.com/Gaurav-Wankhede" target="_blank">
                {instagram_gif_html}
            </a>
        </div>
    """

    # Display HTML code
    st.write(html_code, unsafe_allow_html=True)

    st.markdown("---")
    # Load the Lottie animation
    lottie_coder = load_lottie_url("https://lottie.host/ed492b45-0e8d-4e3f-b1d7-fbdfbb08a6a2/9zEnjfQVEe.json")



    with st.container():
        selected = option_menu(
            menu_title=None,
            options=["Home", "Project", "About", "Contact"],
            icons=["house", "code-slash", "file-person", "envelope"],
            menu_icon="cast",
            default_index=0,
            orientation="horizontal",
            styles={
                "container": {"padding": "0!important", "background-color": "black"},
                "icon": {"color": "black", "font-size": "20px"},
                "nav-link": {
                    "font-size": "16px",
                    "text-align": "left",
                    "margin": "0px",
                    "--hover-color": "Goldenrod",
                    "color": "white",
                    "::first-letter": {"color": "Goldenrod"}
                },
                "nav-link-selected": {
                    "background-color": "Goldenrod",
                    "color": "white",
                    "font-weight": "bold"
                }

            }
        )

    if selected == "Home":
        st.markdown(
            """
            <h1 style='color: Goldenrod;'>W<font color="white">elcome to my Portfolio 🌟</font></h1>
            """,
            unsafe_allow_html=True
        )
        st.write(
            """
            I'm a professional with a Bachelor of Engineering in Information Technology from Atharva College of Engineering, Mumbai, graduating with distinction and consistently achieving a CGPA of 7.93. 

            Throughout my career, I've prioritized precision and attention to detail, leveraging my expertise in Python, SQL, and various data analysis tools. I've led diverse projects in predictive modeling, data analysis, and machine learning, delivering solutions that drive measurable business outcomes. 

            My strength lies in my ability to translate complex data into actionable insights, enabling informed decision-making. I thrive in dynamic environments, where I excel at navigating challenges and delivering results under pressure. 

            I'm committed to continuous learning and development, holding certifications in SQL Intermediate and Python Core from SoloLearn, alongside credentials in digital marketing and Google Analytics. My dedication to staying updated with industry trends underscores my commitment to excellence.
            """
        )

        # Skills
        st.markdown(
            """
            <h1 style='color: Goldenrod;'>S<font color="white">kills</font></h1>
            """,
            unsafe_allow_html=True
        )

        # Load your premium Lottie animation (replace the URL with your own)
        home_lottie_url = load_lottie_url("https://lottie.host/8bb6ced5-fc23-4e0d-a926-825020328237/7gGwo2M71a.json")
        container = st.container()

        with container:
            col1, col2, col3 = st.columns([2, 4, 2])

            with col2:
                st_lottie(home_lottie_url, height='50%', width='50%')

        # Get a list of all PNG files in the 'assets/logo' folder
        folder_path = 'assets/logo'
        logos = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.png')]

        # Create a grid-like structure for your logos
        html = '<div class="container">'
        for logo in logos:
            html += render_png(logo)
        html += '</div>'

        # Add your logos to the Streamlit app
        st.markdown(html, unsafe_allow_html=True)

        # Display My Resume
        st.markdown(
            """
            <h1 style='color: white;'><font color="Goldenrod">R</font>esume</h1>
            """,
            unsafe_allow_html=True
        )



        with open("assets/resume.pdf", "rb") as pdf_file:
            st.download_button(
                label="Download my Resume",
                data=pdf_file,
                file_name="resume.pdf",
                mime="application/octet-stream"
            )

        # Path to your resume
        resume_path = "assets/resume.pdf"

        # Create a link to the PDF file
        pdf_file = f"data:application/pdf;base64,{base64.b64encode(open(resume_path, 'rb').read()).decode()}"

        # Create an iframe that embeds the PDF
        iframe = f'<iframe src="{pdf_file}" width="100%" height="800px"></iframe>'

        # Display the iframe
        st.markdown(iframe, unsafe_allow_html=True)


    elif selected == "Project":
        st.markdown(
            """
            <h1 style='color: Goldenrod;'>M<font color="white">y Projects 👨‍💻</font></h1>
            """,
            unsafe_allow_html=True
        )

        # Create a container
        with st.container():
            head_left, head_middle, head_right = st.columns([2, 1, 1])
            # Add the common header inside the container
            with head_left:
                st.markdown("""
                <h3 style='text-align: left; background-color: rgba(218,165,32,0.1); border: 2px solid Goldenrod; border-radius: 10px; padding: 10px;'> 
                Accident Detection System with twilio 
                </h3>
                """, unsafe_allow_html=True)

            with head_middle:
                st.write("")
            with head_right:
                st.markdown("<h5 style='text-align: left; padding-top: 20px;'> October 2022 </h5>", unsafe_allow_html=True)


            # Create three columns inside the container
            left_col, middle_col, right_col = st.columns([1, 2, 2])

            with left_col:
                st_lottie(lottie_coder, height='100%', width='100%', key="coder1")
            with middle_col:
                # Achievements
                st.markdown("<h3>Summary</h3>", unsafe_allow_html=True)
                st.markdown("""
                        - ResNet-50 Model: Improved experiment results, boosting the training accuracy of the ResNet-50 model to 97% to detect accidents.
- Image Training: Educated the system on 500-600 images of accidents, achieving zero false positives during training.
- Safety Measures: Fortified safety measures, encouraging to a 20% reduction in emergency response time.
                        """)
                st.markdown("<h5><a href='https://github.com/Gaurav-Wankhede/Accident-Detection_And_Alerting_System.git'>Repo</a></h5>",
                            unsafe_allow_html=True)

            with right_col:
                # Time Frame
                # Replace with the actual start and end months and years

                # Skills Used
                st.subheader("Skills Used")
                # Skills Used
                st.markdown("""
                        <div class="skill-button">Python Programming</div>
                        <div class="skill-button">Deep Learning</div>
                        <div class="skill-button">Transfer Learning</div>
                        <div class="skill-button">Image Processing</div>
                        <div class="skill-button">Streamlit Web App Development</div>
                        """, unsafe_allow_html=True)

        # Create a container
        with st.container():
            head_left,head_middle, head_right = st.columns([2, 1, 1])
            # Add the common header inside the container
            with head_left:
                st.markdown("<h3 style='text-align: left; background-color: rgba(218,165,32,0.1); border: 2px solid Goldenrod; border-radius: 10px; padding: 10px;'> Face Mask Detection</h3>", unsafe_allow_html=True)
            with head_middle:
                st.write("")
            with head_right:
                st.markdown("<h3 style='text-align: left;'> March 2022 </h3>", unsafe_allow_html=True)


            # Create three columns inside the container
            left_col, middle_col, right_col = st.columns([1, 2, 2])

            with left_col:
                st_lottie(lottie_coder, height='100%', width='100%', key="coder")
            with middle_col:
                # Achievements
                st.subheader("Summary")
                st.markdown("""
                - **Accuracy Rate**: Gained a **98% accuracy rate** in the face mask detection project.
                - **Precision and Productivity**: Educated the system using **3833 images** to pinpoint correct mask-wearing, boosting precision by **15%** and productivity by **25%**.
                - **Algorithm Fine-Tuning**: Accomplished a **15% boost** in face mask detection accuracy by fine-tuning existing algorithms and integrating real-time feedback mechanisms.
                """)
                st.markdown("<h5><a href='https://github.com/Gaurav-Wankhede/Face-Mask_Detection.git'>Repo</a></h5>",
                            unsafe_allow_html=True)

            with right_col:
                # Time Frame
                  # Replace with the actual start and end months and years

                # Skills Used
                st.subheader("Skills Used")
                # Skills Used
                st.markdown("""
                <div class="skill-button">Python Programming</div>
                <div class="skill-button">Deep Learning</div>
                <div class="skill-button">Transfer Learning</div>
                <div class="skill-button">Image Processing</div>
                <div class="skill-button">Streamlit Web App Development</div>
                """, unsafe_allow_html=True)


    elif selected == "About":
        # About me section
        st.subheader("About Me")
        st.write("""
        - 🧑‍💻 I am **Gaurav Wankhede**, a Bachelor of Engineering in Information Technology from Atharva College of Engineering, Mumbai (August 2019 - July 2023, CGPA: 7.93).
        
        - 📫 How to reach me: pgywww@gmail.com
        
        - 🌐 LinkedIn, GitHub, Portfolio
         
        - ❤️ I am passionate about **Machine Learning/Deep Learning, Data Analysis, Data Science, Computer Vision, WebScraping, Optimization, Automation**, and more!
       
        - 🛩️ I have worked on several projects, including Analysis and Predictive Modeling of IPL Matches and Accident Detection System with Twilio.
        
        - 🤖 I enjoy developing projects such as SpeedClimbing.AI (🏗️under construction) and participating at platforms like Kaggle 📈
        
        - 🏂 Also practicing Cooking, Video Games and Designing 🧗
        
        - 🏠 Boisar
    """)


    elif selected == "Contact":
        st.write("# Contact")
        st.write("## Contact Streamlit")
        st.write("### Streamlit is a web app development library for Python.")

    # Define the HTML code for the footer
    footer_html = """
        <style>
        .footer {
            position: relative;
            bottom: 0;
            width: 100%;
            text-align: center;
            padding: 10px;
        }
        </style>
        <div class="footer">
            <p>© All rights reserved by Gaurav Wankhede, 2024</p>
        </div>
    """

    # Add a horizontal line
    st.markdown("---")

    # Display the footer
    st.markdown(footer_html, unsafe_allow_html=True)


if __name__ == "__main__":
    home()