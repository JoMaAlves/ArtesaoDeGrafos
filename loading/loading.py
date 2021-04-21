import os
import time
os.system("cls")
capivaras = ["capivara1.txt", "capivara2.txt", "capivara3.txt", "capivara2.txt", "capivara1.txt"]


def animator (filesnames, delay, repeat):
    frames = []
    here = os.path.dirname(os.path.abspath(__file__))
    
    for name in filesnames:
        with open(os.path.join(here, name), "r", encoding="utf8") as f:
            frames.append(f.readlines())
    
    for i in range(repeat):
        for frame in frames:
            print("".join(frame))
            time.sleep(delay)
            os.system("cls")


animator(capivaras, 0.2, 5)
