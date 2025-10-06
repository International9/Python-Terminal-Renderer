from src.Constants import * 
from src.VectorLib import * 
from src.Color import * 

import os, sys

def ClearScreen(): 
    '''A Function Utilizing 'os.system' To Clear The Terminal.'''
    os.system('cls' if os.name == 'nt' else 'clear')

def UpdateScreenSize(w, h):
    '''A Function Which Updates Screen Height And Width As With Other Params Involved With It. (Only Call In Initialization!)'''
    
    global SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_HEIGHT_HALF, SCREEN_WIDTH_HALF, SCREEN_HEIGHTXWIDTH
    
    SCREEN_WIDTH = w
    SCREEN_HEIGHT = h

    SCREEN_HEIGHT_HALF = SCREEN_HEIGHT // 2
    SCREEN_WIDTH_HALF  = SCREEN_WIDTH  // 2
    SCREEN_HEIGHTXWIDTH = SCREEN_HEIGHT * SCREEN_WIDTH

def move_cursor(x, y):
    '''A Helper Function To Move The Terminal's Current Cursor Position.'''

    sys.stdout.write(f"\x1b[{y};{x}H")
    sys.stdout.flush()

def InitNewEmptyScreenBuffer(color : Color = None):
    '''A Function Which Initializes A New Screen Pixel Buffer.'''
    return [color for _ in range(SCREEN_HEIGHTXWIDTH)]

# Dumb Little Helper.
def RGBtoANSI(color : Color):
    return f"\033[38;2;{color.r};{color.g};{color.b};48;2;{color.r};{color.g};{color.b}m"

def DrawLine(ScreenPixelBuffer, a : Vector2, b : Vector2, color : Color) -> bool:
    '''A Function Which Uses The DDA Line Drawing Algorithm To Draw A Line On The PixelBuffer Given Two Vector2s'''

    if (a == b): return False

    dx = b.x - a.x
    dy = b.y - a.y
    absX = abs(dx)
    absY = abs(dy)
    
    if absX > absY:
        steps = absX
    else:
        steps = absY

    incX = dx / steps
    incY = dy / steps

    x = a.x
    y = a.y

    for i in range(round(steps)):
        DrawPoint(Vector2(round(x), round(y)), ScreenPixelBuffer, color)
        x += incX
        y += incY
    
    return True

def ConvertVector2ToScreenPixelBufferIndices(pos : Vector2) -> int:
    '''A Function Taking A Vector2 And Converts It Into An Index For A Screen Pixel Buffer.'''

    j = (SCREEN_HEIGHTXWIDTH) // 2 - (int(pos.y) * SCREEN_HEIGHT)
    i = int(pos.x) + SCREEN_WIDTH_HALF

    if (j < 0 or j >= SCREEN_HEIGHTXWIDTH): 
        return None
    
    if (i < 0 or i >= SCREEN_WIDTH): 
        return None

    return int(j + i)

def SetScreenColor(ScreenPixelBuffer, color : Color):
    '''A Function Sets ALL Of A Screen Pixel Buffer's Pixels To One Color.'''
    
    for i in range(SCREEN_HEIGHTXWIDTH):
        ScreenPixelBuffer[i] = color

def DrawPoint(pos : Vector2, ScreenPixelBuffer, Color : Color = Color(0, 0, 0)):
    '''A Function Which Draws A Point On The Screen.'''
    
    index = ConvertVector2ToScreenPixelBufferIndices(pos)
    if (index is None): return False
    
    try:
        ScreenPixelBuffer[index] = Color
        return True
    except:
        return False

def RenderScreen(ScreenPixelBuffer, ScreenBorderColor : Color = Color.white()):
    '''The Function Used To Print The Screen Using The Screen Pixel Buffer To The Console / Terminal.'''
    
    borderColor = RGBtoANSI(ScreenBorderColor)
    
    y = 2
    move_cursor(0, y)

    for i in range(SCREEN_WIDTH+2):
        print(f"\033[38;2;{ScreenBorderColor.r};{ScreenBorderColor.g};{ScreenBorderColor.b}m▄", end=RESET)
    print()

    for i in range(SCREEN_HEIGHTXWIDTH):
        if ((i // SCREEN_WIDTH) % 2 == 1): continue # Thank You ChatG*T.
        
        if i % SCREEN_WIDTH == 0:
            print(borderColor + OCCUPIED_PIXEL, end=RESET)
        
        top = ScreenPixelBuffer[i] # Top Pixel.

        # Bottom Pixel.
        bottomIndex = i + SCREEN_WIDTH
        
        # Print Pixel.
        try:
            bottom = ScreenPixelBuffer[bottomIndex]
            print(f"\033[38;2;{top.r};{top.g};{top.b};48;2;{bottom.r};{bottom.g};{bottom.b}m{OCCUPIED_PIXEL}", end=RESET)

        except:
            print(f"\033[38;2;{top.r};{top.g};{top.b};48;2;{top.r};{top.g};{top.b}m{OCCUPIED_PIXEL}", end=RESET)

        if (i+1) % SCREEN_WIDTH == 0:
            y += 1
            
            print(borderColor + OCCUPIED_PIXEL, end=RESET)
            
            move_cursor(0, y)
            print()
    
    for i in range(SCREEN_WIDTH+2):
        print(f"\033[38;2;{ScreenBorderColor.r};{ScreenBorderColor.g};{ScreenBorderColor.b}m{OCCUPIED_PIXEL}", end=RESET)
    print()
