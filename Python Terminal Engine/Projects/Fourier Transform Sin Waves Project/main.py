# A Little Example Project To Showcase Some Capabilities #
# Check Out 'CallbackRunner.py To See How Everything Runs More Backend - Wise. #

from src import * # Importing The Engine.
from SinDef import * # Importing The Helper Script In The Folder.

UpdateScreenSize(32, 32)

BackgroundColor = Color(0, 150, 255)
ScreenPixelBuffer : list = InitNewEmptyScreenBuffer(BackgroundColor)

def Start():
    # Clean The WHOLE Terminal:``
    ClearScreen()

def Update():
    global DELTA_TIME, QUIT, ScreenPixelBuffer, BackgroundColor, ScreenScale

    if (Input.IsKeyDown("w")):
        ScreenScale += DELTA_TIME

    elif (Input.IsKeyDown("s")):
        ScreenScale -= DELTA_TIME
        ScreenScale = max(0.01, ScreenScale)

    i = 0
    for a in SinWaves:
        i += a.ToSin(-SCREEN_WIDTH)

    now = Vector2(-SCREEN_WIDTH, i)
    prev = now

    for x in range(-SCREEN_WIDTH, SCREEN_WIDTH):
        
        i = 0
        for a in SinWaves:
            i += a.ToSin(x)

        prev = Vector2(x, i)

        DrawLine(ScreenPixelBuffer, prev, now, Color.red())
        now = prev

def OnFinishedRender():

    print("Line Functions:")
    print("-" * 20)

    for a in SinWaves:
        
        a.print()
        a.movespeed = TIME * 5

    print()

def Quit():
    ClearScreen()
