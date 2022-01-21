weight = float(input("Weight"))
responds = input("(K)g or (L)bs:")

lower_Responds = responds.lower()
if lower_Responds == ('g'):
    grams = weight * 1000
    print(grams)
elif lower_Responds == ('l'):
    pounds = weight * 2.20462
    print(pounds)

else: print("you entered a wrong character")
