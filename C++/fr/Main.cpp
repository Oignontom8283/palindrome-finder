#include <iostream>
#include <string>
#include <chrono>
#include <iomanip> // Pour std::setprecision

using namespace std;

// Fonction pour verifier si un nombre est un palindrome
bool is_palindrome(int number) {
    string str_number = to_string(number);
    string reversed_number = string(str_number.rbegin(), str_number.rend());
    return str_number == reversed_number;
}

// Fonction pour trouver le n-ieme palindrome
int find_palindrome(int target) {
    int count = 0;
    int number = 0;

    // Trouver le palindrome
    while (count < target) {
        if (is_palindrome(number)) {
            count++;
        }
        number++;
    }
    return number - 1;
}

int main() {
    int palindrome_target;

    // Boucle pour obtenir une entree valide
    while (true) {
        cout << "Veuillez entrer un nombre palindrome a trouver : ";
        cin >> palindrome_target;

        if (cin.fail() || palindrome_target <= 0) {
            cin.clear(); // Efface les erreurs
            cin.ignore(numeric_limits<streamsize>::max(), '\n'); // Ignore la ligne invalide
            cout << "Oups ! Ce n'etait pas un nombre valide. Essayez a nouveau...\n" << endl;
        }
        else {
            break;
        }
    }

    // Afficher un message de chargement
    cout << "\nLoading ...\n" << endl;

    // Debut de la mesure du temps
    auto start_time = chrono::high_resolution_clock::now();

    // Effectuer la recherche du nombre
    int palindrome = find_palindrome(palindrome_target);

    // Fin de la mesure du temps
    auto end_time = chrono::high_resolution_clock::now();
    chrono::duration<double> duration = end_time - start_time;

    // Afficher les resultats
    cout << fixed << setprecision(5); // Fixe la precision a 5 chiffres apres la virgule
    cout << "Temps d'execution : " << duration.count() << " secondes" << endl;
    cout << "Le " << palindrome_target << "eme nombre palindrome est : " << palindrome << endl;

    return 0;
}
