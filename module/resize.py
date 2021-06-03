import cv2


class resize:
    def run(idx, img, file_name, _input):
        print("   -> Re Size")
        print(_input)

        if _input['type'] == '0':
            height, width, channel = img.shape
            print(" height : "+str(height)+" , "+_input['y'])
            print(" height : "+str(width)+" , "+_input['x'])
            if int(height) >= int(_input['y']) or int(width) >= int(_input['x']):
                resize_img = cv2.resize(img, dsize=(
                    int(_input['x']), int(_input['y'])), interpolation=cv2.INTER_AREA)
            else:
                print("[***]Image Size Error !")
        else:
            resize_img = cv2.resize(img, dsize=(
                0, 0), fx=float(_input['y']), fy=float(_input['y']), interpolation=cv2.INTER_LINEAR)

        return resize_img
