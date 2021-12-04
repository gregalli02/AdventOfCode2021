#include <bits/stdc++.h>

using namespace std;

string rating(list<string>& misurazioni, char comune, char non_comune){
    int pos_bit=0;
    while (misurazioni.size()>1) {
        int sum = 0;
        for (string s: misurazioni)
            if (s.at(pos_bit) == '1') sum++;


        char bit = (sum*2 >= misurazioni.size()) ? comune : non_comune;

        for (auto listIterator = misurazioni.begin(); listIterator != misurazioni.end() ;) {
            if((*listIterator).at(pos_bit)!=bit){
                listIterator = misurazioni.erase(listIterator);
            }
            else ++listIterator;
        }

        ++pos_bit;
    }
    return misurazioni.front();
}

int main() {
    ifstream in("../../input.txt");
    ofstream out("../output.txt");

    list<string> oxigen, CO2;

    string temp;
    while (in >> temp){
        oxigen.push_back(temp);
        CO2.push_back(temp);
    }


    out << stoi( rating(oxigen, '1', '0'), nullptr, 2) *
           stoi(rating(CO2, '0', '1'), nullptr, 2);

    in.close();
    out.close();
    return 0;
}

