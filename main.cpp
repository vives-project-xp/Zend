//mbed deploy then
//mbed compile -f

#include <iostream>
#include "stm32l476xx.h"
#include "mbed.h"
#include "stdint.h"
#include "src/figures.h"
#include <string>
#include "src/stepMotor.h"


using namespace std;

DigitalOut testLed(LED1);
DigitalOut motorSteps[] = {PA_9, PC_7, PB_6, PA_7};
Ticker t;
StepMotor motor(motorSteps);


int main(void){

    int count = 0;


    while(1){

        // motor.twoPhaseRun(1);
        motor.otherDirection(1);

    }


    return 0;
}