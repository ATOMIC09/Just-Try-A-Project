import requests
import time
timer = 0
data = ""

f_write = open("kmitl-cer.txt", "a")
while timer <= 86400:
    hr = int(timer/3600)
    sade = int(timer % 3600)
    min = int(sade / 60)
    sec = int(sade % 60)

    hr_zfill = str(hr).zfill(2)
    min_zfill = str(min).zfill(2)
    sec_zfill = str(sec).zfill(2)

    timer += 1

    try:
        x = requests.get(f'https://engineer.kmitl.ac.th/e-certificate/datas/certificate_ภูตะวัน%20จันทร์เรือง_2021-11-15%20{hr_zfill}:{min_zfill}:{sec_zfill}pm.png')
        print(f"{hr_zfill}:{min_zfill}:{sec_zfill} | {x.status_code}")

        if x.status_code == 200:
            print("====== Found 200 ======")
            data += f"https://engineer.kmitl.ac.th/e-certificate/datas/certificate_replace1%20replace2_2021-11-15%20{hr_zfill}:{min_zfill}:{sec_zfill}pm.png\n"
    except:
        print("====== Error ! ======")
        time.sleep(5)
        continue

f_write.write(data)
f_write.close()