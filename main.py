import streamlit as st

text_answer = st.text_input("Write something here:")

# Create a small sample dataframe
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [23, 34, 28, 45, 31],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'],
    'Occupation': ['Engineer', 'Artist', 'Doctor', 'Lawyer', 'Chef']
}

df = pd.DataFrame(data)

st.download_button(
    label="Download data as CSV",
    data=df,
    file_name="large_df.csv",
    mime="text/csv",
)
