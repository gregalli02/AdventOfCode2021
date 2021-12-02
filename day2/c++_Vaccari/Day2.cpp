#include <iostream>
#include <fstream>
#include <string>
using namespace std;

string estrai(string lin, int* val) {
	int p = lin.find(' ');
	*val = stoi(lin.substr(p));
	return lin.substr(0, p);
}

int es1() {
	ifstream file;
	file.open("file"); 
	string linea;
	int val, h = 0, d = 0;

	if (file.is_open()) {
		while (getline(file, linea)) {

			linea = estrai(linea, &val);
			if (linea == "forward") d += val;
			else if (linea == "down") h += val;
			else if (linea == "up") h -= val;

		}
		file.close();
	}
	return d * h;
}

int es2() {
	ifstream file;
	file.open("file");
	string linea;
	int val, a = 0, h = 0, d = 0;

	if (file.is_open()) {
		while (getline(file, linea)) {

			linea = estrai(linea, &val);
			if (linea == "forward") {
				h += val;
				d += val * a;
			}
			else if (linea == "down") a += val;
			else if (linea == "up") a -= val;

		}
		file.close();
	}
	return d * h;
}


int main()
{
	cout << es1() << endl;
	getchar();
	cout << es2() << endl;
	getchar();
	return 0;
}
