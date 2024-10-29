# segmentation-YOLOv8
This project segments and counts industrial metal materials, like plates and blocks, using data augmentation and YOLOv8 model training. With 200 images, it aims to identify and quantify these materials, underscoring the importance of diverse datasets for industrial applications.
# Metal Material Segmentation and Counting Project (Metal Malzeme Segmentasyonu ve Sayımı Projesi)

This project aims to experiment with the segmentation and counting of industrial metal materials such as metal plates, blocks, and metal sheets. (Bu proje, endüstride kullanılan metal plakalar, bloklar ve metal saç gibi malzemelerin segmentasyon ve sayımı denemesini amaçlamaktadır.)

## Dataset Generation (Veri Seti Oluşturulması)

Initially, only 3 images were available, so data augmentation was performed to expand the dataset. (Başlangıçta yalnızca 3 görüntü mevcuttu, bu nedenle veri setini genişletmek için veri çoğaltma uygulandı.) The images were first flipped, and each flipped image was then rotated by certain degrees to create additional images. (Görüntüler önce çevrilmiş, ardından belirli derecelerde döndürülerek yeni görüntüler oluşturulmuştur.) A total of 200 images were considered sufficient for this experiment. (Toplam 200 görüntü bu deneme için yeterli görülmüştür.)

## Images 

![1](https://github.com/user-attachments/assets/af804f43-a2bb-42d9-b762-4e069708e107)
![2](https://github.com/user-attachments/assets/69f19510-9fa8-4eb4-a144-2bbf81e2c81c)
![3](https://github.com/user-attachments/assets/3c37cdfa-df10-4795-ade8-0162a2bae88d)


## Labeling and Annotation (Etiketleme ve Anotasyon)

Images were annotated in polygon format using CVAT.AI, a tool chosen for its user-friendly interface and AI-assisted segmentation capabilities, which simplified the labeling process. (Görüntüler, kullanıcı dostu arayüzü ve yapay zeka destekli segmentasyon özellikleri nedeniyle tercih edilen CVAT.AI uygulaması kullanılarak poligon formatında etiketlenmiştir.) 

## Labeled Images

![Ekran görüntüsü 2024-10-23 114724](https://github.com/user-attachments/assets/fbccabed-226e-4980-98f2-ff6d5052cf1e)
![Ekran görüntüsü 2024-10-24 111305](https://github.com/user-attachments/assets/3d0aa26b-2a1a-419f-b236-aff274374ac4)


## Model Training (Model Eğitimi)

The augmented dataset, along with the labeled annotations, was used to train a YOLOv8 segmentation model (middle model variant) for 200 epochs. (Çoğaltılmış veri seti ve etiketlenmiş anotasyonlar, YOLOv8 segmentasyon modeli (orta model varyantı) ile 200 epoch boyunca eğitildi.) During training, it was observed that continuously rotating and augmenting the same 3 images led to overfitting. (Eğitim sırasında, aynı 3 görüntünün sürekli döndürülüp çoğaltılmasının aşırı öğrenmeye yol açtığı gözlemlendi.) This suggests that a more diverse dataset could improve the model's performance in future experiments. (Bu durum, gelecekteki deneylerde daha çeşitli bir veri setinin model performansını artırabileceğini önermektedir.)

## Code and Directory Structure (Kod ve Dizin Yapısı)

Within the `src/code` folder, you will find the following scripts: (src/code klasörünün içinde aşağıdaki scriptler bulunur:)
- **Augmentation Code (Çoğaltma Kodu):** Generates augmented images by flipping and rotating the original images. (Orijinal görüntüleri çevirerek ve döndürerek çoğaltılmış görüntüler oluşturur.)
- **Data Split Code (Veri Bölme Kodu):** Splits the dataset into 80% for training and 20% for validation. (Veri setini %80 eğitim ve %20 doğrulama olarak böler.)
- **Prediction Script (Tahmin Scripti):** Uses the trained model to predict and test on the test images with weights obtained from training. (Eğitimden elde edilen ağırlıkları kullanarak test görüntüleri üzerinde tahmin yapar.)
- **Rename Script (İsim Değiştirme Scripti):** Renames images for easier reference and organization. (Görüntülerin daha kolay referans alınıp düzenlenmesi için isimlerini değiştirir.)
- **Train Settings:** The training was conducted on Google Colab. For details on training settings, please refer to the training_colab.ipynb file inside the src folder.(Eğitim Google Colab üzerinden gerçekleştirilmiştir. Eğitim ayarlarıyla ilgili ayrıntılar için src klasörünün içindeki training_colab.ipynb dosyasına bakabilirsiniz.)

## Results (Sonuçlar)

- The `tested_images` folder contains test images that were processed by the model. (Test edilmiş görüntülerin bulunduğu `tested_images` klasörü.)
- The `result_images` folder holds training images with segmentation outputs, where the model detected metal blocks. (Modelin metal blokları tespit ettiği segmentasyon çıktılarıyla eğitim görüntülerini içeren `result_images` klasörü.)

## Future Work (Gelecek Çalışmalar)

Given the results, it’s anticipated that a dataset with more variety in images could reduce overfitting and yield more robust results for industrial material counting and segmentation. (Sonuçlara göre, daha çeşitli görüntülere sahip bir veri setinin aşırı öğrenmeyi azaltabileceği ve endüstriyel malzeme sayımı ve segmentasyonu için daha sağlam sonuçlar verebileceği öngörülmektedir.)

---

