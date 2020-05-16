password = "contraseña"

password_del_usuario = input ("introduzca contraseña: ")
password_del_usuario=password_del_usuario.lower()

if password == password_del_usuario:
    print("el password es correcto")
else:
    print("el password no coincide")