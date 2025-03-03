# 🌏 Unraveling the Water Crisis

## Overview

The growing specter of water scarcity threatens ecosystems, economies, and communities worldwide. While understanding this complex problem and its potential solutions is crucial, sifting through dense, technical reports and navigating fragmented information across numerous official websites can be incredibly time-consuming. Even AI-generated data visualizations often require expert knowledge to interpret effectively.

This app provides a **streamlined, time-savvy, and ethically-sourced solution, designed for researchers, educators, and concerned citizens who need concise insights and actionable data on global water stress.** It brings together curated data, analyzes key impacts, and discovers pathways to a sustainable water future — all in one place. Also, it **includes a powerful AI chatbot, AquaMind,** to answer specific questions related to water stress and accelerate your understanding. Powered by Deepnote, the app offers a robust and collaborative environment for exploring critical water-related issues.


## ⭐ Key Features

- **Global Water Stress:** Explore insights from the WRI Aqueduct Water Risk Atlas, visualize freshwater use and stress data, and analyze the impact of cotton production and global crop conditions in water-stressed regions. The visualization combines interactive plots and illustrative images to highlight critical trends. Links to credible websites such as WRI, Food and Agriculture Organization (FAO), The Water Footprint Network, and many more are also available.

- **Water Stress Conditions in India:** Delve into the specific challenges facing India, examining extreme water stress conditions, unsustainable cotton farming practices, textile disposal issues, and the impact of textile production and dyeing. Discover mitigation initiatives from BCI and other organizations through illustrative images & insights.

- **AquaMind AI Chatbot:** Ask questions and receive summarized answers based on the curated information from an official report. This intelligent chatbot can provide a better output by utilizing web data from credible sites when a more relevant answer from the PDF report is not available, and the AI chatbot will search and provide answers.


## ⚙ How It Works

- The app contains compiled data from official sources, including the World Resources Institute (WRI), the Food and Agriculture Organization (FAO), Planet Tracker, the USDA IPAD, and many more to provide a comprehensive overview of the global water crisis.
- Key trends and impacts are presented through interactive plots (recreated) & illustrative images, allowing users to explore the data in a dynamic and engaging way.
- The AquaMind chatbot uses the **Groq's `llama-3.3-70b-versatile` Llama 3** language model API to answer user questions. It prioritizes information from the provided **PDF report [here](https://pmc.ncbi.nlm.nih.gov/articles/PMC10300917/pdf/membranes-13-00612.pdf).** When needed, it supplements its knowledge with web search results from credible sources like WRI, FAO, and the Water Footprint Network, through *DuckDuckGo Search API*.
    - ⚠ **NOTE:** *Due to occasional API rate limits imposed by DuckDuckGo, web search functionality may be temporarily unavailable or return incomplete results. It is recommended to try your query again later if you encounter this issue.*

## 🛠 Tech Stack Used
- Streamlit
- Pandas
- Ploltly
- Langchain
- Groq API
- DuckDuckGo Search API
- PyMuPDF
