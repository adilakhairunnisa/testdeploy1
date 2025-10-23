import streamlit as st
import gdown
import tensorflow as tf
import os

st.title("Model Deployment - Adila Khairunnisa")

# Link model di Google Drive (ubah ID sesuai punyamu)
model_url = "https://drive.google.com/uc?id=1_mZejUH6zjWZ1_5rwS7qSBnBtaZ7IbbY"
model_path = "Adilakhairunnisa_Laporan2.h5"

# Cek apakah file model sudah ada, kalau belum, unduh dulu
if not os.path.exists(model_path):
    with st.spinner("Mengunduh model dari Google Drive..."):
        gdown.download(model_url, model_path, quiet=False)
    st.success("Model berhasil diunduh!")

# Coba load model
try:
    model = tf.keras.models.load_model(model_path)
    st.success("Model berhasil dimuat!")
except Exception as e:
    st.error(f"Gagal memuat model: {e}")

st.write("Model siap digunakan untuk prediksi 🚀")
