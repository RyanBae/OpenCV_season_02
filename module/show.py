import cv2


class show:
    def run(idx, img, file_name):
        print("   -> Show")
        cv2.imshow("img_"+str(idx), img)

        return img


# if __name__ == '__main__':
    # show("test", "test", "test")
