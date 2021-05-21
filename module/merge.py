import cv2
import numpy as np


class merge:
    def run(idx, img, file_name, _input, type):
        print("     -> Merge")
        print(len(img.shape))
        width, height, channel = img.shape

        mask_img = cv2.imread('mask_img.png', cv2.IMREAD_ANYCOLOR)
        # cv2.imshow("mask", mask_img)

        merge_img = img
        # if 'r' not in _input:
        # print("ReSize Mode Not Found")
        resize_img = cv2.resize(mask_img, dsize=(
            height, width), interpolation=cv2.INTER_AREA)
        # else:
        #     resize_img = mask_img

        # 워터 마크로 넣을 이미지 그레이 스케일 색상 공간으로 변환
        mask_gray_img = cv2.cvtColor(resize_img, cv2.COLOR_BGR2GRAY)
        # 그레이스케일 이미지를 임계값으로 이진화하여 마스크 생성
        ret, mask = cv2.threshold(mask_gray_img, 250, 255, cv2.THRESH_BINARY)
        # 해당 마스크의 역처리(not 비트연산)
        mask_inv = cv2.bitwise_not(mask)

        # 워터마크 이미지에서 워터마크 영역만 추출(and 비트연산, 역마스크 영역)
        img2_fg = cv2.bitwise_and(resize_img, resize_img, mask=mask_inv)

        # 이미지의 높이, 너비, 채널 수 구하기
        height, width, channels = merge_img.shape
        # 배경 이미지의 ROI(Region of Interest : 관심영역) 구하기
        roi = merge_img[0:height, 0:width]

        # 배경 이미지의 ROI 영역과 워터마크 이미지의 워터마크 영역을 블렌딩
        # cv2.addWeighted(src1, alpha, src2, beta, gamma, dst=None, dtype=None) -> dst
        # • src1: (입력) 첫 번째 영상
        # • alpha: 첫 번째 영상 가중치
        # • src2: 두 번째 영상. src1과 같은 크기 & 같은 타입
        # • beta: 두 번째 영상 가중치
        # • gamma: 결과 영상에 추가적으로 더할 값
        # • dst: 가중치 합 결과 영상
        # • dtype: 출력 영상(dst)의 타입

        dst = cv2.addWeighted(roi, 1, img2_fg, 0.9, 0)
        # 배경 이미지의 ROI 영역을 위의 dst 이미지로 변경
        merge_img[0:height, 0:width] = dst

        return merge_img
