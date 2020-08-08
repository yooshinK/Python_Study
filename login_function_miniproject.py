#functions
# def login(user_id):
#     real_members = ['yooshin','noah','keroro','tamama','dororo','kiroro','lifeandstory']
#     real_pwd = "story"
#     pwd_count = 5
#     logged_in = False
#
#     for member in real_members:
#         if member == user_id:
#             while pwd_count>0:
#                 input_pwd = input("Please input your password\n")
#                 if real_pwd == input_pwd:
#                     logged_in = True
#                     return True
#                 else:
#                     print("Wrong Password! Count:"+str(pwd_count-1))
#                     pwd_count -= 1
#             if pwd_count==0:
#                return False
#
#     if (logged_in == False) and (pwd_count==5):
#         return False

import authentication_module
#Main
input_id = input("Please input your id\n")

if authentication_module.login(input_id):
  print("Welcome! "+ input_id)
else:
  print("Wrong ID or Wrong Password!")
