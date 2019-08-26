#Program that reports whether or not someone is eligible to run for president of the U.S

userAge = int(input("Enter your age: "))
userCitizenship = input("Are you a U.S Citizen?(Yes/No): ")
userResidency = int(input("How many years have you been a resident in the U.S? "))

if userAge >= 35 and userCitizenship == "Yes" and userResidency >= 14:
    print("You are eligible to run for president!")
else:
    print("You are not eligible to run for president.")
