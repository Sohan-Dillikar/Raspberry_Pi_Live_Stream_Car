import RPi.GPIO as GPIO

class Car:
    def __init__(self, rightWheelPins, leftWheelPins):
        self.rightWheelPins = rightWheelPins
        self.leftWheelPins = leftWheelPins

    def setup(self):
        for pin_set in self.rightWheelPins + self.leftWheelPins:
            GPIO.setup(pin_set[0], GPIO.OUT, initial=GPIO.LOW)
            GPIO.setup(pin_set[1], GPIO.OUT, initial=GPIO.LOW)
            GPIO.setup(pin_set[2], GPIO.OUT, initial=GPIO.LOW)

    def forward(self):
        for right_set in self.rightWheelPins:
            GPIO.output(right_set[0], GPIO.HIGH)
            GPIO.output(right_set[1], GPIO.LOW)
            GPIO.output(right_set[2], GPIO.HIGH)
        for left_set in self.leftWheelPins:
            GPIO.output(left_set[0], GPIO.HIGH)
            GPIO.output(left_set[1], GPIO.HIGH)
            GPIO.output(left_set[2], GPIO.LOW)

    def backward(self):
        for right_set in self.rightWheelPins:
            GPIO.output(right_set[0], GPIO.HIGH)
            GPIO.output(right_set[1], GPIO.HIGH)
            GPIO.output(right_set[2], GPIO.LOW)
        for left_set in self.leftWheelPins:
            GPIO.output(left_set[0], GPIO.HIGH)
            GPIO.output(left_set[1], GPIO.LOW)
            GPIO.output(left_set[2], GPIO.HIGH)

    def right(self):
        for pin_set in self.rightWheelPins + self.leftWheelPins:
            GPIO.output(pin_set[0], GPIO.HIGH)
            GPIO.output(pin_set[1], GPIO.HIGH)
            GPIO.output(pin_set[2], GPIO.LOW)

    def left(self):
        for pin_set in self.rightWheelPins + self.leftWheelPins:
            GPIO.output(pin_set[0], GPIO.HIGH)
            GPIO.output(pin_set[1], GPIO.LOW)
            GPIO.output(pin_set[2], GPIO.HIGH)

    def stop(self):
        for pin_set in self.rightWheelPins + self.leftWheelPins:
            GPIO.output(pin_set[0], GPIO.LOW)
