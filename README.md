# 🌏 Unraveling the Water Crisis
> *Project developed during [Deepnote x Streamlit Data App Challenge 2025](https://deepnote.com/app/deepnote/Deepnote-x-Streamlit-challenge-5c932eff-a979-47bd-a5ec-dbd7bcaa5f05)*

## ✨ Overview

The growing specter of water scarcity threatens ecosystems, economies, and communities worldwide. While understanding this complex problem and its potential solutions is crucial, sifting through dense, technical reports and navigating fragmented information across numerous official websites can be incredibly time-consuming. Even AI-generated data visualizations often require expert knowledge to interpret effectively.

This app provides a ***streamlined, time-savvy, and ethically sourced solution designed for researchers, educators, and concerned citizens who need concise insights and actionable data on global water stress.*** It brings together curated data, analyzes key impacts, and discovers pathways to a sustainable water future — all in one place.
 - For example, our analysis of data from **"Our World in Data" revealed a strong relationship** between the increasing share of agricultural land under irrigation and accelerated groundwater depletion in South Asia and the Middle East. This **trend is visually represented** in our recreated interactive line chart, highlighting the growing pressure on water resources in these regions.

Also, it **includes a powerful AI chatbot, AquaMind,** to answer specific questions related to water stress and accelerate your understanding. Powered by Deepnote, the app offers a robust and collaborative environment for exploring critical water-related issues.


## ⭐ Key Features

- **Global Water Stress:** Explore insights from the WRI Aqueduct Water Risk Atlas, interactive charts to visualize freshwater use and stress data, and analyze the impact of cotton production and global crop conditions in water-stressed regions through illustrative images. Links to credible websites such as the World Resources Institute (WRI), The Water Footprint Network, and many more are also available.

- **Water Stress Conditions in India:** Delve into the specific challenges facing India, examining extreme water stress conditions, unsustainable cotton farming practices, textile disposal issues, and the impact of textile production and dyeing. Discover mitigation initiatives from BCI and other organizations through illustrative images & insights.

- **AquaMind AI Chatbot:** Ask questions and receive summarized answers based on the curated information from an official report. Try asking, "What are some essential measures to address the worldwide water shortage?" This intelligent chatbot prioritizes information from the provided PDF report but can also leverage web data from credible sites like WRI, FAO, and the Water Footprint Network, to provide a more enhanced output.


## 🕹 Quick App Tour

Dive deeper into the water crisis visually through **[this short video!](https://www.canva.com/design/DAGgxHZigdE/Ze6wFXvShKXfdAqlnuPo2A/watch?utm_content=DAGgxHZigdE&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=h079c0d71bd)**


## ⚙ How It Works

- Pages of the app contain compiled data from official sources, including the WRI, FAO, USDA's IPAD, UN-WATER, and many more to provide a comprehensive overview of the global water crisis. It also highlights the reported connections between textile dyeing processes and levels of water pollution, referencing data from Planet Tracker and similar organizations.

- Key trends and impacts are presented through interactive plots (recreated) & illustrative images, allowing users to explore the data in a dynamic and engaging way.

- The AquaMind chatbot uses the **Groq's `llama-3.3-70b-versatile` Llama 3** language model API to answer user questions. It prioritizes information from the provided **PDF report [here!](https://pmc.ncbi.nlm.nih.gov/articles/PMC10300917/pdf/membranes-13-00612.pdf)** When needed, it supplements its knowledge with web search results from credible sources like WRI, FAO, and the Water Footprint Network, through *DuckDuckGo Search API*.
    - ⚠ **NOTE:** *Due to occasional API rate limits imposed by DuckDuckGo, web search functionality may be temporarily unavailable or return incomplete results. It is recommended to try your query again later if you encounter this issue.*


## 🛠 Tech Stack Used
- Streamlit
- Pandas
- Plotly
- Langchain
- Groq API
- DuckDuckGo Search API
- PyMuPDF


## 💪 Overcoming the Hurdles

Building this app involved navigating several key challenges:

- **Data inconsistencies** across diverse sources like the WRI, Planet Tracker, UNESCO, and others, required careful harmonization using standardized units.

- Addressing **data scarcity** in specific regions meant prioritizing readily available information.

- Rigorously evaluated **data accuracy and reliability**, transparently documenting source limitations.

-  **LLM optimization** was vital; I experimented with prompt engineering to enhance performance within budget constraints, while allowing users to provide their own API keys to avoid relying solely on the project’s resources.

- Finally, I **prioritized ethical considerations** at every step, carefully vetting data sources to minimize misinformation and bias, and diligently avoided scope creep by focusing on core features.


## 🚀 Further Steps

1. **"What You Can Do?" Section:** To add a section with concrete actions that individuals and organizations can take to address the water crisis.

2. **AquaMind Chatbot Structure Refinement:** Refactor the chatbot logic into a more formal AI Agent structure using [Agno](https://www.agno.com/) library for improved planning, tool selection for PDF and web search, and error handling.

3. **Source Citations:** Implement automatic citation of sources (report page numbers or web URLs) within the chatbot's responses to enhance transparency and trust.

4. **AI-Generated Glossary:** Leverage the chatbot to assist in generating a glossary of key terms related to water-crisis, textile production, and agriculture.

5. **User Feedback Mechanism:** Add a simple feedback system (e.g., thumbs up/down) to gather user input on the accuracy and relevance of chatbot responses for future improvements.
