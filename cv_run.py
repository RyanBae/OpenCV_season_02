import sys
import os
import argparse
import cv2

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
            print("\n Img_File_List : {} \n".format(img_file_list))

        else:
            print("Not Found Folder : {} \n".format(IMG_DIR_PATH))

        # 2.입력된 mode 별 이미지 편집
        for mode in MODE_LIST:
            print(mode)
            self.get_mode_process(mode)

        if len(img_file_list) != 0:
            for idx in range(0, len(img_file_list)):
                print(idx)
                print(img_file_list[idx])
                img = cv2.imread(
                    IMG_DIR_PATH+'/'+img_file_list[idx], cv2.IMREAD_ANYCOLOR)

                print("img_"+str(idx))
                cv2.imshow("img_"+str(idx), img)

        k = cv2.waitKey(0)
        if k == 27:
            cv2.destoryAllWindows()

    def get_mode_process(self, mode):
        print("Get Mode Process : {}".format(mode))


if __name__ == '__main__':
    cv_run()
