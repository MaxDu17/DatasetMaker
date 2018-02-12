import os
inhaleCounter = 0
exhaleCounter = 0
unknownCounter = 0

def makereadfileName(curr_number,status):
    if status == 0:
        result = "dataSPLIT/inhale/" + str(curr_number)+"_x" + ".wav"
    elif status == 1:
        result = "dataSPLIT/exhale/" + str(curr_number) +"x"+ ".wav"
    else:
        result = "dataSPLIT/unknown/" + str(curr_number)+ "x" + ".wav"
    return result
for i in range(20):
    try:
        os.remove(makereadfileName(inhaleCounter,0))
        inhaleCounter+=1
    except FileNotFoundError:
        print("end of inhales")
    try:
        os.remove(makereadfileName(exhaleCounter, 1))
        exhaleCounter+=1
    except FileNotFoundError:
        print("end of exhales")
    try:
        os.remove(makereadfileName(unknownCounter, 2))
        unknownCounter+=1
    except FileNotFoundError:
        print("end of unknowns")