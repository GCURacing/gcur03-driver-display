import time
import pandas as pd

x = 0

oilTemp = 90
oilPress = 40
fuelTemp = 40
coolantTemp = 75
rpm = 0
speed = 0
tyrePressFL = 50
tyrePressFR = 40
tyrePressRL = 30
tyrePressRR = 20

while x == 0:
    for y in range(0,10):
        rpm += 200
        time.sleep(0.05)

        if (rpm == 11000):
            rpm = 4000

        dataDF = pd.DataFrame({"oilTemp": [oilTemp], 
                           "oilPressure": [oilPress],
                           "coolantTemp": [coolantTemp], 
                           "rpm": [rpm], 
                           "speed": [speed],
                           })
        print(dataDF.head)
        dataDF.to_csv("displayData.csv", index=False)
    oilTemp += 5
    oilPress -= 5
    coolantTemp += 5
    tyrePressFR -= 3
    tyrePressRR -= 3
    tyrePressRL -= 3
    tyrePressFL -= 3
    
    if (oilTemp == 150):
        oilTemp = 90
        
    if (oilPress == 10):
        oilPress = 40
        
    if (fuelTemp == 90):
        fuelTemp = 40
        
    if (coolantTemp == 130):
        coolantTemp = 75
        
    if (tyrePressFL <= 5):
        tyrePressFL = 30
        
    if (tyrePressRL <= 5):
        tyrePressRL = 30
        
    if (tyrePressFR <= 5):
        tyrePressFR = 30
        
    if (tyrePressRR <= 5):
        tyrePressRR = 30