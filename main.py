from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Axis, Port, Color, Direction, Button, Side, Icon, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait

 
motorLeft = Motor(Port.A, Direction.COUNTERCLOCKWISE)
motorRight = Motor(Port.E, Direction.CLOCKWISE)
 
smallMotorRight = Motor(Port.B)
smallMotorLeft = Motor(Port.F)

WHEEL_DIAMETER = 62.5
AXLE_TRACK = 145

# Initialize the hub
hub = PrimeHub(top_side=Axis.Z,front_side=Axis.Y)
hub.light.on(Color.RED)
hub.imu.reset_heading(0)
hub.display.orientation(Side.RIGHT)
hub.system.set_stop_button(Button.BLUETOOTH)

# Initialize DriveBase
db = DriveBase(motorLeft, motorRight, wheel_diameter=WHEEL_DIAMETER, axle_track=AXLE_TRACK) 
db.use_gyro(True)
db.settings(200, 210, 130, 130)


def straight(distance, speed=100, acc=1000,wait=True):
    db.reset() 
    # Max speed: 1000 deg/s
    db.settings(speed * 10, acc, 130, 130)
    db.straight(distance, wait=wait)

def turnBothWheels( angle, speed=80, acc=1000, wait=True):
    # Max speed: 1000 deg/s
    if angle > 0: #Rechtsdrehung
        ...#angle -= x
    elif angle < 0: #Linksdrehung
        ...#angle += x
    db.settings(200, 210, speed *10, acc)
    db.turn(angle, wait=wait)

    remainingAngle = angle % db.angle()
    
    # while not abs(remainingAngle) <= 0.1:
    #     abs(remainingAngle = angle - db.angle() % angle)
    #     print(remainingAngle)
    #     turnOneWheel(angle=remainingAngle, speed=10, acc=100, wait=wait)


def turnOneWheel( angle, speed=20, acc=200, wait=True):
    db.settings(200, 210, speed * 10, acc)
    db.curve(AXLE_TRACK, angle, wait=wait)

def turnArc(*, radius, angle, speed=20, acc=200, wait=True):
    ...

# Round functions
def roundOne(): 
    print("Round 1 executed")
    wait(100)
    straight(685)
    turnBothWheels(44,speed=40)
    wait(200)
    straight(33,speed=40)
    smallMotorLeft.run_angle(1000,320)
    straight(80,acc=200)
    smallMotorRight.run_angle(2000,450,wait=False)
    turnBothWheels(2)
    smallMotorLeft.run_angle(800,-450)
    wait(500)
    smallMotorRight.run_angle(2000,-400)
    smallMotorRight.run_angle(2000,500)
    smallMotorRight.run_angle(2000,-550)
    smallMotorRight.run_angle(2000,500)
    smallMotorRight.run_angle(2000,-550)
    turnBothWheels(-5)
    turnBothWheels(5)
    straight(30)
    motorRight.run_angle(500,-270)
    motorLeft.run_angle(500,-100)
    straight(-65,50,acc=200)
    motorLeft.run_angle(1000,50)
    turnBothWheels(67)
    straight(730)
    db.stop()



def roundTwo(): #15.01.26 check
    print("Round 2 executed")
    straight(20)
    smallMotorLeft.run_angle(2000,-200,wait=False)
    turnBothWheels(-47,acc=100)
    straight(450,speed=40)
    smallMotorLeft.run_angle(2000,200)
    motorLeft.run_angle(1000,80)
    smallMotorRight.run_angle(1000,-400)
    turnBothWheels(-30)
    straight(-650)



    db.stop()


def roundThree(): #15.10.25 check
    print("Round 3 executed")
    straight(20,speed=50)
    turnOneWheel(-90,speed=10)
    straight(505,40)
    turnBothWheels(-80) 
    straight(72)
    motorRight.run_angle(1000,70)
    smallMotorLeft.run_angle(1000,650)
    motorRight.run_angle(1000,-35.7)
    straight(-135.8,speed=10)
    turnBothWheels(-87.5,speed=10)
    straight(-200)
    smallMotorRight.run_angle(1000,-145)
    straight(-160)
    smallMotorRight.run_angle(1000,-30)
    straight(230,speed=30)
    straight(-50)
    smallMotorRight.run_angle(1000,100)
    turnBothWheels(-5)
    straight(-500)
    turnBothWheels(-20)
    straight(-250)
    db.stop()


def roundFour(): #15.10.25 check
    print("Round 4 executed")
    straight(770)
    smallMotorRight.run_angle(1000,-500,wait=False)
    turnOneWheel(90)
    straight(100,acc=200)
    smallMotorLeft.run_angle(1000,110)
    smallMotorRight.run_angle(1000,600)
    smallMotorRight.run_angle(1000,-600)
    straight(-130)
    turnBothWheels(105)
    straight(870)
    wait(200)
    turnBothWheels(-200)
    db.stop()


def roundFive(): #15.10.25 check
    print("Round 5 executed")
    straight(700)
    straight(-40)
    smallMotorRight.run_angle(1000,350)
    straight(50)
    turnBothWheels(-45)
    smallMotorRight.run_angle(1000,-350)
    smallMotorLeft.run_angle(1000,-350,wait=False)
    straight(210,acc=200)
    turnBothWheels(15)
    turnBothWheels(-15)
    smallMotorRight.run_angle(1000,300)
    straight(-100)
    turnBothWheels(42)
    straight(-162)
    smallMotorLeft.run_angle(1000,400)
    smallMotorLeft.run_angle(1000,50,wait=False)
    motorRight.run_angle(1000,-60)
    motorRight.run_angle(1000,60)
    wait(500)
    smallMotorLeft.run_angle(1000,-300)
    straight(-600)
    db.stop()
    
def roundSix():
    print("Round 6 executed")
    smallMotorLeft.run_angle(1000,-150,wait=False)
    turnOneWheel(67)
    straight(650)
    turnOneWheel(-38)
    straight(350)
    turnOneWheel(-29)
    straight(80)
    smallMotorRight.run_angle(1000,200)
    straight(-150)
    turnBothWheels(40)
    straight(-480)
    turnBothWheels(-80,acc=200)
    smallMotorLeft.run_angle(1000,170)
    straight(65)
    smallMotorLeft.run_angle(1000,-100)
    turnBothWheels(40)
    turnBothWheels(-20)
    straight(-150)
    turnBothWheels(90,acc=200)
    smallMotorLeft.run_angle(1000,-150,wait=False)
    straight(-680)
    db.stop()
    

def roundSeven():
    print("Round 7 executed")
    straight(280,speed=40)
    motorLeft.run_angle(250,270)
    wait(500)
    straight(230,speed=20)
    motorRight.run_angle(100,-50)
    straight(-300,speed=20)
    turnBothWheels(-45)
    straight(-280)
    db.stop()




# Number matrices
NUMBER_MATRICES = {
    1: [
        [0, 100, 0, 0, 0],
        [100, 100, 0, 0, 0],
        [0, 100, 0, 0, 0],
        [0, 100, 0, 0, 0],
        [100, 100, 100, 0, 0],
    ],
    2: [
        [100, 100, 100, 0, 0],
        [0, 0, 100, 0, 0],
        [100, 100, 100, 0, 0],
        [100, 0, 0, 0, 0],
        [100, 100, 100, 0, 0],
    ],
    3: [
        [100, 100, 100, 0, 0],
        [0, 0, 100, 0, 0],
        [100, 100, 100, 0, 0],
        [0, 0, 100, 0, 0],
        [100, 100, 100, 0, 0],
    ],
    4: [
        [100, 0, 100, 0, 0],
        [100, 0, 100, 0, 0],
        [100, 100, 100, 0, 0],
        [0, 0, 100, 0, 0],
        [0, 0, 100, 0, 0],
    ],
    5: [
        [100, 100, 100, 0, 0],
        [100, 0, 0, 0, 0],
        [100, 100, 100, 0, 0],
        [0, 0, 100, 0, 0],
        [100, 100, 100, 0, 0],
    ],
    6: [
        [100, 100, 100, 0, 0],
        [100, 0, 0, 0, 0],
        [100, 100, 100, 0, 0],
        [100, 0, 100, 0, 0],
        [100, 100, 100, 0, 0],
    ],
    7: [
        [100, 100, 100, 0, 0],
        [0, 0, 100, 0, 0],
        [0, 100, 0, 0, 0],
        [0, 100, 0, 0, 0],
        [0, 100, 0, 0, 0],
    ],
    8: [
        [100, 100, 100, 0, 0],
        [100, 0, 100, 0, 0],
        [100, 100, 100, 0, 0],
        [100, 0, 100, 0, 0],
        [100, 100, 100, 0, 0],
    ],
}

class UI:
    def __init__(self):
        self.currentRound = 1 
        self.ROUND_CYCLE = {
            1: roundOne,
            2: roundTwo,
            3: roundThree,
            4: roundFour,
            5: roundFive,
            6: roundSix,
            7: roundSeven,

        }


    def start(self):
        """ Starts the user interface."""
        self.status()
        self.updateNumber(NUMBER_MATRICES[self.currentRound])

        while True:
            self.updateBattery()
            pressedButtons = hub.buttons.pressed()

            if Button.CENTER in pressedButtons:
                self.execute()

            if Button.RIGHT in pressedButtons:
                self.cycle(Direction.CLOCKWISE)

            if Button.LEFT in pressedButtons:
                self.cycle(Direction.COUNTERCLOCKWISE)

            wait(50)  # Reduce CPU usage


    def cycle(self, direction):
        """Cycles up or down."""
        if direction == Direction.CLOCKWISE:
            self.currentRound = self.currentRound % len(self.ROUND_CYCLE) + 1
        else:
            self.currentRound = len(self.ROUND_CYCLE) if self.currentRound == 1 else self.currentRound - 1

        self.updateNumber(NUMBER_MATRICES[self.currentRound])
        hub.speaker.beep(100, 50)
        wait(100)


    def execute(self):
        """Executes the current round."""
        hub.display.icon(Icon.ARROW_UP)  
        self.ROUND_CYCLE[self.currentRound]()  
        wait(200)

        self.cycle(Direction.CLOCKWISE) # Go to the next round


    def status(self):
        """ Print general information about the robot."""
        print("Battery: ", hub.battery.voltage(), " mV")
        print("Calibrated: ", hub.imu.ready())


    def updateBattery(self):
        """ Displays the battery level on the hub."""
        voltage = hub.battery.voltage()
        MAX_VOLTAGE = 8400
        for i in range(5): 
            if voltage >= MAX_VOLTAGE - (i + 1) * 100: # Each level equals 100 mV
                hub.display.pixel(i, 4, 40)


    def updateNumber(self, matrix):
        """ Updates only the left four columns"""
        for i in range(0, 5):
            for j in range(0, 4):
                hub.display.pixel(i, j, matrix[i][j])

ui = UI()
ui.start()
