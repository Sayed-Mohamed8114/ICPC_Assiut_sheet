#include <iostream>
using namespace std;
int main()
{
    long long x, y, z, s;
    cin >> x >> y >> z >> s;
    long long difference;
    difference = (x * y) - (z * s);
    cout << "Difference = " << difference << endl;
    return 0;
}