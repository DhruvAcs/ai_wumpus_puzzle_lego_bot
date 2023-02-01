from ev3dev2.motor import *
from ev3dev2.sensor.lego import *
from ev3dev2.sensor import INPUT_1,INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sound import Sound
from time import sleep
import os
os.system('setfont Lat15-TerminusBold14')
motorLeft = LargeMotor('outA'); motorLeft.stop_action = 'hold'
motorRight = LargeMotor('outB'); motorRight.stop_action = 'hold'
leftSensor = ColorSensor(INPUT_1)
rightSensor = ColorSensor(INPUT_2)
sound = Sound()
rightBlack = leftSensor.reflected_light_intensity
leftBlack = rightSensor.reflected_light_intensity


sleep(1)
print('Start')
sleep(1)
print(leftBlack)
print(rightBlack)

move = input("Enter command").strip()

if move  == 'f':
    x = True
    while x == True:
        rightBlack = leftSensor.reflected_light_intensity
        leftBlack = rightSensor.reflected_light_intensity
        print(leftBlack,"L")
        print(rightBlack,"R")
        motorLeft.on(speed = -25)
        motorRight.on(speed = -25)
        if rightBlack >20 or leftBlack >20:
            #right is short
            while rightBlack <20:
                motorRight.on(speed = -25)
            #left is short
            while leftBlack <20:
                motorLeft.on(speed = -25)
            motorRight.off()
            motorLeft.off()
        motorLeft.run_to_rel_pos(position_sp= -390, speed_sp = 400)
        motorRight.run_to_rel_pos(position_sp= -390, speed_sp = 400)
        motorLeft.wait_while('running')
        motorRight.wait_while('running')
        

    

elif move == 'r':
    motorLeft.run_to_rel_pos(position_sp= -600, speed_sp = 200)
    motorRight.run_to_rel_pos(position_sp= 600, speed_sp = 200)
    motorLeft.wait_while('running')
    motorRight.wait_while('running')
elif move == 'l':
    motorLeft.run_to_rel_pos(position_sp= 600, speed_sp = 200)
    motorRight.run_to_rel_pos(position_sp= -600, speed_sp = 200)
    motorLeft.wait_while('running')
    motorRight.wait_while('running')