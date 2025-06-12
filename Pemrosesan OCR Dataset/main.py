import os
from PIL import Image
import config
from donut_model_handler import DonutModelHandler
from text_detector_cropper import TextDetectorCropper

def run_ocr_preprocessing():
    donut_handler = DonutModelHandler()
    if donut_handler.model is None:
        print("Gagal memuat model Donut. Proses dihentikan.")
        return

    text_detector = TextDetectorCropper()

    if not os.path.exists(config.FULL_LABEL_IMAGE_DIR):
        print(f"Error: Direktori gambar tidak ditemukan: {config.FULL_LABEL_IMAGE_DIR}")
        return

    all_images = [os.path.join(config.FULL_LABEL_IMAGE_DIR, f)
                  for f in os.listdir(config.FULL_LABEL_IMAGE_DIR)
                  if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    if not all_images:
        print(f"Tidak ada gambar ditemukan di {config.FULL_LABEL_IMAGE_DIR}")
        return

    num_to_process = len(all_images)
    if config.MAX_FULL_IMAGES_TO_PROCESS:
        num_to_process = min(num_to_process, config.MAX_FULL_IMAGES_TO_PROCESS)
        print(f"Memproses {num_to_process} gambar (batasi MAX_FULL_IMAGES_TO_PROCESS).")

    images_for_training = []
    pseudo_labels = []

    for i, img_path in enumerate(all_images[:num_to_process]):
        print(f"[{i+1}/{num_to_process}] Memproses: {os.path.basename(img_path)}")
        crops = text_detector.get_cropped_text_images(img_path)
        for crop_np, _ in crops:
            try:
                img = Image.fromarray(crop_np)
                label = donut_handler.generate_pseudo_label(img)
                if label and "ERROR" not in label:
                    images_for_training.append(crop_np)
                    pseudo_labels.append(label)
                else:
                    print(f"  Skip: label tidak valid ('{label}')")
            except Exception as e:
                print(f"  Error proses crop: {e}")

    print(f"Selesai preprocessing: {len(images_for_training)} sampel berhasil dibuat.")

    return images_for_training, pseudo_labels

if __name__ == '__main__':
    run_ocr_preprocessing()
