#functions
def login(user_id):
    real_members = ['yooshin','noah','keroro','tamama','dororo','kiroro','lifeandstory']
    real_pwd = "story"
    pwd_count = 5
    logged_in = False

    for member in real_members:
        if member == user_id:
            while pwd_count>0:
                input_pwd = input("Please input your password\n")
                if real_pwd == input_pwd:
                    logged_in = True
                    return True
                else:
                    print("Wrong Password! Count:"+str(pwd_count-1))
                    pwd_count -= 1
            if pwd_count==0:
               return False

    if (logged_in == False) and (pwd_count==5):
        return False

#Main
input_id = input("Please input your id\n")

if login(input_id):
  print("Welcome! "+ input_id)
else:
  print("Wrong ID or Wrong Password!")

# #Password function 2
# print("Password function 2")
#
# input_id = input("Please input your id\n")
# input_pwd = input("Please input your password\n")
#
# if real_id == input_id and real_pwd == input_pwd:
#     print("Welcome!")
# else:
#     print("Wrong!")
#
# in_str = "TEST"
# input("Please tell me your nickname!\n")
# print(in_str.upper()+" in 10 seconds")


#
# # # Simple Version - with If-Elif
# input = 22
# real_yooshink = "keroro"
# real_noah = "tamama"
# # if in_str == real_yooshink:
# #     print("Hi Yooshin~")
# # elif in_str == real_noah: # else if -> elif
# #     print("Hi Nonah~")
# # else:
# #     print("who are you?")
