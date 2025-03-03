import streamlit as st
from PIL import Image
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, AIMessage
import pymupdf as fitz
import os
from duckduckgo_search import DDGS

# MAIN APP BANNER
bg2 = Image.open('images/main-banner.png')
st.image(bg2)


# ---- PROMPT TEMPLATE ----
PROMPT_TEMPLATE = """You are an expert AI assistant providing summarized answers about water stress. Prioritize information from the provided PDF report to answer the user's question.
If the answer is not explicitly in the PDF report,  supplement with information from the web, preferencing results from the World Resources Institute (WRI), Food and Agriculture Organization (FAO), and the Water Footprint Network.

Respond concisely, summarizing key points from the report or web search.

Context from PDF: {pdf_context}
Web Search Results: {web_results}
User Question: {question}
"""

# ---- UTILITY FUNCTIONS ----
@st.cache_data
def get_pdf_context(pdf_path, query, num_pages=12):
    """Extracts relevant context from the PDF using PyMuPDF's search."""
    context = ""
    try:
        doc = fitz.open(pdf_path)
        for page_num in range(doc.page_count):
            page = doc.load_page(page_num)
            text_instances = page.search_for(query)  #PyMuPDF's search
            if text_instances:
                context += page.get_text()  #Add the whole page's text to the context
            if len(context) > 5000: #Stop after getting enough context
                break
        doc.close()
    except Exception as e:
        st.error(f"Error extracting context from PDF: {e}")
    return context


@st.cache_data
def web_search(query, num_results=3):
    """Searches the web using DuckDuckGo, preferencing specific sites."""
    preferred_sites = "site:wri.org OR site:fao.org OR site:waterfootprint.org"
    search_query = f"{query} {preferred_sites}"
    try:
        with DDGS() as ddgs:
            results = [r for r in ddgs.text(search_query, max_results=num_results)]
        return "\n".join([f"{r['title']}: {r['body']}" for r in results])  #Concatenate title & body
    except Exception as e:
        st.error(f"Web search failed: {e}")
        return "No web search results available."


@st.cache_resource
def generate_response(groq_api_key, final_prompt):
    """Generates the chatbot response using Groq."""
    try:
        model = ChatGroq(groq_api_key=groq_api_key, temperature=0.5, model_name="llama-3.3-70b-versatile", max_tokens=1024,)
        response = model.invoke(final_prompt)
        return response.content
    except Exception as e:
        st.error(f"Error generating response: {e}")
        return None


# =========== CHATBOT APP ===========
def chat_app():
    st.subheader('⭐ :rainbow[This app uncovers global and Indian perspectives through curated data, expert analysis, and AI-driven exploration.]')
    st.write('---')

    # ---- Chatbot UI ----
    st.title("AquaMind AI 🤖🧠")
    st.write('''
    ✨ *Provides concise summaries from the official reports and credible web sources when available. Get instant answers
    to your water-stress-related queries and quickly explore potential solutions.*
    
    You can ask questions such as ---
    - How does climate change exacerbate water scarcity?
    - What are some essential measures to address the worldwide water shortage?
    - What are some water conservation techniques that private households can implement?
    - What are the advantages and disadvantages of rainwater harvesting systems?
    ''')

    # Load PDF Report
    pdf_path = "data/sustainable-report.pdf"
    if not os.path.exists(pdf_path):
        st.error(f"PDF report not found: {pdf_path}")
        return

    # ---- API Key Input ----
    groq_api_key = st.text_input("Enter your Groq API key:", type="password")
    if not groq_api_key:
        st.warning("Please enter your Groq API key to use the chatbot!", icon='⚠️')
        return


    # Clear Chat History Button
    if st.button("Clear Chat History 🧹"):
        st.session_state.messages = [AIMessage(content="Hello! How can I help you with water-stress related queries?")]
        st.success("Chat history is now cleaned! 🎉")


    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state["messages"] = [AIMessage(content="Hello! How can I help you with water-stress related queries?")
]

    # Display chat messages
    for msg in st.session_state.messages:
        if isinstance(msg, AIMessage):
            st.chat_message("assistant").write(msg.content)
        elif isinstance(msg, HumanMessage):
            st.chat_message("user").write(msg.content)
    # Chatbot Input
    if prompt := st.chat_input():
        st.session_state.messages.append(HumanMessage(content=prompt))
        st.chat_message("user").write(prompt) #Displays what user typed

        #---- Building Response ----
        with st.spinner("Generating Answer..."):
            #---- Search PDF  ----
            pdf_context = get_pdf_context(pdf_path, prompt) # Search based on User prompt
            #---- Web Search Fallback ----
            web_results = ""
            if not pdf_context:  # Only search if PDF doesn't have the answer
                web_results = web_search(prompt)

            #---- Creating Prompt ----
            final_prompt = PROMPT_TEMPLATE.format(
                pdf_context=pdf_context,
                web_results=web_results,
                question=prompt
            )
             #---- Groq LLM Integration ----
            response_content = generate_response(groq_api_key, final_prompt)

            if response_content:
                st.session_state.messages.append(AIMessage(content=response_content))  # Append response to messages
                st.chat_message("assistant").write(response_content)  # Displays bot output


chat_app()