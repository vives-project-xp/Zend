//mbed deploy then
//mbed compile -f

#include <iostream>
#include "stm32l476xx.h"
#include "mbed.h"
#include "stdint.h"
#include <string>
#include "src/sandTable.h"


using namespace std;

DigitalOut testLed(LED1);
DigitalOut motorSteps[] = {PA_9, PC_7, PB_6, PA_7};
Ticker t;

int main(void){

    int count = 0;


    return 0;
}