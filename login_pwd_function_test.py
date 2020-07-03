real_id = "lifeandstory"
real_pwd = "story"

#Password function 1
print("Password function 1")

input_id = input("Please input your id\n")

if real_id == input_id:
    input_pwd = input("Please input your password\n")
    if real_pwd == input_pwd:
        print("Welcome!")
    else:
        print("Wrong Password!")
else:
    print("Wrong ID")

#Password function 2
print("Password function 2")

input_id = input("Please input your id\n")
input_pwd = input("Please input your password\n")

if real_id == input_id and real_pwd == input_pwd:
    print("Welcome!")
else:
    print("Wrong!")
