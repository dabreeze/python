weight = float(input("Pls Enter Weight: "))
responds = input("(K)g or (L)bs:")

if responds.lower() == ('g'):
    grams = weight / 0.45
    print("Your weight in kilograms is: " + str(grams))
elif responds.lower() == ('l'):
    pounds = weight * 0.45
    print("Your weight in pounds is: " + str(pounds))

else: print("you entered a wrong character")
