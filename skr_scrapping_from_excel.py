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

URL = [
    "https://academic.skr.ac.th/grade/2564/1/",
    "https://academic.skr.ac.th/grade/2563/2/",
    "https://academic.skr.ac.th/grade/2563/1/",
    "https://academic.skr.ac.th/grade/2562/2/",
    "https://academic.skr.ac.th/grade/2562/1/",
    "https://academic.skr.ac.th/grade/2561/2/",
    "https://academic.skr.ac.th/grade/2561/1/",
    "https://academic.skr.ac.th/grade/2560/2/",
    "https://academic.skr.ac.th/grade/2560/1/",
    "https://academic.skr.ac.th/grade/2559/2/",
    "https://academic.skr.ac.th/grade/2559/1/"]

GPA_LIST = ["AL","AI","AF","AC","Z","W","T","Q","N","K","H"]
CLASS_RATING_LIST = ["AM","AJ","AG","AD","AA","X","U","R","O","L","I"]
SCHOOL_RATING_LIST = ["AN","AK","AH","AE","AB","Y","V","S","P","M","J"]
    
    
for student in range(4,635):
    usr = sheet[f"B{student}"].value
    pwd = sheet[f"G{student}"].value
    print(f"🧑🏻UID: {usr} ")
    print(f" 🔑 PWD: {pwd}")
    print(f"👧🏻Students {student} of 634")
    
    # หาเกรด 11 เทอม
    for i in range(11):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(URL[i])
        print(f"🔍 Opening: {URL[i]}")
        username_box = driver.find_element_by_id('ContentPlaceHolder1_TextBox1').send_keys(usr)

        if pwd == "NOT_FOUND":
            GPA = "NOT FOUND"
            CLASS_RATING = "NOT FOUND"
            SCHOOL_RATING = "NOT FOUND"
            print(f"❌ NOT FOUND ❌")
            break
        else:
            try:
                password_box = driver.find_element_by_id('ContentPlaceHolder1_TextBox2').send_keys(pwd)
                login_box = driver.find_element_by_id('ContentPlaceHolder1_Button1').click()
                GPA = driver.find_element_by_xpath('/html/body/form/div[3]/div[2]/div/table[1]/tbody/tr[4]/td[2]/span').text
                RATING = driver.find_element_by_xpath('/html/body/form/div[3]/div[2]/div/table[1]/tbody/tr[4]/td[4]/span').text
                CLASS_RATING,SCHOOL_RATING = RATING.split("/")
            except:
                GPA = "NOT SKR"
                CLASS_RATING = "NOT SKR"
                SCHOOL_RATING = "NOT SKR"
                print(f"❌❌ NOT SKR ❌❌")
                continue

        # กรอกข้อมูลใน Excel
        sheet[f'{GPA_LIST[i]}{student}'] = GPA
        sheet[f'{CLASS_RATING_LIST[i]}{student}'] = CLASS_RATING
        sheet[f'{SCHOOL_RATING_LIST[i]}{student}'] = SCHOOL_RATING
        driver.quit()

    wb_obj.save('Grade(M6).xlsx')

print("ℹ Program Finished")