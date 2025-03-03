import streamlit as st
from PIL import Image

bg1 = Image.open('images/water-stress-banner-1.png')
cp_im1 = Image.open('images/water_stress_9.png')
cp_im2 = Image.open('images/water_stress_10.png')
cp_im3 = Image.open('images/water_stress_11.png')
cp_im4 = Image.open('images/water_stress_12.png')
cp_im5 = Image.open('images/water_stress_13.png')
cp_im6 = Image.open('images/water_stress_14-1.png')
cp_im7 = Image.open('images/water_stress_14-2.png')
cp_im8 = Image.open('images/water_stress_14-3.png')
cp_im11 = Image.open('images/water_stress_16.png')
cp_im12 = Image.open('images/water_stress_17.png')
cp_im13 = Image.open('images/water_stress_18.png')
cp_im14 = Image.open('images/water_stress_18-1.png')
cp_im15 = Image.open('images/water_stress_18-2.png')
cp_im16 = Image.open('images/water_stress_18-3.png')
cp_im17 = Image.open('images/water_stress_18-4.png')

#---------------------------------------------------
st.image(bg1)

st.write('---')
st.success('''
    ✨ *This page examines the multifaceted water challenges facing India, from unsustainable agricultural practices to the impacts of the
    textile industry, and explores potential solutions for a more water-secure future. We'll delve into the state of cotton production,
    the environmental consequences of textile dyeing, and the role of sustainable initiatives in mitigating water stress.*
''')

# ====================================================
t1, t2, t3, t4 = st.tabs(["Widespread Water Stress 🚱💧", "Unsustainable Cotton Practices 😲",
"The Apparel Industry Effects 👕👖", "Path Towards Sustainability 🌱"])

with t1:
    st.markdown('''
        ### :orange[1. Extremely High Water Stress]
        - :green[**54% of India faces significant water stress**, meaning over 40% of available surface water is used annually.]
        This puts nearly 600 million people at risk of supply disruptions.

        - **Northwest India Hotspot:** This crucial agricultural region, responsible for a large share of India's grain production,
        experiences particularly intense water stress.
        - The :blue[**states of Punjab and Haryana alone produce 50% of the national government's rice supply and 85% of its wheat stocks.**]
        Both crops are highly water intensive.

        📌 The map below illustrates competition between companies, farms and people for surface water in rivers, lakes, streams, and shallow groundwater.
    ''')
    st.image(cp_im1, width=600)
    st.write('---')

    with st.expander('😰Deep diving insights...'):

        ind1, ind2 = st.columns(2, gap="small")
        with ind1:
            st.markdown('''
                ### :green[2. Groundwater Depletion]
                - :blue[**54% of India's monitored groundwater wells are showing declining water levels, with 16% declining by over 1 meter per year.**]
                - **Unsustainable Agricultural Practices:** Government subsidies for electric pumps and a lack of extraction limits contribute to
                excessive groundwater use.

                - :green[58% of monitored wells in Northwest India show declining groundwater levels], further stressing this critical region.
            ''')
            st.image(cp_im2, width=600)

        with ind2:
            st.markdown('''
                ### 3. Water Quality Concerns
                - **Unsafe Drinking Water:** A majority of India's groundwater districts (573 out of 632) have pollutant levels
                exceeding national safety standards.

                - :blue[Over 130 million people live in districts with **unsafe drinking water due to excessive chlorine, fluoride,
                iron, arsenic, nitrate, and/or electrical conductivity.**]
                - 8 districts have at least three pollutants exceeding safe limits, impacting over 20 million people.
            ''')
            st.image(cp_im3, width=600)
            st.warning('''
            **Bagalkot, Karnataka**, is the most polluted, with five of six groundwater quality indicators at unsafe levels. Only arsenic falls
            below the government-recommended concentration level.
            ''')
    st.write('---')
    st.markdown('''
    ### :blue[4. Global Food Trade and Water Stress: A Looming Crisis]
    - 📌 **This analysis explores the interconnectedness of global food trade and water resources, highlighting the significant water footprint
    of various food products and the risks posed by water stress in major producing regions.**

    - Understanding these global dynamics is crucial for context as we delve into India's specific water challenges, where similar pressures
    on water resources are evident within its agricultural and textile sectors.

    - :orange[**The increasing global demand for food, including water-intensive crops like cotton, nuts, and meat, exerts pressure on water resources,
    particularly in water-stressed regions, impacting both local communities and global supply chains.**]

    - This poses a **growing risk**, particularly in major exporting countries like the USA and India, where a substantial portion of crop
    production occurs in already water-stressed regions.
    ''')
    st.success('''
    👉 **For a deeper dive into these issues, explore the full report by Planet Tracker [here](https://planet-tracker.org/stressing-about-water-footprints/)**. Learn more about **water footprints and
    sustainable solutions** at the **Water Footprint Network [here](https://www.waterfootprint.org/)**
    ''')


with t2:
    st.markdown('''
    ### :orange[1. The State of Cotton Production]
    - **Cotton is a crucial & thirsty cash crop of India**, covering about **34% of the global area under cultivation, supporting
    roughly 60 million livelihoods**, and contributing significantly to the economy and foreign exchange earnings.  

    - :blue[Approximately 70% of cotton cultivation in India is rain-fed, making it **vulnerable to variable rainfall patterns
    and pest infestations, particularly from bollworm and sucking pests.**]

    - Despite occupying only 5% of total cultivable land, **cotton farming consumes around 50% of India's pesticide use**, highlighting
    its impact on sustainable production.  
    - :green[**Economic challenges include inefficiencies in production processes, such as seed selection, harvesting methods, and post-harvest
    storage and transportation.**]

    👉 *You can view more detailed visualizations on cotton production for specific Indian states at*
    **[USDA's IPAD Cotton Explorer](https://ipad.fas.usda.gov/cropexplorer/cropview/comm_chartview.aspx?fattributeid=1&cropid=2631000&sel_year=2024&startrow=1&ftypeid=47&regionid=sasia&cntryid=IND)**
    ''')
    st.image(cp_im5)
    st.write('---')

    st.markdown('''
    ### :green[2. The Environmental Impacts]
    - :blue[**Excessive use of water, pesticides, and fertilizers leads to soil and water contamination, impacting human health and the environment.**]
    - The form of trash mixed with cotton during harvesting and processing negatively impacts the environment.
    - Inefficient choices in seeds, harvesting techniques, and post-harvest storage lead to economic losses and environmental strain.
    - :blue[**Intensive farming practices contribute to soil erosion and reduced soil fertility**, jeopardizing long-term
    agricultural productivity.]
    
    - Runoff from fields carries pesticides and fertilizers into water sources, polluting rivers and groundwater.
    - Over-reliance on irrigation depletes water resources and can lead to increased soil salinity.
    - :red[**The entire cotton production and processing chain contributes to greenhouse gas emissions, exacerbating climate change.**]
    ''')

    with st.expander('⭐ An important insight...'):
        st.info('*Monoculture cotton farming and pesticide use can harm beneficial insects and other wildlife, reducing biodiversity.*')
        cp_im10 = Image.open('images/water_stress_15-2.png')
        st.image(cp_im10, width=800)

    st.write('---')
    st.markdown('''
    ## 3. What is the Cotton Value Chain?
    In the Indian context, the cotton value chain encompasses all the stages involved in cotton production, from growing the crop on the farm
    to the final consumer product.
    - :orange[*This includes: **farming, aggregation, ginning and pressing, spinning, weaving/knitting, dyeing and finishing, garment manufacturing,
    and retail.** Each stage has its own environmental and social impacts.*]
    ''')
    st.image(cp_im4)
    st.info('''It is observed that *while the **small-scale sector is largely unorganised and labour-intensive, large-scale enterprises
    are mostly organised** and capital-intensive.*''')


with t3:
    st.markdown('''
    ### :blue[1. Water's Crucial Role & Growing Risks in Textile Sector]
    - **Heavy Footprint:** Wet processing (dyeing, finishing) is the most polluting stage of textile production, using significant amounts of
    water and chemicals. It requires an :orange[estimated **430 liters of water to produce 1 kg of fabric and uses around 8,000 toxic chemicals.**]

    - **740 publicly listed wet processing companies** are identified, mostly in emerging markets facing water stress.
    - :red[**51 companies with a combined market cap of USD 29 billion are ranked "High" or "Extremely High" water risk.**]

    - **Wet processing companies are financially weaker than retail brands** (lower returns on assets, EBIT margins, and higher debt),
    making it difficult for them to fund transitions to sustainable practices without support.
    ''')

    with st.expander('👇 Look below to understand better:', expanded=True):
        tex1, tex2 = st.columns([3, 2.5])
        with tex1:
            st.info('''
            *The textiles supply chain often consists of tens or even hundreds of independent companies in a complex network co-ordinated
            by textile orders from the brand owner or end retailer.*''')
            st.image(cp_im6)
            st.image(cp_im8)
        with tex2:
            st.info('**India ranks first, with 25% of the wet processing factories identified. Pakistan came second with only 7%.**')
            st.image(cp_im7)

    st.write('---')
    st.markdown('''
    ### 2. Apparel Industry's Overlooked Water Risks
    - **Limited Disclosure:** 90% of analyzed documents from apparel companies barely mention water-related risks, despite
    their significant water footprint.
    - :orange[While *mentions of water risk have risen from 2,000 disclosures (2018) to 9,000 (2022)*, the **quality of disclosures
    remains flat.**]
    - :red[**Non-luxury brands discuss water risk more than luxury brands or retailers.**]
    - Most water risk mentions are found in sustainability and annual reports, rarely in investor transcripts, suggesting investor indifference.
    ''')
    with st.expander('👇 Look below to understand better:'):
        tex3, tex4 = st.columns(2, gap="small")
        st.info('''
            #### What's apparel's future?
            *Apparel spending is projected to grow tremendously. This is particularly true in Asia, as hundreds of millions of people
            in **China and India** enter the global middle class.*
        ''')
        with tex3:
            st.image(cp_im12)
        with tex4:
            st.image(cp_im11)
    
    st.write('---')
    st.warning('### 🎯 Some stories you should read from India')
    with st.expander('👇Explore below...'):
        c1, c2, c3, c4 = st.columns(4, gap="medium")
        with c1:
            st.markdown('''
            As textile waste continues to contaminate communities and the environment, **green entrepreneurs are coming up with innovative
            solutions to bring down the volumes of annual waste**.

            #### 💠 [READ MORE](https://www.fairplanet.org/story/walking-the-runway-towards-a-regenerative-fashion-economy/)
            ''')
        with c2:
            st.success('''
            Surat's textile industry is improving its manufacturing processes by efficiently using coal, electricity, and water,
            and adopting renewable energy to combat climate change and enhance sustainability.

            #### 🦎 :rainbow[[READ MORE](https://india.mongabay.com/2024/02/stitching-sustainability-amidst-climate-change-challenges/)]
            ''')
        with c3:
            st.markdown('''
            Second-hand clothes are refurbished in the **textile hub of India's Panipat**, but *toxic byproducts of the seemingly sustainable
            process have polluted the region's air and water.*

            #### 💠 [READ MORE](https://www.fairplanet.org/story/voices-from-panipat-condemn-clothes-recyclers-for-polluting-air-and-water/)
            ''')
        with c4:
            st.success('''
            Experts assert that changing consumer mindsets is crucial for encouraging the adoption of naturally dyed products.
            Sellers of natural dyes should educate consumers about the temporary nature of these dyes to foster a greater
            appreciation for them.

            #### 🦎 :rainbow[[READ MORE](https://india.mongabay.com/2023/10/to-dye-or-not-to-dye-the-fashion-industrys-natural-dye-conundrum/)]
            ''')

    
with t4:
    with st.expander('🤔 How is India responding to all these challenges?'):
        st.markdown('''
        - **Government Initiatives:** While India has various policies and regulations (**National Textile Policy 2000, Technology Mission on
        Cotton**), there's a lack of direct crop-specific policies for cotton sustainability.
        
        - Technology Mission on Cotton (TMC) program aims to improve productivity, develop new technologies, transfer knowledge to farmers,
        improve marketing infrastructure, and enhance seed cotton processing.

        - :orange[**Regulations on Hazardous Inputs:** Regulations exist for managing hazardous microorganisms and genetically engineered
        organisms (GMOs), and the **use of certain pesticides is restricted or banned**. *Integrated Crop Management (ICM) and
        Integrated Pest Management (IPM) are promoted.*]
        ''')

    st.markdown('''
    ### :green[1. The Impact Of the Better Cotton Initiative (BCI) Program]  
    - :blue[**53% reduction in total reported pesticide use by Better Cotton farmers from the 2014-2016 average to 2021-22.
    Highly Hazardous Pesticide (HHP) use dropped from 64% to 10%.**]
    
    - Better Cotton farmers achieved higher yields (650 kg/ha ) than the national average (449 kg/ha ) in 2021-22.
    - Better Cotton farmers showed decreased irrigation water use per hectare and per metric ton of lint, indicating improved efficiency.
    - Farmer Profitability: Production costs decreased, while profits increased due to higher yields and better market access.
    - Women's Empowerment: Efforts are ongoing to increase women's participation in training, decision-making, and access to resources.
    ''')
    st.image(cp_im13)
    st.image(cp_im15)
    st.image(cp_im16)
    st.image(cp_im14)
    
    st.write('---')
    st.info('''
    ⭐ **The blue water footprint** measures the amount of freshwater used in crop production, while the **green water footprint** refers
    to the total rainfall or soil moisture utilized to grow plants. The **grey water footprint** indicates the volume of water needed
    to dilute pollutants to ambient meet quality standards.
    ''')
    st.markdown('''
    ### :orange[2. Toward Sustainable Water Use in the Cotton Supply Chain]  
    - **Organic Farming:** While having the **lowest grey water footprint, organic cotton currently has lower yields.**
    Increasing yields is crucial for making organic cotton the most sustainable option.

    - **REEL Cotton:** Demonstrates good performance in terms of reduced water pollution and high yields, making it a promising
    interim solution.
    - **Irrigation Efficiency:** Irrigation accounts for a small percentage (2-9%) of total water use, but drip irrigation showed
    a 12% reduction in blue water footprint compared to furrow irrigation.
    
    - **Grey Water Footprint Variation:** :blue[Conventional farming has a significantly higher grey water footprint than
    REEL and organic, with wide variation across farms and states. Optimizing pesticide and fertilizer use is essential for
    reducing pollution.]

    *The below figure shows -- Combining the three agricultural practices within each state, provides further insight into the
    variations in cotton production between states.*
    ''')
    st.image(cp_im17)

    
st.write('---')
st.info('''
    ### 🔗 :rainbow[Sources]
    - [3 Maps Explain India's Growing Water Risks, an article by WRI](https://www.wri.org/insights/3-maps-explain-indias-growing-water-risks)
    - [India's Cotton Production Area Map & Yield chart by USDA IPAD](https://ipad.fas.usda.gov/countrysummary/Default.aspx?id=IN&crop=Cotton)
    - [Environmental Sustainability Challenges in India's Cotton Value Chain Paper by CUTS Citee](https://cuts-citee.org/pdf/Briefing_Paper13-Environmental_Sustainability_Challenges_in_Cotton_Value_Chain-How_is_India_Responding_to_these_Challenges.pdf)
    - [Exposing Water Risk Report by Planet Tracker](https://planet-tracker.org/wp-content/uploads/2024/01/Exposing-Water-Risk.pdf)
    - [The Apparel Industry's Environmental Impact in 6 Graphics, an insight article by WRI](https://www.wri.org/insights/apparel-industrys-environmental-impact-6-graphics)
    - [Better Cotton Initiative (BCI) India Impact Report from 2014-2023](https://bettercotton.org/field-level-results-impact/demonstrating-results-and-impact/farmer-results/)
    - [Toward Sustainable Water Use in the Cotton Supply Chain, an assessment by Water Footprint Network](https://waterfootprint.org/resources/Assessm_water_footprint_cotton_India.pdf)

    ### 📖 :rainbow[A Few Interesting Deep Dives]
    - [How Water Challenges Threaten India’s Energy Security, an article by WRI](https://www.wri.org/insights/water-challenges-energy-sector-india)
    - [Hannah Ritchie, Fiona Spooner and Max Roser (2019) - “Clean Water”](https://ourworldindata.org/clean-water)
    - [Cotton Production and Environmental Sustainability in India Report by CUTS Citee](https://cuts-citee.org/pdf/Reasearh-Report-Cotton_Production_and_Environmental_Sustainability_in_India.pdf)
    - [Will Fashion Dye Another Day? Report by Planet Tracker](https://planet-tracker.org/wp-content/uploads/2021/07/Will-Fashion-Dye-another-Day.pdf)
    - [The Innovative Business Models That Can Transform Cotton Supply Chains, an article by WRI](https://www.wri.org/technical-perspectives/innovative-business-models-can-transform-cotton-supply-chains)
    - [Need of the Hour - Ethical and Responsible Cotton Production in India, a publication by CAI](https://cicr.org.in/wp-content/uploads/PA_64_ethical_usha.pdf)
''')