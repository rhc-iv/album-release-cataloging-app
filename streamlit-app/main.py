import streamlit as st
import pandas as pd
import uuid

df = pd.read_json('music.json')

columns = df.columns.tolist()
columns.remove('id') # Remove 'id' column from the list

st.title('Album Release Cataloging Database (ARCD)')

# Create a selectbox and submit buttons for each column
submit_buttons = []
for column in columns:
    capitalized_column = column.capitalize()
    selectbox_label = f"Select {capitalized_column}"
    submit_button_label = "Submit"

    # Show the selectbox and submit button for this column in the sidebar
    selection = st.sidebar.selectbox(selectbox_label, df[column].unique(), key=f"{column}_select")
    submit_button_key = str(uuid.uuid4()) # Generate a unique key for the submit button
    submit_button = st.sidebar.button(submit_button_label, key=submit_button_key)
    submit_buttons.append(submit_button)

# Render the table and clear button when any submit button is pressed
if any(submit_buttons):
    selected_df = df
    for i, column in enumerate(columns):
        selection = st.sidebar.selectbox("", df[column].unique(), key=f"{column}_select")
        if submit_buttons[i]:
            selected_df = selected_df[selected_df[column] == selection]
    selected_df = selected_df.drop('id', axis=1).sort_values('year')
    table_key = str(uuid.uuid4()) # Generate a unique key for the table
    st.table(selected_df)
    clear_button_key = str(uuid.uuid4()) # Generate a unique key for the clear button
    st.button("Clear", key=clear_button_key)

# Clear the table and show a message in the main Streamlit window when the Clear button is pressed
if st.button("Clear"):
    st.experimental_set_query_params()
    st.write("Awaiting your release selection")
