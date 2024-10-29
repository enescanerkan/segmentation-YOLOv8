import os

# Görüntülerin bulunduğu dizin
input_dir = r"C:\Users\Monster\Desktop\block\duplicated_images"
# Yeniden adlandırılmış görüntülerin kaydedileceği dizin
output_dir = r"C:\Users\Monster\Desktop\block\data"

# Çıktı dizinini oluştur
os.makedirs(output_dir, exist_ok=True)

# Görüntü numarası için sayaç
image_counter = 1

# Görüntüleri yeniden adlandır
for filename in os.listdir(input_dir):
    if filename.endswith(".jpeg") or filename.endswith(".jpg"):
        img_path = os.path.join(input_dir, filename)

        # Yeni dosya adını oluştur
        new_img_path = os.path.join(output_dir, f"{image_counter}.jpeg")

        # Görüntüyü yeni adla kaydet
        os.rename(img_path, new_img_path)

        # Sayaçı artır
        image_counter += 1

print("Tüm görüntüler yeniden adlandırıldı ve kaydedildi.")
