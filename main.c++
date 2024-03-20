#include <iostream>
#include <vector>
#include <map>
#include <string>

using namespace std;

map <int, char> mapa_IC =
{
    {0, '0'}, {1, '1'}, {2, '2'}, {3, '3'}, {4, '4'}, {5, '5'}, {6, '6'}, {7, '7'}, {8, '8'}, {9, '9'},
    {10, 'A'}, {11, 'B'}, {12, 'C'}, {13, 'D'}, {14, 'E'}, {15, 'F'},
    {16, 'G'}, {17, 'H'}, {18, 'I'}, {19, 'J'}, {20, 'K'}, {21, 'L'}, {22, 'M'}, {23, 'N'},
    {24, 'O'}, {25, 'P'}, {26, 'Q'}, {27, 'R'}, {28, 'S'}, {29, 'T'},
    {30, 'U'}, {31, 'V'}, {32, 'W'}, {33, 'X'}, {34, 'Y'}, {35, 'Z'}
};

map <char, int> map_CI =
{
    {'0', 0}, {'1', 1}, {'2', 2}, {'3', 3}, {'4', 4}, {'5', 5}, {'6', 6}, {'7', 7}, {'8', 8}, {'9', 9},
    {'A', 10}, {'B', 11}, {'C', 12}, {'D', 13}, {'E', 14}, {'F', 15},
    {'G', 16}, {'H', 17}, {'I', 18}, {'J', 19}, {'K', 20}, {'L', 21}, {'M', 22}, {'N', 23},
    {'O', 24}, {'P', 25}, {'Q', 26}, {'R', 27}, {'S', 28}, {'T', 29},
    {'U', 30}, {'V', 31}, {'W', 32}, {'X', 33}, {'Y', 34}, {'Z', 35}
};

vector <int> tab_residual(int p, int n)
{
   vector <int> tab_resid;
   int r;
   while (n>0)
   {
      r=n%p;
      tab_resid.push_back(r);
      n=n/p;
   }
   return tab_resid;    
}

string number_conv(vector <int> tab_resid)
{
   string numb_conv = "";
   int s;
   s = tab_resid.size();
   for(int i = s - 1; i>= 0; i--)
   {
      numb_conv = numb_conv + mapa_IC[tab_resid[i]];
   }
   return numb_conv;
}

void print_conv(vector <int> tab_resid)
{
   int s;
   s = tab_resid.size();
   cout << "Liczba po konwersji = ";
   for (int i = s - 1; i>=0; i--)
   {
       cout << tab_resid[i];
   }
   cout << "\n";
   return;
}

int main()
{
    int p,n;
    vector <int> tab_resid;
    cout << "Podaj podstawe systemu od 2 do 36 = ";
    cin >> p;
    if (p>=2 && p<=36 && p!=10)
    {
       cout << "Podaj liczbe całkowitą > 0 = ";
       cin >> n;
       if (n>0)
       {
          tab_resid = tab_residual(p, n);
          print_conv(tab_resid);
         
         
         
       }
       else
       {
           cout << "Niepoprawna liczba";
       }
    }
    else
    {
       cout << "Niepoprawna podstawa systemu";    
    }
   return 0;  
}