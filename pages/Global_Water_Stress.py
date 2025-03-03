import streamlit as st
import pandas as pd
from PIL import Image
import plotly.express as px

df_wri_water_stress = pd.read_csv('data/wri_2030_water_stress_bau.csv')

bg = Image.open('images/water-stress-banner-0.png')
wri_im1 = Image.open('images/water_stress_2.png')
wri_im2 = Image.open('images/water_stress_3.png')
wri_im3 = Image.open('images/water_stress_4.png')
wd_im1 = Image.open('images/water_stress_5.png')
wd_im2 = Image.open('images/water_stress_6.png')
pl_img = Image.open('images/water_stress_7.png')
wri_im4 = Image.open('images/water_stress_8-1.png')
wri_im5 = Image.open('images/water_stress_8-2.png')
wri_im6 = Image.open('images/water_stress_8-3.png')

st.image(bg)
st.write('---')

# ================== Dashboard Main Panel =====================
col = st.columns((1.5, 4, 2.5), gap='small')

with col[0]:
    st.markdown('### What is Water Stress?')
    with st.expander('About', expanded=True):
        st.info('**Water stress, the ratio of water demand to renewable supply, measures the competition over local water resources.**')
        st.write('''
            :orange[**In simple words**]: Water stress occurs when the demand for water exceeds the available amount during a certain period or when poor quality restricts its use.
            ''')
    
    st.warning('😰 By 2050, an additional 1 billion people are expected to live with extremely high water stress!')

with col[1]:
    st.image(wri_im1, caption="Aqueduct projection by 2050")
    with st.expander('👆 About Image', expanded=True):
        st.markdown('''
        The 25 countries, home to a quarter of the global population, encounter extreme water stress each year, often depleting their water
        resources.
        :orange[With about 4 billion people—over 50% of the world—living under highly water-stressed conditions] for
        **at least a month annually**, the issue demands urgent attention!
    ''')

with col[2]:
    # container = st.container(border=True)
    with st.expander('About the Dataset 👇'):
        st.markdown('''
            #### :blue[Aqueduct Projected Water Stress Country Rankings by 2030]
            **Water stress indicates (here) how much water is withdrawn annually from different sectors compared to the total available blue water. A higher
            percentage signifies increased competition for this vital resource.**
            - *Scores between 0 and 1 indicate a value of Low (<10%), while scores between 4 and 5 indicate a value of Extremely High (>80%), and so on.*
        ''')

    st.dataframe(df_wri_water_stress, hide_index=True, width=None,
        column_config={
            "Rank": st.column_config.NumberColumn(
                "Rank",
            ),
            "Name": st.column_config.TextColumn(
                "Country",
            ),
            "All Sectors": st.column_config.NumberColumn(
                "All Sectors Rank",
            ),
            "Industrial": st.column_config.ProgressColumn(
                "Industrial Sector Rank 🏭",
                    format="%f",
                    min_value=0.00,
                    max_value=5.00,
            ),
            "Domestic": st.column_config.ProgressColumn(
                "Domestic Sector Rank 💧",
                    format="%f",
                    min_value=0.00,
                    max_value=5.00,
            ),
            "Agricultural": st.column_config.ProgressColumn(
                "Agricultural Sector Rank 🌾",
                    format="%f",
                    min_value=0.00,
                    max_value=5.00,
            )}
    ) 

    
    st.write(''':green-background[Aqueduct projected future country-level water stress for 2030 under a **business-as-usual (BAU)** scenario], where each country's
    water stress scores for each scenario and year are weighted by overall water withdrawals. Scores are also weighted by individual sectors such as
    agricultural, domestic, and industrial.''')


#====================== Tabs Interface ====================
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Water Stress Causes", "Freshwater Usage I", "Freshwater Usage II", "World's Crops Threatened",
"Water Stress Impacts Apparel Industry"])

with tab1:
    st.markdown('''
    ### 1. What's Causing Global Water Stress?

    - Across the world, demand for water is exceeding what’s available. :red[**Globally, demand has more than doubled since 1960.**]
    - :blue-background[Increased water demand is often the result of growing populations and industries like irrigated agriculture, livestock,
    energy production and manufacturing.]

    - The :orange[smaller the gap between supply and demand], the more vulnerable a place is to water shortages.
    - Meanwhile, *lack of investment in water infrastructure, unsustainable water use policies or increased variability due to climate change*
    can all affect the available water supply.
    ''')

    st.markdown('#### :blue[National Water Stress Rankings]')
    st.image(wri_im2)
    st.write('---')

    st.markdown('''
    ### 2. Which Countries Face the Worst Water Stress?

    - 25 countries shown above are facing extreme water stress, :orange[relying on more than **80% of their renewable water supply** for
    irrigation, livestock, industry, and domestic use.]
    
    - Even a short drought can put their water security at risk, sometimes resulting in drastic actions like shutting off water access,
    as seen in countries like **England, India, Iran, Mexico, and South Africa.**

    - :red-background[**Bahrain, Cyprus, Kuwait, Lebanon, Oman, and Qatar** are the six countries experiencing the most significant water
    stress. This issue arises mainly from a low available water supply combined with high demand from domestic, agricultural, and
    industrial uses.]
    
    ''')

    with st.expander('😲 The most water-stressed regions are with highest % of population exposed...'):
        met1, met2 = st.columns([1.5, 4])
        with met1:
            st.metric(label="Middle East and North Africa", value="83%")
            st.metric(label="South Asia", value="74%")
        with met2:
            st.image(wri_im3, width=800)

    st.warning('''
    - Global water demand is projected to increase by **20% to 25%** by 2050, while the number of watersheds facing high year-to-year variability,
    or less predictable water supplies, is expected to increase by 19%. That’s a problem not just for consumers and water-reliant industries,
    but for political stability.
    
    ''')


with tab2:
    st.markdown('''
    ### 1. Freshwater withdrawals by country

    - A growing global population and economic shift towards more resource-intensive consumption patterns means that
    global freshwater use has increased approximately six-fold since 1900.

    - **Water withdrawals** are defined as :green[freshwater taken from ground or surface water sources (such as rivers or lakes), either permanently
    or temporarily], and used for agricultural, industrial, or municipal (domestic) uses.
    ''')

    with st.expander('Breakdown of Total Freshwater Withdrawals...'):
        st.markdown('''
        #### :blue[Annual Freshwater Withdrawals by Country Over Time]

        Annual freshwater withdrawals refer to total water withdrawals, not counting evaporation losses from storage basins,
        measured in cubic metres (m³) per year. Withdrawals also include water from desalination plants in countries where
        they are a significant source.
        ''')

        #----------------------------- Freshwater Line Plot --------------------------
        # Load & cache the data to improve performance
        @st.cache_data  
        def load_freshwater_data(fp):
            df = pd.read_csv(fp)
            df = df.rename(columns={"Annual freshwater withdrawals, total (billion cubic meters)": "Annual freshwater withdrawals"})
            return df

        # Function to generate chart
        @st.cache_resource
        def create_freshwater_line_chart(data):
            """Generates a Plotly line chart of freshwater withdrawals."""
            fig = px.line(
                data,
                x="Year",
                y="Annual freshwater withdrawals",
                color="Entity",
                labels={"Annual freshwater withdrawals, total (billion cubic meters)": "Annual freshwater withdrawals"},
                height=600,
                markers=True,
                template="plotly_dark",
            )

            return fig

        # Loading & preparing the data
        df_wd = load_freshwater_data(fp="data/annual-freshwater-withdrawals.csv")

        countries = df_wd['Entity'].unique()
        default_countries = ['India', 'China', 'United States', 'Brazil']
        available_years = sorted(df_wd['Year'].unique().tolist())

        # Options to choose from for the user
        selected_countries = st.multiselect(
            "Select Countries:",
            options=countries,
            default=default_countries,
            help="Choose countries to display on the chart. Start with the defaults (India, China, United States, Brazil) and add or remove others."
        )

        if not selected_countries:
            st.warning("Please select at least one country to display.")
            # Stop further execution if no country is selected.
            st.stop()

        # Data filtering based on user selection
        filtered_df = df_wd[df_wd['Entity'].isin(selected_countries)]
        # Generates and displays the line chart
        if not filtered_df.empty:

            # Using .copy() to avoid SettingWithCopyWarning
            fig = create_freshwater_line_chart(filtered_df.copy())
            st.plotly_chart(fig)
        else:
            st.error("No data available for the selected countries and year range.")

    st.write('---')
    st.markdown('''
    ### :blue[2. Per capita Renewable water resources by region]

    - :green[**Renewable internal freshwater resources** refers to the quantity of internal freshwater from inflowing river basins
    and recharging groundwater aquifers.]

    - Renewable internal flows are, therefore, an **important indicator** of water security or scarcity. :orange[If rates of freshwater
    withdrawal begin to exceed the renewable flows, resources begin to decline.]

    *The chart shows the **average per capita** renewable freshwater resources across geographical regions, measured in **cubic meters per person per year**.*
    ''')

    #------------------- Renewable Freshwater Per Person Bar Chart ------------------
    @st.cache_data
    def load_renewable_data(fp):
        df = pd.read_csv(fp)
        return df

    @st.cache_resource
    def create_renewable_bar_chart(df_ren, entities):
        """Generates a Plotly bar chart of renewable freshwater per person."""
        ren_filtered_df = df_ren[df_ren['Entity'].isin(entities)]
        fig1 = px.bar(
            ren_filtered_df,
            x="Renewable internal freshwater resources per capita (cubic meters)",
            y="Entity",
            orientation='h',
            text="Renewable internal freshwater resources per capita (cubic meters)",
            template="plotly_dark",
        )
        fig1.update_traces(
            texttemplate="%{x:.2f}",
            textposition="outside",
        )
        fig1.update_layout(
            uniformtext_minsize=8, 
            uniformtext_mode='hide',
            plot_bgcolor='rgba(0,0,0,0)', # Remove background color to eliminate lines
            paper_bgcolor='rgba(0,0,0,0)' # Remove paper background color if it exists.
        )
        return fig1


    # Load the data
    df_ren = load_renewable_data(fp='data/per-capita-renewable-freshwater-resources.csv')

    # Default entities to display
    default_entities = ["Brazil", "Australia", "United States", "Austria", "World", "United Kingdom",
    "South Asia (WB)", "India", "Nigeria", "South Africa", "Bangladesh"]

    # Get list of all unique entities in dataset
    all_entities = sorted(df_ren['Entity'].unique().tolist())
    # Multi-select box for user to select entities. Defaults to the top entities
    selected_entities = st.multiselect(
        "Select entities to display:",
        options=all_entities,
        default=[entity for entity in default_entities if entity in all_entities]
    )

    # Generates and displays the bar chart
    if selected_entities:

        # Check if any entities are selected before creating the chart
        fig1 = create_renewable_bar_chart(df_ren, selected_entities)
        st.plotly_chart(fig1, use_container_width=True)
    else:
        st.warning("Please select at least one entity to display the chart.")


with tab3:
    st.markdown('''
    ### :blue[1.1 Freshwater use in agriculture]
    - :green[**Agricultural water** is defined as the annual quantity of self-supplied water withdrawn for irrigation,
    livestock and aquaculture purposes.]

    - Water is a vital resource for global agriculture, and it :orange[**constitutes approximately 70%** of freshwater withdrawals], whether
    sourced from rainfed systems or pumped irrigation.
    ''')
    
    with st.expander('However, this share varies significantly by country -- as shown in the below chart:'):
        st.markdown('''
        - *There are large variations geographically and by income level.* :orange[The average agricultural water use for **low-income countries
        is much higher than it is for high-income countries.**]
        ''')
        st.image(wd_im1)

    st.write('---')
    st.markdown('''
    ### 1.2 What share of agricultural land is irrigated?
    - **Irrigation**, the intentional water supply to agricultural land, has significantly contributed towards :green[increased crop yields
    in many countries over recent decades and has driven higher water usage in agriculture.]

    #### :blue[Share of agricultural land which is irrigated, 2001 to 2021]
    **The percentage of total agricultural land area which is irrigated** (i.e. purposely provided with water), **including land irrigated
    by controlled flooding.** Agricultural land is the combination of crop (arable) and grazing land.
    ''')

    #------------------- Share of agricultural land which is irrigated Line Chart Code -------------------
    @st.cache_data
    def load_agricultural_data(fp):
        df = pd.read_csv(fp)
        return df

    @st.cache_resource
    def create_agricultural_line_chart(agri_df, countries):
        """Creates a Plotly line chart for the share of agricultural land which is irrigated."""
        agri_df_filtered = agri_df[agri_df['Entity'].isin(countries)]
        
        fig2 = px.line(
            agri_df_filtered,
            x="Year",
            y="Agricultural irrigated land (% of total agricultural land)",
            color="Entity",
            labels={"Agricultural irrigated land (% of total agricultural land)": "in % of total agricultural land"},
            height=600,
            markers=True,
            # template="plotly_white",
        )
        return fig2


    # Load the data
    agri_df = load_agricultural_data(fp='data/agricultural-land-irrigation.csv')

    # Displays the irrigated line chart
    countries = ["Pakistan", "India", "Brazil", "Ghana"]
    fig2 = create_agricultural_line_chart(agri_df, countries)
    st.plotly_chart(fig2)
    st.write('---')

    st.markdown('''
    ### :orange[2. Industrial water withdrawals]
    **Water serves various industrial purposes, such as :green[dilution, steam generation, washing, and cooling of manufacturing equipment.]**
    It is also used as cooling water in fossil fuel and nuclear power plants and can be a byproduct of certain industrial processes.
    ''')
    st.image(wd_im2)
    st.info('''
    In contrast to the global distribution of agricultural water withdrawals, **industrial water usage tends to dominate in high-income
    countries and is small in low-income countries.**
    ''')


with tab4:
    st.markdown('''
    ### As per WRI analysis which shows that :orange[one-quarter of the world's crops are grown in areas where the water supply is highly stressed, highly unreliable or both.]
    
    - *Mounting risks like climate change and increased competition for water are threatening water supplies and, in turn, food security.*
    - :orange[Research shows the world will need to **produce 56% more food calories in 2050** than it did in 2010 to feed a projected
    10 billion people.]
    ---
    ''')
    st.image(wri_im4)

    st.markdown('''
    ### 1. Just a Handful of Countries Produce Most of the World's Irrigated Crops
    - 10 countries — *China, India, United States, Pakistan, Brazil, Egypt, Mexico, Vietnam, Indonesia, and Thailand* —
    **produce 72% of the world's irrigated crops**, including :orange[key staples such as sugarcane, rice, wheat, vegetables, cotton, and maize.]
    
    - With two-thirds of these crops facing high to extremely high water stress, this poses significant challenges for food security
    and global economies. :green-background[Irrigated crops are often “cash crops” exported to other nations.]
    ''')
    with st.expander("Let's Understand this better with charts!"):
        st.subheader(':blue[60% of Irrigated crops face high to extremely high water stress & over 70% are grown in just 10 countries]')
        ch1, ch2 = st.columns(2, gap="small")
        ch1.image(wri_im5)
        ch2.image(wri_im6)
        st.warning('''
        The demand for water to irrigate crops is projected to **rise by 16% by 2050, compared to 2019.**
        Warming temperatures are partially driving this trend. **The warmer it is, the thirstier crops become.**
        ''')
    
    st.write('---')
    st.markdown('''
    ### 2. Rainfed Agriculture Supplies Most of the World's Crops
    - The majority of the world's food — 66% of all crop production — still comes from rainfed agriculture.
    - As climate change leads to longer droughts and deforestation changes rainfall patterns, farmers will struggle to grow rainfed crops.
    :green[Currently, 8% of rainfed agriculture faces high to extremely high variations (by weight) in annual water supply.]

    - By 2050, :orange[**40% more rainfed crops will face unreliable water supplies** than in 2020, with the greatest increases
    **occurring in India, the U.S., Australia, Niger and China.**]
    ''')

with tab5:
    st.markdown('''
    ### :orange[The Price of Fashion]
    #### *How Water Stress Impacts Brands and Investors*

    - The apparel industry's **biggest water risks lie in its supply chain (raw material production, dyeing)**, not direct operations (retail stores).
    - Increasing water stress in manufacturing regions threatens textile production and can disrupt the flow of goods.
    - :green[Even minor water-related disruptions can significantly reduce profit margins for apparel companies.]
    - Brands face reputational risks if their water usage practices are perceived as unsustainable.
    - Standardized reporting of water usage *(including Scope 3 emissions)* is crucial for investors to assess and address water risks.

    #### :blue[Mapping Textiles Factories To Water Risk]
    The dashboard provides a geospatial snapshot of nearly 800 brands.
    - 👉 *You can interact with this dashboard live on: https://planet-tracker.org/ripple-effects-dashboard/*
    ''')
    st.image(pl_img)

    st.success('''
    #### Call to Action
    Investors must engage with apparel companies to promote sustainable water management and reduce water-related risks.
    ''')


st.markdown('---')
st.info('''
    ### 🔗 :rainbow[Sources]
    - [WRI Article](https://www.wri.org/insights/highest-water-stressed-countries)
    - [WRI Aqueduct Country Rankings Dataset](https://www.wri.org/data/aqueduct-40-country-rankings)
    - [Water Stress Definition](https://www.eea.europa.eu/archived/archived-content-water-topic/wise-help-centre/glossary-definitions/water-stress#:~:text=Water%20stress%20occurs%20when%20the,%2C%20dry%20rivers%2C%20etc.)
    - [Freshwater Usage Stats](https://ourworldindata.org/water-use-stress)
    - [WRI World's Crops Threatened Article](https://www.wri.org/insights/growing-water-risks-food-crops)
    - [Ripple Effects Report by Planet tracker](https://planet-tracker.org/wp-content/uploads/2024/02/Ripple-Effects.pdf)
''')