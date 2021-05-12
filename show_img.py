import cv2

img = cv2.imread('image/IMG_0001.JPG', cv2.IMREAD_ANYCOLOR)

# import resize


height, width, channel = img.shape
print(height)
print(width)
print(channel)
cv2.imshow("img", img)
#
cv2.waitKey()
cv2.destoryAllWindows()
