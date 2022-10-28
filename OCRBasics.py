import easyocr
import cv2
from matplotlib import pyplot as plt
import numpy as np

IMAGE_PATH = 'Test\EasyOCR\studentCard.jpg'

reader = easyocr.Reader(['vi'])
result = reader.readtext(IMAGE_PATH)
# print(result)
for line in result:
        print(line[1])