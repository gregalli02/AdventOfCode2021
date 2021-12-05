#include <bits/stdc++.h>

using namespace std;

#define VAL_MASSIMO 1000
#define NSEGMENTI 500;
int mappa[VAL_MASSIMO][VAL_MASSIMO];

int main() {
    ofstream out("../output.txt");

    for (auto &i: mappa) for (auto &j: i) j = 0;

    int x1, y1, x2, y2;
    FILE *f = fopen("../../input.txt", "r");
    while (fscanf(f, "%d,%d -> %d,%d", &x1, &y1, &x2, &y2) != EOF) {
        if (x1 == x2) {
            if (y1 > y2) swap(y1, y2);
            for (int y = y1; y <= y2; ++y)
                mappa[y][x1]++;
        } else if (y1 == y2) {
            if (x1 > x2) swap(x1, x2);
            for (int x = x1; x <= x2; ++x)
                mappa[y1][x]++;
        }
    }


    int QUANTI = 0;
    for (auto &i: mappa)
        for (auto &el: i)
            if (el >= 2)
                QUANTI++;

    out << QUANTI;


    return 0;
}
