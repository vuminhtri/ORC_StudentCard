import cv2
import numpy as np

img1 = cv2.imread('assets\img\studentCard.jpg', 0)

# Sharpe
kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]]) #bo loc
sharpening = cv2.filter2D(img1, -1, kernel)
cv2.imwrite('result\img\studentCard(Sharpe).jpg', sharpening)

# Blur
# blurred_1 = cv2.blur(img1, (5, 5))
# cv2.imwrite('result\img\studentCard_small(Blur).jpg', blurred_1)

# cv2.imshow("orjinal", img1)
# cv2.imshow("Sharpe ", sharping)
# cv2.imshow("Blur ", blurred_1)
cv2.waitKey(0)
cv2.destroyAllWindows()