import os
import shutil
import numpy as np

def split_data(image_dir, label_dir, train_image_dir, val_image_dir, train_label_dir, val_label_dir, split_size=0.8):
    if not os.path.exists(train_image_dir):
        os.makedirs(train_image_dir)
    if not os.path.exists(val_image_dir):
        os.makedirs(val_image_dir)
    if not os.path.exists(train_label_dir):
        os.makedirs(train_label_dir)
    if not os.path.exists(val_label_dir):
        os.makedirs(val_label_dir)

    # Список изображений
    images = [f for f in os.listdir(image_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    np.random.shuffle(images)
    split = int(len(images) * split_size)

    train_files = images[:split]
    val_files = images[split:]

    # Копирование изображений и меток в соответствующие директории
    for f in train_files:
        shutil.copy(os.path.join(image_dir, f), train_image_dir)
        label_file = f.replace(f.split('.')[-1], 'txt')
        label_path = os.path.join(label_dir, label_file)
        if os.path.exists(label_path):
            shutil.copy(label_path, train_label_dir)

    for f in val_files:
        shutil.copy(os.path.join(image_dir, f), val_image_dir)
        label_file = f.replace(f.split('.')[-1], 'txt')
        label_path = os.path.join(label_dir, label_file)
        if os.path.exists(label_path):
            shutil.copy(label_path, val_label_dir)

# Определите пути к директориям
image_dir = 'C:/Users/Андрей/PycharmProjects/AITurkey/YOLOTEST/Apple__black_rot'
label_dir = 'C:/Users/Андрей/PycharmProjects/AITurkey/YOLOTEST/labels_my-project-name_2024-04-15-10-02-14'
train_image_dir = 'C:/Users/Андрей/PycharmProjects/AITurkey/YOLOTEST/images/train'
val_image_dir = 'C:/Users/Андрей/PycharmProjects/AITurkey/YOLOTEST/images/val'
train_label_dir = 'C:/Users/Андрей/PycharmProjects/AITurkey/YOLOTEST/labels/train'
val_label_dir = 'C:/Users/Андрей/PycharmProjects/AITurkey/YOLOTEST/labels/val'

split_data(image_dir, label_dir, train_image_dir, val_image_dir, train_label_dir, val_label_dir)
