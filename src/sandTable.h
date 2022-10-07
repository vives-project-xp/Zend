#pragma once 
#include <iostream>
#include "figure.h"

class SandTable{

    public:
    SandTable(void); //default constructor
    void sendFigure(Figure figure);
    void resetPosition();
    void testSerialPort();


    private:
    Figure _figure;


};          