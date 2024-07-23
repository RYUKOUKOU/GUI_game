import os
import picture_base
import config
import base_class
import screen

import matplotlib.pyplot as plt

def main():
    config.PATH=os.path.dirname(os.path.abspath(__file__))
    pass

if __name__=="__main__":
    main()
    screen.start()