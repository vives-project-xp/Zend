#include "stepMotor.h"

StepMotor::StepMotor(void){}

StepMotor::StepMotor(DigitalOut *steps){
    this->_steps = steps;
    
}


void StepMotor::twoPhaseRun(uint8_t speed){

    _steps[0].write(1);
    _steps[1].write(0);
    wait_us(speed * 10000);
    _steps[0].write(0);
    _steps[1].write(1);
    wait_us(speed * 10000);

}

void StepMotor::otherDirection(uint8_t speed){

    _steps[0].write(0);
    _steps[1].write(1);
    wait_us(speed * 10000);
    _steps[0].write(1);
    _steps[1].write(0);
    wait_us(speed * 10000);



}







