import time

# Fonction pour vérifier si un nombre est un palindrome
def is_palindrome(number: int):
    str_number = str(number)
    return str_number == str_number[::-1]

def find_palindrome(target: int):
    count = 0
    number = 0

    # Trouver le palindrome
    while count < target:
        if is_palindrome(number):
            count += 1
        number += 1
    
    return number - 1


# --- Programme ---

if __name__ == "__main__":  # Cette ligne est pour la logistique. Ne t'y attarde pas.
    
    while True:
        try:
            palindrome_target = int(input("Veuillez entrer un nombre palindrome à trouver : "))
            if palindrome_target <= 0:
                raise ValueError()
            break
        except ValueError:
            print("Oups ! Ce n'était pas un nombre valide. Essayez à nouveau...\n")
    
    # Début de la mesure du temps
    start_time = time.time()
    
    # Effectuer la recherche du nombre
    palindrome = find_palindrome(palindrome_target)
    
    # Fin de la mesure du temps
    duration = time.time() - start_time
    
    # Afficher les résultats
    print(f"Temps d'exécution : {duration:.3f} secondes")
    print(f"Le {palindrome_target}éme nombre palindrome est : {palindrome}")
