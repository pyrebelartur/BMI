weight = int(input("Enter the weight:\n"))
height = int(input("Enter the height:\n"))

bmi = weight / (height ** 2)

if bmi < 18.5:
    print("Underweight")
elif bmi <= 25:
    print("normal weight")
else:
    print("Overweight")
