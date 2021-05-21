from module.show import show
from module.crop import crop
from module.resize import resize
from module.grayscale import grayscale
from module.rotate import rotate
from module.merge import merge
from module.stack import stack
import cv2

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
    def get_process(type, idx, img, file_name, _input, img_list):
        print("Process ====== > ")

        if type == 's':
            return show.run(idx, img, file_name)

        elif type == 'c':
            # number = input("입력입력")
            # print(number)
            return crop.run(idx, img, file_name, _input[type])

        elif type == 'r':
            return resize.run(idx, img, file_name, _input[type])

        elif type == 'g':
            # print("Gray Scaleg")
            return grayscale.run(idx, img, file_name)

        elif type == 't':
            return rotate.run(idx, img, file_name, _input[type])

        elif type == 'm':
            # print("Merge")
            return merge.run(idx, img, file_name, _input, type)

        elif type == 'v':
            # print("Stack")
            return stack.run(idx, img, file_name, _input, img_list, type)

        elif type == 'h':
            return stack.run(idx, img, file_name, _input, img_list, type)
