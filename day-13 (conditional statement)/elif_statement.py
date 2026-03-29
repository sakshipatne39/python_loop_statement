user_age = input("enter your age : ")

print(f"user_age = {user_age}, type of user_age = {type(user_age)}")

valid_user_age = int(user_age)

print(f"valid_user_age = {valid_user_age}, type of valid_user_age = {type(valid_user_age)}")



if valid_user_age < 10:
    print('user is child')
elif valid_user_age < 18:
    print('user is teenage')
else :
    print('user is older')