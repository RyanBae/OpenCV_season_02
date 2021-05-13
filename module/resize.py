import cv2


class resize:
    def run(idx, img, file_name):
        print("   -> Re Size")
        resize_img = cv2.resize(img, dsize=(
            0, 0), fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)

        return resize_img
