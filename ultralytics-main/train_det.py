from ultralytics import YOLO
import os
os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'


def main():
    model = YOLO('data/yolov8l.yaml')
    # model = YOLO("weight/yolov8s.pt")  # 加载预训练模型（推荐用于训练）
    results = model.train(data="data/my_data.yaml", imgsz=640, epochs=200, batch=4, device=0, workers=0, patience=50)


if __name__ == '__main__':
    main()
