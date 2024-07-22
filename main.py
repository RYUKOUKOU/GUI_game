import os
import picture_base
import config
import base_class

import matplotlib.pyplot as plt

def main():
    config.PATH=os.path.dirname(os.path.abspath(__file__))

if __name__=="__main__":
    main()
    ground = base_class.all_base(1077,False)
    plt.imshow(ground.pic)
    plt.axis('on')
    plt.show()
