import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Identitas
st.sidebar.title("📌 Proyek Akhir Analisis Data dengan Python")
st.sidebar.write("**Nama:** Radithya Fawwaz Aydin")
st.sidebar.write("🔗 [LinkedIn](https://www.linkedin.com/in/radithya-fawwaz-/)")
st.sidebar.write("🐙 [GitHub](https://github.com/wingscode123)")

# Load data (gunakan df_cleaned yang sudah diproses sebelumnya)
df_cleaned = pd.read_csv("Dashboard\customers_dataset_v2_cleaned.csv")

# Analisis Pelanggan yang Kembali Bertransaksi
repeat_customers = df_cleaned["customer_unique_id"].value_counts()
repeat_count = (repeat_customers > 1).sum()
unique_customers = repeat_customers.count()
repeat_percentage = (repeat_count / unique_customers) * 100

# Analisis Distribusi Pelanggan Berdasarkan Kota
top_cities = df_cleaned["customer_city"].value_counts().head(10)

# Streamlit UI
st.title("📊 Dashboard Analisis Data Pelanggan")

# Visualisasi 1: Proporsi Pelanggan Baru vs Berulang
st.subheader("1️⃣ Proporsi Pelanggan Baru vs Pelanggan Berulang")
fig1, ax1 = plt.subplots()
labels = ["Pelanggan Baru", "Pelanggan Berulang"]
sizes = [unique_customers - repeat_count, repeat_count]
colors = ["#66b3ff", "#ff9999"]
ax1.pie(sizes, labels=labels, autopct="%1.1f%%", colors=colors, startangle=140, wedgeprops={"edgecolor": "black"})
ax1.set_title("Proporsi Pelanggan Baru vs Pelanggan Berulang")
st.pyplot(fig1)

st.write(f"- **Total Pelanggan Unik:** {unique_customers}")
st.write(f"- **Pelanggan Berulang:** {repeat_count} ({repeat_percentage:.2f}%)")
st.write("\n📌 **Mayoritas pelanggan hanya bertransaksi sekali (96.88%)**, menunjukkan bahwa retensi pelanggan cukup rendah. Program loyalitas bisa menjadi solusi!")

# Visualisasi 2: Distribusi Pelanggan Berdasarkan Kota
st.subheader("2️⃣ Distribusi Pelanggan Berdasarkan Kota")
fig2, ax2 = plt.subplots(figsize=(10, 6))
sns.barplot(x=top_cities.values, y=top_cities.index, palette="coolwarm", ax=ax2)
ax2.set_xlabel("Jumlah Pelanggan")
ax2.set_ylabel("Kota")
ax2.set_title("Distribusi Pelanggan Berdasarkan Kota (Top 10)")
st.pyplot(fig2)

st.write("📌 **São Paulo memiliki jumlah pelanggan terbanyak (15.540 pelanggan)**, menjadikannya pasar utama. Rio de Janeiro, Belo Horizonte, dan Brasília juga memiliki potensi besar untuk pemasaran lebih lanjut.")

# Kesimpulan
st.subheader("📝 Kesimpulan")
st.write("✅ **Retensi pelanggan cukup rendah (3.12%)**, jadi strategi seperti program loyalitas dan pemasaran ulang bisa diterapkan.")
st.write("✅ **São Paulo adalah pasar utama**, dengan pelanggan terbanyak, sehingga bisa menjadi prioritas dalam strategi pemasaran.")
st.write("✅ **Kota besar lainnya seperti Rio de Janeiro dan Belo Horizonte juga potensial**, jadi bisa menjadi target ekspansi berikutnya.")

st.success("Dashboard ini membantu dalam memahami pola belanja pelanggan dan menemukan peluang bisnis lebih lanjut!")