gender = input("Enter Gender M/FM : ")
weight = int(input("Enter Weight (kg) : "))
height = int(input("Enter Height (cm) : "))
age = int(input("Enter Age : "))

bmr_male = 66 + (13.7 * weight) + (5 * height) - (6.8 * age)
bmr_female = 665 + (9.6 * weight) + (1.8 * height) - (4.7 * age)

if gender == "M" or "m" :
    print(f"Your calories per day: {bmr_male}")

elif gender == "FM" or "fm" :
    print(f"Your calories per day : {bmr_female}")