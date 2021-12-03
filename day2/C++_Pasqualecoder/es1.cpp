#include <iostream>
#include <fstream>
using namespace std;

class Comando {
	public:
		string direzione;
		int valore;

		Comando(string s) {
			direzione = s.substr(0, s.find(' '));
			char carattere_valore = s[s.length()-1];
			valore = carattere_valore - '0';
			if (direzione == "up")
			{
				valore *= -1;
			}
		}
};

int main()
{
	ifstream input("numberDay2.txt");
	string stringa;
	int horizontal = 0, depth = 0;

	while (getline(input, stringa))
	{
		Comando comando(stringa);

		if (comando.direzione == "forward")
		{
			horizontal += comando.valore;
		}
		else {
			depth += comando.valore;
		}
	}

	cout << (horizontal * depth);
	input.close();
	return 0;
}
