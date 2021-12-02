#include <iostream>
#include <fstream>
#include <vector>
#include <array>
using namespace std;

vector<int> fillvector() 
{
    ifstream input("numberDay1.txt");
	vector<int> a;
	int n;
	while (input >> n)
	{
		a.push_back(n);
	}
	return a;
}

int sum(array<int, 3> a)
{
	int somma = 0;
	for (int n : a) somma += n;
	return somma;
}

int main()
{
    int cont = 0;
    vector<int> vettore = fillvector();
	array<int, 3> array = {vettore[0], vettore[1], vettore[2]};
	int somma = sum(array);
	
	for (int i = 1; i < vettore.size(); i++)
	{
		array = {vettore[i], vettore[i+1], vettore[i+2]};
		int nuovasomma = sum(array);
		if (somma < nuovasomma)
		{
			cont++;
		}
		somma = nuovasomma;
	}
	
	cout << cont;
    return 0;    
}
