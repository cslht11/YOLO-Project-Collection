# YOLO 目标检测项目集合

> 本仓库包含多个 YOLO 系列目标检测模型的源码和工具，涵盖 YOLOv3、YOLOv5、YOLOv7、YOLOv8 等主流版本。

---

## 📁 项目结构

```
YOLO_RAW/
├── README.md                 # 本文件
├── draw_pic.py               # 绘制 PR/F1/P/R 曲线工具
├── draw_result.py            # 检测结果可视化工具
├── data/                     # 数据集（⚠️ 未包含在 Git 中）
│   ├── images/               # 训练图像
│   ├── labels/               # YOLO 格式标签
│   └── ImageSets/            # 训练/验证集划分
├── eva_img/                  # 训练结果可视化图像
│   ├── pr.png                # PR 曲线
│   ├── F1.png                # F1 分数曲线
│   ├── mAP50.png             # mAP@50 曲线
│   ├── mAP50-95.png          # mAP@50-95 曲线
│   └── loss.png              # 损失函数曲线
├── ultralytics-main/         # YOLOv8 (Ultralytics 官方版本)
├── yolov3-9.6.0/             # YOLOv3 (v9.6.0)
├── yolov5-7.0/               # YOLOv5 (v7.0 官方版本)
├── yolov7-main/              # YOLOv7 (官方版本)
└── yolov7-ours/              # YOLOv7 (改进版本) ⭐
```

---

## 🚀 各版本简介

### 1. YOLOv8 (ultralytics-main)

**最新版本，功能最全面**

- **特性**: 支持检测、分割、分类、姿态估计
- **框架**: PyTorch + Ultralytics
- **优势**: 易用性强，API 简洁，支持多种导出格式
- **文档**: https://docs.ultralytics.com/

**快速开始**:
```bash
cd ultralytics-main
pip install -r requirements.txt
pip install ultralytics

# 使用 Python API
from ultralytics import YOLO
model = YOLO("yolov8n.pt")
model.train(data="coco128.yaml", epochs=3)
```

### 2. YOLOv5 (yolov5-7.0)

**最成熟的版本，生产环境首选**

- **版本**: v7.0 (支持分割)
- **特性**: 稳定、文档齐全、社区活跃
- **优势**: 部署方案成熟，支持多种后端
- **权重**: 自动下载或从 [releases](https://github.com/ultralytics/yolov5/releases) 获取

**快速开始**:
```bash
cd yolov5-7.0
pip install -r requirements.txt

# 训练
python train.py --data coco128.yaml --weights yolov5s.pt --epochs 100

# 检测
python detect.py --weights yolov5s.pt --source 0
```

### 3. YOLOv7 (yolov7-main)

**精度和速度平衡**

- **论文**: [YOLOv7: Trainable bag-of-freebies](https://arxiv.org/abs/2207.02696)
- **优势**: 在 5FPS-160FPS 范围内 SOTA
- **AP**: 51.4% (YOLOv7), 53.1% (YOLOv7-X)

**性能对比**:
| Model | Size | AP<sup>test</sup> | FPS |
|-------|------|-------------------|-----|
| YOLOv7 | 640 | 51.4% | 161 |
| YOLOv7-X | 640 | 53.1% | 114 |
| YOLOv7-W6 | 1280 | 54.9% | 84 |

### 4. YOLOv7 改进版 (yolov7-ours) ⭐

**本项目的改进版本**

- 基于官方 YOLOv7 改进
- 包含自定义修改和优化
- 训练结果保存在 `runs/` 目录

**与官方版本对比**:
```bash
# 使用 draw_pic.py 对比性能
python ../draw_pic.py
```

### 5. YOLOv3 (yolov3-9.6.0)

**经典版本，适合学习**

- **版本**: v9.6.0
- **特点**: 结构简单，适合入门学习
- **用途**: 教学、baseline 对比

---

## 📊 训练结果

训练结果可视化图像保存在 [`eva_img/`](./eva_img/) 目录：

| 图像 | 说明 |
|------|------|
| `pr.png` | Precision-Recall 曲线 |
| `F1.png` | F1 分数曲线 |
| `mAP50.png` | mAP@0.5 曲线 |
| `mAP50-95.png` | mAP@0.5:0.95 曲线 |
| `P.png` | Precision 曲线 |
| `R.png` | Recall 曲线 |
| `loss.png` | 训练损失曲线 |

---

## 🛠️ 工具脚本

### draw_pic.py

绘制 YOLOv7 官方版本与改进版本的性能对比图：

```bash
python draw_pic.py
```

生成图像：
- `pr.png` - PR 曲线对比
- `F1.png` - F1 曲线对比
- `P.png` - Precision 曲线对比
- `R.png` - Recall 曲线对比

### draw_result.py

检测结果可视化工具（具体功能见源码）。

---

## 📦 环境配置

### 通用依赖

```bash
# Python >= 3.8
# PyTorch >= 1.8
# CUDA 11.0+ (推荐 GPU 训练)
```

### 各版本依赖

**YOLOv8**:
```bash
cd ultralytics-main
pip install ultralytics
```

**YOLOv5**:
```bash
cd yolov5-7.0
pip install -r requirements.txt
```

**YOLOv7**:
```bash
cd yolov7-main
pip install -r requirements.txt
```

---

## 📚 数据集说明

### ⚠️ 重要提示

**本仓库不包含数据集文件**，因为数据集体积过大（通常数十 GB）。

### 数据集位置

训练数据位于 `data/` 目录：
```
data/
├── images/          # 训练图像
├── labels/          # YOLO 格式标签 (.txt)
└── ImageSets/       # 训练集/验证集划分
```

### 准备数据集

1. **使用公开数据集**:
   - COCO: https://cocodataset.org/
   - VOC: http://host.robots.ox.ac.uk/pascal/VOC/
   - 自定义数据集需转换为 YOLO 格式

2. **YOLO 格式标签**:
   ```
   <object-class> <x_center> <y_center> <width> <height>
   ```
   - 坐标归一化到 [0, 1]
   - 每个图像对应一个 `.txt` 文件

3. **数据集配置文件**:
   修改各项目 `data/` 目录下的 `.yaml` 文件，指定：
   ```yaml
   train: /path/to/data/images/train
   val: /path/to/data/images/val
   nc: 80  # 类别数
   names: ['class1', 'class2', ...]
   ```

---

## 🔬 改进版 YOLOv7 (yolov7-ours)

### 改进内容

（在此处描述你的具体改进，例如：）
- 修改了 backbone 结构
- 优化了损失函数
- 添加了注意力机制
- 改进了数据增强策略

### 训练配置

```bash
cd yolov7-ours

# 单 GPU 训练
python train.py --data data/custom.yaml --weights yolov7.pt --epochs 300 --batch-size 16 --img 640

# 多 GPU DDP 训练
python -m torch.distributed.run --nproc_per_node 4 --master_port 9527 train.py --weights yolov7.pt --data data/custom.yaml --batch-size 64
```

### 性能对比

| Model | mAP@50 | mAP@50-95 | FPS |
|-------|--------|-----------|-----|
| YOLOv7 (官方) | XX.X% | XX.X% | XXX |
| YOLOv7 (ours) | XX.X% | XX.X% | XXX |

---

## 📝 使用指南

### 1. 快速体验

```bash
# 使用 YOLOv8（最简单）
cd ultralytics-main
pip install ultralytics

python -c "from ultralytics import YOLO; m = YOLO('yolov8n.pt'); m.predict(source='https://ultralytics.com/images/bus.jpg')"
```

### 2. 训练自定义数据集

```bash
# 1. 准备数据（YOLO 格式）
# 2. 修改 data/custom.yaml
# 3. 开始训练
cd yolov5-7.0
python train.py --data data/custom.yaml --weights yolov5s.pt --epochs 100
```

### 3. 模型导出

```bash
# YOLOv5 导出 ONNX
python export.py --weights yolov5s.pt --include onnx

# YOLOv8 导出多种格式
yolo export model=yolov8n.pt format=onnx
```

---

## 🎓 学习资源

- **YOLOv8 文档**: https://docs.ultralytics.com/
- **YOLOv5 文档**: https://github.com/ultralytics/yolov5
- **YOLOv7 论文**: https://arxiv.org/abs/2207.02696
- **Papers With Code**: https://paperswithcode.com/sota/real-time-object-detection-on-coco

---

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

---

## 📄 许可证

- **ultralytics-main**: AGPL-3.0 / 商业许可
- **yolov5-7.0**: AGPL-3.0 / 商业许可
- **yolov7-main**: GPL-3.0
- **yolov7-ours**: （根据你的需求选择）

---

## 📧 联系方式

- GitHub: [@chai1110](https://github.com/chai1110)
- Email: chai011379@gmail.com

---

<div align="center">

**如果这个项目对你有帮助，请给一个 ⭐ Star！**

</div>
