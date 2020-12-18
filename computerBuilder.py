"""
Name: Henri Goosen
Date: November 30th, 2020
Purpose: Make a python application that presents the user with different parts
for a computer and they can select the ones they want to build their own PC.
"""

from tkinter import *

partList = [["MasterBox Q300L", 49.99, "MasterBox Q300L.gif", 0, "partDesc", "Computer Case","TL", "MasterBox Q300L D.gif", "MasterBox Q300L G.gif",2,360,159],
            ["Cooler Master Cosmos C700P", 349.99, "Cooler Master Cosmos C700P.gif", 0, "partDesc", "Computer Case","TR", "Cooler Master C700P D.gif", "Cooler Master C700P G.gif",4,490,198],
            ["Corsair 110Q", 67.99, "Corsair 110Q.gif", 0, "partDesc", "Computer Case","BL", "Corsair 110Q D.gif", "Corsair 110Q G.gif", 3,330,160],
            ["Corsair CARBIDE 275R", 89.99, "Corsair CARBIDE 275R.gif", 0, "partDesc", "Computer Case","BR", "Corsair CARBIDE 275R D.gif", "Corsair CARBIDE 275R G.gif",3,370,170]
    ]

selectedPartList = [
    ]

print("List of parts loaded.")
print(".")
print(".")
print(".")
clickCounter = 0
print("Click counter has been reset.")
print(".")
print(".")
print(".")
currentType = ""
print("Current type has been reset.")
print(".")
print(".")
print(".")
partNameTL = ""
print("Part name TL has been reset.")
print(".")
print(".")
print(".")
partNameTR = ""
print("Part name TR has been reset.")
print(".")
print(".")
print(".")
partNameBL = ""
print("Part name BL has been reset.")
print(".")
print(".")
print(".")
partNameBR = ""
print("Part name BR has been reset.")
print(".")
print(".")
print(".")
partImage1 = ""
print("Image 1 has been reset.")
print(".")
print(".")
print(".")
partImage1D = ""
print("Image 1D has been reset.")
print(".")
print(".")
print(".")
partImage1G = ""
print("Image 1G has been reset.")
print(".")
print(".")
print(".")
partImage2 = ""
print("Image 2 has been reset.")
print(".")
print(".")
print(".")
partImage2D = ""
print("Image 2D has been reset.")
print(".")
print(".")
print(".")
partImage2G = ""
print("Image 2G has been reset.")
print(".")
print(".")
print(".")
partImage3 = ""
print("Image 3 has been reset.")
print(".")
print(".")
print(".")
partImage3D = ""
print("Image 3D has been reset.")
print(".")
print(".")
print(".")
partImage3G = ""
print("Image 3G has been reset.")
print(".")
print(".")
print(".")
partImage4 = ""
print("Image 4 has been reset.")
print(".")
print(".")
print(".")
partImage4D = ""
print("Image 4D has been reset.")
print(".")
print(".")
print(".")
partImage4G = ""
print("Image 4G has been reset.")
print(".")
print(".")
print(".")
currentImageTL = str(partImage1)
print("Current image TL has been reset.")
print(".")
print(".")
print(".")
currentImageTR = str(partImage2)
print("Current image TR has been reset.")
print(".")
print(".")
print(".")
currentImageBL = str(partImage3)
print("Current image BL has been reset.")
print(".")
print(".")
print(".")
currentImageBR = str(partImage4)
print("Current image BR has been reset.")
print(".")
print(".")
print(".")
totalPriceCounter = 0
print("Total price counter has been reset.")
print(".")
print(".")
print(".")
totalWattCounter = 0
print("Total watt counter has been reset.")
print(".")
print(".")
print(".")


  
class StartScreen():

    def __init__(self):
        self.window = Tk()

        self.topFrame = Frame(self.window, width=640, height=480)
        self.bottomFrame = Frame(self.window, width=640, height=480)

        self.window.title("PC builder")
        self.window.geometry("1240x1770")

        self.topFrame.pack(side=TOP)
        self.bottomFrame.pack(side=BOTTOM)

        self.createStartButton()
        self.createMainImage()
        
    def createStartButton(self):
         try:
            startImage = PhotoImage(file="start.gif")
            self.startImage = startImage
            startButton = Button(self.bottomFrame,
                                text="Start",
                                width = 500, height = 100,
                                command = lambda: self.startButtonClick(),
                                image=startImage)
            startButton.pack(side=BOTTOM)
         except Exception as exception:
            print("Problem loading start button")
            print(".")
            print("Error: %s" %(exception))
            print(".")
            print(".")
            print(".")

    def createMainImage(self):
        try:
            mainImage = PhotoImage(file="main.gif")
            
            self.mainPhoto =\
            Label(self.topFrame,
                  anchor="center",
                  image=mainImage,
                  width=480, height=480)
            self.mainPhoto.image = mainImage

        except Exception as exception:
            print("Problem loading main image")
            print(".")
            print("Error: %s" %(exception))
            print(".")
            print(".")
            print(".")
            
        self.mainPhoto.pack()

    def startButtonClick(self):
        currentType = "Computer Case"
        for part in partList:
            if part[5] == str(currentType) and part[6] == "TL":
                
                partNameTL = ("%s"%(part[0]))
                print("Part name TL has been set to %s." %(partNameTL))
                print(".")
                print(".")
                print(".")
                partImage1 = ("%s"%(part[2]))
                print("Image 1 has been set to %s." %(partImage1))
                print(".")
                print(".")
                print(".")
                partImage1D = "%s"%(part[7])
                print("Image 1D has been set to %s." %(partImage1D))
                print(".")
                print(".")
                print(".")
                partImage1G = ("%s"%(part[8]))
                print("Image 1G has been set to %s." %(partImage1G))
                print(".")
                print(".")
                print(".")
                
            elif part[5] == str(currentType) and part[6] == "TR":
                
                partNameTR = ("%s"%(part[0]))
                print("Part name TR has been set to %s." %(partNameTR))
                print(".")
                print(".")
                print(".")
                partImage2 = ("%s"%(part[2]))
                print("Image 2 has been set to %s." %(partImage2))
                print(".")
                print(".")
                print(".")
                partImage2D = "%s"%(part[7])
                print("Image 2D has been set to %s." %(partImage2D))
                print(".")
                print(".")
                print(".")
                partImage2G = ("%s"%(part[8]))
                print("Image 2G has been set to %s." %(partImage2G))
                print(".")
                print(".")
                print(".")
                
            elif part[5] == str(currentType) and part[6] == "BL":
                
                partNameBL = ("%s"%(part[0]))
                print("Part name BL has been set to %s." %(partNameBL))
                print(".")
                print(".")
                print(".")
                partImage3 = ("%s"%(part[2]))
                print("Image 3 has been set to %s." %(partImage3))
                print(".")
                print(".")
                print(".")
                partImage3D = "%s"%(part[7])
                print("Image 3D has been set to %s." %(partImage3D))
                print(".")
                print(".")
                print(".")
                partImage3G = ("%s"%(part[8]))
                print("Image 3G has been set to %s." %(partImage3G))
                print(".")
                print(".")
                print(".")

            elif part[5] == str(currentType) and part[6] == "BR":
                
                partNameBR = ("%s"%(part[0]))
                print("Part name BR has been set to %s." %(partNameBR))
                print(".")
                print(".")
                print(".")
                partImage4 = ("%s"%(part[2]))
                print("Image 4 has been set to %s." %(partImage4))
                print(".")
                print(".")
                print(".")
                partImage4D = "%s"%(part[7])
                print("Image 4D has been set to %s." %(partImage4D))
                print(".")
                print(".")
                print(".")
                partImage4G = ("%s"%(part[8]))
                print("Image 4G has been set to %s." %(partImage4G))
                print(".")
                print(".")
                print(".")
        ComputerBuilder()


class ComputerBuilder():
    def __init__(self):

        self.mainwindow = Toplevel()

        self.topFrameTwo = Frame(self.mainwindow, width=100, height=100)
        self.topFrame = Frame(self.mainwindow, width=640, height=480)
        self.bottomFrame = Frame(self.mainwindow,width=640, height=480)
        self.bottomFrameTwo = Frame(self.mainwindow, width=100, height=100)
        self.topFrameL = Frame(self.topFrame, width=320, height=480)
        self.topFrameR = Frame(self.topFrame, width=320, height=480)
        self.bottomFrameL = Frame(self.bottomFrame, width=320, height=480)
        self.bottomFrameR = Frame(self.bottomFrame, width=320, height=480)

        self.mainwindow.title("PC Builder")
        self.mainwindow.geometry("1380x1060")

        self.topFrameTwo.pack(side=TOP)
        self.topFrame.pack(side=TOP)
        self.bottomFrame.pack(side=BOTTOM)
        self.bottomFrameTwo.pack(side=BOTTOM)
        self.topFrameL.pack(side=LEFT)
        self.topFrameR.pack(side=RIGHT)
        self.bottomFrameL.pack(side=LEFT)
        self.bottomFrameR.pack(side=RIGHT)
    
        self.loadWidgets()

        self.compatabilityChecker()

        self.mainwindow.mainloop()

    def loadWidgets(self):
        
        self.createExitButton()
        self.createLeftArrow()
        self.createRightArrow()
        self.createPartImageOne()
        self.createPartImageTwo()
        self.createPartImageThree()
        self.createPartImageFour()
        self.createInfoButtonTL()
        self.createInfoButtonTR()
        self.createInfoButtonBL()
        self.createInfoButtonBR()
        self.createSelectPartTL()
        self.createSelectPartTR()
        self.createSelectPartBL()
        self.createSelectPartBR()
        self.createLabelTL()
        self.createLabelTR()
        self.createLabelBL()
        self.createLabelBR()
        self.createTotalWattLabel()
        self.createTotalPriceLabel()

        
    def createExitButton(self):
        try:
            exitImage = PhotoImage(file="exit.gif")
            self.exitImage = exitImage
            exitButton = Button(self.bottomFrameTwo,
                                text="Exit",
                                width = 96, height = 94,
                                command = lambda: self.exitButtonClick(),
                                image=exitImage)
            exitButton.pack(side=LEFT)
            
        except Exception as exception:
            print("Problem loading exit button")
            print(".")
            print("Error: %s" %(exception))
            print(".")
            print(".")
            print(".")

    def createLeftArrow(self):
        try:
            leftArrowImage = PhotoImage(file="leftarrow.gif")
            self.leftArrowImage = leftArrowImage
            leftArrowButton = Button(self.bottomFrameTwo,
                                text="Left Arrow",
                                width = 98, height = 100,
                                command = lambda: self.leftArrowClick(),
                                image=leftArrowImage)
            leftArrowButton.pack(side=LEFT)
        except Exception as exception:
            print("Problem loading left arrow button")
            print(".")
            print("Error: %s" %(exception))
            print(".")
            print(".")
            print(".")
        
    def createRightArrow(self):
        try:
            rightArrowImage = PhotoImage(file="rightarrow.gif")
            self.rightArrowImage = rightArrowImage
            rightArrowButton = Button(self.bottomFrameTwo,
                                text="Right Arrow",
                                width = 98, height = 100,
                                command= lambda: self.rightArrowClick(),
                                image= rightArrowImage)
            rightArrowButton.pack(side=RIGHT)
        except Exception as exception:
            print("Problem loading right arrow button")
            print(".")
            print("Error: %s" %(exception))
            print(".")
            print(".")
            print(".")

    def createPartImageOne(self):
            try:
                partImageOne = PhotoImage(file="%s"%(currentImageTL))
            
                self.partPhotoOne =\
                Label(self.topFrameL,
                      anchor="center",
                      image=partImageOne,
                      width=380, height=380)
                self.partPhotoOne.image = partImageOne
                self.partPhotoOne.pack()
            except Exception as exception:
                print("Problem loading part image one")
                print(".")
                print("Error: %s" %(exception))
                print(".")
                print(".")
                print(".")    

    def createPartImageTwo(self):
            try:
                partImageTwo = PhotoImage(file="%s" %(currentImageTR))
            
                self.partPhotoTwo =\
                Label(self.topFrameR,
                      anchor="center",
                      image=partImageTwo,
                      width=380, height=380)
                self.partPhotoTwo.image = partImageTwo
                self.partPhotoTwo.pack()
            except Exception as exception:
                print("Problem loading part image two")
                print(".")
                print("Error: %s" %(exception))
                print(".")
                print(".")
                print(".")
            
        

    def createPartImageThree(self):
            try:
                partImageThree = PhotoImage(file="%s" %(currentImageBL))
            
                self.partPhotoThree =\
                Label(self.bottomFrameL,
                      anchor="center",
                      image=partImageThree,
                      width=380, height=380)
                self.partPhotoThree.image = partImageThree
                self.partPhotoThree.pack()

            except Exception as exception:
                print("Problem loading part image three")
                print(".")
                print("Error: %s" %(exception))
                print(".")
                print(".")
                print(".")
            
        
            



    def createPartImageFour(self):
            try:
                partImageFour = PhotoImage(file="%s" %(currentImageBR))
            
                self.partPhotoFour =\
                Label(self.bottomFrameR,
                      anchor="center",
                      image=partImageFour,
                      width=380, height=380)
                self.partPhotoFour.image = partImageFour
                self.partPhotoFour.pack(side=TOP)
            except Exception as exception:
                print("Problem loading part image four")
                print(".")
                print("Error: %s" %(exception))
                print(".")
                print(".")
                print(".")
            
        
            
    def createInfoButtonTL(self):
        try:
            infoImageTL = PhotoImage(file="info.gif")
            self.infoImageTL = infoImageTL
            infoButtonTL = Button(self.topFrameL,
                                text="Info",
                                width = 49, height = 49,
                                command = lambda: self.infoButtonTLClick(),
                                image=infoImageTL)
            infoButtonTL.pack(side=BOTTOM)
        except Exception as exception:
            print("Problem loading info button TL")
            print(".")
            print("Error: %s" %(exception))
            print(".")
            print(".")
            print(".")
    
    def createInfoButtonTR(self):
        try:
            infoImageTR = PhotoImage(file="info.gif")
            self.infoImageTR = infoImageTR
            infoButtonTR = Button(self.topFrameR,
                                text="Info",
                                width = 49, height = 49,
                                command = lambda: self.infoButtonTRClick(),
                                image=infoImageTR)
            infoButtonTR.pack(side=BOTTOM)

        except Exception as exception:
            print("Problem loading info button TR")
            print(".")
            print("Error: %s" %(exception))
            print(".")
            print(".")
            print(".")

    def createInfoButtonBL(self):
        try:
            infoImageBL = PhotoImage(file="info.gif")
            self.infoImageBL = infoImageBL
            infoButtonBL = Button(self.bottomFrameL,
                                text="Info",
                                width = 49, height = 49,
                                command = lambda: self.infoButtonBLClick(),
                                image=infoImageBL)
            infoButtonBL.pack(side=BOTTOM)
        except Exception as exception:
            print("Problem loading info button BL")
            print(".")
            print("Error: %s" %(exception))
            print(".")
            print(".")
            print(".")

    def createInfoButtonBR(self):
        try:
            infoImageBR = PhotoImage(file="info.gif")
            self.infoImageBR = infoImageBR
            infoButtonBR = Button(self.bottomFrameR,
                                text="Info",
                                width = 49, height = 49,
                                command = lambda: self.infoButtonBRClick(),
                                image=infoImageBR)
            infoButtonBR.pack(side=BOTTOM)
        except Exception as exception:
            print("Problem loading info button BR")
            print(".")
            print("Error: %s" %(exception))
            print(".")
            print(".")
            print(".")

    def createSelectPartTL(self):
        try:
            selectImageTL = PhotoImage(file="select.gif")
            self.selectImageTL = selectImageTL
            selectButtonTL = Button(self.topFrameL,
                                text="Select",
                                width = 48, height = 48,
                                command = lambda: self.selectButtonClickTL(),
                                image=selectImageTL)
            selectButtonTL.pack(side=BOTTOM)
        except Exception as exception:
            print("Problem loading select button TL")
            print(".")
            print("Error: %s" %(exception))
            print(".")
            print(".")
            print(".")
    
    def createSelectPartTR(self):
        try:
            selectImageTR = PhotoImage(file="select.gif")
            self.selectImageTR = selectImageTR
            selectButtonTR = Button(self.topFrameR,
                                text="Select",
                                width = 48, height = 48,
                                command = lambda: self.selectButtonClickTR(),
                                image=selectImageTR)
            selectButtonTR.pack(side=BOTTOM)
        except Exception as exception:
            print("Problem loading select button TR")
            print(".")
            print("Error: %s" %(exception))
            print(".")
            print(".")
            print(".")

    def createSelectPartBL(self):
        try:
            selectImageBL = PhotoImage(file="select.gif")
            self.selectImageBL = selectImageBL
            selectButtonBL = Button(self.bottomFrameL,
                                text="Select",
                                width = 48, height = 48,
                                command = lambda: self.selectButtonClickBL(),
                                image=selectImageBL)
            selectButtonBL.pack(side=BOTTOM)
        except Exception as exception:
            print("Problem loading select button BL")
            print(".")
            print("Error: %s" %(exception))
            print(".")
            print(".")
            print(".")

    def createSelectPartBR(self):
        try:
            selectImageBR = PhotoImage(file="select.gif")
            self.selectImageBR = selectImageBR
            selectButtonBR = Button(self.bottomFrameR,
                                text="Select",
                                width = 48, height = 48,
                                command = lambda: self.selectButtonClickBR(),
                                image=selectImageBR)
            selectButtonBR.pack(side=BOTTOM)
        except Exception as exception:
            print("Problem loading select button BR")
            print(".")
            print("Error: %s" %(exception))
            print(".")
            print(".")
            print(".")

    def createLabelTL(self):

        self.labelTL = StringVar()
        self.labelTL.set("%s"%(partNameTL))
        self.labelTopLeft = Label(self.topFrameL,
                             textvariable=self.labelTL,
                             font=("Helvetica", 18),
                             wraplength=400)
        self.labelTopLeft.pack(side=BOTTOM, anchor=W)
        
    
    def createLabelTR(self):
        
        self.labelTR = StringVar()
        self.labelTL.set("%s"%(partNameTR))
        self.labelTopRight = Label(self.topFrameR,
                             textvariable=self.labelTR,
                             font=("Helvetica", 18),
                             wraplength=400)
        self.labelTopRight.pack(side=BOTTOM, anchor=W)
        
    def createLabelBL(self):

        self.labelBL = StringVar()
        self.labelBL.set("%s"%(partNameBL))
        self.labelBottomLeft = Label(self.bottomFrameL,
                             textvariable=self.labelBL,
                             font=("Helvetica", 18),
                             wraplength=400)
        self.labelBottomLeft.pack(side=BOTTOM, anchor=W)
        
    def createLabelBR(self):

        self.labelBR = StringVar()
        self.labelBR.set("%s"%(partNameBR))
        self.labelBottomRight = Label(self.bottomFrameR,
                             textvariable=self.labelBR,
                             font=("Helvetica", 18),
                             wraplength=400)
        self.labelBottomRight.pack(side=BOTTOM, anchor=W)
    
    def createTotalWattLabel(self):

        global totalWattCounter

        for part in selectedPartList:
            totalWattCounter += part[3]

        self.labelWatt = StringVar()
        self.labelWatt.set(" Total Watts: %s "%(str(totalWattCounter)))
        self.labelTotalWatt = Label(self.topFrameTwo,
                             textvariable=self.labelWatt,
                             font=("Helvetica", 18),
                             wraplength=400)
        self.labelTotalWatt.pack(side=LEFT, anchor=W)
        
    def createTotalPriceLabel(self):

        global totalPriceCounter
        
        for part in selectedPartList:
            totalPriceCounter += part[1]

        self.labelPrice = StringVar()
        self.labelPrice.set(" Total Price: %s "%(str(totalPriceCounter)))
        self.labelTotalPrice = Label(self.topFrameTwo,
                             textvariable=self.labelPrice,
                             font=("Helvetica", 18),
                             wraplength=400)
        self.labelTotalPrice.pack(side=RIGHT, anchor=W)

    def exitButtonClick(self):

        self.window.destroy()

    def leftArrowClick(self):

        compatabilityChecker()

        loadWidgets()
        
        partChangerLeft()
    
    def rightArrowClick(self):

        compatabilityChecker()

        loadWidgets()
        
        partChangerRight()

    def partChangerRight(self):

        compatabilityChecker()
        
        if (clickCounter < 7):
            clickCounter += 1
        else:
            print("You have reached the end!")
            
        if (clickCounter <= 7):
            if clickCounter == 0:
                currentType = "Computer Case"
                print("Current type set to: %s"%(currentType))
                print(".")
                print(".")
                print(".")
            elif clickCounter == 1:
                currentType = "Motherboard"
                print("Current type set to: %s"%(currentType))
                print(".")
                print(".")
                print(".")
            elif clickCounter == 2:
                currentType = "Processor"
                print("Current type set to: %s"%(currentType))
                print(".")
                print(".")
                print(".")
            elif clickCounter == 3:
                currentType = "Graphics Card"
                print("Current type set to: %s"%(currentType))
                print(".")
                print(".")
                print(".")
            elif clickCounter == 4:
                currentType = "CPU Cooler"
                print("Current type set to: %s"%(currentType))
                print(".")
                print(".")
                print(".")
            elif clickCounter == 5:
                currentType = "RAM"
                print("Current type set to: %s"%(currentType))
                print(".")
                print(".")
                print(".")
            elif clickCounter == 6:
                currentType = "Storage"
                print("Current type set to: %s"%(currentType))
                print(".")
                print(".")
                print(".")
            elif clickCounter == 7:
                currentType = "Power Supply"
                print("Current type set to: %s"%(currentType))
                print(".")
                print(".")
                print(".")
            else:
                print("Error: No Current Type")
                
        for part in partList:
            if part[5] == str(currentType) and part[6] == "TL":
                
                partNameTL = ("%s"%(part[0]))
                print("Part name TL has been set to %s." %(partNameTL))
                print(".")
                print(".")
                print(".")
                partImage1 = ("%s"%(part[2]))
                print("Image 1 has been set to %s." %(partImage1))
                print(".")
                print(".")
                print(".")
                partImage1D = "%s"%(part[7])
                print("Image 1D has been set to %s." %(partImage1D))
                print(".")
                print(".")
                print(".")
                partImage1G = ("%s"%(part[8]))
                print("Image 1G has been set to %s." %(partImage1G))
                print(".")
                print(".")
                print(".")
                
            elif part[5] == str(currentType) and part[6] == "TR":
                
                partNameTR = ("%s"%(part[0]))
                print("Part name TR has been set to %s." %(partNameTR))
                print(".")
                print(".")
                print(".")
                partImage2 = ("%s"%(part[2]))
                print("Image 2 has been set to %s." %(partImage2))
                print(".")
                print(".")
                print(".")
                partImage2D = "%s"%(part[7])
                print("Image 2D has been set to %s." %(partImage2D))
                print(".")
                print(".")
                print(".")
                partImage2G = ("%s"%(part[8]))
                print("Image 2G has been set to %s." %(partImage2G))
                print(".")
                print(".")
                print(".")
                
            elif part[5] == str(currentType) and part[6] == "BL":
                
                partNameBL = ("%s"%(part[0]))
                print("Part name BL has been set to %s." %(partNameBL))
                print(".")
                print(".")
                print(".")
                partImage3 = ("%s"%(part[2]))
                print("Image 3 has been set to %s." %(partImage3))
                print(".")
                print(".")
                print(".")
                partImage3D = "%s"%(part[7])
                print("Image 3D has been set to %s." %(partImage3D))
                print(".")
                print(".")
                print(".")
                partImage3G = ("%s"%(part[8]))
                print("Image 3G has been set to %s." %(partImage3G))
                print(".")
                print(".")
                print(".")

            elif part[5] == str(currentType) and part[6] == "BR":
                
                partNameBR = ("%s"%(part[0]))
                print("Part name BR has been set to %s." %(partNameBR))
                print(".")
                print(".")
                print(".")
                partImage4 = ("%s"%(part[2]))
                print("Image 4 has been set to %s." %(partImage4))
                print(".")
                print(".")
                print(".")
                partImage4D = "%s"%(part[7])
                print("Image 4D has been set to %s." %(partImage4D))
                print(".")
                print(".")
                print(".")
                partImage4G = ("%s"%(part[8]))
                print("Image 4G has been set to %s." %(partImage4G))
                print(".")
                print(".")
                print(".")

    def partChangerLeft(self):
        
        if (0 < clickCounter):
            clickCounter -= 1
        else:
            print("You have reached the beginning!")
            
        if (0 <= clickCounter):
            if clickCounter == 0:
                currentType = "Computer Case"
                print("Current type set to: %s"%(currentType))
                print(".")
                print(".")
                print(".")
            elif clickCounter == 1:
                currentType = "Motherboard"
                print("Current type set to: %s"%(currentType))
                print(".")
                print(".")
                print(".")
            elif clickCounter == 2:
                currentType = "Processor"
                print("Current type set to: %s"%(currentType))
                print(".")
                print(".")
                print(".")
            elif clickCounter == 3:
                currentType = "Graphics Card"
                print("Current type set to: %s"%(currentType))
                print(".")
                print(".")
                print(".")
            elif clickCounter == 4:
                currentType = "CPU Cooler"
                print("Current type set to: %s"%(currentType))
                print(".")
                print(".")
                print(".")
            elif clickCounter == 5:
                currentType = "RAM"
                print("Current type set to: %s"%(currentType))
                print(".")
                print(".")
                print(".")
            elif clickCounter == 6:
                currentType = "Storage"
                print("Current type set to: %s"%(currentType))
                print(".")
                print(".")
                print(".")
            elif clickCounter == 7:
                currentType = "Power Supply"
                print("Current type set to: %s"%(currentType))
                print(".")
                print(".")
                print(".")
            else:
                print("Error: No Current Type")
                
        for part in partList:
            if part[5] == str(currentType) and part[6] == "TL":
                
                partNameTL = ("%s"%(part[0]))
                print("Part name TL has been set to %s." %(partNameTL))
                print(".")
                print(".")
                print(".")
                partImage1 = ("%s"%(part[2]))
                print("Image 1 has been set to %s." %(partImage1))
                print(".")
                print(".")
                print(".")
                partImage1D = "%s"%(part[7])
                print("Image 1D has been set to %s." %(partImage1D))
                print(".")
                print(".")
                print(".")
                partImage1G = ("%s"%(part[8]))
                print("Image 1G has been set to %s." %(partImage1G))
                print(".")
                print(".")
                print(".")
                
            elif part[5] == str(currentType) and part[6] == "TR":
                
                partNameTR = ("%s"%(part[0]))
                print("Part name TR has been set to %s." %(partNameTR))
                print(".")
                print(".")
                print(".")
                partImage2 = ("%s"%(part[2]))
                print("Image 2 has been set to %s." %(partImage2))
                print(".")
                print(".")
                print(".")
                partImage2D = "%s"%(part[7])
                print("Image 2D has been set to %s." %(partImage2D))
                print(".")
                print(".")
                print(".")
                partImage2G = ("%s"%(part[8]))
                print("Image 2G has been set to %s." %(partImage2G))
                print(".")
                print(".")
                print(".")
                
            elif part[5] == str(currentType) and part[6] == "BL":
                
                partNameBL = ("%s"%(part[0]))
                print("Part name BL has been set to %s." %(partNameBL))
                print(".")
                print(".")
                print(".")
                partImage3 = ("%s"%(part[2]))
                print("Image 3 has been set to %s." %(partImage3))
                print(".")
                print(".")
                print(".")
                partImage3D = "%s"%(part[7])
                print("Image 3D has been set to %s." %(partImage3D))
                print(".")
                print(".")
                print(".")
                partImage3G = ("%s"%(part[8]))
                print("Image 3G has been set to %s." %(partImage3G))
                print(".")
                print(".")
                print(".")

            elif part[5] == str(currentType) and part[6] == "BR":
                
                partNameBR = ("%s"%(part[0]))
                print("Part name BR has been set to %s." %(partNameBR))
                print(".")
                print(".")
                print(".")
                partImage4 = ("%s"%(part[2]))
                print("Image 4 has been set to %s." %(partImage4))
                print(".")
                print(".")
                print(".")
                partImage4D = "%s"%(part[7])
                print("Image 4D has been set to %s." %(partImage4D))
                print(".")
                print(".")
                print(".")
                partImage4G = ("%s"%(part[8]))
                print("Image 4G has been set to %s." %(partImage4G))
                print(".")
                print(".")
                print(".")
            

    def selectButtonClickTL(self):
        currentImageTL = partImage1G
        for part in partList:
            if part[0] == partNameTL:
                if part[6] == "TL":
                    selectedPartList.append([str(part[0]), str(part[1]), str(part[2]), str(part[3]), str(part[4]), str(part[5]), str(part[6]), str(part[7]), str(part[8])],)
        for selectedPart in selectedPartList:
            print(str(selectedPart))
    def selectButtonClickTR(self):
        currentImageTR = partImage2G
        for part in partList:
            if part[0] == partNameTR:
                if part[6] == "TR":
                    selectedPartList.append([str(part[0]), str(part[1]), str(part[2]), str(part[3]), str(part[4]), str(part[5]), str(part[6]), str(part[7]), str(part[8])],)
    
    def selectButtonClickBL(self):
        currentImageBL = partImage3G
        for part in partList:
            if part[0] == partNameBL:
                if part[6] == "BL":
                    selectedPartList.append([str(part[0]), str(part[1]), str(part[2]), str(part[3]), str(part[4]), str(part[5]), str(part[6]), str(part[7]), str(part[8])],)
            
    def selectButtonClickBR(self):
        currentImageBR = partImage4G
        for part in partList:
            if part[0] == partNameBR:
                if part[6] == "BR":
                    selectedPartList.append([str(part[0]), str(part[1]), str(part[2]), str(part[3]), str(part[4]), str(part[5]), str(part[6]), str(part[7]), str(part[8])],)

    def compatabilityChecker(self):

        self.compatabilityCheckerMotherboard()
        self.compatabilityCheckerProcessor()
        self.compatabilityCheckerGFX()
        self.compatabilityCheckerCPUCooler()

    
    def compatabilityCheckerMotherboard(self):
        compatNumber = 0
        for selectedPart in selectedPartList:
            if selectedPart[5] == "Computer Case":
                compatNumber = selectedPart[9]
                
        for part in partList:
            if part[5] == "Motherboard" and "Motherboard" == currentType:
                if part[9] <= compatNumber:
                    print("Motherboard (%s) is compatible with case (%s)." %(part[0],selectedPart[0]))
                elif part[9] > compatNumber:
                    print("Motherboard (%s) is incompatible with case (%s)." %(part[0],selectedPart[0]))
                    if part[6] == "TL":

                        currentImageTL = partImage1D

                    elif part[6] == "TR":

                        currentImageTR = partImage2D

                    elif part[6] == "BL":

                        currentImageBL = partImage3D

                    elif part[6] == "BR":

                        currentImageBR = partImage4D

    def compatabilityCheckerProcessor(self):
        compatNumber = 0
        for selectedPart in selectedPartList:
            if selectedPart[5] == "Motherboard":
                compatNumber = selectedPart[10]
                
        for part in partList:
            if part[5] == "Processor" and "Processor" == currentType:
                if part[9] <= compatNumber:
                    print("Processor (%s) is compatible with motherboard (%s)." %(part[0],selectedPart[0]))
                elif part[9] > compatNumber:
                    print("Processor (%s) is incompatible with motherboard (%s)." %(part[0],selectedPart[0]))
                    if part[6] == "TL":

                        currentImageTL = partImage1D

                    elif part[6] == "TR":

                        currentImageTR = partImage2D

                    elif part[6] == "BL":

                        currentImageBL = partImage3D

                    elif part[6] == "BR":

                        currentImageBR = partImage4D

    def compatabilityCheckerGFX(self):
        compatNumber = 0
        for selectedPart in selectedPartList:
            if selectedPart[5] == "Computer Case":
                compatNumber = selectedPart[10]
                
        for part in partList:
            if part[5] == "Graphics Card" and "Graphics Card" == currentType:
                if part[9] <= compatNumber:
                    print("GFX card (%s) is compatible with case (%s)." %(part[0],selectedPart[0]))
                elif part[9] > compatNumber:
                    print("GFX card (%s) is incompatible with case (%s)." %(part[0],selectedPart[0]))
                    if part[6] == "TL":

                        currentImageTL = partImage1D

                    elif part[6] == "TR":

                        currentImageTR = partImage2D

                    elif part[6] == "BL":

                        currentImageBL = partImage3D

                    elif part[6] == "BR":

                        currentImageBR = partImage4D

    def compatabilityCheckerCPUCooler(self):
        compatNumber = 0
        for selectedPart in selectedPartList:
            if selectedPart[5] == "Computer Case":
                compatNumber = selectedPart[10]
                
        for part in partList:
            if part[5] == "Graphics Card" and "Graphics Card" == currentType:
                if part[9] <= compatNumber:
                    print("GFX card (%s) is compatible with case (%s)." %(part[0],selectedPart[0]))
                elif part[9] > compatNumber:
                    print("GFX card (%s) is incompatible with case (%s)." %(part[0],selectedPart[0]))
                    if part[6] == "TL":

                        currentImageTL = partImage1D

                    elif part[6] == "TR":

                        currentImageTR = partImage2D

                    elif part[6] == "BL":

                        currentImageBL = partImage3D

                    elif part[6] == "BR":

                        currentImageBR = partImage4D
        

    def infoButtonTLClick(self):

        print("Displaying TL part.")

        InfoButtonTL(partNameTL)

    def infoButtonTRClick(self):

        print("Displaying TR part.")

        InfoButtonTR(partNameTR)

    def infoButtonBLCLick(self):

        print("Displaying BL part.")

        InfoButtonBL(partNameBL)

    def infoButtonBRClick(self):

        print("Displaying BR part.")

        InfoButtonBR(partNameBR)


class InfoButtonTL():
    
    def __init__(self, partNameTL):

        global infoPartPriceTL
        global infoPartImageTL
        global infoPartWattTL
        global infoPartDescTL

        infoPartPriceTL = ""
        infoPartImageTL = ""
        infoPartWattTL = ""
        infoPartDescTL = ""

        for part in partList:

            if (part[0] == partNameTL):

                infoPartPriceTL = str(part[1])

                infoPartImageTL = str(part[2])

                infoPartWattTL = str(part[3])

                infoPartDescTL = str(part[4])

        self.window = Toplevel()

        self.window.title("More Info about %s" %(partNameTL))
        self.window.geometry("1240x1770")
        
        titleText = StringVar()
        titleText.set("%s" %(partNameTL))
        self.title = Label(self.window,
                            textvariable=titleText,
                            font=("Helvetica", 25),
                            wraplength=500)
        self.title.pack(side=TOP)
        
        mainText = StringVar()
        mainText.set("%s" %(infoPartDescTL))
        self.mainText = Label(self.window,
                            textvariable=mainText,
                            font=("Helvetica", 18),
                            wraplength=500)
        self.mainText.pack(side=BOTTOM)

        try:
            partImage = PhotoImage(file=str(infoPartImageTL))
            
            self.partPhoto =\
            Label(self.window,
                  anchor="center",
                  image=partImage,
                  width=1000, height=1000)
            self.partPhoto.image = partImage

        except Exception as exception:
            
            print(exception)
            
        self.partPhoto.pack()

class InfoButtonTR():
    
    def __init__(self, partNameTR):

        global infoPartPriceTR
        global infoPartImageTR
        global infoPartWattTR
        global infoPartDescTR

        infoPartPriceTR = ""
        infoPartImageTR = ""
        infoPartWattTR = ""
        infoPartDescTR = ""

        for part in partList:

            if (part[0] == partNameTR):

                infoPartPriceTR = str(part[1])

                infoPartImageTR = str(part[2])

                infoPartWattTR = str(part[3])

                infoPartDescTR = str(part[4])

        self.window = Toplevel()

        self.window.title("More Info about %s" %(partNameTR))
        self.window.geometry("1240x1770")
        
        titleText = StringVar()
        titleText.set("%s" %(partNameTR))
        self.title = Label(self.window,
                            textvariable=titleText,
                            font=("Helvetica", 25),
                            wraplength=500)
        self.title.pack(side=TOP)
        
        mainText = StringVar()
        mainText.set("%s" %(infoPartDescTR))
        self.mainText = Label(self.window,
                            textvariable=mainText,
                            font=("Helvetica", 18),
                            wraplength=500)
        self.mainText.pack(side=BOTTOM)

        try:
            partImage = PhotoImage(file=str(infoPartImageTR))
            
            self.partPhoto =\
            Label(self.window,
                  anchor="center",
                  image=partImage,
                  width=1000, height=1000)
            self.partPhoto.image = partImage

        except Exception as exception:
            
            print(exception)
            
        self.partPhoto.pack()

class InfoButtonBL():
    
    def __init__(self, partNameBL):

        global infoPartPriceBL
        global infoPartImageBL
        global infoPartWattBL
        global infoPartDescBL

        infoPartPriceBL = ""
        infoPartImageBL = ""
        infoPartWattBL = ""
        infoPartDescBL = ""

        for part in partList:

            if (part[0] == partNameBL):

                infoPartPriceBL = str(part[1])

                infoPartImageBL = str(part[2])

                infoPartWattBL = str(part[3])

                infoPartDescBL = str(part[4])

        self.window = Toplevel()

        self.window.title("More Info about %s" %(partNameBL))
        self.window.geometry("1240x1770")
        
        titleText = StringVar()
        titleText.set("%s" %(partNameBL))
        self.title = Label(self.window,
                            textvariable=titleText,
                            font=("Helvetica", 25),
                            wraplength=500)
        self.title.pack(side=TOP)
        
        mainText = StringVar()
        mainText.set("%s" %(infoPartDescBL))
        self.mainText = Label(self.window,
                            textvariable=mainText,
                            font=("Helvetica", 18),
                            wraplength=500)
        self.mainText.pack(side=BOTTOM)

        try:
            partImage = PhotoImage(file=str(infoPartImageBL))
            
            self.partPhoto =\
            Label(self.window,
                  anchor="center",
                  image=partImage,
                  width=1000, height=1000)
            self.partPhoto.image = partImage

        except Exception as exception:
            
            print(exception)
            
        self.partPhoto.pack()

class InfoButtonBR():
    
    def __init__(self, partNameBR):

        global infoPartPriceBR
        global infoPartImageBR
        global infoPartWattBR
        global infoPartDescBR

        infoPartPriceBR = ""
        infoPartImageBR = ""
        infoPartWattBR = ""
        infoPartDescBR = ""

        for part in partList:

            if (part[0] == partNameBR):

                infoPartPriceBR = str(part[1])

                infoPartImageBR = str(part[2])

                infoPartWattBR = str(part[3])

                infoPartDescBR = str(part[4])

        self.window = Toplevel()

        self.window.title("More Info about %s" %(partNameBR))
        self.window.geometry("1240x1770")
        
        titleText = StringVar()
        titleText.set("%s" %(partNameBR))
        self.title = Label(self.window,
                            textvariable=titleText,
                            font=("Helvetica", 25),
                            wraplength=500)
        self.title.pack(side=TOP)
        
        mainText = StringVar()
        mainText.set("%s" %(infoPartDescBR))
        self.mainText = Label(self.window,
                            textvariable=mainText,
                            font=("Helvetica", 18),
                            wraplength=500)
        self.mainText.pack(side=BOTTOM)

        try:
            partImage = PhotoImage(file=str(infoPartImageBR))
            
            self.partPhoto =\
            Label(self.window,
                  anchor="center",
                  image=partImage,
                  width=1000, height=1000)
            self.partPhoto.image = partImage

        except Exception as exception:
            
            print(exception)
            
        self.partPhoto.pack()


    
    
        
def main():

    app = StartScreen()

main()
