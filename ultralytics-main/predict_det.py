import cv2
from ultralytics import YOLO

weight = r'D:\A_Python\ultralytics-main\runs\detect\train\weights\best.pt'
source = r'D:\A_Python\yolov5-6.1_qrcode\imgs\2.bmp'


model = YOLO(weight)  # load an official model
results = model(source)  # predict on an image

res_plotted = results[0].plot()
cv2.imshow("result", res_plotted)
cv2.waitKey(0)
