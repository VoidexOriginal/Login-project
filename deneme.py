import users_data

username = input("kullanıcı adı: ")
password = input("şifre: ")

if username in users_data.users and users_data.users[username] == password:
    print("giriş başarılı")
else:
    print("hatalı giriş")
