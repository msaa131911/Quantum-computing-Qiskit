#include <iostream>
#include <complex>
#include <vector>
using namespace std;

int main()
{
    vector<complex<double>> state_vector = {{1, 0}, {0, 0}, {0, 0}, {0, 0}};
    cout << "state vector: ";
    for (auto amplitude : state_vector)
    {
        cout << amplitude << " ";
    }
}