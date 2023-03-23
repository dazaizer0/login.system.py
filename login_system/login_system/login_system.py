
print("Welcome to LoginSystem")
print("Please, write your email to login or register")

mail = input("email: ")
checker = 0

users = {
    "0:email": "0:password",
}

f = open("data.txt", "r")
data = f.readlines()

for i in range(0, len(data)):

    if i % 2 == 0:
        users.update({data[i]: data[i + 1]})

f.close()
print(users)

if mail in users.values():

    print("LOGIN: Welcome, please type your password, email: ", mail)
    password = input("type password: ")

    if password == list(users.keys())[mail]:
        print("loged!")

    else:
        print("error")

else:

     mail = input("REGISTER: Welcome, please type your mail again: ")
     password = input("please type your password: ")

     f = open("data.txt", "w")
     f.writelines(mail + "\n")
     f.writelines(password + "\n")
