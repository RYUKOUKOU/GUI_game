from picture_base import load_image

#0-1077
class all_base:
    def __init__(self,num):
        self.num = num
        self.pic = load_image(num)

class terrain(all_base):
    def __init__(self,can_pass):
        super().__init__(num)
        self.can_pass = can_pass