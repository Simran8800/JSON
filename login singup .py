from cgitb import strong
import json


print("Welcome to login singup page")

login_signup=input("Do you want login & singup:-")
if login_signup=="signup":
    name=input("enter the name:-")
    surname=input("enter your surname:-")
    mail=input("enter the email:-")
    password=input("enter the password:-")
    strong_password=input("enter the password:-")
    phon_no=int(input("enter the no :- "))
    a=login_signup
    if password==strong_password:
        print("your password is coorect")
        birth=input("enter your birth of date")
        gender=input("choose your gender m/f:")
        print("signup sucessfully")
        dict={"login_signup":login_signup,"name":name,"surname":surname,"mail":mail,"password":password,"strong_password":strong_password}
        with open('login.json',"w") as f:
            b=json.dump(dict,f,indent=9)
    else:
        print("wrong password")
else:
    if login_signup=="login":
        name=input("enter the name")
    surname=input("enter your surname")
    mail=int(input("enter the email"))
    password=int(input("enter the password"))
    strong_password=int(input("enter the password"))
    phon_no=int(input("enter the no"))
    a=login_signup
    if password==strong_password:
        print("your password is coorect")
        birth=input("enter your birth of date")
        gender=input("choose your gender m/f:")
        print("signup sucessfully")
        dict={"login_signup":login_signup,"name":"surname"}
        with open('login.json',"w") as f:
            b=json.dump(dict,f,indent=4)
    else:
        print("wrong password")
        