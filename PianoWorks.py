

class PlayPiano():

    def __init__(self):
        
        self.keys = ["c","c#","d","d#","e","f","f#","g","g#","a", "a#","b"]

    def getNoteIndex(self, Note):
        for i in range(len(self.keys)):
            if Note == self.keys[i]:
                return i

    def getAdjustedScale(self, Note):

        for i in range(len(self.keys)):
            if self.keys[i] == Note:
                scale = self.keys[i:len(self.keys)]+self.keys[0:i+1]
                return scale

    """
    THESE ARE ALL SCALES
    """

    def getMajorScale(self, startNote):
        scale = []
        adjustedScale = self.getAdjustedScale(startNote)

        for i in range(len(adjustedScale)):
            if i == 1 or i == 3 or i == 6 or i == 8 or i == 10:
                continue
            scale.append(adjustedScale[i])
        return scale

    def getMinorScale(self,startNote):
        scale = []
        adjustedScale = self.getAdjustedScale(startNote)

        for i in range(len(adjustedScale)):
            if i == 1 or i == 4 or i == 6 or i == 9 or i == 11:
                continue
            scale.append(adjustedScale[i])
        return scale

    def getPentatonicScale(self,startNote):
        scale = []
        adjustedScale = self.getAdjustedScale(startNote)

        for i in range(len(adjustedScale)):
            if i == 0 or i == 2 or i == 4 or i == 7 or i == 11:
                scale.append(adjustedScale[i])
        scale.append(adjustedScale[0])
        return scale

    """
    THESE ARE CHORDS
    """

    def getDomSevenChord(self, Note):
        getScaleM = self.getMajorScale(Note)
        getScaleMI = self.getMinorScale(Note)

        chord = getScaleM[0]+" - "+getScaleM[2]+" - "+getScaleM[4]+" - "+getScaleMI[6]
        
        return chord

    def getMajorChord(self, Note):
        getScale = self.getMajorScale(Note)
        chord = getScale[0]+" - "+getScale[2]+" - "+getScale[4]

        return chord

    def getMinorChord(self, Note):
        getScale = self.getMinorScale(Note)
        chord = getScale[0]+" - "+getScale[2]+" - "+getScale[4]

        return chord

    """
    THESE ARE CHORD PROGRESSIONS
    """

    def ProgOneFourFive7(self, Note):
        Scale = self.getMajorScale(Note)
        firstChord = self.getMajorChord(Scale[0])
        secondChord = self.getMajorChord(Scale[3])
        thirdChord = self.getDomSevenChord(Scale[4])
        return("\n"+firstChord+" |->| "+secondChord+" |->| "+thirdChord+"\n")

    def ProgOneSixFourFive(self, Note):
        Scale = self.getMajorScale(Note)
        firstChord = self.getMajorChord(Scale[0])
        secondChord = self.getMinorChord(Scale[5])
        thirdChord = self.getMajorChord(Scale[3])
        fourthChord = self.getMajorChord(Scale[4])
        return("\n"+firstChord+" |->| "+secondChord+" |->| "+thirdChord+" |->| "+fourthChord+"\n")

    """
    MAIN METHOD
    """
    def main(self):
        piano = PlayPiano()
        print("\nWelcome to Piano Player! You will be able to explore many formulas used to create scales,\nchords, chord progressions and much more. Use spaces to seperate multiple selections!\n")
        input("Press enter to continue\n")
        while True:
            print("What do you want to do(type quit to leave): Scale[1], Chord[2], Chord Progression[3]?")
            getRequest = input()
            if getRequest == "quit":
                break
            print("Pick a key: ", self.keys)
            getKey = input()
           
            if getRequest == "1":
                while True:
                    print("Pick the scale you want(type quit to leave): Major[1], Minor[2], Pentatonic Scale[3], etc..")
                    scalePicked = input()
                    if scalePicked == "quit":
                        break
                    
                    switcher = {
                    "1": ["Major",piano.getMajorScale(getKey)], 
                    "2": ["Minor",piano.getMinorScale(getKey)],
                    "3": ["Penatonic",piano.getPentatonicScale(getKey)]
                    }
                    askAgain = True
                    for i in range(len(switcher)):
                        if scalePicked == str(i+1):
                            askAgain = False
                            break
                    if askAgain:
                        continue

                    print("\nHere is the {} scale of {}: {}\n\n".format(switcher.get(scalePicked)[0],getKey,switcher.get(scalePicked)[1]))
            
            elif getRequest == "2":
                while True:
                    print("Pick the chord you want(type quit to leave): Major[1], Minor[2], Dominant Seventh[3], etc")
                    chordPicked = input()
                    if chordPicked == "quit":
                        break

                    switcher = {
                        "1": ["Major",piano.getMajorChord(getKey)],
                        "2": ["Minor",piano.getMinorChord(getKey)],
                        "3": ["Dominant Seventh",piano.getDomSevenChord(getKey)]
                    }
                    print("\nHere is the {} chord of {}: {}\n\n".format(switcher.get(chordPicked)[0],getKey,switcher.get(chordPicked)[1]))
            
            elif getRequest == "3":
                while True:
                    print('''Pick the chord progression you want(type quit to leave): I-IV-V Seventh[1], I-vi-IV-V[2],
                        ii-V-I[3], I-vi-ii-V[4], I-V-vi-IV[5], I-IV-VI-V[6]
                        '''
                    )
                    progPicked = input()
                    if progPicked == "quit":
                        break

                    switcher = {
                        "1": ["I-IV-V",piano.ProgOneFourFive7(getKey)],
                        "2": ["I-vi-IV-V",piano.ProgOneSixFourFive(getKey)]
                    }
                    print("\nHere is the {} chord progression of {}: \n{}\n".format(switcher.get(progPicked)[0],getKey,switcher.get(progPicked)[1]))

x = PlayPiano()
x.main()