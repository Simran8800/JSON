import json
print("welcome to login singup page")
login_signup=input("Do you want login & singup:-")
# a=open("login.json","r")
# c=a.read()
# data=json.loads(c)
if login_signup=="singup":
    firstname=input("enter the name:-")
    lastname=input("enter your surname:-")
    mail=input("enter the email:-")
    password=input("enter the password:-")
    strong_password=input("enter the password:-")
    phon_no=int(input("enter the phon no :- "))
    if password==strong_password:
        print("your password is coorect:-")
        birth=input("enter your birth of date:-")
        gender=input("choose your gender m/f:-")
        print("signup sucessfully:-")
        dict={"login_signup":login_signup,"firstname":firstname,"lastname":lastname,"mail":mail,"password":password,"strong_password":strong_password}
        with open('login.json',"w") as f:
            b=json.dump(dict,f,indent=9)
    else:
        print("wronge user id:-")
else:
    if login_signup=="login":
        username=input("enter the username:-")
        password=int(input("enter your password:-"))
        if username=="firstname" and password=="strong_password:-":
            print("it's is correct:-")
            ict={"login_signup":login_signup,"name":"surname:-"}
            # my_file=open("login.json","r:-")
            # a=json.load(my_file)
        else:
            print("wrong information")
    else:
        print("try again")
    
            
        
        
        
        
    
    