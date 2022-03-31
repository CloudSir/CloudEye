# CloudEye
[简体中文](README.md) | English (coming soon)


CloudEye，一个玩具级的Python计算机视觉库。

## 快速开始

### 1. 安装

```bash
pip3 install cloudeye==0.0.3
```

### 2. 识别手势

**使用opencv**

```python
import cloudeye
import cv2

img = cv2.imread("test.jpg")

classification = cloudeye.gesture.classification()

classification.init(print_info=True)
hand = classification.classify(img=img, score_threshold=0.5)

if not hand == -1: 
	print("手势：", hand)
else:
    print("未知手势")
```

**直接调用**

```python
import cloudeye

classification = cloudeye.gesture.classification()

classification.init(print_info=True)
hand = classification.classify(img="test.jpg", score_threshold=0.5)

if not hand == -1: 
	print("手势：", hand)
else:
    print("未知手势")
```

## API接口说明

### cloudeye.gesture

> 手势识别接口。

**cloudeye.gesture.classification**

```pytho
cloudeye.gesture.classification()
```

手势分类器。

**cloudeye.classification.init**

```python
cloudeye.classification.init(print_info=True)
```

初始化手势分类器。

- 参数
  - print_info: 是否输出初始化时的信息

**cloudeye.classification.classify**

```python
cloudeye.classification.classify(img, score_threshold=0.5)
```

从图片中获取手势。

- 参数

  - img: 图片文件路径或numpy数组(HWC排列，BGR格式，opencv读取的图片默认是这种格式)。
  - score_threshold: 置信度，大于置信度的预测结果会被返回，否则认为是未知手势。

- 返回结果

  - -1: 未知手势。
  - 0 - 9: 分别对应10种手势。

  | 数字 |           手势           |
  | :--: | :----------------------: |
  |  0   | ![](./images/hand_0.JPG) |
  |  1   | ![](./images/hand_1.JPG) |
  |  2   | ![](./images/hand_2.JPG) |
  |  3   | ![](./images/hand_3.JPG) |
  |  4   | ![](./images/hand_4.JPG) |
  |  5   | ![](./images/hand_5.JPG) |
  |  6   | ![](./images/hand_6.JPG) |
  |  7   | ![](./images/hand_7.JPG) |
  |  8   | ![](./images/hand_8.JPG) |
  |  9   | ![](./images/hand_9.JPG) |
