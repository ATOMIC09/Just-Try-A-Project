from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import openpyxl
from pathlib import Path

# Setting the path to the xlsx file:
xlsx_file = Path('A:/Documents/GitHub/Just-Try-A-Project/grade.xlsx')
wb_obj = openpyxl.load_workbook(xlsx_file)
sheet = wb_obj.active
usr = sheet["C167"].value
pwd = sheet["D167"].value

url = "https://academic.skr.ac.th/grade/2562/1/"
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)

# Login

username_box = driver.find_element_by_id('ContentPlaceHolder1_TextBox1').send_keys(usr)
password_box = driver.find_element_by_id('ContentPlaceHolder1_TextBox2').send_keys(pwd)
login_box = driver.find_element_by_id('ContentPlaceHolder1_Button1').click()

# Scrapping
try:
    GPA = driver.find_element_by_xpath('/html/body/form/div[3]/div[2]/div/table[1]/tbody/tr[4]/td[2]/span').text
    RATING = driver.find_element_by_xpath('/html/body/form/div[3]/div[2]/div/table[1]/tbody/tr[4]/td[4]/span').text
    CLASS_RATING,SCHOOL_RATING = RATING.split("/")
except:
    print("ERROR")

sheet['F167'] = GPA
sheet['G167'] = CLASS_RATING
sheet['H167'] = SCHOOL_RATING
wb_obj.save('write2cell.xlsx')

driver.quit()