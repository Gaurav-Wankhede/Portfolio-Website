import requests
import streamlit as st
from streamlit_option_menu import option_menu
import base64
from streamlit_lottie import st_lottie
import streamlit.components.v1 as components
import os

# Path to your resume
resume_path = "assets/resume.pdf"

st.set_page_config(layout='wide', page_title="Gaurav Wankhede", page_icon="./assets/hacker.png")


@st.cache_data


@st.cache_data
def render_svg(svg_path, width=16, height=16):
    with open(svg_path, 'rb') as f:
        svg_bytes = f.read()
    b64 = base64.b64encode(svg_bytes).decode()
    html = f'<img src="data:image/svg+xml;base64,{b64}" width="{width}" height="{height}"/>'
    return html


@st.cache_data
def render_gif(gif_path, width=16, height=16):
    with open(gif_path, 'rb') as f:
        gif_bytes = f.read()
    b64 = base64.b64encode(gif_bytes).decode()
    html = f'<img src="data:image/gif;base64,{b64}" width="{width}" height="{height}"/>'
    return html


@st.cache_data
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


@st.cache_data
def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


@st.cache_data
def load_lottie_file(file_path):
    with open(file_path, 'rb') as file:
        lottie_bytes = file.read()
    base64_str = base64.b64encode(lottie_bytes).decode()
    return f"data:application/json;base64,{base64_str}"

# Function to count projects
def count_projects():
    return project_counter
def count_self():
    return self_project
def count_freelance():
    return freelance
def other_project():
    return other

def home():
    # Initializing a counter
    global project_counter, self_project, freelance, other
    self_project = 3
    freelance = 1
    other = 3
    project_counter = self_project + freelance + other
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
            <a href="https://www.instagram.com/_gaurav_wankhede_/" target="_blank">
                {instagram_gif_html}
            </a>
        </div>
        <div style="
        display: flex; 
        align-items: center; 
        justify-content: center;
        ">
        Click me
        </div>
    """

    # Display HTML code
    st.write(html_code, unsafe_allow_html=True)

    st.markdown("---")
    # Load the Lottie animation
    lottie_coder = load_lottie_url("https://lottie.host/ed492b45-0e8d-4e3f-b1d7-fbdfbb08a6a2/9zEnjfQVEe.json")
    face_mask = load_lottie_url("https://lottie.host/00b300d9-76c1-4e30-a00c-11013a6b6be1/Q2S93NdQUM.json")
    accident = load_lottie_url("https://lottie.host/7c7bb3fb-493a-4d5f-8730-23739d4116db/oVMr5pU61s.json")
    web_scrapping = load_lottie_url("https://lottie.host/02cc2c85-f4f8-40b1-accf-312e7dc131f9/9qKOLO0Nd8.json")
    analysis = load_lottie_url("https://lottie.host/7ad00812-5657-450f-85a1-6172ee647244/dlW8yNGNot.json")
    attendance = load_lottie_url("https://lottie.host/4a1e9f9e-1bc4-41e6-bec7-16985456371b/HvuY54WYnk.json")
    bot = load_lottie_url("https://lottie.host/db0b89ed-4ffa-42bf-bb4e-4a8947dec02b/mloKEKtTNN.json")
    weather = load_lottie_url("https://lottie.host/2e5e71a0-634a-4bf1-9cb8-25e40855f6c9/hSMVjoAOGd.json")
    amazon = load_lottie_url("https://lottie.host/f0082e89-fbc9-4d28-a805-014db29c13e1/Uahtp5ml6F.json")

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
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Portfolio</title>
                <style>
                    body {
                        font-family: Arial;
                        line-height: 1.6;
                        background-color: #f4f4f4;
                        margin: 0;
                        padding: 20px;
                    }
            
                    .content {
                        background: transparent;
                        padding: 20px;
                        max-width: 800px;
                    }
            
                    @keyframes blink {
                      0% {
                        color: transparent;
                      }
                      50% {
                        color: yellow;
                      }
                      100% {
                        color: transparent;
                      }
                    }
                    
                    .highlight {
                      font-weight: bold;
                      font-size: 2em;
                      animation: blink 2s infinite;
                    }
            
                    .first-letter {
                        color: goldenrod; /* Default color of 'B' */
                        Font-Size: 50px;
                    }
                    
                    .text {
                        color: white;
                        font-weight: bold;
                        font-family: Arial;
                        Font-Size: 40px;
                    }
                    
                </style>
            </head>
            <body>
                <div class="content">
                    <span class="highlight">
                        <span class="first-letter">D</span>ata Science 
                        <span class="text">&</span>
                        <span class="first-letter">A</span>rtificial Intelligence
                    </span> 
                    <span class="text"><span class="first-letter">E</span>nthusiast</span>
                </div>
            </body>
            </html>

            """,
            unsafe_allow_html=True
        )

        with st.container():
            st.markdown("""
                <style>
                .metric-box {
                    background-color: rgba(218,165,32,0.0);
                    border: 2px solid Goldenrod;
                    border-radius: 10px;
                    padding: 20px;
                    text-align: center;
                    font-size: 24px;
                    color: Goldenrod;
                }
                
                h2 {
                    text-align: center
                }
                </style>
            """, unsafe_allow_html=True)

            # Using columns to organize metrics
            col1, col2, col3, col4 = st.columns(4)

            # Displaying the number of projects in the first column
            with col1:
                st.markdown(f"""
                    <div class="metric-box">
                        <h2>Total Projects</h2>
                        <p>{count_projects()}</p>
                    </div>
                    
                """, unsafe_allow_html=True)

            # Placeholder for other metrics or information in col2 and col3
            with col2:
                st.markdown(f"""
                    <div class="metric-box">
                        <h2>Self Projects</h2>
                        <p>{count_self()}</p>
                    </div>
                """, unsafe_allow_html=True)

            with col3:
                st.markdown(f"""
                    <div class="metric-box">
                        <h2>Freelancing Projects</h2>
                        <p>{count_freelance()}</p>
                    </div>
                """, unsafe_allow_html=True)

            with col4:
                st.markdown(f"""
                    <div class="metric-box">
                        <h2>Other Projects</h2>
                        <p>{other_project()}</p>
                    </div>
                """, unsafe_allow_html=True)

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


    elif 'selected' in locals() and selected == "Project":
        st.markdown(
            """
            <h1 style='color: Goldenrod;'>M<font color="white">y Projects 👨‍💻</font></h1>
            """,
            unsafe_allow_html=True
        )

        with st.container():
            project_counter += 1
            head_left, head_middle, head_right = st.columns([2, 1, 1])
            # Add the common header inside the container
            with head_left:
                st.markdown("""
                        <h3 style='text-align: left; background-color: rgba(218,165,32,0.1); 
                        border: 2px solid Goldenrod; border-radius: 10px; padding: 10px;'> 
                        Heroic AI
                        </h3>
                        <h4>Self Project</h4>
                        """, unsafe_allow_html=True)

            with head_middle:
                st.write("")
            with head_right:
                st.markdown("<h5 style='text-align: left; padding-top: 20px;'> May 2024 </h5>",
                            unsafe_allow_html=True)

            # Create three columns inside the container
            left_col, middle_col, right_col = st.columns([1, 2, 2])

            with left_col:
                st_lottie(bot, height='100%', width='100%', key="coder6")
            with middle_col:
                # Achievements
                st.markdown("<h3>Summary</h3>", unsafe_allow_html=True)
                st.markdown("""
                        - 	Developed an AI chatbot using Large Language Models
                        
                        - 	Used **Groq API** to use these models to generate responses
                        
                        -   Added **Chat with CSV** functionality using **PandasAI**
                            """
                            )
                st.markdown(
                    """<h5><a href='https://github.com/Gaurav-Wankhede/Heroic-AI.git'>GitHub</a>
                    |
                    <a href="https://heroic-ai.onrender.com">Website</a>
                    </h5>


                    """,
                    unsafe_allow_html=True)

            with right_col:
                # Time Frame
                # Replace with the actual start and end months and years

                # Skills Used
                st.subheader("Skills Used")
                # Skills Used
                st.markdown("""
                                <div class="skill-button">Python</div>
                                <div class="skill-button">Streamlit</div>
                                <div class="skill-button">Groq API</div>
                                <div class="skill-button">Pandas</div>
                                <div class="skill-button">PandasAI</div>
                                """, unsafe_allow_html=True)

        with st.container():
            head_left, head_middle, head_right = st.columns([2, 1, 1])
            # Add the common header inside the container
            with head_left:
                st.markdown("""
                        
                        <h3 style='text-align: left; background-color: rgba(218,165,32,0.1); border: 2px solid Goldenrod; border-radius: 10px; padding: 10px;'> 
                        Smart Attendance System
                        </h3>
                        <h4>Freelancing Project</h4>
                        """, unsafe_allow_html=True)

            with head_middle:
                st.write("")
            with head_right:
                st.markdown("<h5 style='text-align: left; padding-top: 20px;'> April 2024 </h5>",
                            unsafe_allow_html=True)

            # Create three columns inside the container
            left_col, middle_col, right_col = st.columns([1, 2, 2])

            with left_col:
                st_lottie(attendance, height='100%', width='100%', key="coder5")
            with middle_col:
                # Achievements
                st.markdown("<h3>Summary</h3>", unsafe_allow_html=True)
                st.markdown("""
                        - 	Smart Attendance System
                            """
                            )
                st.markdown(
                    """<h5><a href='https://github.com/Gaurav-Wankhede/Smart-Attendance-System/tree/main'>GitHub</a>
                        </h5>


                    """,
                    unsafe_allow_html=True)

            with right_col:
                # Time Frame
                # Replace with the actual start and end months and years

                # Skills Used
                st.subheader("Skills Used")
                # Skills Used
                st.markdown("""
                                <div class="skill-button">Python</div>
                                <div class="skill-button">Streamlit</div>
                                <div class="skill-button">Open CV</div>
                                <div class="skill-button">Face_Recognition</div>
                                <div class="skill-button">MatplotLib</div>
                                <div class="skill-button">Plotly</div>
                                <div class="skill-button">Numpy</div>
                                <div class="skill-button">Pandas</div>
                                <div class="skill-button">Pillow</div>
                                <div class="skill-button">Sklearn</div>
                                <div class="skill-button">Tensorflow</div>
                                <div class="skill-button">Keras</div>
                                """, unsafe_allow_html=True)

        with st.container():
            head_left, head_middle, head_right = st.columns([2, 1, 1])
            # Add the common header inside the container
            with head_left:
                st.markdown("""
                        <h3 style='text-align: left; background-color: rgba(218,165,32,0.1); border: 2px solid Goldenrod; border-radius: 10px; padding: 10px;'> 
                        Weather Data Analysis
                        </h3>
                        <h4>Project by <a href="https://course.acciojob.com/start-project?project=77f96d6b-7920-47a4-8eaf-1f4fcfa8b75d">AccioJobs</a></h4>
                        """, unsafe_allow_html=True)

            with head_middle:
                st.write("")
            with head_right:
                st.markdown("<h5 style='text-align: left; padding-top: 20px;'> April 2024 </h5>",
                            unsafe_allow_html=True)

            # Create three columns inside the container
            left_col, middle_col, right_col = st.columns([1, 2, 2])

            with left_col:
                st_lottie(weather, height='100%', width='100%', key="coder4")
            with middle_col:
                # Achievements
                st.markdown("<h3>Summary</h3>", unsafe_allow_html=True)
                st.markdown("""
                        - 	**Power BI Dashboard:** Constructed a Power BI dashboard, augmenting decision-making efficiency by **30%**.
                        
                        -	**Decision-Making:** Enabled informed decision-making, giving rise to **20%** improvement in resource allocation.
                        
                        -	**Conclusion Efficacy:** Built a Power BI dashboard, boosting conclusion efficacy by **30%**.
                            """
                            )
                st.markdown(
                    """<h5><a href='https://github.com/Gaurav-Wankhede/Weather-Analysis.git'>GitHub</a>
                    |
                    <a href="https://app.powerbi.com/groups/3eb1e7fb-b5b4-495d-8aad-8e79b57424a7/reports/f111e4b9-6aea-41a0-9d37-309db01cf381/ReportSection2ba2795d61b5728b3624?experience=power-bi">Dashboard</a>
                    </h5>
                    
                    
                    """,
                    unsafe_allow_html=True)

            with right_col:
                # Time Frame
                # Replace with the actual start and end months and years

                # Skills Used
                st.subheader("Skills Used")
                # Skills Used
                st.markdown("""
                                <div class="skill-button">Excel</div>
                                <div class="skill-button">Power BI</div>
                                <div class="skill-button">My SQL</div>
                                <div class="skill-button">MS PowerPoint</div>
                                """, unsafe_allow_html=True)

        with st.container():
            head_left, head_middle, head_right = st.columns([2, 1, 1])
            # Add the common header inside the container
            with head_left:
                st.markdown("""
                        <h3 style='text-align: left; background-color: rgba(218,165,32,0.1); border: 2px solid Goldenrod; border-radius: 10px; padding: 10px;'> 
                        Performance Monitor Automation
                        </h3>
                        <h4>Self Project</h4>
                        """, unsafe_allow_html=True)

            with head_middle:
                st.write("")
            with head_right:
                st.markdown("<h5 style='text-align: left; padding-top: 20px;'> March 2024 </h5>",
                            unsafe_allow_html=True)

            # Create three columns inside the container
            left_col, middle_col, right_col = st.columns([1, 2, 2])

            with left_col:
                st_lottie(lottie_coder, height='100%', width='100%', key="coder3")
            with middle_col:
                # Achievements
                st.markdown("<h3>Summary</h3>", unsafe_allow_html=True)
                st.markdown("""
                        - **Fetched:** Fetched system data using Python
                        
                        - **Stored:** Stored data in a SSMS database
                        
                        - **Visualized:** Visualized Realtime data using PowerBI
                            """
                            )
                st.markdown(
                    "<h5><a href='https://github.com/Gaurav-Wankhede/Performance-Monitor-Automation.git'>GitHub</a></h5>",
                    unsafe_allow_html=True)

            with right_col:
                # Time Frame
                # Replace with the actual start and end months and years

                # Skills Used
                st.subheader("Skills Used")
                # Skills Used
                st.markdown("""
                                <div class="skill-button">Python Programming</div>
                                <div class="skill-button">Power BI</div>
                                <div class="skill-button">MS SQL Server Management Studio</div>
                                """, unsafe_allow_html=True)

        # Create a container
        with st.container():
            head_left, head_middle, head_right = st.columns([2, 1, 1])
            # Add the common header inside the container
            with head_left:
                st.markdown("""
                        <h3 style='text-align: left; background-color: rgba(218,165,32,0.1); border: 2px solid Goldenrod; border-radius: 10px; padding: 10px;'> 
                        Amazon Web Scrapping 
                        </h3>
                        <h4>Self Project</h4>
                        """, unsafe_allow_html=True)

            with head_middle:
                st.write("")
            with head_right:
                st.markdown("<h5 style='text-align: left; padding-top: 20px;'> March 2024 </h5>",
                            unsafe_allow_html=True)

            # Create three columns inside the container
            left_col, middle_col, right_col = st.columns([1, 2, 2])

            with left_col:
                st_lottie(amazon, height='100%', width='100%', key="coder2")
            with middle_col:
                # Achievements
                st.markdown("<h3>Summary</h3>", unsafe_allow_html=True)
                st.markdown("""
                        - **Search:** Searched "Laptops" on Amazon.com
                        
                        - **Download:** Downloaded offline pages of Amazon
                        
                        - **Scrape:** Scrapped data and stored it in a CSV file
                                """
                            )
                st.markdown(
                    "<h5><a href='https://github.com/Gaurav-Wankhede/Amazon-Web-Scrapping.git'>GitHub</a></h5>",
                    unsafe_allow_html=True)

            with right_col:
                # Time Frame
                # Replace with the actual start and end months and years

                # Skills Used
                st.subheader("Skills Used")
                # Skills Used
                st.markdown("""
                                <div class="skill-button">Python Programming</div>
                                <div class="skill-button">Web Scrapping</div>
                                <div class="skill-button">Beautiful Soup</div>
                                <div class="skill-button">Csv</div>
                                <div class="skill-button">HTML</div>
                                """, unsafe_allow_html=True)

        # Create a container
        with st.container():
            head_left, head_middle, head_right = st.columns([2, 1, 1])
            # Add the common header inside the container
            with head_left:
                st.markdown("""
                <h3 style='text-align: left; background-color: rgba(218,165,32,0.1); border: 2px solid Goldenrod; border-radius: 10px; padding: 10px;'> 
                Accident Detection System with twilio 
                </h3>
                <h4>Third Year Engineering Mini-Project</h4>
                """, unsafe_allow_html=True)

            with head_middle:
                st.write("")
            with head_right:
                st.markdown("<h5 style='text-align: left; padding-top: 20px;'> October 2022 </h5>",
                            unsafe_allow_html=True)

            # Create three columns inside the container
            left_col, middle_col, right_col = st.columns([1, 2, 2])

            with left_col:
                st_lottie(accident, height='100%', width='100%', key="coder1")
            with middle_col:
                # Achievements
                st.markdown("<h3>Summary</h3>", unsafe_allow_html=True)
                st.markdown("""
                        - **ResNet-50 Model:** Improved experiment results, boosting the training accuracy of the **ResNet-50** model to **97%** to detect accidents.
                        
                        - **Image Training:** Educated the system on **500-600** images of accidents, achieving zero **false positives** during training.
                        
                        - **Safety Measures:** Fortified safety measures, encouraging to a **20%** reduction in emergency response time.
                        """)
                st.markdown(
                    """<h5><a href='https://github.com/Gaurav-Wankhede/Accident-Detection_And_Alerting_System.git'>GitHub</a>
                    |
                    <a href='https://github.com/Gaurav-Wankhede/Project-Report/blob/main/Accident.pdf'>Report</a>
                    </h5>
                                                                                                                                
                    """,
                    unsafe_allow_html=True)

            with right_col:
                # Time Frame
                # Replace with the actual start and end months and years

                # Skills Used
                st.subheader("Skills Used")
                # Skills Used
                st.markdown("""
                        <div class="skill-button">Python Programming</div>
                        <div class="skill-button">OpenCV</div>
                        <div class="skill-button">ResNet-50</div>
                        <div class="skill-button">InceptionResnetV2</div>
                        """, unsafe_allow_html=True)

        # Create a container
        with st.container():
            head_left, head_middle, head_right = st.columns([2, 1, 1])
            # Add the common header inside the container
            with head_left:
                st.markdown(
                    """<h3 style='text-align: left; background-color: rgba(218,165,32,0.1); border: 2px solid Goldenrod; border-radius: 10px; padding: 10px;'> 
                    Face Mask Detection
                    </h3>
                    <h4>Third Year Engineering Mini-Project</h4>
                    
                    """
                    ,
                    unsafe_allow_html=True)
            with head_middle:
                st.write("")
            with head_right:
                st.markdown("<h5 style='text-align: left; padding-top: 20px;'> March 2022 </h5>", unsafe_allow_html=True)

            # Create three columns inside the container
            left_col, middle_col, right_col = st.columns([1, 2, 2])

            with left_col:
                st_lottie(face_mask, height='100%', width='100%', key="coder")
            with middle_col:
                # Achievements
                st.subheader("Summary")
                st.markdown("""
                - **Accuracy Rate**: Gained a **98% accuracy rate** in the face mask detection project.
                
                - **Precision and Productivity**: Educated the system using **3833 images** to pinpoint correct mask-wearing, boosting precision by **15%** and productivity by **25%**.
                
                - **Algorithm Fine-Tuning**: Accomplished a **15% boost** in face mask detection accuracy by fine-tuning existing algorithms and integrating real-time feedback mechanisms.
                """)
                st.markdown("""<h5><a href='https://github.com/Gaurav-Wankhede/Face-Mask_Detection.git'>GitHub</a> 
                | 
                <a href="https://github.com/Gaurav-Wankhede/Project-Report/blob/main/Facemask.pdf">Report</h5>
                            
                            """,
                            unsafe_allow_html=True)

            with right_col:
                # Time Frame
                # Replace with the actual start and end months and years

                # Skills Used
                st.subheader("Skills Used")
                # Skills Used
                st.markdown("""
                <div class="skill-button">Python Programming</div>
                <div class="skill-button">MobilenetV2</div>
                <div class="skill-button">OpenCV</div>
                <div class="skill-button">TensorFlow</div>
                <div class="skill-button">Keras</div>
                <div class="skill-button">Numpy</div>
                <div class="skill-button">MatplotLib</div>
                
                """, unsafe_allow_html=True)


        # Create a container
        with st.container():
            st.markdown("""
                <h3 style='text-align: left; background-color: rgba(218,165,32,0.1); border: 2px solid Goldenrod; border-radius: 10px; padding: 10px;'> 
                Coming soon......
                </h3>
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
        
        - 🤖 I enjoy developing projects such as LLM (🏗️under construction) and participating at platforms like Kaggle 📈
        
        - 🏂 Also practicing Cooking, Video Games and Designing 🧗
        
        - 🏠 Boisar, Palghar, Maharashtra, 🧡🤍💚️India 
    """)

        st.subheader("Certificates")

        imgcol1, imgcol2= st.columns(2)

        with imgcol1:
            st.image(["./assets/certificate/html.png", "./assets/certificate/core_python.png", "./assets/certificate/Google_Analytics.png"])
        with imgcol2:
            st.image(["./assets/certificate/sql.png", "./assets/certificate/sql_intermediate.png", "./assets/certificate/Digital_Marketing.png"])


    elif selected == "Contact":
        st.header(":mailbox: Get In Touch With Me!")

        # Add a contact form
        contact_form = """
        <form action="https://formsubmit.co/pgywww@gmail.com" method="POST">
             <input type="hidden" name="_captcha" value="false">
             <input type="text" name="name" placeholder="Your name" required>
             <input type="email" name="email" placeholder="Your email" required>
             <textarea name="message" placeholder="Your message here"></textarea>
             <button type="submit">Send</button>
        </form>
        """

        st.markdown(contact_form, unsafe_allow_html=True)

        # Use Local CSS File
        def local_css(file_name):
            with open(file_name) as f:
                st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

        local_css("styles/style.css")

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
