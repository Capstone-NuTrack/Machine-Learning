import pytesseract
from PIL import Image
import os
import cv2
import numpy as np

class TesseractOCRHandler:
    def __init__(self, language='eng', default_config='--oem 1 --psm 7'):
        self.language = language
        self.default_config = default_config
        print(f"Tesseract OCR Handler diinisialisasi dengan bahasa: {self.language}, config default: '{self.default_config}'")
        try:
            version = pytesseract.get_tesseract_version()
            print(f"Versi Tesseract yang terdeteksi: {version}")
        except Exception as e:
            print(f"Peringatan: Tidak dapat memverifikasi versi Tesseract. Error: {e}")

    def _preprocess_for_numbers(self, image_pil: Image.Image) -> Image.Image:
        try:
            open_cv_image = np.array(image_pil.convert('L'))
            h, w = open_cv_image.shape[:2]
            if h < 40:
                scale_factor = max(1, 40 / h)
                open_cv_image = cv2.resize(open_cv_image, (int(w * scale_factor), int(h * scale_factor)), interpolation=cv2.INTER_CUBIC)
            threshed_img = cv2.adaptiveThreshold(open_cv_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                                 cv2.THRESH_BINARY, 11, 2)
            return Image.fromarray(threshed_img)
        except Exception as e_preprocess:
            print(f"  Error saat preprocessing: {e_preprocess}. Menggunakan gambar asli.")
            return image_pil

    def generate_pseudo_label(self, image_crop_pil: Image.Image, custom_config: str = None, preprocess_for_numbers: bool = False) -> str:
        if not isinstance(image_crop_pil, Image.Image):
            print("Error: Input bukan objek PIL Image yang valid.")
            return "ERROR_INVALID_IMAGE_INPUT"

        img_to_process = self._preprocess_for_numbers(image_crop_pil) if preprocess_for_numbers else image_crop_pil
        current_config = custom_config if custom_config is not None else self.default_config

        try:
            text = pytesseract.image_to_string(img_to_process, lang=self.language, config=current_config)
            cleaned_text = text.strip()
            if not cleaned_text:
                return ""
            return cleaned_text
        except pytesseract.TesseractNotFoundError:
            print("CRITICAL ERROR: Tesseract executable tidak ditemukan.")
            return "ERROR_TESSERACT_NOT_FOUND"
        except Exception as e:
            print(f"Error saat inferensi Tesseract (config: '{current_config}'): {e}")
            return "ERROR_TESSERACT_INFERENCE"
