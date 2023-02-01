#!/usr/bin/env python3
from ev3dev2.motor import *
from ev3dev2.sensor.lego import *
from ev3dev2.sensor import INPUT_1,INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sound import Sound
from time import sleep
import time
import os
os.system('setfont Lat15-TerminusBold14')
#Initializing motors
#CHECK THAT YOUR CHANNELS "outA, outB, outC, outD" ARE CORRECT BEFORE RUNNING
motorLeft = LargeMotor('outB'); motorLeft.stop_action = 'hold'
motorRight = LargeMotor('outC'); motorRight.stop_action = 'hold'
cannon = MediumMotor('outD'); motorRight.stop_action = 'hold'
#Uncomment the line below if you want to use the third, smaller, motor for anything
#MM = MediumMotor('outA'); MM.stop_action = 'hold' z

#face = 'north'

#Initializing lightsensors
# 
leftSensor = ColorSensor(INPUT_3)
rightSensor = ColorSensor(INPUT_2)

#If you want your robot to make sounds!
sound = Sound()

#Setting a black value to compare to. Reflected light intensity returns a number between 0 and 100 -- higher values are brighter, lower values are darker.
rightBlack = leftSensor.reflected_light_intensity
leftBlack = rightSensor.reflected_light_intensity



sleep(1)
print('Start')
sound.speak('Halla halla')
sleep(1)
print(leftBlack)
print(rightBlack)


kill=False
def move(kill,current,next,face):
    print(face)
    print('face should have just been printed')
    y1,x1 = current
    y2,x2 = next
    change = 'change'
    #find out what position from startingt position the box is if you look at the grid as a xy plane
    if x2 == x1:
        if y1 < y2:
            change = 'up'
        else:
            change = 'down'
    else:
        if x1 < x2:
            change = 'right'
        else:
            change = 'left'   

    if face == 'north':
        if change == 'up': # move forward
            x = True
            while x == True:
                rightBlack = leftSensor.reflected_light_intensity
                leftBlack = rightSensor.reflected_light_intensity
                print(leftBlack,"L")
                print(rightBlack,"R")
                motorLeft.on(speed = -20)
                motorRight.on(speed = -20)
                if rightBlack >20 or leftBlack >20:
                    motorLeft.off()
                    motorRight.off()
                    break
            #right is short
            if rightBlack < 20:
                while rightBlack <20:
                    rightBlack = leftSensor.reflected_light_intensity
                    leftBlack = rightSensor.reflected_light_intensity
                    motorRight.on(speed = -15)
                
            #left is short
            if leftBlack <20:
                while leftBlack <20:
                    rightBlack = leftSensor.reflected_light_intensity
                    leftBlack = rightSensor.reflected_light_intensity
                    motorLeft.on(speed = -15)
                    if rightBlack >20 and leftBlack >20:
                        motorLeft.off()
                        motorRight.off()
                   
            if kill==False:
                motorLeft.run_to_rel_pos(position_sp= -600, speed_sp = 300)
                motorRight.run_to_rel_pos(position_sp= -600, speed_sp = 300)
                motorLeft.wait_while('running')
                motorRight.wait_while('running')
        elif change == 'down': # 180 and then forward\
            motorLeft.run_to_rel_pos(position_sp= 380, speed_sp = 200)
            motorRight.run_to_rel_pos(position_sp= -380, speed_sp = 200)
            motorLeft.wait_while('runninfg')
            motorRight.wait_while('running')
            x = True
            while x == True:
                rightBlack = leftSensor.reflected_light_intensity
                leftBlack = rightSensor.reflected_light_intensity
                print(leftBlack,"L")
                print(rightBlack,"R")
                motorLeft.on(speed = -20)
                motorRight.on(speed = -20)
                if rightBlack >20 or leftBlack >20:
                    motorLeft.off()
                    motorRight.off()
                    break
            #right is short
            if rightBlack < 20:
                while rightBlack <20:
                    rightBlack = leftSensor.reflected_light_intensity
                    leftBlack = rightSensor.reflected_light_intensity
                    motorRight.on(speed = -15)
                
            #left is short
            if leftBlack <20:
                while leftBlack <20:
                    rightBlack = leftSensor.reflected_light_intensity
                    leftBlack = rightSensor.reflected_light_intensity
                    motorLeft.on(speed = -15)
                    if rightBlack >20 and leftBlack >20:
                        motorLeft.off()
                        motorRight.off()
                
            if kill==False:
                motorLeft.run_to_rel_pos(position_sp= -600, speed_sp = 300)
                motorRight.run_to_rel_pos(position_sp= -600, speed_sp = 300)
                motorLeft.wait_while('running')
                motorRight.wait_while('running')

        elif change == 'right':#right then forward
            motorLeft.run_to_rel_pos(position_sp= -190, speed_sp = 200)
            motorRight.run_to_rel_pos(position_sp= 190, speed_sp = 200)
            motorLeft.wait_while('running')
            motorRight.wait_while('running')
            x = True
            while x == True:
                rightBlack = leftSensor.reflected_light_intensity
                leftBlack = rightSensor.reflected_light_intensity
                print(leftBlack,"L")
                print(rightBlack,"R")
                motorLeft.on(speed = -20)
                motorRight.on(speed = -20)
                if rightBlack >20 or leftBlack >20:
                    motorLeft.off()
                    motorRight.off()
                    break
            #right is short
            if rightBlack < 20:
                while rightBlack <20:
                    rightBlack = leftSensor.reflected_light_intensity
                    leftBlack = rightSensor.reflected_light_intensity
                    motorRight.on(speed = -15)
                
            #left is short
            if leftBlack <20:
                while leftBlack <20:
                    rightBlack = leftSensor.reflected_light_intensity
                    leftBlack = rightSensor.reflected_light_intensity
                    motorLeft.on(speed = -15)
                    if rightBlack >20 and leftBlack >20:
                        motorLeft.off()
                        motorRight.off()
                
            if kill==False:
                motorLeft.run_to_rel_pos(position_sp= -600, speed_sp = 300)
                motorRight.run_to_rel_pos(position_sp= -600, speed_sp = 300)
                motorLeft.wait_while('running')
                motorRight.wait_while('running')
        else:#left then forward
            motorLeft.run_to_rel_pos(position_sp= 190, speed_sp = 200)
            motorRight.run_to_rel_pos(position_sp= -190, speed_sp = 200)
            motorLeft.wait_while('running')
            motorRight.wait_while('running')
            x = True
            while x == True:
                rightBlack = leftSensor.reflected_light_intensity
                leftBlack = rightSensor.reflected_light_intensity
                print(leftBlack,"L")
                print(rightBlack,"R")
                motorLeft.on(speed = -20)
                motorRight.on(speed = -20)
                if rightBlack >20 or leftBlack >20:
                    motorLeft.off()
                    motorRight.off()
                    break
            #right is short
            if rightBlack < 20:
                while rightBlack <20:
                    rightBlack = leftSensor.reflected_light_intensity
                    leftBlack = rightSensor.reflected_light_intensity
                    motorRight.on(speed = -15)
                
            #left is short
            if leftBlack <20:
                while leftBlack <20:
                    rightBlack = leftSensor.reflected_light_intensity
                    leftBlack = rightSensor.reflected_light_intensity
                    motorLeft.on(speed = -15)
                    if rightBlack >20 and leftBlack >20:
                        motorLeft.off()
                        motorRight.off()
                
            if kill==False:
                motorLeft.run_to_rel_pos(position_sp= -600, speed_sp = 300)
                motorRight.run_to_rel_pos(position_sp= -600, speed_sp = 300)
                motorLeft.wait_while('running')
                motorRight.wait_while('running')

    elif face == 'east':
        if change == 'up': # move forward
            motorLeft.run_to_rel_pos(position_sp= 190, speed_sp = 200)
            motorRight.run_to_rel_pos(position_sp= -190, speed_sp = 200)
            motorLeft.wait_while('running')
            motorRight.wait_while('running')
            x = True
            while x == True:
                rightBlack = leftSensor.reflected_light_intensity
                leftBlack = rightSensor.reflected_light_intensity
                print(leftBlack,"L")
                print(rightBlack,"R")
                motorLeft.on(speed = -20)
                motorRight.on(speed = -20)
                if rightBlack >20 or leftBlack >20:
                    motorLeft.off()
                    motorRight.off()
                    break
            #right is short
            if rightBlack < 20:
                while rightBlack <20:
                    rightBlack = leftSensor.reflected_light_intensity
                    leftBlack = rightSensor.reflected_light_intensity
                    motorRight.on(speed = -15)
                
            #left is short
            if leftBlack <20:
                while leftBlack <20:
                    rightBlack = leftSensor.reflected_light_intensity
                    leftBlack = rightSensor.reflected_light_intensity
                    motorLeft.on(speed = -15)
                    if rightBlack >20 and leftBlack >20:
                        motorLeft.off()
                        motorRight.off()
                
            if kill==False:
                motorLeft.run_to_rel_pos(position_sp= -600, speed_sp = 300)
                motorRight.run_to_rel_pos(position_sp= -600, speed_sp = 300)
                motorLeft.wait_while('running')
                motorRight.wait_while('running')
        elif change == 'down':
            motorLeft.run_to_rel_pos(position_sp= -190, speed_sp = 200)
            motorRight.run_to_rel_pos(position_sp= 190, speed_sp = 200)
            motorLeft.wait_while('running')
            motorRight.wait_while('running')
            x = True
            while x == True:
                rightBlack = leftSensor.reflected_light_intensity
                leftBlack = rightSensor.reflected_light_intensity
                print(leftBlack,"L")
                print(rightBlack,"R")
                motorLeft.on(speed = -20)
                motorRight.on(speed = -20)
                if rightBlack >20 or leftBlack >20:
                    motorLeft.off()
                    motorRight.off()
                    break
            #right is short
            if rightBlack < 20:
                while rightBlack <20:
                    rightBlack = leftSensor.reflected_light_intensity
                    leftBlack = rightSensor.reflected_light_intensity
                    motorRight.on(speed = -15)
                
            #left is short
            if leftBlack <20:
                while leftBlack <20:
                    rightBlack = leftSensor.reflected_light_intensity
                    leftBlack = rightSensor.reflected_light_intensity
                    motorLeft.on(speed = -15)
                    if rightBlack >20 and leftBlack >20:
                        motorLeft.off()
                        motorRight.off()
                
            if kill==False:
                motorLeft.run_to_rel_pos(position_sp= -600, speed_sp = 300)
                motorRight.run_to_rel_pos(position_sp= -600, speed_sp = 300)
                motorLeft.wait_while('running')
                motorRight.wait_while('running')

        elif change == 'right':#right then forward
            x = True
            while x == True:
                rightBlack = leftSensor.reflected_light_intensity
                leftBlack = rightSensor.reflected_light_intensity
                print(leftBlack,"L")
                print(rightBlack,"R")
                motorLeft.on(speed = -20)
                motorRight.on(speed = -20)
                if rightBlack >20 or leftBlack >20:
                    motorLeft.off()
                    motorRight.off()
                    break
            #right is short
            if rightBlack < 20:
                while rightBlack <20:
                    rightBlack = leftSensor.reflected_light_intensity
                    leftBlack = rightSensor.reflected_light_intensity
                    motorRight.on(speed = -15)
                
            #left is short
            if leftBlack <20:
                while leftBlack <20:
                    rightBlack = leftSensor.reflected_light_intensity
                    leftBlack = rightSensor.reflected_light_intensity
                    motorLeft.on(speed = -15)
                    if rightBlack >20 and leftBlack >20:
                        motorLeft.off()
                        motorRight.off()
                
            if kill==False:
                motorLeft.run_to_rel_pos(position_sp= -600, speed_sp = 300)
                motorRight.run_to_rel_pos(position_sp= -600, speed_sp = 300)
                motorLeft.wait_while('running')
                motorRight.wait_while('running')
        else:
            motorLeft.run_to_rel_pos(position_sp= 380, speed_sp = 200)
            motorRight.run_to_rel_pos(position_sp= -380, speed_sp = 200)
            motorLeft.wait_while('running')
            motorRight.wait_while('running')
            x = True
            while x == True:
                rightBlack = leftSensor.reflected_light_intensity
                leftBlack = rightSensor.reflected_light_intensity
                print(leftBlack,"L")
                print(rightBlack,"R")
                motorLeft.on(speed = -20)
                motorRight.on(speed = -20)
                if rightBlack >20 or leftBlack >20:
                    motorLeft.off()
                    motorRight.off()
                    break
            #right is short
            if rightBlack < 20:
                while rightBlack <20:
                    rightBlack = leftSensor.reflected_light_intensity
                    leftBlack = rightSensor.reflected_light_intensity
                    motorRight.on(speed = -15)

                
            #left is short
            if leftBlack <20:
                while leftBlack <20:
                    rightBlack = leftSensor.reflected_light_intensity
                    leftBlack = rightSensor.reflected_light_intensity
                    motorLeft.on(speed = -15)
                    if rightBlack >20 and leftBlack >20:
                        motorLeft.off()
                        motorRight.off()
                
            if kill==False:
                motorLeft.run_to_rel_pos(position_sp= -600, speed_sp = 300)
                motorRight.run_to_rel_pos(position_sp= -600, speed_sp = 300)
                motorLeft.wait_while('running')
                motorRight.wait_while('running')

    elif face == 'south':
        if change == 'up': # move forward
            motorLeft.run_to_rel_pos(position_sp= 380, speed_sp = 200)
            motorRight.run_to_rel_pos(position_sp= -380, speed_sp = 200)
            motorLeft.wait_while('running')
            motorRight.wait_while('running')
            x = True
            while x == True:
                rightBlack = leftSensor.reflected_light_intensity
                leftBlack = rightSensor.reflected_light_intensity
                print(leftBlack,"L")
                print(rightBlack,"R")
                motorLeft.on(speed = -20)
                motorRight.on(speed = -20)
                if rightBlack >20 or leftBlack >20:
                    motorLeft.off()
                    motorRight.off()
                    break
            #right is short
            if rightBlack < 20:
                while rightBlack <20:
                    rightBlack = leftSensor.reflected_light_intensity
                    leftBlack = rightSensor.reflected_light_intensity
                    motorRight.on(speed = -15)
                
            #left is short
            if leftBlack <20:
                while leftBlack <20:
                    rightBlack = leftSensor.reflected_light_intensity
                    leftBlack = rightSensor.reflected_light_intensity
                    motorLeft.on(speed = -15)
                    if rightBlack >20 and leftBlack >20:
                        motorLeft.off()
                        motorRight.off()
               
            if kill==False:
                motorLeft.run_to_rel_pos(position_sp= -600, speed_sp = 300)
                motorRight.run_to_rel_pos(position_sp= -600, speed_sp = 300)
                motorLeft.wait_while('running')
                motorRight.wait_while('running')
        elif change == 'down': # 180 and then forward\
            x = True
            while x == True:
                rightBlack = leftSensor.reflected_light_intensity
                leftBlack = rightSensor.reflected_light_intensity
                print(leftBlack,"L")
                print(rightBlack,"R")
                motorLeft.on(speed = -20)
                motorRight.on(speed = -20)
                if rightBlack >20 or leftBlack >20:
                    motorLeft.off()
                    motorRight.off()
                    break
            #right is short
            if rightBlack < 20:
                while rightBlack <20:
                    rightBlack = leftSensor.reflected_light_intensity
                    leftBlack = rightSensor.reflected_light_intensity
                    motorRight.on(speed = -15)
                
            #left is short
            if leftBlack <20:
                while leftBlack <20:
                    rightBlack = leftSensor.reflected_light_intensity
                    leftBlack = rightSensor.reflected_light_intensity
                    motorLeft.on(speed = -15)
                    if rightBlack >20 and leftBlack >20:
                        motorLeft.off()
                        motorRight.off()
                
            if kill==False:
                motorLeft.run_to_rel_pos(position_sp= -600, speed_sp = 300)
                motorRight.run_to_rel_pos(position_sp= -600, speed_sp = 300)
                motorLeft.wait_while('running')
                motorRight.wait_while('running')

        elif change == 'right':#right then forward
            motorLeft.run_to_rel_pos(position_sp= 190, speed_sp = 200)
            motorRight.run_to_rel_pos(position_sp= -190, speed_sp = 200)
            motorLeft.wait_while('running')
            motorRight.wait_while('running')
            x = True
            while x == True:
                rightBlack = leftSensor.reflected_light_intensity
                leftBlack = rightSensor.reflected_light_intensity
                print(leftBlack,"L")
                print(rightBlack,"R")
                motorLeft.on(speed = -20)
                motorRight.on(speed = -20)
                if rightBlack >20 or leftBlack >20:
                    motorLeft.off()
                    motorRight.off()
                    break
            #right is short
            if rightBlack < 20:
                while rightBlack <20:
                    rightBlack = leftSensor.reflected_light_intensity
                    leftBlack = rightSensor.reflected_light_intensity
                    motorRight.on(speed = -15)
               
            #left is short
            if leftBlack <20:
                while leftBlack <20:
                    rightBlack = leftSensor.reflected_light_intensity
                    leftBlack = rightSensor.reflected_light_intensity
                    motorLeft.on(speed = -15)
                    if rightBlack >20 and leftBlack >20:
                        motorLeft.off()
                        motorRight.off()
               
            if kill==False:
                motorLeft.run_to_rel_pos(position_sp= -600, speed_sp = 300)
                motorRight.run_to_rel_pos(position_sp= -600, speed_sp = 300)
                motorLeft.wait_while('running')
                motorRight.wait_while('running')
        else:#left then forward
            motorLeft.run_to_rel_pos(position_sp= -190, speed_sp = 200)
            motorRight.run_to_rel_pos(position_sp= 190, speed_sp = 200)
            motorLeft.wait_while('running')
            motorRight.wait_while('running')
            x = True
            while x == True:
                rightBlack = leftSensor.reflected_light_intensity
                leftBlack = rightSensor.reflected_light_intensity
                print(leftBlack,"L")
                print(rightBlack,"R")
                motorLeft.on(speed = -20)
                motorRight.on(speed = -20)
                if rightBlack >20 or leftBlack >20:
                    motorLeft.off()
                    motorRight.off()
                    break
            #right is short
            if rightBlack < 20:
                while rightBlack <20:
                    rightBlack = leftSensor.reflected_light_intensity
                    leftBlack = rightSensor.reflected_light_intensity
                    motorRight.on(speed = -15)
                
            #left is short
            if leftBlack <20:
                while leftBlack <20:
                    rightBlack = leftSensor.reflected_light_intensity
                    leftBlack = rightSensor.reflected_light_intensity
                    motorLeft.on(speed = -15)
                    if rightBlack >20 and leftBlack >20:
                        motorLeft.off()
                        motorRight.off()
               
            if kill==False:
                motorLeft.run_to_rel_pos(position_sp= -600, speed_sp = 300)
                motorRight.run_to_rel_pos(position_sp= -600, speed_sp = 300)
                motorLeft.wait_while('running')
                motorRight.wait_while('running')
    
    elif face == 'west':
        if change == 'up': # move forward
            motorLeft.run_to_rel_pos(position_sp= -190, speed_sp = 200)
            motorRight.run_to_rel_pos(position_sp= 190, speed_sp = 200)
            motorLeft.wait_while('running')
            motorRight.wait_while('running')
            x = True
            while x == True:
                rightBlack = leftSensor.reflected_light_intensity
                leftBlack = rightSensor.reflected_light_intensity
                print(leftBlack,"L")
                print(rightBlack,"R")
                motorLeft.on(speed = -20)
                motorRight.on(speed = -20)
                if rightBlack >20 or leftBlack >20:
                    motorLeft.off()
                    motorRight.off()
                    break
            #right is short
            if rightBlack < 20:
                while rightBlack <20:
                    rightBlack = leftSensor.reflected_light_intensity
                    leftBlack = rightSensor.reflected_light_intensity
                    motorRight.on(speed = -15)
                
            #left is short
            if leftBlack <20:
                while leftBlack <20:
                    rightBlack = leftSensor.reflected_light_intensity
                    leftBlack = rightSensor.reflected_light_intensity
                    motorLeft.on(speed = -15)
                    if rightBlack >20 and leftBlack >20:
                        motorLeft.off()
                        motorRight.off()
              
            if kill==False:
                motorLeft.run_to_rel_pos(position_sp= -600, speed_sp = 300)
                motorRight.run_to_rel_pos(position_sp= -600, speed_sp = 300)
                motorLeft.wait_while('running')
                motorRight.wait_while('running')
        elif change == 'down': # 180 and then forward\
            motorLeft.run_to_rel_pos(position_sp= 190, speed_sp = 200)
            motorRight.run_to_rel_pos(position_sp= -190, speed_sp = 200)
            motorLeft.wait_while('running')
            motorRight.wait_while('running')
            x = True
            while x == True:
                rightBlack = leftSensor.reflected_light_intensity
                leftBlack = rightSensor.reflected_light_intensity
                print(leftBlack,"L")
                print(rightBlack,"R")
                motorLeft.on(speed = -20)
                motorRight.on(speed = -20)
                if rightBlack >20 or leftBlack >20:
                    motorLeft.off()
                    motorRight.off()
                    break
            #right is short
            if rightBlack < 20:
                while rightBlack <20:
                    rightBlack = leftSensor.reflected_light_intensity
                    leftBlack = rightSensor.reflected_light_intensity
                    motorRight.on(speed = -15)
                
            #left is short
            if leftBlack <20:
                while leftBlack <20:
                    rightBlack = leftSensor.reflected_light_intensity
                    leftBlack = rightSensor.reflected_light_intensity
                    motorLeft.on(speed = -15)
                    if rightBlack >20 and leftBlack >20:
                        motorLeft.off()
                        motorRight.off()
               
            if kill==False:
                motorLeft.run_to_rel_pos(position_sp= -600, speed_sp = 300)
                motorRight.run_to_rel_pos(position_sp= -600, speed_sp = 300)
                motorLeft.wait_while('running')
                motorRight.wait_while('running')

        elif change == 'right':#right then forward
            motorLeft.run_to_rel_pos(position_sp= 380, speed_sp = 200)
            motorRight.run_to_rel_pos(position_sp= -380, speed_sp = 200)
            motorLeft.wait_while('running')
            motorRight.wait_while('running')
            x = True
            while x == True:
                rightBlack = leftSensor.reflected_light_intensity
                leftBlack = rightSensor.reflected_light_intensity
                print(leftBlack,"L")
                print(rightBlack,"R")
                motorLeft.on(speed = -20)
                motorRight.on(speed = -20)
                if rightBlack >20 or leftBlack >20:
                    motorLeft.off()
                    motorRight.off()
                    break
            #right is short
            if rightBlack < 20:
                while rightBlack <20:
                    rightBlack = leftSensor.reflected_light_intensity
                    leftBlack = rightSensor.reflected_light_intensity
                    motorRight.on(speed = -15)
               
            #left is short
            if leftBlack <20:
                while leftBlack <20:
                    rightBlack = leftSensor.reflected_light_intensity
                    leftBlack = rightSensor.reflected_light_intensity
                    motorLeft.on(speed = -15)
                    if rightBlack >20 and leftBlack >20:
                        motorLeft.off()
                        motorRight.off()
                
            if kill==False:
                motorLeft.run_to_rel_pos(position_sp= -600, speed_sp = 300)
                motorRight.run_to_rel_pos(position_sp= -600, speed_sp = 300)
                motorLeft.wait_while('running')
                motorRight.wait_while('running')
        else:#left then forward
            x = True
            while x == True:
                rightBlack = leftSensor.reflected_light_intensity
                leftBlack = rightSensor.reflected_light_intensity
                print(leftBlack,"L")
                print(rightBlack,"R")
                motorLeft.on(speed = -20)
                motorRight.on(speed = -20)
                if rightBlack >20 or leftBlack >20:
                    motorLeft.off()
                    motorRight.off()
                    break
            #right is short
            if rightBlack < 20:
                while rightBlack <20:
                    rightBlack = leftSensor.reflected_light_intensity
                    leftBlack = rightSensor.reflected_light_intensity
                    motorRight.on(speed = -15)
                
            #left is short
            if leftBlack <20:
                while leftBlack <20:
                    rightBlack = leftSensor.reflected_light_intensity
                    leftBlack = rightSensor.reflected_light_intensity
                    motorLeft.on(speed = -15)
                    if rightBlack >20 and leftBlack >20:
                        motorLeft.off()
                        motorRight.off()
                
            if kill==False:
                motorLeft.run_to_rel_pos(position_sp= -600, speed_sp = 300)
                motorRight.run_to_rel_pos(position_sp= -600, speed_sp = 300)
                motorLeft.wait_while('running')
                motorRight.wait_while('running')
    if change == 'up':
        face = 'north'
    elif change == 'down':
        face = 'south'
    elif change == 'right':
        face = 'east'
    elif change == 'left':
        face = 'west'
    print(change)
    print(face)
    return face
    

grid=[(0,0),(0,1),(0,2),(0,3),\
      (1,0),(1,1),(1,2),(1,3),\
      (2,0),(2,1),(2,2),(2,3),\
      (3,0),(3,1),(3,2),(3,3)]
    
def close_to(tup1,tup2):  #outputs places that are between the first and second tuple
    ret=[]
    x1,y1=tup1
    x2,y2=tup2
    if x1<x2:
        if ((x1+1),y1) in grid:
            ret.append(((x1+1),y1))
    if x1>x2:
        if ((x1-1),y1) in grid:
            ret.append(((x1-1),y1))
    if y1<y2:
        if (x1,(y1+1)) in grid:
            ret.append((x1,(y1+1)))
    if y1>y2:
        if (x1,(y1-1)) in grid:
            ret.append((x1,(y1-1)))
    return(ret)
    
def nbrs(tup):   #gets neighbors
    ret=[]
    x=tup[0]
    y=tup[1]
    for place in grid:
        if (place[0]==x) and (abs(place[1]-y)==1) or ((abs(place[0]-x)==1) and (place[1]==y)) and (place[0],place[1]) in grid:
            ret.append((place[0],place[1]))
    return(ret)

def check(FreeList):  #checks if the robot has all the info it needs to find the gold
    for free in FreeList:
        for nbr in nbrs(free):
            if dic[nbr]==False:
                return(False)
    return(True)

def move_to(now,then,say,PlaceList,face):
    failsafe=[]
    des=0
    while now!=then:
        dest=nbrs(now)
        if then in dest:
            print(face)
            face=move(False,now,then,face)
            now=then
            print('move to {}'.format(now))    #done
            if (not say==''):
                print('{}{}'.format(say,now))
            break
        for nbr in dest:
            if (dic[nbr]==True) and (nbr in close_to(now,then)):  
                face=move(False,now,nbr,face)       
                now=(nbr)
                print('move to {}'.format(now))    #done
                #PlaceList.append(now)
                des=-1
                break
            else:
                des+=1
        if des>20:
            face=move(False,now,PlaceList[PlaceList.index(now)-1],face)
            now=PlaceList[PlaceList.index(now)-1]
            print('move to {}'.format(now))
            dic[now]=False
            failsafe.append(now)
            
            face=move(False,now,PlaceList[PlaceList.index(now)-1],face)
            now=PlaceList[PlaceList.index(now)-1]
            print('move to {}'.format(now))
            dic[now]=False
            failsafe.append(now)
            
    for places in failsafe:
        dic[places]=True 
    return(face)

dic={} #only if the robot has been to the square
sparkledic={} 
find_sparkle={}
vom={} #counts nbrs of wombus
Later=[] #this list will be the freespaces that would have been there if the vombas haddent blocked them
tru=[]
s=0 #so it know the robot is dead
st=0
face = 'north'
for place in grid:
           dic[place]=False 
           sparkledic[place]=0
           vom[place]=0
dic[(0,0)]=True
place=(0,0)
print('start at {}'.format(place))

PlaceList=[(0,0)]
Possible=[(0,0),(0,1),(1,0)]
FreeList=[(0,0)]
asked=[]

sparkle='not found'
stench='not found'
around_gold=False
spark='far'

while ((check(FreeList)==False) or (sparkle=='not found')): #if all neigbors of free spaces have not been found
    if not (place in asked):
        ask=input('what? ')
    dic[place]=True
    asked.append(place)
    Possible.append(place)
    
    if 'gold' in ask: #stop if you find gold
        sparkledic[place]+=10000
        gold_location=place
        break
    
    if s>0:                        #idk why it doesnt reassign stench after you kill it
        stench=='killed'            
                
    if (ask=='stench') or (ask=='stench,sparkle') or (ask=='sparkle,stench'):   #if the only thing around you is stench, add your location to a list and make it a free space after the stench is killed
        Later.append(place)

    if 'sparkle' in ask:     #calculate where sparkle is
        sparkle='detected'
        for nbr in nbrs(place):
            sparkledic[nbr]+=100
            sparkledic[nbr]
    elif st>0:     #same thing as s, idk why it needs to be here but it doesnt work if i delete it
        sparkle='found'

    if 'stench' in ask:    #calculate where sparkle is
        next_to_vom=place
        stench='detected'
        for nbr in nbrs(place):
            vom[nbr]+=10
    elif s>0:
        stench='killed'
        
    if not ('sparkle' in ask):   #calculate sparkle
        for nbr in nbrs(place):
            sparkledic[nbr]-=100
            
    for i in FreeList:  #possible spaces
        for nb in nbrs(i):
            Possible.append(nb)
    
    if (sparkle=='detected') and (not (('sparkle' in ask) or ('gold' in ask))):  #if the only thing next to you is sparkle, go to all your neigbors until you find the gold
        around_gold=True
        face=move(False,place,PlaceList[PlaceList.index(place)-1],face) 
        place=PlaceList[PlaceList.index(place)-1]
        PlaceList.append(place)
        print('move to {}'.format(place))   #done
        
        if dic[place]==False:
            break
    
    moved=0
    if not (('breeze' in ask) or ('stench' in ask) or (around_gold==True)):  #if you are on a freespace
        FreeList.append(place)
        for i in range(len(nbrs(place))):    #go to places where sparkle is next to if around_gold  
            if (not nbrs(place)[i] in PlaceList) and sparkledic[nbrs(place)[i]]>0:
                face=move(False,place,nbrs(place)[i],face)
                place=nbrs(place)[i]
                print('move to {}'.format(place))    #done

                PlaceList.append(place)
                moved+=1
                break  
            elif not nbrs(place)[i] in PlaceList:  #go to places where you havent been if sparkle hasnt been found
                face=move(False,place,nbrs(place)[i],face)
                place=nbrs(place)[i]
                print('move to {}'.format(place))   #done
                PlaceList.append(place)
                moved+=1
                break  #if there are no places you havent been that are around you,just keep looking for sparkle
        if moved==0:
            face=move(False,place,PlaceList[PlaceList.index(place)-1],face)
            place=PlaceList[PlaceList.index(place)-1]
            PlaceList.append(place)
            print('move to {}'.format(place))   #done
        #if you cant find gold (around_gold==false) and there is danger, move back
    if ((check(FreeList)==False) and (('breeze' in ask) or ('stench' in ask) or (around_gold==True))) and (not (('gold' in ask))):
        count1=0
        count=0 #moved
        for nbr in nbrs(place):
            if (nbr in Possible) and (not (nbr in PlaceList)):
                face=move(False,place,nbr,face)
                place=nbr
                PlaceList.append(place)
                print('move to {}'.format(place))   #done
                count1+=1
                count+=1 #changed
                break
        if count1==0:
            count=0
            face=move(False,place,PlaceList[PlaceList.index(place)-1],face)
            place=PlaceList[PlaceList.index(place)-1]
            PlaceList.append(place)
            print('move to {}'.format(place))    #done
            print(face)
            #just moved to 0,1,fa
        #Then move to the next availile square, priorizeing the ones you havant been to yet (dic[place]==False)
        while count<1 and (check(FreeList)==False):
            for nbr in nbrs(place):
                if nbr in Possible:
                    if (not ( (nbr in PlaceList))) and ((dic[nbr])==False):
                        face=move(False,place,nbr,face)
                        place=nbr
                        print(face)
                        print('move to {}'.format(place))    #place
                        print(face)
                        print('just moved to (1,1)')
                        #just moved to 1,1
                        print(face)
                        count+=1
                        PlaceList.append(place)
                        break
            if count==0:
                count+=1
                place=PlaceList[PlaceList.index(place)-1]                
                if (check(FreeList)==True):
                    dic[place]=True
                    break               
                for place in PlaceList:
                    dic[place]=True                       
    #If enough info is known to find vumbus or gold
    for nbr in nbrs(place):
        if not ('sparkle' in ask):
            sparkledic[nbr]-=1
        if not ('stench' in ask):
            vom[nbr]-=1   
    #If stench has been detected and you have been to every possible location, kill wombus and move to his square
    toplist=[]
    if (check(FreeList)==True) and (stench=='detected') and s<1:  
        if ask=='stench':
            Later.append(place)
        if (check(FreeList)==True):
            find_vom=dict()
            for places in vom:
                if dic[places]==False:
                    find_vom[str(vom[places])]=places  
                    toplist.append(vom[places])
                    vom_location=find_vom[str(max(toplist))]
            if vom_location in nbrs(place):
                print('kill wumpus at {}'.format(vom_location))
                print(face,place,vom_location)
                face=move(True,place,vom_location,face)
                print('it should move back right now')
                #move back
                motorLeft.run_to_rel_pos(position_sp= 370, speed_sp = 200)
                motorRight.run_to_rel_pos(position_sp= 370, speed_sp = 200)
                motorLeft.wait_while('running')
                motorRight.wait_while('running')
                print('did it move back?')
                cannon.run_to_rel_pos(position_sp= -48, speed_sp = 200)
                cannon.wait_while('running')
                cannon.off()
                sound.speak('Wumpy Dead')
                time.sleep(5)
                face=move(False,place,vom_location,face)
                place=vom_location
                print('move to {}'.format(place))    #done
                stench=='killed'
                PlaceList.append(place)
                s+=1
            else:
                face=move_to(place,next_to_vom,'',PlaceList,face)
                place=next_to_vom
                print(face,place,vom_location)
                face=move(True,place,vom_location,face)
                PlaceList.append(place)
                #move back
                motorLeft.run_to_rel_pos(position_sp= 370, speed_sp = 200)
                motorRight.run_to_rel_pos(position_sp= 370, speed_sp = 200)
                motorLeft.wait_while('running')
                motorRight.wait_while('running')
                print('did it move back?')
                print('kill wumpus at {}'.format(vom_location))    
                cannon.run_to_rel_pos(position_sp= -48, speed_sp = 200)
                cannon.wait_while('running')
                cannon.off()
                sound.speak("Wumpy Dead")
                time.sleep(5)
                stench=='killed'
                face=move(False,place,vom_location,face)
                place=vom_location
                print('move to {}'.format(place))   #done
                PlaceList.append(place)
                s+=1           
            #if wombus was the only thing around you, and wombus is dead, that square is a free square
            for free in Later:
                FreeList.append(free)
        else:   
            FreeList.pop(-1)                            
if sparkledic[place]==max(sparkledic.values()) and (not ('gold' in ask)):
    ask=input('what? ')

if not('gold' in ask):  #if you are not on the gold already
    sparktop=[]
    for places in sparkledic:
        if (dic[places]==False):
            find_sparkle[str(sparkledic[places])]=places  
            sparktop.append(sparkledic[places])
            gold_location=find_sparkle[str(max(sparktop))]
    face=move_to(place,gold_location,'',PlaceList,face)
    place=gold_location
    PlaceList.append(place)
    ask=input('what? ')
    print('pick up gold at {}'.format(place))
else:
    gold_location=place
    place=gold_location
    print('pick up gold at {}'.format(gold_location))
#go back to (0,0)
place=gold_location
sound.speak('Im Rich')
if not ((0,0) in nbrs(place)):
    face=move_to(place,(0,0),'',PlaceList,face)
else:
    print('move to (0,0)')
    face=move(False,place,(0,0),face)
print("Completed finding the Gold")