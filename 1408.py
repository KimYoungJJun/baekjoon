currentTime = input()
missionStartTime = input()

currentTime = currentTime.split(":")
missionStartTime = missionStartTime.split(":")

currentHour = int(currentTime[0])
currentMinute = int(currentTime[1])
currentSecond = int(currentTime[2])

missionStartHour = int(missionStartTime[0])
missionStartMinute = int(missionStartTime[1])
missionStartSecond = int(missionStartTime[2])


answerHour = missionStartHour-currentHour
answerMinute = missionStartMinute-currentMinute
answerSecond = missionStartSecond-currentSecond

if(answerSecond < 0):
    answerMinute-=1
    answerSecond += 60
if(answerMinute < 0):
    answerHour-=1
    answerMinute += 60
if(answerHour < 0):
    answerHour += 24
    
if(answerHour < 10):
    answerHour = '0'+str(answerHour)
if(answerMinute < 10):
    answerMinute = '0'+str(answerMinute)
if(answerSecond < 10):
    answerSecond = '0'+str(answerSecond)
print(f"{answerHour}:{answerMinute}:{answerSecond}")