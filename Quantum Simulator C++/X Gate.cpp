#include <iostream>
#include <complex>
#include <vector>

using namespace std;
int main()
{
    complex<double> X[2][2] = {
        {0, 1},
        {1, 0}};
    vector<complex<double>> state = {
        {1, 0},
        {0, 0}};
    vector<complex<double>> new_state(2, {0, 0});
    for (int i = 0; i < 2; i++)
    {
        for (int j = 0; j < 2; j++)
        {
            new_state[i] += X[i][j] * state[j];
        }
    }

    cout << "New state vector: ";
    for (auto amplitude : state)
    {
        cout << amplitude << " ";
    }

    for (auto amplitude : new_state)
    {
        cout << amplitude << " ";
    }
}
