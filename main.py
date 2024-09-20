import streamlit as st
# import pandas as pd

# text_answer = st.text_input("Write something here:")

# def convert_df(df):
#     # IMPORTANT: Cache the conversion to prevent computation on every rerun
#     return df.to_csv().encode("utf-8")


# # Create a small sample dataframe
# data = {
#     'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
#     'Age': [23, 34, 28, 45, 31],
#     'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'],
#     'Occupation': ['Engineer', 'Artist', 'Doctor', 'Lawyer', 'Chef']
# }

# df = pd.DataFrame(data)

# csv = convert_df(df)

# st.download_button(
#     label="Download data as CSV",
#     data=csv,
#     file_name="large_df.csv",
#     mime="text/csv",
# )


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType

@st.cache_resource
def get_driver():
    return webdriver.Chrome(
        service=Service(
            ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()
        ),
        options=options,
    )

# Streamlit part
url = st.text_input("Enter a Website URL: ")

# Function to render content with Selenium
def get_rendered_html(url):
    
    # Set up Selenium WebDriver options
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito") # Run Chrome in incognito mode
    options.add_argument("--headless")  # Run in headless mode for Streamlit
    
    # Start WebDriver and get the URL
    driver = get_driver()
    driver.get(url)
    
    # Allow the page to load and render JavaScript
    time.sleep(3)
    
    # Get the page source after JavaScript execution
    html_content = driver.page_source
    
    # Close the WebDriver
    driver.quit()
    
    return html_content

if st.button("Scrape Site"):
    st.write("Scraping the website...")
