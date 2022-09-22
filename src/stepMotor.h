#pragma once
#include <iostream>
#include "mbed.h"
#include <bitset>
#include <stdint.h>
#include "math.h"


class StepMotor{

    public:
    StepMotor(void); //default
    StepMotor(DigitalOut *pins);
    void twoPhaseRun(uint8_t speed);
    void otherDirection(uint8_t speed);

    private:
    int _length;
    DigitalOut *_steps;
    bitset<4> _nibble = 0b0001;
    


};