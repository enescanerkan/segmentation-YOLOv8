import os
import random
import shutil

# Dosya yolları
image_dir = r"C:\Users\Monster\Desktop\block\data\images"
label_dir = r"C:\Users\Monster\Desktop\block\data\labels"
train_image_dir = r"C:\Users\Monster\Desktop\block\data\train\images"
train_label_dir = r"C:\Users\Monster\Desktop\block\data\train\labels"
val_image_dir = r"C:\Users\Monster\Desktop\block\data\val\images"
val_label_dir = r"C:\Users\Monster\Desktop\block\data\val\labels"

# Yüzde oranları
train_ratio = 0.8

# Klasörlerin var olup olmadığını kontrol edip oluşturma
os.makedirs(train_image_dir, exist_ok=True)
os.makedirs(train_label_dir, exist_ok=True)
os.makedirs(val_image_dir, exist_ok=True)
os.makedirs(val_label_dir, exist_ok=True)

# Tüm görüntü dosyalarını al
all_images = [f for f in os.listdir(image_dir) if f.endswith('.jpg') or f.endswith('.jpeg') or f.endswith('.png')]

# Karıştır ve böl
random.shuffle(all_images)
train_size = int(len(all_images) * train_ratio)
train_images = all_images[:train_size]
val_images = all_images[train_size:]


# Train ve val için görüntü ve etiket dosyalarını taşıma
def move_files(image_list, src_image_dir, src_label_dir, dest_image_dir, dest_label_dir):
    for image in image_list:
        label = image.replace('.jpg', '.txt').replace('.jpeg', '.txt').replace('.png', '.txt')

        # Dosya yolları
        src_image_path = os.path.join(src_image_dir, image)
        src_label_path = os.path.join(src_label_dir, label)
        dest_image_path = os.path.join(dest_image_dir, image)
        dest_label_path = os.path.join(dest_label_dir, label)

        # Taşıma işlemi
        if os.path.exists(src_image_path) and os.path.exists(src_label_path):
            shutil.move(src_image_path, dest_image_path)
            shutil.move(src_label_path, dest_label_path)


# Train dosyalarını taşı
move_files(train_images, image_dir, label_dir, train_image_dir, train_label_dir)

# Val dosyalarını taşı
move_files(val_images, image_dir, label_dir, val_image_dir, val_label_dir)

print(f"{len(train_images)} görüntü train klasörüne taşındı.")
print(f"{len(val_images)} görüntü val klasörüne taşındı.")
