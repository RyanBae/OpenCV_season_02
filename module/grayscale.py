import cv2


class grayscale:
    def run(idx, img, file_name):
        print("   -> Re Size")
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        print(gray_img.shape)

        return gray_img
