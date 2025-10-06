#                      {!IMPORTANT!}                         #
# ---------------------------------------------------------- #
# THIS SCRIPT IS RESPONSIBLE FOR RUNNING main.py's CALLBACKS #
# BUILD THIS SCRIPT IN CASE YOU WANT TO TURN IT INTO AN EXE! #
# ---------------------------------------------------------- #



import threading, time, main




# Get All Callbacks / Attrs In main.py:

quitMethod           = getattr(main, "Quit",   None) # Called On Trying To Exit Program.
initMethod           = getattr(main, "Start",  None) # Called On Starting Program.
updateMethod         = getattr(main, "Update", None) # Called Every Frame, BEFORE Screen Rendering.
finishedRenderMethod = getattr(main, "OnFinishedRender", None) # Called Every Frame, AFTER Screen Rendering.

# Main Screen Pixel Buffer:
ScreenPixelBuffer = getattr(main, "ScreenPixelBuffer", None)
ScreenPixelBufferExists = ScreenPixelBuffer is not None

# If No Background Color Exists It Will Be Reverted To A Black Color.
BackgroundColor = getattr(main, "BackgroundColor", main.Color.black())




# Print Program Name:
main.move_cursor(0, 0)
print("Virus.exe" + (" " * main.SCREEN_WIDTH))




# Mains:
# -------------------------------------------------------------------------------- #

def DrawFrame():
    # Continously Get Background Color.
    BackgroundColor = getattr(main, "BackgroundColor", main.Color.black())

    if (ScreenPixelBufferExists):
        main.SetScreenColor(ScreenPixelBuffer, BackgroundColor)

    if updateMethod is not None:
        if callable(updateMethod):
            main.Update()

    if (not ScreenPixelBufferExists):
        return
    
    renderThread = threading.Thread(target=main.RenderScreen, args=(ScreenPixelBuffer,))
    renderThread.start()

    renderThread.join()

    if finishedRenderMethod is not None:
        if callable(finishedRenderMethod):
            main.OnFinishedRender()
    
    # Other Updates Of "Constants":
    main.TIME += main.DELTA_TIME
    main.FPS = 1 / main.DELTA_TIME

    # Debug:
    print(f"FPS: {round(main.FPS, 2)}           ")
    print(f"Delta Time: {main.DELTA_TIME}       ")

def Update():
    while not main.QUIT:
        DrawFrame()
        T1 = time.perf_counter()
        
        DrawFrame()
        T2 = time.perf_counter()

        main.DELTA_TIME = T2 - T1

def Quit():
    global QUIT
    QUIT = True

    if quitMethod is not None:
        if callable(quitMethod):
            main.Quit()




# Call In Order:

if initMethod is not None:
    if callable(initMethod):
        main.Start()

try:
    Update()
except KeyboardInterrupt:
    Quit()
