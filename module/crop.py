import cv2


class crop:
    def run(idx, img, file_name, _input):
        print("   -> Crop")
        print(_input)
        crop_img = img[int(_input['y1']):int(_input['y2']),
                       int(_input['x1']):int(_input['x2'])].copy()

        return crop_img
