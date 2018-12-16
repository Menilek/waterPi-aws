from datetime import datetime
from random import randint
import time
import statistics

#Variables representing dimensions of water container measured in cm
height = 7
width = 13
length = 19

distanceAwayFromSensor = 1 #distance between sensor and the container in cm

#Generates a figure to simulate the result of the physical sensor reading
#The figure represents the distance between the sensor and the water
#Subtracting the distance between the sensor and the maximum
#water height we arrive at the remaining water height
def takeMockReading():
    mockWaterHeight = randint(0,7)
    mockWaterHeight = height - mockWaterHeight
    return(mockWaterHeight)

#The dimensions of the container are taken and used to calculate the cubic volume
#The corresponding volume in litres is derived
#Using the dimensions at the top of the file would give us a result of 1.729
def calculateCubicVolumeInLitres(l,w,h):
    cubicVolume = l*w*h
    cubicVolumeAsAFloat = float(cubicVolume) #Converts value to a float
    volumeInLitres = cubicVolumeAsAFloat/1000 #Dividing cubic volume by 1000 produces the corresponding volume in litres
    volumeInLitres = ("%.2f" % volumeInLitres) #Represent the volume in litres to two decimal places
    return(volumeInLitres)

#Calculates the volume in litres based on the height of the water within the container
def calculateRemainingLitres(waterHeight):
    remainingVolumeInLitres = calculateCubicVolumeInLitres(length,width,waterHeight)
    remainingLitres = float(remainingVolumeInLitres)
    return(remainingLitres)

#This method takes the remaining water height as an argument and calculates the
#percentage of water remaining
def percentageRemaining(litres):
    percentageRemaining = (litres / height) * 100
    percentageRemaining = int(percentageRemaining)
    return(percentageRemaining)

#Using the Python datetime module, get the current time
def getCurrentDateTime():
    now = datetime.now().replace(microsecond = 0)
    now.strftime('%H:%M %d/%m/%Y')
    return(now)

#Method invokes multiple functions inserting the results in a list to be returned
def newEntry():
    mockWaterHeight = takeMockReading()
    litres = calculateRemainingLitres(mockWaterHeight)
    percentage = percentageRemaining(mockWaterHeight)
    newReadingEntry = [litres, percentage]
    return(newReadingEntry)