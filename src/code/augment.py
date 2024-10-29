import os
from PIL import Image

# Görüntülerin bulunduğu dizin
input_dir = r"C:\Users\Monster\Desktop\block\images"
# Çoğaltılan görüntülerin kaydedileceği dizin
output_dir = r"C:\Users\Monster\Desktop\block\duplicated_images"

# Çıktı dizinini oluştur
os.makedirs(output_dir, exist_ok=True)

# 1'den 39'a kadar olan açılar
angles = [i for i in range(40)]  # 0, 1, 2, ..., 39

# Görüntüleri işle
for filename in os.listdir(input_dir):
    if filename.endswith(".jpeg") or filename.endswith(".jpg"):
        img_path = os.path.join(input_dir, filename)
        img = Image.open(img_path)

        # Orijinal görüntü kaydet
        original_img_path = os.path.join(output_dir, f"{os.path.splitext(filename)[0]}_original.jpeg")
        img.save(original_img_path)

        # Her açı için döndür ve flip uygula
        for angle in angles:
            # 1 derece döndür
            rotated_img = img.rotate(angle)

            # Döndürülmüş görüntüyü kaydet
            rotated_img_path = os.path.join(output_dir, f"{os.path.splitext(filename)[0]}_rotated_{angle}.jpeg")
            rotated_img.save(rotated_img_path)

            # Yatay flip
            horizontal_flip = rotated_img.transpose(method=Image.FLIP_LEFT_RIGHT)
            horizontal_flip_path = os.path.join(output_dir, f"{os.path.splitext(filename)[0]}_horizontal_flip_rotated_{angle}.jpeg")
            horizontal_flip.save(horizontal_flip_path)

            # Dikey flip
            vertical_flip = rotated_img.transpose(method=Image.FLIP_TOP_BOTTOM)
            vertical_flip_path = os.path.join(output_dir, f"{os.path.splitext(filename)[0]}_vertical_flip_rotated_{angle}.jpeg")
            vertical_flip.save(vertical_flip_path)

            # Hem yatay hem dikey flip
            both_flip = rotated_img.transpose(method=Image.FLIP_LEFT_RIGHT).transpose(method=Image.FLIP_TOP_BOTTOM)
            both_flip_path = os.path.join(output_dir, f"{os.path.splitext(filename)[0]}_both_flip_rotated_{angle}.jpeg")
            both_flip.save(both_flip_path)

print("Tüm görüntüler döndürüldü ve flip işlemleri uygulandı, kaydedildi.")
