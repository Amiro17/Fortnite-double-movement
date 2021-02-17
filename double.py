import keyboard
import pyxinput

def move_forward(Amiro):
 
    Amiro.set_value('AxisLy', 1)

def move_backward(Amiro):
    #moves joystick backwards
    Amiro.set_value('AxisLy', -1)

def move_true_left(Amiro):
    Amiro.set_value('AxisLx', -1)

def move_true_right(Amiro):
    Amiro.set_value('AxisLx', 1)

def move_left(Amiro):
    
    Amiro.set_value('AxisLx', -32768)
    Amiro.set_value('AxisLy', -10000) 

def move_right(Amiro):
    Amiro.set_value('AxisLx', 1)
    Amiro.set_value('AxisLy', -10000) 

def move_backLeft(Amiro):

    Amiro.set_value('AxisLx', -32768)
    Amiro.set_value('AxisLy', -1)

def move_backRight(Amiro):

    Amiro.set_value('AxisLx', 1)
    Amiro.set_value('AxisLy', -1)

def resetStick(Amiro):
   
    Amiro.set_value('AxisLx', 0)
    Amiro.set_value('AxisLy', 0)

def reset_stick_x(Amiro):
   
    Amiro.set_value('AxisLx', 0)

def reset_stick_y(Amiro):
    
    Amiro.set_value('AxisLy', 0)

def main():
    Amiro = pyxinput.vController(1)

    while True:

        if keyboard.is_pressed('w+a'):
            move_left(Amiro)
        
        elif keyboard.is_pressed('w+d'):
            move_right(Amiro)
        
        elif keyboard.is_pressed('w'):
            move_forward(Amiro)
            reset_stick_x(Amiro)

        elif keyboard.is_pressed('a'):
            move_true_left(Amiro)
        elif keyboard.is_pressed('d'):
            move_true_right(Amiro)
        elif keyboard.is_pressed('s'):
            move_backward(Amiro)
            reset_stick_x(Amiro)
        
        elif keyboard.is_pressed('s+a'):
            move_backLeft(Amiro)
        
        elif keyboard.is_pressed('s+d'):
            move_backRight(Amiro)
        
        else:
            resetStick(Amiro)

main()