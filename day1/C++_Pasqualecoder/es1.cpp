#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    ifstream input("numberDay1.txt");
    int counter = 0;
    int n1, n2;
    input >> n1;
    

    while (input >> n2)
    {
        if (n1 < n2)
        {
            counter++;
        }
        n1 = n2;
    }
    
    cout << counter << endl;
    return 0;
}
