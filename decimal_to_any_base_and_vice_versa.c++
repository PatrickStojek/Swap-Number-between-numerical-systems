#include <iostream>
#include <map>
#include <vector>
#include <cmath>
using namespace std;

map<int, char> mapa_IC = {
    {0, '0'}, {1, '1'}, {2, '2'}, {3, '3'}, {4, '4'}, {5, '5'}, {6, '6'}, {7, '7'}, {8, '8'}, {9, '9'},
    {10, 'A'}, {11, 'B'}, {12, 'C'}, {13, 'D'}, {14, 'E'}, {15, 'F'},
    {16, 'G'}, {17, 'H'}, {18, 'I'}, {19, 'J'}, {20, 'K'}, {21, 'L'}, {22, 'M'}, {23, 'N'},
    {24, 'O'}, {25, 'P'}, {26, 'Q'}, {27, 'R'}, {28, 'S'}, {29, 'T'},
    {30, 'U'}, {31, 'V'}, {32, 'W'}, {33, 'X'}, {34, 'Y'}, {35, 'Z'}
};

map<char, int> map_CI = {
    {'0', 0}, {'1', 1}, {'2', 2}, {'3', 3}, {'4', 4}, {'5', 5}, {'6', 6}, {'7', 7}, {'8', 8}, {'9', 9},
    {'A', 10}, {'B', 11}, {'C', 12}, {'D', 13}, {'E', 14}, {'F', 15},
    {'G', 16}, {'H', 17}, {'I', 18}, {'J', 19}, {'K', 20}, {'L', 21}, {'M', 22}, {'N', 23},
    {'O', 24}, {'P', 25}, {'Q', 26}, {'R', 27}, {'S', 28}, {'T', 29},
    {'U', 30}, {'V', 31}, {'W', 32}, {'X', 33}, {'Y', 34}, {'Z', 35}
};

int any_base_to_decimal(string any_base_number, int base) {
    int decimal_num = 0;
    int power = any_base_number.length() - 1;
    for (char digit : any_base_number) {
        decimal_num += map_CI[digit] * pow(base, power);
        power--;
    }
    return decimal_num;
}

string decimal_to_any_base(int decimal_num, int base) {
    string any_base_num = "";
    while (decimal_num > 0) {
        int r = decimal_num % base;
        any_base_num = mapa_IC[r] + any_base_num;
        decimal_num /= base;
    }
    return any_base_num;
}

vector<int> tab_residual(int base, int integer_number) {
    vector<int> tab_resid;
    while (integer_number > 0) {
        int r = integer_number % base;
        tab_resid.push_back(r);
        integer_number /= base;
    }
    return tab_resid;
}

string number_conv(vector<int> tab_resid) {
    string numb_conv = "";
    int s = tab_resid.size();
    for (int i = s - 1; i >= 0; i--) {
        numb_conv += mapa_IC[tab_resid[i]];
    }
    return numb_conv;
}

void execution() {
    int p, n;
    cout << "Podaj podstawe systemu od 2 do 36 = ";
    cin >> p;
    cout << "Podaj liczbe całkowitą > 0 = ";
    cin >> n;
    cout << number_conv(tab_residual(p, n)) << endl;
}

void main_menu() {
    char choice;
    cout << "Wybierz opcję (1 - aby zamienić liczbę na system dziesiętny, 2 - aby zamienić liczbę z systemu dziesiętnego): ";
    cin >> choice;
    if (choice == '1') {
        string any_base_number;
        int desired_base;
        cout << "Podaj liczbę w dowolnym systemie: ";
        cin >> any_base_number;
        cout << "Podaj podstawę jaką chcesz osiągnąć: ";
        cin >> desired_base;
        cout << any_base_to_decimal(any_base_number, desired_base) << endl;
    } else if (choice == '2') {
        int decimal_num, desired_base;
        cout << "Podaj liczbę dziesiętną: ";
        cin >> decimal_num;
        cout << "Podaj podstawę jaką chcesz osiągnąć: ";
        cin >> desired_base;
        cout << decimal_to_any_base(decimal_num, desired_base) << endl;
    } else {
        cout << "Niepoprawny wybór." << endl;
    }
}

int main() {
    main_menu();
    return 0;
}
