import settings

def main():
    print('This is a Hello World project.')
    print('La variable de ambiente MESSAGE es:', settings.MESSAGE)
    print('El valor del argumento --name es: ', settings.name)

if __name__ == "__main__":
    main()