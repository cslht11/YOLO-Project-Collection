from ultralytics import YOLO
import os

os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'


def main():
    model = YOLO(r'D:\A_Python\YOLO_RAW\ultralytics-main\runs\detect\train\weights\best.pt')  # load a custom model

    # Validate the model
    metrics = model.val()  # no arguments needed, dataset and settings remembered
    metrics.box.map  # map50-95
    metrics.box.map50  # map50
    metrics.box.map75  # map75
    metrics.box.maps  # a list contains map50-95 of each category


if __name__ == '__main__':
    main()
