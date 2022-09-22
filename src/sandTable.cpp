#include "sandTable.h"

SandTable::SandTable(){};

SandTable::SandTable(StepMotor *yMotor, StepMotor *xMotor){

    this->_stepMotorX = xMotor;
    this->_stepMotorY = yMotor;

}





