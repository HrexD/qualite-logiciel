def addition(x, y):
    return x + y

def soustraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    if y == 0:
        return "Erreur : Division par zéro !"
    return x / y

def calculatrice():
    print("La fonction calculatrice a été appelée.") 
    print("Sélectionnez l'opération.")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division")

    while True:
        choix = input("Entrez votre choix (1/2/3/4): ")

        if choix in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Entrez le premier nombre: "))
                num2 = float(input("Entrez le deuxième nombre: "))
            except ValueError:
                print("Veuillez entrer des nombres valides.")
                continue

            if choix == '1':
                print(f"{num1} + {num2} = {addition(num1, num2)}")

            elif choix == '2':
                print(f"{num1} - {num2} = {soustraction(num1, num2)}")

            elif choix == '3':
                print(f"{num1} * {num2} = {multiplication(num1, num2)}")

            elif choix == '4':
                result = division(num1, num2)
                if isinstance(result, str):  # Si le résultat est un message d'erreur
                    print(result)
                else:
                    print(f"{num1} / {num2} = {result}")

        else:
            print("Choix invalide. Veuillez sélectionner une opération valide.")

        nouvelle_operation = input("Voulez-vous effectuer une autre opération ? (oui/non): ")
        if nouvelle_operation.lower() != 'oui':
            break

    print("Merci d'avoir utilisé la calculatrice.")

# Exécuter la calculatrice
calculatrice()
