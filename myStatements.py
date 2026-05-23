my_list = ["apple", "banana", "cherry", "date", "elderberry"]
my_dict = {"drink": "coffee", "milk": "whole"}

for item in my_list:
    print(f"My favourite thing to eat is: {item}")

##cool thing about python is that you can throw away the key with  _ if you don't care about it, and just want the value or vice versa
for _,value in my_dict.items():
    print(f"My favourite thing to drink is: {value}")


