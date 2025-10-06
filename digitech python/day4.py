# thisprogram checks on the use input and validates it
print("this program needs the credentials to verify them to grant access to users")
print()

username = input("Enter your username: ")
password = input("Enter your password: ")

if username == "Texasus" and password == "p1234":
    print("Access granted")

elif username != "Texasus" and password == "p1234":
    print("check your credentials")
    
else:
    print("Access denied")

