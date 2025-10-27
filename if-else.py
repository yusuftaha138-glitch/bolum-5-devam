emaiil = "info@ytdirican.com"
parola = "123456"

login = (emaiil == "info@ytdirican.com") and (parola == "123456")

if( (emaiil == "info@ytdirican.com")):
    if((parola == "123456")):
        print("giriş başarılı")
    else:
        print(" parola yanlış")
else:
    print("email yanlış")