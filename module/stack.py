import cv2
import numpy as np


class stack:
    def run(idx, img, file_name, _input):
        print(_input)
        # print(img_list)
        stack_img = cv2.resize(img, dsize=(
            0, 0), fx=0.3, fy=0.7, interpolation=cv2.INTER_LINEAR)

        # if _input['type'] == 'v':
        # for i in img_list:
        # print(img_list[i]['img'])
        # resize_img = cv2.resize(img_list[i]['img'], dsize=(
        # 0, 0), fx=0.3, fy=0.3, interpolation=cv2.INTER_LINEAR)
        # stack_img = np.vstack([stack_img, img_list[1]['img']])

        # else:
        # for i in img_list:
        # print(img_list[i]['img'])
        # resize_img = cv2.resize(img_list[i]['img'], dsize=(
        # 0, 0), fx=0.3, fy=0.7, interpolation=cv2.INTER_LINEAR)
        # stack_img = np.vstack([img_list])

        # cv2.imshow("img_"+str(idx), stack_img)

        return stack_img
