import cv2
import numpy as np


class stack:
    def run(idx, img, file_name, _input, img_list, type):
        width, height = img.shape
        print("????")
        stack_img = img

        for i in img_list:
            if i != idx:
                if 'r' not in _input:
                    print("ReSize Mode Not Found")
                    resize_img = cv2.resize(img_list[i]['back_img'], dsize=(
                        height, width), interpolation=cv2.INTER_AREA)
                else:
                    resize_img = img_list[i]['back_img']

                if _input[type]['type'] == 'v':
                    # 위에서 아래로 붙이기
                    stack_img = np.vstack((stack_img, resize_img))
                else:
                    # 왼쪽에서 오른쪽으로 붙이기
                    stack_img = np.hstack((stack_img, resize_img))

        return stack_img
