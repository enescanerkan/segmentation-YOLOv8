from ultralytics import YOLO
import matplotlib.pyplot as plt
import cv2

# Modeli yükle
model_path = r"C:\Users\Monster\Desktop\üsamehoca\runs\content\runs\segment\blocks_segmentation\weights\best.pt"
model = YOLO(model_path)

# Test edilecek görüntü yolu
image_path = r"C:\Users\Monster\Desktop\üsamehoca\block\images1\1.jpeg"

# Görüntüyü model ile çalıştır
results = model(image_path)

# Segmentasyon maskeleri ile görüntüyü çiz ve numaralandır
for result in results:
    # Segmentasyon maskelerini görüntüye çizdir
    segmented_img = result.plot(show=False)  # Maskeyi çiz, show=False ile plt.imshow'a gönderilecek

    # Nesne numaralarını çiz
    for i, (box, mask) in enumerate(zip(result.boxes.xyxy, result.masks.data)):
        x1, y1, x2, y2 = map(int, box)  # Bbox koordinatları

        # Nesne numarasını ekle
        cv2.putText(segmented_img, f"{i + 1}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 10, (0, 0, 0), 20)

    # Son görüntüyü göster
    plt.imshow(segmented_img)
    plt.axis('off')
    plt.show()
