// Online C++ compiler to run C++ program online
#include <iostream>
#include <string>
using namespace std;


int main() {
    // Write C++ code here
    double x, y, z;
    char op;
    string choices;
    
    do{
            
    cout << "Welcome to the Simple Calculator Program!" << endl;
    cout << "Enter the first number:\t";
    cin >> x;
    
    cout << "Enter the second number:\t";
    cin >> y;
    
    cout << "Please enter an operator (+, -, *, /):\t";
    cin >> op;
    
    switch(op){
        case '+':
            z = x+y;
            cout << x << " " << op << " " << y << " is equal to " << z << endl;
            break;
        case '-':
            z = x-y;
            cout << x << " " << op << " " << y << " is equal to " << z << endl;
            break;
        case '*':
            z = x*y;
            cout << x << " " << op << " " << y << " is equal to " << z << endl;
            break;
        case '/':
            if (y!=0){
                z = x/y;
                cout << x << " " << op << " " << y << " is equal to " << z << endl;
            }
            else{
                cout << "Error! Division with zero is not allowed!" << endl;
            }
            break;
        default:
        cout << "Invalid operator !";
    } // switch curly brace

    cout << "Do you want to perform another operation? (yes/no)\t" << endl;
    cin >> choices;
    } while (choices == "yes");
    
    cout << "Thank you for using the simple calculator! See you!";
    return 0;
}