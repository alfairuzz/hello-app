import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType


text_answer = st.text_input("Write something here:")

# Function to render content with Selenium
def get_rendered_html(url):
    
    # Set up Selenium WebDriver options
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito") # Run Chrome in incognito mode
    options.add_argument("--headless")  # Run in headless mode for Streamlit
    
    # Start WebDriver and get the URL
    driver = webdriver.Chrome(
        service=Service(
            ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()
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
    try:
        # Scrape and render the website content using Selenium
        html_content = get_rendered_html(url)
    except Exception as e:
        st.error(f"An error occurred: {e}")

    st.code(html_content)

    
