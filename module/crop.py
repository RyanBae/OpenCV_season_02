import cv2


class crop:
    def run(idx, img, file_name):
        print("   -> Crop")
        crop_img = img[100:600, 200:700].copy()

        return crop_img
