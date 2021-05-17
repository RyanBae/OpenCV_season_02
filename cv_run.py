import sys
import os
import glob
import argparse
import cv2
from pathlib import Path

from module.modules import modules


# python3 cv_run.py --img_dir=./image --mode=s,r --result_dir=test

parser = argparse.ArgumentParser(description="Please enter your argument.")
parser.add_argument('--img_dir', required=True,
                    help='Please enter an image folder to import.')
parser.add_argument('--mode', required=True,
                    help='''Please enter the required mode. Examples) c,r,g,v,h  Mode List :
                     Crop - c ,
                     Re Size - r ,
                     Gray Scaleg - g ,
                     Rotate - t,
                     Merge - m ,
                     VStack - v ,
                     HStack - h
                     Show Image - s''')
parser.add_argument('--result_dir', required=True,
                    help='Please enter the folder where you want to save the results.')

# argparse 사용 안할경우 import sys 이후 아래 로직으로 argument 가져올수 있음.
# for idx, arg in enumerate(sys.argv):
#     if idx != 0:
#         # STORAGE_FILE_LIST.append(arg)
#         print(arg)

args = parser.parse_args()
IMG_DIR_PATH = args.img_dir
RESULT_DIR_PATH = args.result_dir
MODE_LIST = args.mode.split(',')
CONVERSION_IMG_LIST = {}

_input = {}


class cv_run():
    def __init__(self):
        self.run()

    def run(self):
        print("==> Run!!\n")
        print('[IMG_DIR_PATH] : '+IMG_DIR_PATH+' , [RESULT_DIR_PATH] : ' +
              RESULT_DIR_PATH+' , [MODE_LIST] : '+str(MODE_LIST)+"\n")

        # if 'm' in MODE_LIST:
        #     print("m !!!!")

        for mode in MODE_LIST:
            self.mode_input_data(mode)

        # 1. img_dir_path 의 이미지 파일 가져오기
        flag = os.path.isdir(IMG_DIR_PATH)
        img_file_list = []
        if flag == True:
            img_file_list = os.listdir(IMG_DIR_PATH)
            extensions = ['.jpg', '.png', '.jpeg']
            img_file_list = [x.name for x in Path(
                IMG_DIR_PATH).iterdir() if x.suffix.lower() in extensions]
            print("\n Img_File_List : {} \n".format(img_file_list))

        else:
            print("Not Found Folder : {} \n".format(IMG_DIR_PATH))

        # 2.입력된 mode 별 이미지 편집
        if len(img_file_list) != 0:
            for idx in range(0, len(img_file_list)):
                print("[Process] idx : {} , File Name : {}".format(
                    idx, img_file_list[idx]))
                get_img = cv2.imread(
                    IMG_DIR_PATH+'/'+img_file_list[idx], cv2.IMREAD_ANYCOLOR)

                if type(get_img) is not type(None):
                    for mode in MODE_LIST:
                        get_img = modules.get_process(
                            mode, idx, get_img, str(img_file_list[idx]), _input, CONVERSION_IMG_LIST)

                else:
                    print("[Image Mode Process] Not Image Type!")

                CONVERSION_IMG_LIST.update({idx: {'id': idx, 'img': get_img}})

            # 편집된 이미지 저장
            # if type(get_img) is not type(None):
            #     self.save_img(MODE_LIST, idx, get_img, str(
            #         img_file_list[idx]), RESULT_DIR_PATH)
            # else:
            #     print("[Image Save Fun] Not Image Type!")

        # if len(MODE_LIST) != 0:
        #     for mode in MODE_LIST:
        #         if len(img_file_list) != 0:
        #             for idx in range(0, len(img_file_list)):
        #                 get_img = cv2.imread(
        #                     IMG_DIR_PATH+'/'+img_file_list[idx], cv2.IMREAD_ANYCOLOR)

        #                 if type(get_img) is not type(None):
        #                     get_img = modules.get_process(mode, idx, get_img, str(
        #                         img_file_list[idx]), _input, CONVERSION_IMG_LIST)
        #                         # key 값으로 있으면
        #                     CONVERSION_IMG_LIST.update(
        #                         {idx: {'id': idx, 'img': get_img}})
        #                 else:
        #                     print("[Image Mode Process] Not Image Type!")

        # print(CONVERSION_IMG_LIST)
        # cv2.imshow(
        #     "img_"+str(CONVERSION_IMG_LIST[8]), CONVERSION_IMG_LIST[8]['img'])
        if 's' in MODE_LIST:
            k = cv2.waitKey(0)
            if k == 27:
                cv2.destoryAllWindows()
        else:
            k = cv2.waitKey(0)
            if k == 27:
                cv2.destoryAllWindows()

    def save_img(self, mode, idx, img, file_name, floder):
        print("Save Image ==>")
        print("[Process2] idx : {} , File Name : {} , Mode :{} , img : {}".format(
            idx, file_name, ','.join(mode), img))

        if os.path.isdir(floder) == False:
            os.mkdir(floder)

        cv2.imwrite(floder+'/'+str(idx)+'_' +
                    ("".join(mode))+'_'+file_name, img)

    def mode_input_data(self, mode):
        # Show
        if mode == 's':
            print("Show")

        # Crop
        elif mode == 'c':
            print("Crop")
            y = input("높이 범위를 입력하세요. ex) 100:500 \n")
            y = y.split(':')
            if int(y[1]) < int(y[0]):
                print("[Fail Input] "+y[0]+":"+y[1] +
                      " = y2("+y[1]+") 는 y1("+y[0]+") 보다 작을수 없습니다. ")
                exit()

            x = input("너비 범위를 입력하세요. ex) 200:700 \n")
            x = x.split(":")
            if int(x[1]) < int(x[0]):
                print("[Fail Input] "+x[0]+":"+x[1] +
                      " = x2("+x[1]+") 는 x1("+x[0]+") 보다 작을수 없습니다. ")
                exit()

            _input.update(
                {'c': {'y1': y[0], 'y2': y[1], 'x1': x[0], 'x2': x[1]}})

        # ReSize
        elif mode == 'r':
            print("Resize")
            check = input("절대크기 = 0 , 상대크기 = 1 중 선택해주세요. \n")
            if check == '0':
                x = input("너비를 입력해주세요. ex) 640 \n")
                y = input("높이를 입력해주세요. ex) 480 \n")
                _input.update({'r': {'y': y, 'x': x, 'type': check}})
            elif check == '1':
                x = input("너비 비율을 입력해주세요. ex) 0.3 \n")
                y = input("높이 비율을 입력해주세요. ex) 0.7 \n")
                _input.update({'r': {'y': y, 'x': x, 'type': check}})

            else:
                print("잘못 입력하였습니다.")
                exit()

        # Gray Scale Not Input
        # elif mode == 'g':
        #     print("Gray Scale")

        # Rotate
        elif mode == 't':
            print("Rotate")
            check = input("회전 변환 행렬 = 0 , Rotate Method = 1 중 선택해주세요. \n")
            if check == '0':
                angle = input("회전 각을 입력해주세요. ex)Max 360, min -360 \n")
                if int(angle) > 360 or int(angle) < -360:
                    print("최대값 360, 최소값 -360 을 넘을수 없습니다.")
                    exit()

                scale = input("확대 및 축소 비율을 입력해주세요. \n")
                if int(scale) > 100 or int(scale) < 0:
                    print("최대값 100, 최소값 0 을 넘을수 없습니다.")
                    exit()

                _input.update({'t': {'a': angle, 's': scale, 'type': check}})

            elif check == '1':
                angle = input(
                    "choice Rotate Method \n 1. ROTATE_90_CLOCKWISE (시계방향 90) \n 2. ROTATE_180 (180) \n 3. ROTATE_90_COUNTERCLOCKWISE (반시계방향 90) \n")
                if int(angle) > 3:
                    print("잘못 입력하였습니다.")
                    exit()

                _input.update({'t': {'a': angle, 'type': check}})

            else:
                print("잘못 입력하였습니다.")
                exit()

        # Merge
        elif mode == 'm':
            print("Merge")

        # VStack
        elif mode == 'v' or mode == 'h':
            print("VStack")
            # check = input(" V Stack = 0 , H Stack = 1 방향을 선택해주세요. \n ")
            # self.mode_input_data('r')
            _input.update({'v': {'type': 'v'}})

        elif mode == 'h':
            print("HStack")
            _input.update({'h': {'type': 'h'}})
        # HStack
        # print("===> _input")
        # print(_input)


if __name__ == '__main__':
    cv_run()
