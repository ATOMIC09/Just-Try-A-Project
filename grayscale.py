import cv2

img = cv2.imread("napha.jpg",cv2.IMREAD_GRAYSCALE)
cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('result_grayscale.jpg',img)