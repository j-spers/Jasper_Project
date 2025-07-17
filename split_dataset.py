import os
import shutil
import random
from pathlib import Path

input_dir = "dataset"  # points to the dataset folder you showed
output_dir = "."       # save splits into current folder
split_ratio = (0.7, 0.15, 0.15)
emotion_classes = ["Angry", "Happy", "Neutral", "Sad", "Surprise"]

for split in ["train", "val", "test"]:
    for emotion in emotion_classes:
        os.makedirs(os.path.join(output_dir, split, emotion), exist_ok=True)

for emotion in emotion_classes:
    class_path = os.path.join(input_dir, emotion)
    images = list(Path(class_path).glob("*.jpg")) + \
             list(Path(class_path).glob("*.jpeg")) + \
             list(Path(class_path).glob("*.png"))

    random.shuffle(images)
    total = len(images)

    if total == 0:
        print(f"⚠️ No images found in: {class_path}")
        continue

    n_train = int(split_ratio[0] * total)
    n_val = int(split_ratio[1] * total)

    train_imgs = images[:n_train]
    val_imgs = images[n_train:n_train + n_val]
    test_imgs = images[n_train + n_val:]

    for split, img_list in zip(["train", "val", "test"], [train_imgs, val_imgs, test_imgs]):
        for img in img_list:
            dest = os.path.join(output_dir, split, emotion, img.name)
            shutil.copy(img, dest)

print("✅ Dataset split complete!")
