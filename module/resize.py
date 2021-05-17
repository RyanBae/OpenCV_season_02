import cv2


class resize:
    def run(idx, img, file_name, _input):
        print("   -> Re Size")
        print(_input)

        if _input['type'] == '0':
            resize_img = cv2.resize(img, dsize=(
                int(_input['y']), int(_input['x'])), interpolation=cv2.INTER_AREA)
        else:
            resize_img = cv2.resize(img, dsize=(
                0, 0), fx=float(_input['y']), fy=float(_input['y']), interpolation=cv2.INTER_LINEAR)

        return resize_img
