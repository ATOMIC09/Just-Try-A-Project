import time
import math

count = 0
start = int(input("Range Start : "))
end = int(input("Range End : "))
distance = int(input("Distance : "))   
div_num = int(input("Enter Number (Divide) : "))
undiv_num = int(input("Enter Number (Undivide) : "))

real_end = end + 1

for i in range(start,real_end,distance):
    #Check Mod
    if i%div_num == 0 and i%undiv_num != 0:
        count += 1
        print(i)
print(f"\nTotal n = {count}")

time.sleep(300)