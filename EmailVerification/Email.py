# Using Regex module >> Regular expression
# a-z
# 0-9
# . _ time 1
# @ time 1
# . 2nd , 3rd position
import re
email_condition = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"            # ^= start with, \ is used to check ,? 0 and 1 are valid, \w search,{2,3} position, $ = reverse search
user_email = input(' Enter your email address: ')

if re.search(email_condition,user_email):
     print("Valid Email")
else:
     print("Invalid Email")
