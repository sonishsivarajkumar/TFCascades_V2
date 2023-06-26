import streamlit as st
import pandas as pd
from streamlit_agraph import agraph, Node, Edge, Config
import time

# Define app name and title
app_name = "TF cascades"
st.set_page_config(page_title=app_name)

# Create a sidebar with tabs
tabs = ["Introduction", "Dataset Viewer", "Transcription Factors", "Pathways", "Docs"]
tab = st.sidebar.selectbox("Select a tab", tabs)

# Display app name and logo
# st.image("logo.png", width=100)
st.title(app_name)

# Display introduction tab
if tab == "Introduction":
    # Display abstract
    st.markdown("""
    ## Abstract
    """)

    # Display links to dataset and website
    st.markdown("""
    ## Links

    - [Dataset](https://github.com/TFcascades/TFcascades)
    - [Website](https://tfcascades.github.io/)
    """)

    # Display a carousel of 3 images at the center
    st.markdown("""
    <style>
    .carousel {
      position: relative;
      width: 800px;
      height: 600px;
      margin: auto;
    }

    .carousel img {
      position: absolute;
      width: 800px;
      height: 600px;
      opacity: 0;
      transition: opacity 1s ease-in-out;
    }

    .carousel img.active {
      opacity: 1;
    }
    </style>

    <div class="carousel">
      <img src="./image1.png" class="active">
      <img src="./image2.png">
      <img src="./image3.png">
    </div>

    <script>
    // Get the images and the index
    var images = document.getElementsByClassName("carousel")[0].children;
    var index = 0;

    // Define a function to show the next image and hide the others
    function showNextImage() {
      for (var i = 0; i < images.length; i++) {
        if (i == index) {
          images[i].classList.add("active");
        } else {
          images[i].classList.remove("active");
        }
      }
      // Increment the index and wrap around if needed
      index = (index + 1) % images.length;
    }

    // Set an interval to call the function every 2 seconds
    setInterval(showNextImage, 2000);
    </script>
    """, unsafe_allow_html=True)

# Display visualization tab
elif tab == "Dataset Viewer":
    # Display metadata
    st.markdown("""
    ## Metadata 
    """)
    # Create a list of row numbers
    row_numbers = list(range(1, 81488))

    # Read csv file into dataframe
    df = pd.read_csv("../Data/TFChains_reindexed.csv")

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
elif tab == "Docs":
     # Display metadata
     st.markdown("""
     ## Download Links

     - [Dataset](https://github.com/TFcascades/TFcascades)
     - [Website](https://tfcascades.github.io/)
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
