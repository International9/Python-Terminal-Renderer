from src import * 

UpdateScreenSize(20, 20)

ColorVal = 1

BackgroundColor = Color.red()
ScreenPixelBuffer : list = InitNewEmptyScreenBuffer(BackgroundColor)

def Start():
    global BackgroundColor, ScreenPixelBuffer

def Update():
    global DELTA_TIME, ScreenPixelBuffer, BackgroundColor, ColorVal
    
    if (ColorVal >= 1): ColorVal = 0
    ColorVal += DELTA_TIME * .1

    BackgroundColor = Color.hsvToRgb(ColorVal, 1, 1)

def OnFinishedRender():
    print("FRAME RENDERED!")

def Quit():
    ClearScreen()
    print("QUIT PROGRAM!")
