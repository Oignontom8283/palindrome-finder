# Trouver un Nombre Palindrome en Python

Nous allont voire comment trouver un n-iéme nombre palindrome grace a un programme fait avec le language de programmation Python.

Pour cela on va voire
- [Qu'es qu'un nombre Palindrome ?](#what_is_markdown)
- [Code du Programme](#program_code)
- [Explication Globale du Programme](#program_overview)
- [Explication par Bloc](#explanation_by_nlock)
- [Explication Ligne par Ligne avec Commentaires](#line_by_line_explanation_with_comments)

## Qu'es qu'un nombre Palindrome ?
<div id='what_is_markdown'/>  

Un nombre palindrome est un nombre qui reste le même lorsqu'on inverse l'ordre de ses chiffres. En d'autres termes, il se lit de la même manière de gauche à droite et de droite à gauche.

Par exemple :

- 121 est un nombre palindrome parce que si on inverse l'ordre des chiffres, on obtient toujours 121.
- 1331 est également un nombre palindrome car 1331 lu de droite à gauche donne aussi 1331.
- Un autre exemple est 1221, car en inversant les chiffres, on obtient encore 1221.

En revanche, un nombre comme 123 n'est pas un nombre palindrome car 123 lu de droite à gauche donne 321, ce qui est différent de 123.

## Code du Programme
<div id='program_code'/>  

```python
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

    # Afficher un message de chargement
    print("\nLoading ...\n")
    
    # Début de la mesure du temps
    start_time = time.time()
    
    # Effectuer la recherche du nombre
    palindrome = find_palindrome(palindrome_target)
    
    # Fin de la mesure du temps
    duration = time.time() - start_time
    
    # Afficher les résultats
    print(f"Temps d'exécution : {duration:.3f} secondes")
    print(f"Le {palindrome_target}éme nombre palindrome est : {palindrome}")
```

## Explication Globale du Programme
<div id='program_overview'/>

Ce programme fonctionne de manière simple : il vérifie un à un chaque nombre entier pour voir s'il est un palindrome. Dès qu'il en trouve un, il augmente un compteur. Lorsque le compteur atteint le nombre de palindromes demandé par l'utilisateur, le programme s'arrête et affiche le résultat, tout en mesurant et affichant le temps d'exécution.

## Explication par Bloc
<div id='explanation_by_nlock'/>  

### Importation des Bibliothèques

```python
import time
```
Cette ligne importe la bibliothèque `time`, qui est utilisée pour mesurer le temps d'exécution du programme.

### Fonction pour Vérifier un Palindrome

```python
# Fonction pour vérifier si un nombre est un palindrome
def is_palindrome(number: int):
    str_number = str(number)
    return str_number == str_number[::-1]
```
Cette fonction convertit un nombre en une chaîne de caractères (texte) pour comparer sa version normale et inversée. Si elles sont identiques, le nombre est un palindrome.

### Fonction pour Trouver un Palindrome

```python
def find_palindrome(target: int):
    count = 0
    number = 0

    # Trouver le palindrome
    while count < target:
        if is_palindrome(number):
            count += 1
        number += 1
    
    return number - 1
```

Cette fonction cherche le **n-ième palindrome** en incrémentant un compteur `count` chaque fois qu’un palindrome est trouvé. Le nombre est retourné une fois le compteur atteint la valeur cible.

### Interface Utilisateur et Mesure de Temps

#### 1. Demande de saisie utilisateur et validation

```python
if __name__ == "__main__":
    while True:
        try:
            palindrome_target = int(input("Veuillez entrer un nombre palindrome à trouver : "))
            if palindrome_target <= 0:
                raise ValueError()
            break
        except ValueError:
            print("Oups ! Ce n'était pas un nombre valide. Essayez à nouveau...\n")
```

Ce bloc demande à l’utilisateur de saisir un entier valide, vérifie qu’il est strictement positif, et recommence en cas d’erreur.

#### 2. Préparation et affichage du message de chargement

```python
    # Afficher un message de chargement
    print("\nLoading ...\n")
```

Cette ligne informe l’utilisateur que le programme commence la recherche.

#### 3. Mesure et calcul

```python
    # Début de la mesure du temps
    start_time = time.time()
    
    # Effectuer la recherche du nombre
    palindrome = find_palindrome(palindrome_target)
    
    # Fin de la mesure du temps
    duration = time.time() - start_time
```

Ces lignes mesurent le temps nécessaire pour trouver le palindrome en enregistrant le moment du début et de la fin de l’opération.

#### 4. Résultats

```python
    # Afficher les résultats
    print(f"Temps d'exécution : {duration:.3f} secondes")
    print(f"Le {palindrome_target}éme nombre palindrome est : {palindrome}")
```

Ce bloc affiche le temps d’exécution ainsi que le palindrome trouvé.

## Explication Ligne par Ligne avec Commentaires
<div id='line_by_line_explanation_with_comments'/>  
  
Voici le programme avec des commentaires pour chaque ligne :

```python
import time  # Importation de la bibliothèque pour mesurer le temps d'exécution

# Fonction pour vérifier si un nombre est un palindrome
def is_palindrome(number: int):
    str_number = str(number)  # Convertit le nombre en une chaîne de caractères
    return str_number == str_number[::-1]  # Compare la chaîne normale et inversée

# Fonction pour trouver le n-ième palindrome
def find_palindrome(target: int):
    count = 0  # Compteur pour suivre le nombre de palindromes trouvés
    number = 0  # Le nombre actuellement analysé

    # Boucle jusqu'à ce que le compteur atteigne la cible
    while count < target:
        if is_palindrome(number):  # Vérifie si le nombre actuel est un palindrome
            count += 1  # Incrémente le compteur si c'est le cas
        number += 1  # Passe au nombre suivant
    
    return number - 1  # Retourne le dernier palindrome trouvé

# --- Programme principal ---

if __name__ == "__main__":  # Point d'entrée du programme
    
    while True:  # Boucle pour demander une entrée valide à l'utilisateur
        try:
            palindrome_target = int(input("Veuillez entrer un nombre palindrome à trouver : "))  # Demande un nombre entier
            if palindrome_target <= 0:  # Vérifie que le nombre est positif
                raise ValueError()  # Lève une erreur si ce n'est pas le cas
            break  # Sort de la boucle si l'entrée est valide
        except ValueError:  # Capture les erreurs liées à une entrée invalide
            print("Oups ! Ce n'était pas un nombre valide. Essayez à nouveau...\n")

    print("\nLoading ...\n")  # Message de chargement
    
    start_time = time.time()  # Enregistre l'heure de début
    
    palindrome = find_palindrome(palindrome_target)  # Trouve le n-ième palindrome
    
    duration = time.time() - start_time  # Calcule le temps d'exécution
    
    print(f"Temps d'exécution : {duration:.3f} secondes")  # Affiche le temps d'exécution
    print(f"Le {palindrome_target}éme nombre palindrome est : {palindrome}")  # Affiche le résultat
```

