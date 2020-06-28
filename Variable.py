x=100
y=5
print(x+y)

title = "Photography"
#Converting Data to Strings .__str__ or str(x)
print("Story"+title+x.__str__())
print("Story"+title+str(x))

#Converting Strings to Numbers int(x), float(x)
print(int("5"))
print(float("5"))
# print(int("5.8")) # int에 소수점있으면 에러남

donation = 200
sponsor = 20
student = 5
print("Amount of donations per sponsors = "+ ((donation*student)/sponsor).__str__())
