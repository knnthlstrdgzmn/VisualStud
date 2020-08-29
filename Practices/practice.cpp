#include <iostream>
#include <cmath>
using namespace std;

int main () {

while(true){

int fnum, snum, sum;
char operation;


cout << "input first num: " << endl;
cin >> fnum;
cout << "input operator: " << endl;
cin >> operation;
cout << "input second num: " << endl;
cin >> snum;

if (operation == '+') {
    sum = fnum + snum;
    cout << "result:" << sum;

}
else if (operation == '-') {
    sum = fnum - snum;
    cout << "result:" << sum;

}
else if (operation == '*') {
    sum = fnum * snum;
    cout << "result:" << sum;

}
else if (operation == '/') {
        if (snum == 0){

            cout << "error";
        }
    sum = fnum / snum;
    cout << "result:" << sum;

}
else {
cout << "error";
}
 continue;
}

return 0;


}
