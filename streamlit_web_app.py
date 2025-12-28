import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("💄 Make Up Insight Dashboard")

st.header("Tren dan Informasi Produk Make Up")
st.subheader("Analisis Produk Make Up Populer")

st.text(
    "Make up adalah bagian dari industri kecantikan yang digunakan "
    "untuk mempercantik wajah dan meningkatkan rasa percaya diri."
)

st.caption("Dashboard Make Up menggunakan Streamlit")

data = {
    "Produk Make Up": ["Foundation", "Lipstik", "Bedak", "Maskara", "Blush On"],
    "Kategori": ["Base", "Lips", "Face", "Eyes", "Cheeks"],
    "Pengguna (%)": [85, 90, 78, 70, 65]
}

df = pd.DataFrame(data)

st.subheader("📋 Tabel Produk Make Up")
st.dataframe(df)

st.subheader("💻 Contoh Potongan Kode")
st.code("""
produk_terpopuler = df.loc[df["Pengguna (%)"].idxmax()]
print(produk_terpopuler)
""", language="python")

st.subheader("📊 Grafik Popularitas Produk")

fig, ax = plt.subplots()
ax.bar(df["Produk Make Up"], df["Pengguna (%)"])
ax.set_xlabel("Produk")
ax.set_ylabel("Pengguna (%)")
ax.set_title("Popularitas Produk Make Up")

st.pyplot(fig)
