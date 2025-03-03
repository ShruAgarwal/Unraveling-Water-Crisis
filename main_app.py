import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Unraveling Water Crisis",
    page_icon="🌏",
    layout="wide",
    initial_sidebar_state="expanded")


# APP SIDEBAR ==============
with st.sidebar:

    st.markdown(
        """
         **👀 How to use:**
        1. Navigate the top pages to switch different sections.
        2. Hover over to interact with Plotly charts for details.
        3. Enter your Groq API key to activate the AquaMind AI chatbot for
        instant answers about the water crisis.
        
        4. Click "Clear Chat History" to start a new chat.
        
        ---
        """
    )

# APP'S PAGES ===============
water_stress_page = st.Page(
    "pages/Global_Water_Stress.py",
    title="Global Water Stress",
    icon="🌐",
)

cotton_prod_page = st.Page(
    "pages/Water_Stress_in_India.py",
    title="Exploring Water Stress In India",
    icon="💧",
)

main_page = st.Page(
    "pages/AI_Chatbot.py",
    title="AquaMind AI",
    icon="🤖",
    default=True,
)

pg = st.navigation([water_stress_page, cotton_prod_page, main_page])

pg.run()