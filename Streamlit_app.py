import streamlit as st
import pandas as pd
from streamlit_agraph import agraph, Node, Edge, Config
import base64

# Define app name and title
app_name = "TF cascades"
st.set_page_config(page_title=app_name)

# Create a sidebar with tabs
# tabs = ["Introduction", "Dataset Viewer", "Transcription Factors", "Pathways", "Docs"]
# tab = st.sidebar.selectbox("Select a tab", tabs)

# Display app name and logo
# st.image("logo.png", width=100)

st.title(app_name)
with open("./KL_logo.jpg", "rb") as f:
    data = base64.b64encode(f.read()).decode("utf-8")
    st.sidebar.markdown(
        f"""
        <div style="display:flex;flex-direction: column;
  align-items: center;
  justify-content: center;">
            <img src="data:image/png;base64,{data}" width="100" height="100">
        </div>
        <div style="text-align: center;">
        <span style="font-weight: bold; font-size: 24px;">Khader Lab</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.sidebar.markdown("")


# Display introduction tab
if st.sidebar.button(":house: Home", use_container_width=True,type="primary"):

    st.image(image="./image1.png", caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

    # Display abstract
    st.markdown("""
    ## Abstract

    Transcription factors (TFs) play a vital role in the regulation of gene expression, making them critical to many cellular processes. In this study, we created a compendium of TF cascades using data extracted from the STRING database, resulting in a total of 81,488 unique TF cascades, with the longest cascade consisting of 62 TFs. Our results highlight the complex and intricate nature of TF interactions, with multiple TFs working together to regulate gene expression. We also identified 10 TFs with the highest regulatory influence based on centrality measurements, providing valuable information for researchers interested in studying specific TFs. Furthermore, our pathway enrichment analysis revealed significant enrichment of various pathways and functional categories, including those involved in cancer and other diseases, as well as development, differentiation, and cell signaling. The enriched pathways identified in this study may have potential as targets for therapeutic intervention in diseases associated with dysregulation of transcription factors. We have released the dataset, knowledge graph, and graphML methods for the TF cascades, and created a website to display the results, which can be accessed by researchers interested in using this dataset. Our study provides a valuable resource for researchers interested in understanding the complex network of interactions between TFs and their regulatory roles in cellular processes.
    
    - :point_right: Read our paper here:  https://www.biorxiv.org/content/...
    """)


    # Display links to dataset and website
    st.markdown("""
    ## Links

    - [Dataset](https://github.com/TFcascades/TFcascades)
    - [Website](https://tfcascades.github.io/)
    """)

# Display visualization tab
if st.sidebar.button(":mag_right: Dataset Viewer", use_container_width=True): 
    # Display metadata
    st.markdown("""
    ## Metadata 
    """)
    # Create a list of row numbers
    row_numbers = list(range(1, 81488))

    # Read csv file into dataframe
    df = pd.read_csv("./Data/TFChains_reindexed.csv")

    # Display original dataframe
    st.dataframe(df)

    # Use multiselect widget to let user choose row numbers
    selected_rows = st.multiselect("Select row numbers", row_numbers)

    # Filter dataframe based on selected row numbers
    filtered_df = df.loc[selected_rows]

    # Display filtered dataframe
    st.dataframe(filtered_df)



    # Display filtered dataframe
    st.markdown("""
    ## Visualization
    """)
    # Create empty list of nodes and edges
    nodes = []
    edges = []

    # Loop through each row of filtered dataframe
    for index, row in filtered_df.iterrows():
        # Loop through each transcription factor in row
        for i in range(len(row)):
            # Get transcription factor name
            tf = row[i]
            # Create node for transcription factor
            node = Node(id=tf, label=tf)
            # Append node to nodes list
            nodes.append(node)
            # Check if there is a next transcription factor in row
            if i < len(row) - 1:
                # Get next transcription factor name
                tf_next = row[i+1]
                # Create edge between transcription factors
                edge = Edge(source=tf, target=tf_next)
                # Append edge to edges list
                edges.append(edge)

    # Create config object for graph settings
    config = Config(width=800, height=600, directed=True)

    # Display graph using agraph function
    agraph(nodes=nodes, edges=edges, config=config)


# Display visualization tab
if st.sidebar.button(":bar_chart: EDA", use_container_width=True): 
    # Display metadata
    st.markdown("""
    ## EDA Report 
    """)
    st.components.v1.iframe("https://sonishsivarajkumar.github.io/TFCascades/", width=None, height=600, scrolling=True)


# Display visualization tab
if st.sidebar.button(":spiral_note_pad: Docs", use_container_width=True):
    # Display metadata
    st.markdown("""
    ## Download Links

    - [Dataset](https://github.com/sonishsivarajkumar/TFCascades)
    - [Website](https://tfcascades.streamlit.app/)
    """)

    st.markdown("""
    ## Exploratory Data Analysis(EDA) Report

    - [EDA](https://sonishsivarajkumar.github.io/TFCascades/)
    """)

    st.markdown("""
    ## Contact

    - Shameer Khader, PhD : skhadar@gmail.com
    - Sonish Sivarajkumar : sonish.sivarajkumar@gmail.com
    """)

# Display visualization tab
if st.sidebar.button(":floppy_disk: Download", use_container_width=True):
    # Display metadata
    st.markdown("""
    ## Download Links

    - [Dataset](https://github.com/sonishsivarajkumar/TFCascadess)
    - [Website](https://tfcascades.streamlit.app/)
    """)

    st.download_button(
    label="Download data as CSV",
    data="./Data/TFChains_reindexed.csv",
    file_name='large_df.csv',
    mime='text/csv',
)

st.sidebar.text('Last updated at 01:30 on 2023-06-26')

