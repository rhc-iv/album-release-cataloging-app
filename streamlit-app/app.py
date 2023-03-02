# Import statements:
import streamlit as st
from streamlit_agraph import agraph, Node, Edge, Config

# Create node/edge (empty) lists:
nodes = []
edges = []

# Create a page title for the app:
st.title('Album Release Cataloging App (ARCA)')


# --- Create PARENT nodes ---

# Create main Artists node:
nodes.append(
    Node(
        id='Artists',
        color='#8a508f',
        label='Artists',
        size=35,
        shape='dot',
    )
)
# Create main Releases node:
nodes.append(
    Node(
        id='Releases',
        color='#bc5090',
        label='Releases',
        size=35,
        shape='dot',
    )
)
# Create main Year node:
nodes.append(
    Node(
        id='Year',
        color='#ff6361',
        label='Year',
        size=35,
        shape='dot',
    )
)
# Create main Genre node:
nodes.append(
    Node(
        id='Genre',
        color='#ff8531',
        label='Genre',
        size=35,
        shape='dot',
    )
)
# Create main BPM node:
nodes.append(
    Node(
        id='BPM',
        color='#ffa600',
        label='BPM',
        size=35,
        shape='dot',
    )
)
#Create main Song Key node:
nodes.append(
    Node(
        id='Song Key',
        color='#ffd380',
        label='Song Key',
        size=35,
        shape='dot',
    )
)
# Create main Record Label node:
nodes.append(
    Node(
        id='Record Label',
        color='#ffe680',
        label='Record Label',
        size=35,
        shape='dot',
    )
)

# --- CHILDREN NODES ---

# All Artist nodes:
nodes.append(
    Node(
        id='2000AndOne',
        label='2000 And One',
        size=25,
        shape='circularImage',
        image='https://github.com/rhc-iv/album-release-cataloging-app/blob/9a2b1e04246c6a1a048c1abc7381b3310a240d49/streamlit-app/images/artists/2000AndOne/artist_img.jpeg?raw=true'
    )
)
nodes.append(
    Node(
        id='999999999',
        label='999999999',
        size=25,
        shape='circularImage',
        image='https://github.com/rhc-iv/album-release-cataloging-app/blob/main/streamlit-app/images/artists/999999999/artist_img.jpeg?raw=true'
    )
)
nodes.append(
    Node(
        id='ASacredGeometry',
        label='A Sacred Geometry',
        size=25,
        shape='circularImage',
        image='https://github.com/rhc-iv/album-release-cataloging-app/blob/main/streamlit-app/images/artists/A%20Sacred%20Geometry/artist_img.jpeg?raw=true'
    )
)
# All Release nodes:
nodes.append(
    Node(
        id='Kawasaki',
        label='Kawasaki',
        size=25,
        shape='circularImage',
        image='https://github.com/rhc-iv/album-release-cataloging-app/blob/main/streamlit-app/images/releases/Kawasaki/cover.jpg?raw=true',
    )
)
nodes.append(
    Node(
        id='RaveReworks',
        label='Rave Reworks',
        size=25,
        shape='circularImage',
        image='https://github.com/rhc-iv/album-release-cataloging-app/blob/main/streamlit-app/images/releases/Rave%20Reworks/cover.jpg?raw=true'
    )
)
nodes.append(
    Node(
        id='ChapterIII',
        label='Chapter III',
        size=25,
        shape='circularImage',
        image='https://github.com/rhc-iv/album-release-cataloging-app/blob/main/streamlit-app/images/releases/Chapter%20III/cover.jpg?raw=true'
    )
)
# All Year nodes:
nodes.append(
    Node(
        id='2015',
        label='2015',
        size=20,
        shape='dot',
    )
)
nodes.append(
    Node(
        id='2017',
        label='2017',
        size=20,
        shape='dot',
    )
)
nodes.append(
    Node(
        id='2018',
        label='2018',
        size=20,
        shape='dot',
    )
)
# All Genre nodes:
nodes.append(
    Node(
        id='Techno',
        label='Techno',
        size=20,
        shape='dot',
    )
)
# All BPM nodes:
nodes.append(
    Node(
        id='128',
        label='128',
        size=15,
        shape='dot',
    )
)
nodes.append(
    Node(
        id='135',
        label='135',
        size=15,
        shape='dot',
    )
)


# --- EDGES ---

# PARENT/CHILD Artists edges:
edges.append(
    Edge(
        color='white',
        source='Artists',
        target='2000AndOne',
    )
)
edges.append(
    Edge(
        color='white',
        source='Artists',
        target='999999999',
    )
)
edges.append(
    Edge(
        color='white',
        source='Artists',
        target='ASacredGeometry',
    )
)
# PARENT/CHILD Releases edges:
edges.append(
    Edge(
        color='white',
        source='Releases',
        target='Kawasaki',
    )
)
edges.append(
    Edge(
        color='white',
        source='Releases',
        target='RaveReworks',
    )
)
edges.append(
    Edge(
        color='white',
        source='Releases',
        target='ChapterIII',
    )
)
# PARENT/CHILD Year edges:
edges.append(
    Edge(
        color='white',
        source='Year',
        target='2015',
    )
)
edges.append(
    Edge(
        color='white',
        source='2015',
        target='Kawasaki',
    )
)
edges.append(
    Edge(
        color='white',
        source='Year',
        target='2017',
    )
)
edges.append(
    Edge(
        color='white',
        source='2017',
        target='ChapterIII',
    )
)
edges.append(
    Edge(
        color='white',
        source='Year',
        target='2018',
    )
)
edges.append(
    Edge(
        color='white',
        source='2018',
        target='RaveReworks',
    )
)
# PARENT/CHILD Genre edges:
edges.append(
    Edge(
        color='white',
        source='Genre',
        target='Kawasaki',
    )
)
edges.append(
    Edge(
        color='white',
        source='Genre',
        target='RaveReworks',
    )
)
edges.append(
    Edge(
        color='white',
        source='Genre',
        target='ChapterIII',
    )
)
# PARENT/CHILD BPM edges:
edges.append(
    Edge(
        color='white',
        source='128',
        target='Kawasaki',
    )
)
edges.append(
    Edge(
        color='white',
        source='128',
        target='ChapterIII',
    )
)
edges.append(
    Edge(
        color='white',
        source='135',
        target='RaveReworks',
    )
)
# Artist/Release edges:
edges.append(
    Edge(
        color='white',
        label='produced by',
        source='Kawasaki',
        target='2000AndOne',
    )
)
edges.append(
    Edge(
        color='white',
        label='produced by',
        source='RaveReworks',
        target='999999999',
    )
)
edges.append(
    Edge(
        color='white',
        label='produced by',
        source='ChapterIII',
        target='ASacredGeometry',
    )
)

config = Config(
    width=1100,
    height=950,
    directed=False,
    physics=True,
    hierarchical=True,
)

return_value = agraph(
    nodes=nodes,
    edges=edges,
    config=config)