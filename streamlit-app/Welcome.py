# Import statements:
import streamlit as st

# Create the app page configurations:
st.set_page_config(
    page_title='ARCA - Album Release Cataloging App',
    page_icon='🎧',
    layout='wide'
)

# Logo sidebar function:
def add_logo():
    st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"] {
                background-image: url(https://github.com/rhc-iv/album-release-cataloging-app/blob/main/logo.png?raw=true);
                background-repeat: no-repeat;
                padding-top: 120px;
                background-position: 20px 20px;
            }
            [data-testid="stSidebarNav"]::before {
                content: "";
                margin-left: 20px;
                margin-top: 20px;
                font-size: 30px;
                position: relative;
                top: 100px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )


add_logo()


# Create Streamlit app title/info:
st.title('ARCA')
st.markdown('### Album Release Cataloging App')
st.markdown('***')
st.markdown('Wecome to **ARCA**, a _Streamlit_ app to enter, view, and search for details about your music collection.')
st.write()
st.markdown('The links on the sidebar to the left will allow you to choose '
            'your interaction with the **ARCA** app.')