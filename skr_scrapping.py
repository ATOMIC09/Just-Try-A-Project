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
    
for student in range(2,552):
    usr = sheet[f"C{student}"].value
    pwd = sheet[f"D{student}"].value

    URL = ["https://academic.skr.ac.th/grade/2559/1/",
    "https://academic.skr.ac.th/grade/2559/2/",
    "https://academic.skr.ac.th/grade/2560/1/",
    "https://academic.skr.ac.th/grade/2560/2/",
    "https://academic.skr.ac.th/grade/2561/1/",
    "https://academic.skr.ac.th/grade/2561/2/"]

    GPA_LIST = ["F","I","L","O","R","U"]
    CLASS_RATING_LIST = ["G","J","M","P","S","V"]
    SCHOOL_RATING_LIST = ["H","K","N","Q","T","W"]

    for i in range(6):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(URL[i])

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

        sheet[f'{GPA_LIST[i]}{student}'] = GPA
        sheet[f'{CLASS_RATING_LIST[i]}{student}'] = CLASS_RATING
        sheet[f'{SCHOOL_RATING_LIST[i]}{student}'] = SCHOOL_RATING
        driver.quit()

    wb_obj.save('write2cell.xlsx')