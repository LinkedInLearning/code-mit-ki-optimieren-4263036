/*#################################################
Die Funktionen eingabe() und ausgabe()
################################################# */
#include <iostream>
using namespace std;

int eingabe()
{
  int eingabeZahl;
  cout << "Bitte geben Sie eine Zahl ein: ";
  cin >> eingabeZahl;
  
  return (eingabeZahl);
}

void ausgabe(int zahl)
{
  cout << "Sie haben " << zahl << " eingegeben.\n";
}
