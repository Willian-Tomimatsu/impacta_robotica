#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, UltrasonicSensor)
from pybricks.parameters import Port, Stop
from pybricks.tools import wait

ev3 = EV3Brick()
sensor = UltrasonicSensor(Port.S2)
motor = Motor(Port.B)

while True:
    distancia = sensor.distance()
    
    if 0 <= distancia < 400:
        # Calcula o índice do intervalo (0 a 15 para 0-375)
        index = int(distancia / 10)
        # Velocidade inicial é 50, aumento de 75 por faixa
        velocidade = 50 + index * 50
        motor.run(velocidade)
    else:
        motor.stop(Stop.BRAKE)
        
    wait(100)
