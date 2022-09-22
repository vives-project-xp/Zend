#pragma once
#include <iostream>
#include "stepMotor.h"

class SandTable {

    public:
    SandTable(); //default constructors
    SandTable(StepMotor *yMotor, StepMotor *xMotor);


    private:
    StepMotor *_stepMotorY;
    StepMotor *_stepMotorX;
    
};