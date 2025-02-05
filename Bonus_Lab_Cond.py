
userW = float(input(" Enter your weight "))
userH = float(input(" Enter your height "))
BMI =  userW / (userH ** 2)
print("Your BMI is: ", BMI)

if BMI <= 18.5:
    print("You are underweight. Watch your health")
elif BMI <= 24.9:
    print("You are fit and healthy")
elif BMI <= 29.9:
    print("You are overwieght you need to work out more and watch your diet.")


