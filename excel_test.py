from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import openpyxl
from pathlib import Path

# Setting the path to the xlsx file:
xlsx_file = Path('A:/Documents/GitHub/Just-Try-A-Project/M6(2564).xlsx')
wb_obj = openpyxl.load_workbook(xlsx_file)
sheet = wb_obj.active
    
usr = sheet[f"B4"].value
pwd = sheet[f"G4"].value
print("usr: ",usr)
print("pwd: ",pwd)