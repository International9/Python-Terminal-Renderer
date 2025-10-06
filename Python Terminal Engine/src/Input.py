held_keys = set()

def IsKeyDown(key : str) -> bool:
    if (not held_keys): return False
    return key in held_keys
    
def on_press(key):
    global QUIT

    try:
        # if (key == keyboard.Key.esc):
        #     QUIT = True
        #     return False

        held_keys.add(key.char)
    except AttributeError:
        held_keys.add(str(key))
    
    return True

def on_release(key):
    try:
        held_keys.remove(key.char)
    except AttributeError:
        held_keys.discard(str(key))
    
    return True
