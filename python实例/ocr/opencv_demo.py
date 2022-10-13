import cv2

rgb_img = cv2.imread('resource/yuan.jpg')
# print(rgb_img.shape)
# print(rgb_img[0,0]) # 像素(0,0)的值RGB
# print(rgb_img[0,0,2])
gray_img = cv2.cvtColor(rgb_img,cv2.COLOR_RGB2GRAY)
reverse_img = 255-gray_img
cv2.imshow('reverse_img',reverse_img)