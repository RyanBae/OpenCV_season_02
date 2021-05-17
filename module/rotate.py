import cv2


class rotate:
    def run(idx, img, file_name, _input):
        print("     -> Rotate")
        print(_input)

        if _input['type'] == '0':
            height, width, channel = img.shape
            matrix = cv2.getRotationMatrix2D(
                (width/2, height/2), int(_input['a']), int(_input['s']))
            rotate_img = cv2.warpAffine(img, matrix, (width, height))
        else:
            angle = _input['a']
            if angle == '1':
                rotate_img = cv2.rotate(img, cv2.cv2.ROTATE_90_CLOCKWISE)

            elif angle == '2':
                rotate_img = cv2.rotate(img, cv2.cv2.ROTATE_180)

            elif angle == '3':
                rotate_img = cv2.rotate(
                    img, cv2.cv2.ROTATE_90_COUNTERCLOCKWISE)

        return rotate_img
