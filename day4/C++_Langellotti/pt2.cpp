#include <bits/stdc++.h>

using namespace std;

const int righe=500;
int grids[righe][5];
bool marked[righe][5];

void init_estrazione(vector<int>& estrazione, const string& s){
    unsigned int pos_num=0, pos_virg=s.find(',', 1);
    while (pos_virg!=string::npos){
        estrazione.push_back(stoi(s.substr(pos_num, pos_virg-pos_num)));
        pos_num = pos_virg+1;
        pos_virg = s.find(',', pos_num);
    }
}

bool trovato(int riga, int colonna) {
    bool risultato = true;
    for (bool mark: marked[riga])
        if(!mark){
            risultato = false;
            break;
        }

    if(risultato) return true;

    risultato = true;
    int r0 = riga-riga%5;//prima riga del tabellone
    for (int i = 0; i<5; ++i)
        if(!marked[i+r0][colonna]){
            risultato = false;
            break;
        }

    return risultato;
}

int main() {
    ifstream in("../../input.txt");
    ofstream out("../output.txt");

    vector<int> estrazione;
    string stringa_estrazione;
    in >> stringa_estrazione;
    init_estrazione(estrazione, stringa_estrazione);

    for(auto & riga: grids)
        in >> riga[0] >> riga[1] >> riga[2] >> riga[3] >> riga[4];

    for (auto &riga: marked) for(bool& el: riga) {el = false;}

    int ultimo_tab=0;
    pair<int,int> i_val_ultimo = {-1, -1};
    for (int rO = 0; rO < righe; rO+=5) {
        int pos_estrazione = 0;
        bool vinto=false;
        while (!vinto) {
            int estratto = estrazione.at(pos_estrazione);

            for (int i = 0; i < 5; ++i) {
                for (int j = 0; j < 5; ++j) {
                    if (grids[i+rO][j] == estratto) {
                        marked[i+rO][j] = true;
                        if (trovato(i+rO, j)) {
                            if(pos_estrazione > ultimo_tab) {
                                ultimo_tab=pos_estrazione;
                                i_val_ultimo = {i+rO, j};
                            }
                            vinto=true;
                            i=5; break;
                        }
                    }
                }
            }
            pos_estrazione++;
        }
    }

    int sum_non_estratti=0;
    int r0 = i_val_ultimo.first - i_val_ultimo.first%5;//prima riga del tabellone
    for (int i = 0; i<5; ++i)
        for (int j = 0; j<5; ++j)
            if(!marked[i+r0][j]) sum_non_estratti+=grids[i+r0][j];

    cout << grids[i_val_ultimo.first][i_val_ultimo.second] << " " << sum_non_estratti;
    out << grids[i_val_ultimo.first][i_val_ultimo.second] * sum_non_estratti;

    in.close();
    out.close();
    return 0;
}

/*
    for (int i = 0; i < righe; ++i) {
        for (int j = 0; j < 5; ++j) {
            cout << grids[i][j] << " ";
        }
        cout << "\n";
    }
*/

