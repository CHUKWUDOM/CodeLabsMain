#include <iostream>
#include <string>

using namespace std;

string alpha_check(char alphabet) {
    // Define the vowel and consonant alphabets
    string vowels = "aeiouAEIOU";
    string consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ";

    // Check if the input is a single alphabet character
    if (isalpha(alphabet)) {
        if (vowels.find(alphabet) != string::npos) {
            return "The alphabet is a vowel.";
        } else if (consonants.find(alphabet) != string::npos) {
            return "The alphabet is a consonant.";
        } else {
            return "Invalid input, Enter another Letter";
        }
    } else {
        return "Invalid input, Enter another Letter";
    }
}

int main() {
    char letter;
    cout << "Enter alphabet to check: ";
    cin >> letter;

    // Check the input and print
    string output = alpha_check(letter);
    cout << output << endl;

    return 0;
}
