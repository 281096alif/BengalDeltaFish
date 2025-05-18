import cv2
import matplotlib.pyplot as plt
import os

# Sample paths (update with your actual paths)
image_path = 'dataset/train/iamges/IMG_0081_jpg.rf.8221e6799bc530d454e9e4e97ef3ed1b.jpg'
annotation_path = 'dataset/train/labels/IMG_0081_jpg.rf.8221e6799bc530d454e9e4e97ef3ed1b.txt'

# Optional: class names (update as needed)
class_names = {
    9:'Kayakanta'
}

# Read image
image = cv2.imread(image_path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
h, w, _ = image.shape

# Read annotation file
with open(annotation_path, 'r') as f:
    lines = f.readlines()

for line in lines:
    parts = line.strip().split()
    class_id = int(parts[0])
    x_center = float(parts[1]) * w
    y_center = float(parts[2]) * h
    box_width = float(parts[3]) * w
    box_height = float(parts[4]) * h

    xmin = int(x_center - box_width / 2)
    ymin = int(y_center - box_height / 2)
    xmax = int(x_center + box_width / 2)
    ymax = int(y_center + box_height / 2)

    label = class_names[class_id] if class_id < len(class_names) else str(class_id)
    cv2.rectangle(image, (xmin, ymin), (xmax, ymax), (255, 0, 0), 2)
    cv2.putText(image, label, (xmin, max(ymin-10, 0)), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255,0,0), 2)

plt.imshow(image)
plt.axis('off')
plt.show()