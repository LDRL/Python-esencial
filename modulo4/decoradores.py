# Los decoradores permiten entender y modificar el funcionamiento de las funciones
# Los decoradores envuelven a otra función y permiten ejecutar código antes y después de que es llamada

PASSWORD = '12345'

def password_required(func):
    def wrapper():
        password = input('Cual es tu contraseña ?')

        if password == PASSWORD:
            return func()
        else:
            print('La contraseña no es correcta')
    return wrapper

@password_required
def needs_password():
    print('La contraseña es correcta')


def upper(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        return result.upper()
    
    return wrapper

@upper
def say_my_name(name):
    return 'Hola, {}'.format(name)

if __name__ == '__main__':
    needs_password()
    print(say_my_name('L'))