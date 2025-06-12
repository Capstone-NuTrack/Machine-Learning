# NuTrack - Machine Learning

Repositori ini berisi semua model dan kode machine learning yang digunakan dalam proyek NuTrack. Proyek ini bertujuan untuk menyediakan solusi cerdas terkait kesehatan dan gizi, mencakup klasifikasi penyakit, perhitungan skor kesehatan, rekomendasi nutrisi, dan pemindaian komposisi produk melalui OCR.

## 📜 Daftar Isi

- [Fitur Utama](#-fitur-utama)
- [Struktur Proyek](#📁-struktur-proyek)
- [Model](#-model)
- [Envy](#-teknologi-yang-digunakan)
- [Instalasi](#️-instalasi)
- [Penggunaan](#️-penggunaan)

## ✨ Fitur Utama

- **Klasifikasi Penyakit**: Memprediksi potensi penyakit berdasarkan riwayat konsumsi makanan dan nutrisi.
- **Perhitungan Skor Kesehatan**: Menghitung skor kesehatan pengguna (1-10) berdasarkan asupan nutrisi harian.
- **Rekomendasi Nutrisi**: Memberikan rekomendasi makanan berdasarkan skor kesehatan dan kebutuhan nutrisi pengguna.
- **Deteksi Komposisi Produk (OCR)**: Memindai dan mengenali teks komposisi pada label produk makanan.

## 📁 Struktur Proyek

```
.
├── Dataset/
│   ├── Dataset_Klasifikasi_Penyakit/
│   ├── Dataset_Klasifikasi_Skor_Kesehatan/
│   └── ...
├── Model Klasifikasi Penyakit/
│   ├── Code.ipynb
│   ├── best_multilabel_keras_model.keras
│   └── *.joblib
├── Model OCR/
│   ├── recognizer_finetuned_weights.h5
├── Model Recommendation/
│   ├── Code.ipynb
│   ├── logika_rekomendasi.py
│   └── rekomendasi_gizi.joblib
├── Pemrosesan OCR Dataset/
│   ├── main.py
│   └── *.py
├── Fungsi Skor Kesehatan.py
├── LICENSE
└── README.md
```

- ``: Berisi semua dataset yang digunakan untuk melatih dan menguji model.
- ``: Model untuk mengklasifikasikan penyakit. `best_multilabel_keras_model.keras` adalah model utama.
- ``: Model untuk mengenali teks. `recognizer_finetuned_weights.h5` berisi bobot dari model yang telah dilatih.
- ``: Model untuk memberikan rekomendasi gizi.
- ``: Skrip untuk memproses dan menyiapkan dataset OCR.
- ``: Berisi fungsi rule-based untuk menghitung skor kesehatan pengguna.

## 🤖 Model

Proyek ini terdiri dari empat komponen pemodelan utama:

1. **Model Klasifikasi Penyakit**

   - **Fungsi**: Menganalisis data asupan makanan untuk memprediksi risiko penyakit secara multilabel.
   - **Metode**: Jaringan Saraf Tiruan (Deep Learning).
   - **Arsitektur**: Model sekuensial yang dibangun dengan Keras.
   - **File Penting**: `best_multilabel_keras_model.keras`, `feature_columns.joblib`, `mlb_binarizer.joblib`, `scaler.joblib`.

2. **Model Rekomendasi Gizi**

   - **Fungsi**: Memberikan rekomendasi produk makanan berdasarkan data kesehatan pengguna.
   - **Metode**: Rule Based Optimization System.
   - **File Penting**: `rekomendasi_gizi.joblib`, `logika_rekomendasi.py`.

3. **Model OCR**

   - **Fungsi**: Mendeteksi dan mengekstrak teks dari gambar label komposisi produk.
   - **Metode**: Deep Learning untuk Optical Character Recognition.
   - **Arsitektur**: Model OCR Keras yang di-fine-tune, dengan bobot disimpan di `recognizer_finetuned_weights.h5`.

4. **Fungsi Skor Kesehatan**

   - **Fungsi**: Menghitung skor kesehatan harian (skala 1–10) berdasarkan input kalori, protein, lemak, karbohidrat, dan serat, yang dibandingkan dengan standar Angka Kecukupan Gizi (AKG).
   - **Metode**: **Rule-Based System**. 
   - **File Penting**: `Fungsi Skor Kesehatan.py`.

## 💻 Envy

- **Python**: Bahasa pemrograman utama.
- **TensorFlow/Keras**: Untuk membangun dan melatih model deep learning (Klasifikasi Penyakit & OCR).
- **Scikit-learn**: Untuk prapemrosesan data dan membangun model machine learning klasik.
- **Pandas & NumPy**: Untuk manipulasi dan analisis data.
- **Joblib**: Untuk menyimpan dan memuat objek Python (model, scaler).
- **Jupyter Notebook**: Untuk eksplorasi data dan pengembangan model.

## ⚙️ Instalasi

1. **Clone repositori:**

   ```sh
   git clone https://github.com/Capstone-NuTrack/Machine-Learning.git
   cd Machine-Learning
   ```

2. **Buat dan aktifkan virtual environment (disarankan):**

   ```sh
   python -m venv venv
   source venv/bin/activate  # Untuk Linux/macOS
   .\venv\Scripts\activate  # Untuk Windows
   ```

3. **Instal dependensi yang dibutuhkan:**

   Buat file `requirements.txt` dengan isi seperti:

   ```txt
   tensorflow
   scikit-learn
   pandas
   numpy
   keras
   ```

   Kemudian jalankan:

   ```sh
   pip install -r requirements.txt
   ```

## ▶️ Penggunaan

Setiap komponen memiliki cara penggunaan yang berbeda. Pastikan Anda berada di direktori yang sesuai.

**Contoh menggunakan Fungsi Skor Kesehatan:**

```python
from Fungsi_Skor_Kesehatan import infer_health_score_p_w

# Hitung skor untuk seorang wanita berumur 25 tahun
score = infer_health_score_p_w(
    age=25,
    gender='female',
    energy_kcal=2000,
    protein_g=50,
    fat_g=60,
    carb_g=300,
    fiber_g=28
)

print(f"Skor Kesehatan Anda: {score}/10")
```

