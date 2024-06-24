import cv2
import PIL.ImageGrab
import numpy as np
import time

def inGame():
    start_time = time.time()
        
    scnsht = PIL.ImageGrab.grab(bbox=(160, 820, 175, 835))
    comp = cv2.matchTemplate(np.array(scnsht), templateBigGen, cv2.TM_CCOEFF_NORMED)[0][0]
    
    if sampleRate - (time.time() - start_time) > 0:
        time.sleep(sampleRate - (time.time() - start_time))
        
    return comp > threshHold
    
def printResults():
    for v in _list:
        if sum(_list) > 0:
            print(format(v/sum(_list), '.2f'), f"%, total time: {v*sampleRate}")
        
def genTrack():
    scnsht = PIL.ImageGrab.grab(bbox=(195, 460, 210, 740))

    s = ""
    for i, v in enumerate(pos):
        im = np.array(scnsht)[v[0]:v[1], v[2]:v[3]]
        _if = cv2.matchTemplate(im, template, cv2.TM_CCOEFF_NORMED)[0][0] > threshHold
        s += "Player " + str(i) + ": " + str(_if) + ", "
        if _if:
            _list[i] +=1
    
    return s[:-2]

def inGameMultipleFail():
    for i in range(10):
        if inGame():
            return True        
                
    return False

template = cv2.imread("assets/generator.png")
templateBigGen = cv2.imread("assets/generator_big.png")

threshHold = 0.5
pos = [[0, 15, 0, 15], [88, 103, 0, 15], [176, 191, 0, 15], [265, 280, 0, 15]]
sampleRate = 0.5

while True:
    _list = [0, 0, 0, 0]
    print("Searching for game...")
    while not inGame(): 
        pass
    print("Game found...")
    while inGameMultipleFail():
        print(genTrack(), end='\r') 
    print("\nGame finished")
    printResults()