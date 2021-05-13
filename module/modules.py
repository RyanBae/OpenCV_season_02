from module.show import show
from module.crop import crop
from module.resize import resize

'''
Crop - c ,
Re Size - r ,
Gray Scaleg - g ,
Merge - m ,
VStack - v ,
HStack - h,
Show - s
'''


class modules:
    # def __init__(self, type, idx, img, file_name):
    #     self.get_process(type, idx, img, file_name)

    def get_process(type, idx, img, file_name):
        # print("Type : "+type)
        # print(img)
        if type == 's':

            return show.run(idx, img, file_name)

        elif type == 'c':
            # number = input("입력입력")
            # print(number)
            return crop.run(idx, img, file_name)

        elif type == 'r':
            return resize.run(idx, img, file_name)

        elif type == 'g':
            print("Gray Scaleg")

        elif type == 'm':
            print("Merge")

        elif type == 'v':
            print("VStack")

        elif type == 'h':
            print("HStack")
