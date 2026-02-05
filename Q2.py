username = "muddasir"
password = '12345678'
attempt=3
for i in range(3):
    user = input("Enter your username : ")
    pas = input("Enter your password : ")
    if password==pas and username==user:
        print("Success")
        break
    else:
        print("Failure")
        attempt=attempt-1
        print(f"{attempt} attempts left")
        if attempt==0:
            print("You ran out of attempts")
