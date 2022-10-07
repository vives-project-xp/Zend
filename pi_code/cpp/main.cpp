#include <iostream>
#include <fstream>
#include <string.h>
#include <ctime>
#include <unistd.h> //DEZE LIB IS NODIG OM DE BOEL OP LINUX TE DOEN WERKEN


using namespace std;

int main(){

    fstream iofile;
    ifstream ifs;
    iofile.open("/dev/ttyACM0", ios::out | ios::in);
       

    if(!iofile){
        cerr << "could not connect " << endl;
    }else{

        cout << "connected" << endl;
    }

    if(!ifs){
        cerr << "input reading not ok" << endl;

    }else{

        cout << "input reading file stuff opened" << endl;
    }

    string output;
    cout << "Enter command" << endl;
    getline(cin, output);

    iofile.close();

    ifs.open("/dev/ttyACM0");


    ifs >> output;

    cout << output << endl;

    ifs.close();





    

    cout << "file succesfully closed" << endl;

}