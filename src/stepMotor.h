#pragma once
#include <iostream>
#include "mbed.h"
#include <bitset>
#include <stdint.h>
#include "math.h"

#ifndef SEGMENT_BUFFER_SIZE 6
#define SEGMENT_BUFFER_SIZE 6
#endif




class StepMotor{

    public:
    
    // initialize stepper subsystem
    void stepper_init();

    // Enable steppers but don't start moving yet
    void wake_up();

    // Immediatly disable steppers
    void go_idle();

    // Generate step and direction port invert masks(???)
    void generate_step_dir_invert_masks();

    // Reset stepper subsystem variables
    void reset();

    // Changes the run state of the step segment buffer to execute the special parking motion
    void parking_setup_buffer();

    // Restores the step segment buffer to the normal run state after a parking motion
    void parking_restore_buffer();

    // Reloads the step segment buffer. Called continuously by realtime execution system
    void prep_buffer();

    // This function is called by planner_recalculate() when the executing block is updated by the new plan
    void update_plan_block_parameters();

    // Called by realtime status reporting if realtime rate reporting is enabled in config.h
    float get_realtime_rate();

};