#include <complex>
#include <iostream>
using namespace std;
int main()
{
    complex<double> alpha(1.0, 0.0); // α=1+0i
    complex<double> beta(0.0, 0.0);  // β=0+0i
                                     // ∣ψ⟩=1∣0⟩+0∣1⟩

    cout << "alpha = " << alpha << endl;
    cout << "beta  = " << beta << endl;
}