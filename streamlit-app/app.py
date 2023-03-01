# Import statements:
import streamlit as st
from streamlit_agraph import agraph, Node, Edge, Config

# Create node/edge (empty) lists:
nodes = []
edges = []

# Create nodes for graphing:
nodes.append(
    Node(
        id='2000 And One',
        label='2000 And One',
        size=25,
        shape='circularImage',
        image='/Users/rhc.iv/Music/Crates/Techno/2000 And One/artist_img.jpeg',
    )
)
nodes.append(
    Node(
        id='Kawasaki',
        label='Kawasaki',
        size=25,
        shape='circularImage',
        image='/Users/rhc.iv/Music/Crates/Techno/2000 And One/Kawasaki - ['
              'PURE098]/cover.jpg',
    )
)
edges.append(
    Edge(
        source='Kawasaki',
        label='produced by',
        target='2000 And One',
    )
)

config = Config(
    width=750,
    height=950,
    directed=True,
    physics=True,
    hierarchical=True,
)

return_value = agraph(nodes=nodes,
                      edges=edges,
                      config=config)