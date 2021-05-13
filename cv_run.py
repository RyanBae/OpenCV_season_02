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


class cv_run():
    def __init__(self):
        self.run()

    def run(self):
        print("==> Run!!\n")
        print('[IMG_DIR_PATH] : '+IMG_DIR_PATH+' , [RESULT_DIR_PATH] : ' +
              RESULT_DIR_PATH+' , [MODE_LIST] : '+str(MODE_LIST)+"\n")

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

                if get_img is not None:
                    for mode in MODE_LIST:
                        get_img = modules.get_process(
                            mode, idx, get_img, str(img_file_list[idx]))

                # 편집된 이미지 저장
                if get_img is not None:
                    self.save_img(MODE_LIST, idx, get_img, str(
                        img_file_list[idx]), RESULT_DIR_PATH)

        k = cv2.waitKey(0)
        if k == 27:
            cv2.destoryAllWindows()

    def save_img(self, mode, idx, img, file_name, floder):
        print("Save Image ==>")
        print("[Process] idx : {} , File Name : {} , Mode :{} , img : {}".format(
            idx, file_name, ','.join(mode), img))

        if os.path.isdir(floder) == False:
            os.mkdir(floder)

        cv2.imwrite(floder+'/'+str(idx)+'_' +
                    ("".join(mode))+'_'+file_name, img)


if __name__ == '__main__':
    cv_run()
