from pyfirmata import Arduino 

import time 

if __name__ == "__main__":
    board = Arduino("COM3")
    print("connection started")
    while True:
        board.digital[7].write(1)
        time.sleep(2)
        board.digital[7].write(0)
        time.sleep(2)
