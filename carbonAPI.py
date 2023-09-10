"""
Module Name: carbonAPI
Author: Capt.Pyrite
Created: May 3, 2023
Last Modified: May 4, 2023
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from os import path
from urllib import request
import urllib.parse

class Carbon:
    class sh():
        def __init__(self, driver:path):
            """
            Initialize a new Carbon.sh object.

            Args:
            driver (str): Path to the Chrome WebDriver executable.
            """
            options = Options()
            DRIVER_PATH = driver
            options.add_argument("headless")
            options.add_argument("start-maximized")
            options.add_argument("window-size=1600,1000"); 
            
            self.driver = webdriver.Chrome(executable_path=DRIVER_PATH, options=options)
        
        def code2url(self, code:str, filename:path="Untitled.py"):
            """
            Convert code to a carbon.now.sh URL.

            Args:
            code (str): The code to convert.
            filename (str): The filename to use in the URL.

            Returns:
            str: A URL for the code snippet on carbon.now.sh.
            """
            
            return f"https://carbon.now.sh/?bg=rgba%28176%2C188%2C197%2C1%29&t=verminal&\
            wt=boxy&l=python&width=1920&ds=false&dsyoff=20px&dsblur=68px&wc=true&\
            wa=false&pv=56px&ph=56px&ln=true&fl=1&fm=JetBrains+Mono&fs=13.5px&\
            lh=136%25&si=false&es=2x&wm=false&code={urllib.parse.quote(str(code))}&tb={filename}"
            
        def url2img(self, url:request.urlopen, filename:path):
            """
            Take a screenshot of a carbon.now.sh URL and save it to a file.

            Args:
            url (str): The URL to take a screenshot of.
            image (str): The filename to save the screenshot to.
            """
            self.driver.get(url)
            element = self.driver.find_element(By.ID, "export-container")
            element.screenshot(filename)

if __name__ == "__main__":
    API = Carbon.sh()
    
    url = API.code2url("print('Hello, World')", "HelloWorld.py")
    API.url2img(url, "output.png")
