#Jackson McElhaugh, The Walt Disney World Simulator, 12/5/22
import random
data = open("magicKingdomData.txt", "r")
text = data.read()
lines = text.split("\n")
#print(lines)
name = []
nineWaitTime = []
tenWaitTime = []
elevenWaitTime = []
twelveWaitTime = []
oneWaitTime = []
twoWaitTime = []
threeWaitTime = []
fourWaitTime = []
fiveWaitTime = []
sixWaitTime = []
sevenWaitTime = []
eightWaitTime = []
# all of the intial lists
startingTime = 540
time = 0
time = time + startingTime
numOfRides = 0
numOfCharacters = 0
numOfFood = 0
numOfShops = 0
for line in lines:
        newList = line.split(",")
        name.append(newList[0])
        nineWaitTime.append(int(newList[1]))
        tenWaitTime.append(int(newList[2]))
        elevenWaitTime.append(int(newList[3]))
        twelveWaitTime.append(int(newList[4]))
        oneWaitTime.append(int(newList[5]))
        twoWaitTime.append(int(newList[6]))
        threeWaitTime.append(int(newList[7]))
        fourWaitTime.append(int(newList[8]))
        fiveWaitTime.append(int(newList[9]))
        sixWaitTime.append(int(newList[10]))
        sevenWaitTime.append(int(newList[11]))
        eightWaitTime.append(int(newList[12]))
        #translating the different wait times and rides into different lists based on the hour

print("Hello and welcome to the Walt Disney World day planner! We will be creating a magical day for you. The park opens at 9 AM and closes at 8 PM today. You will choose the area you would most like to go first, however you may discover something else magical on the way...")
#diningReservation = int(input("If you have a dining reservation, enter '1'. If you do not, enter '0'"))
#if(diningReservation == 1):
       # diningTimeHour = int(input("Please enter the hour of your reservation"))
       # diningTimeMinutes = int(input("Please enter the minutes of your reservation"))
       # diningTime = (diningTimeHour * 60) + diningTimeMinutes

#ridePreference = int(input("Enter the number of what you prefer: Thrill Rides (1) Dark Rides (2) Shows and Experiences (3) Characters (4)"))
counter = 0
landPreference = int(input("Enter the number of the area of the park you would most like to go to first: Adventureland (1) Frontierland (2) Liberty Square (3) Fantasyland (4) Tomorrowland (5): "))
while(counter == 0):
        if(0 < landPreference < 6):
                counter = 1
        else:
                print("Oops! You entered the wrong value. Try again!")
                landPreference = int(input("Enter the number of the area of the park you would most like to go to first: Adventureland (1) Frontierland (2) Liberty Square (3) Fantasyland (4) Tomorrowland (5): "))


print("Your magical day awaits you...")


def attractionGenerator(area):
        leaveLoop = 0
        ride = 0
        while(leaveLoop == 0):
                if(area == 1):
                        #adventureland
                        ride = random.randrange(1,11)
                        #always a 50% chance of staying or leaving the land even in the first ride. this is why it is only a chance you stay there
                        if(1 <= ride <= 6):
                                return ride
                                leaveLoop = 1
                        else:
                                area = random.randrange(1,6)
                if(area == 2):
                        #frontierland
                        ride = random.randrange(1,8)
                        if(1 <= ride <= 4):
                                return (ride + 5)
                                leaveLoop = 1
                        else:
                                area = random.randrange(1,6)
                if(area == 3):
                        #liberty square
                        ride= random.randrange(1,7)
                        if(1 <= ride <= 3):
                                return (ride + 9)
                                leaveLoop = 1
                        else:
                                area = random.randrange(1,6)
                if(area == 4):
                        #fantasyland
                        ride = random.randrange(1,27)
                        if(1 <= ride <= 13):
                                return(ride + 12)
                                leaveLoop = 1
                        else:
                                area = random.randrange(1,6)
                if(area == 5):
                        #tomorrowland
                        
                        ride = random.randrange(1,13)
                        if(1 <= ride <= 6):
                                return(ride + 25)
                                leaveLoop = 1
                        else:
                                area = random.randrange(1,6)
                        
                                
        
def attractionWaitTime(time, whatRUDoing):
        attraction = whatRUDoing
        hour = time // 60
        minutes = time % 60
        #print(hour)
        #print(minutes)
        if(0 <= minutes <= 15):
                #if it is in the beginning of the hour, it will only take the hour time
                if(hour == 9):
                        return nineWaitTime[attraction]
                elif(hour == 10):
                        return tenWaitTime[attraction]
                elif(hour == 11):
                        return elevenWaitTime[attraction]
                elif(hour == 12):
                        return twelveWaitTime[attraction]
                elif(hour == 13):
                        return oneWaitTime[attraction]
                elif(hour == 14):
                        return twoWaitTime[attraction]
                elif(hour == 15):
                        return threeWaitTime[attraction]
                elif(hour == 16):
                        
                        return fourWaitTime[attraction]
                elif(hour == 17):
                        return fiveWaitTime[attraction]
                elif(hour == 18):
                        return sixWaitTime[attraction]
                elif(hour == 19):
                        return sevenWaitTime[attraction]
                elif(hour == 20):
                        return eightWaitTime[attraction]
        elif(15 <= minutes <= 45):
                #if it is in the middle, it will take the average of both the current hour and the next hours wait time
                if(hour == 9):
                        return ((nineWaitTime[attraction] + tenWaitTime[attraction]) / 2)
                elif(hour == 10):
                        return ((tenWaitTime[attraction] + elevenWaitTime[attraction]) / 2)
                elif(hour == 11):
                        return ((elevenWaitTime[attraction] + twelveWaitTime[attraction]) / 2)
                elif(hour == 12):
                        return ((twelveWaitTime[attraction] + oneWaitTime[attraction]) / 2)
                elif(hour == 13):
                        return ((oneWaitTime[attraction] + twoWaitTime[attraction]) / 2)
                elif(hour == 14):
                        return ((twoWaitTime[attraction] + threeWaitTime[attraction]) / 2)
                elif(hour == 15):
                        return ((threeWaitTime[attraction] + fourWaitTime[attraction]) / 2)
                elif(hour == 16):
                        return ((fourWaitTime[attraction] + fiveWaitTime[attraction]) / 2)
                elif(hour == 17):
                        return ((fiveWaitTime[attraction] + sixWaitTime[attraction]) / 2)
                elif(hour == 18):
                        return ((sixWaitTime[attraction] + sevenWaitTime[attraction]) / 2)
                elif(hour == 19):
                        return ((sevenWaitTime[attraction] + eightWaitTime[attraction]) / 2)
                elif(hour == 20):
                        return eightWaitTime[attraction]
        elif(45 <= minutes <= 60):
                #if it is at the end of the hour, it will take the next hour's time
                if(hour == 9):
                        return tenWaitTime[attraction]
                elif(hour == 10):
                        return elevenWaitTime[attraction]
                elif(hour == 11):
                        return twelveWaitTime[attraction]
                elif(hour == 12):
                        return oneWaitTime[attraction]
                elif(hour == 13):
                        return twoWaitTime[attraction]
                elif(hour == 14):
                        return threeWaitTime[attraction]
                elif(hour == 15):
                        return fourWaitTime[attraction]
                elif(hour == 16):
                        return fiveWaitTime[attraction]
                elif(hour == 17):
                        return sixWaitTime[attraction]
                elif(hour == 18):
                        return sevenWaitTime[attraction]
                elif(hour == 19):
                        return eightWaitTime[attraction]
                elif(hour == 20):
                        return eightWaitTime[attraction]
def timePrinter(time):
        #basically a clock based on the time starting at 9 and ending at 8
        hour = time // 60
        newHour = 0
        if(hour > 12):
                newHour = hour - 12
        else:
                newHour = hour
        minutes = time % 60
        #clock = (int(newHour),':0',int(minutes))
        if(minutes < 10):
                print("It is currently ",int(newHour),":0",int(minutes))
        else:
                 print("It is currently ",int(newHour),":",int(minutes))
                
while(time < 1260):
        timePrinter(time)
        activity = random.randrange(1,51)
        if(0 < activity < 31):
                #chance of going on a ride
                currentRide = attractionGenerator(landPreference)
                currentRide = currentRide - 1
                waitTime = attractionWaitTime(time, currentRide)
                #print(name[currentRide],",",waitTime)
                print("You went on ",name[currentRide],". It had a wait time of ",int(waitTime)," minutes.")
                time = time + waitTime
                numOfRides = numOfRides + 1
                #print(time)
        elif(30 < activity < 38):
                #chance of eating food
                timeToEat = random.randrange(1,46)
                if(0 < timeToEat < 16):
                        print("You decided to eat a little snack! Time for a Mickey Pretzel, a Dole Whip, or a Mickey Bar - whatever your heart's desire!")
                        time = time + timeToEat
                elif(15 < timeToEat < 31):
                        print("You decided you wanted to eat a meal. You don't want to eat at a table service resturant, so you sit down for a bite to eat at a quick-service resturant.")
                        time = time + timeToEat
                elif(30 < timeToEat < 45):
                        print("You want a good hearty meal, so you decide to try your luck at a table service resturant. It takes a little longer, but it will be worth your while!")
                        time = time + timeToEat
                numOfFood = numOfFood + 1
        elif(37 < activity < 44):
                #chance of shopping
                timeToShop = random.randrange(1,31)
                print("You decide to go in a gift shop and look around! You could buy some Mickey ears, a new sweatshirt, or even something from the newest Disney film! So much to choose from!")
                numOfShops = numOfShops + 1
        elif(43 < activity < 51):
                #chance of meeting a character
                timeToCharacter = random.randrange(1,21)
                whoYouGot = random.randrange(0,20)
                character = ["Mickey", "Minnie", "Donald", "Goofy", "Daisy", "Pluto", "Chip", "Dale", "Dopey", "Jack Sparrow", "Stitch", "Woody", "Buzz Lightyear", "Sulley", "Mike Wazowski", "Peter Pan", "Tinker Bell",
                             "Mirabel Madrigal", "Snow White", "Ariel"]
                print("You were walking around and ran into ",character[whoYouGot],"! You stopped to get an autograph and take a picture! It took ", timeToCharacter, " minutes!")
                time = time + timeToCharacter
                numOfCharacters = numOfCharacters + 1

        walkingTime = random.randrange(0,11)
        time = time + walkingTime
        print("It takes you ",walkingTime," minutes to get to your next destination! \n")

print("We hope you had a magical day at the Magic Kingdom! See you real soon pal!")
print("You went on ",numOfRides," rides.")
print("You ate food,",numOfFood," times.")
print("You shopped for a souvenir ", numOfShops," times.")
print("You saw a character" ,numOfCharacters," times.")





