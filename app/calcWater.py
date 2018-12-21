from random import randint
import statistics
from datetime import datetime

tankHeight = 7
tankWidth = 13
tankLength = 19

#Simulates the physical sensor reading
def takeMockWaterHeightReading():
    mockWaterHeight = randint(0,7)
    mockWaterHeight = tankHeight - mockWaterHeight
    return(mockWaterHeight)

def calcCubicVolumeInLitres(l,w,h):
    cubicVolume = l*w*h
    cubicVolumeAsAFloat = float(cubicVolume) #Converts value to a float
    volumeInLitres = cubicVolumeAsAFloat/1000 #Dividing cubic volume by 1000 produces the corresponding volume in litres
    volumeInLitres = ("%.2f" % volumeInLitres) #Represent the volume in litres to two decimal places
    return(volumeInLitres)

def calcRemainingVolume(waterHeight):
    remainingVolumeInLitres = calcCubicVolumeInLitres(tankLength,tankWidth,waterHeight)
    remainingLitres = float(remainingVolumeInLitres)
    return(remainingLitres)

def calcPercentageRemaining(litres):
    percentageRemaining = (litres / tankHeight) * 100
    percentageRemaining = int(percentageRemaining)
    return(percentageRemaining)

def calcWaterData():
    mockWaterHeight = takeMockWaterHeightReading()
    litres = calcRemainingVolume(mockWaterHeight)
    percentage = calcPercentageRemaining(mockWaterHeight)
    waterData = [litres, percentage]
    return(waterData)