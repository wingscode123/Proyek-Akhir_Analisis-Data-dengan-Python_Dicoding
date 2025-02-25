import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Identitas
st.sidebar.title("📌 Proyek Akhir Analisis Data dengan Python")
st.sidebar.write("**Nama:** Radithya Fawwaz Aydin")
st.sidebar.write("🔗 [LinkedIn](https://www.linkedin.com/in/radithya-fawwaz-/)")
st.sidebar.write("🐙 [GitHub](https://github.com/wingscode123)")

# Load data
df_cleaned = pd.read_csv("Dashboard/customers_dataset_v2_cleaned.csv", parse_dates=["order_purchase_timestamp"])

# Sidebar - Filtering berdasarkan rentang tanggal
st.sidebar.header("🗓️ Filter Berdasarkan Rentang Tanggal")
start_date = st.sidebar.date_input("Tanggal Mulai", df_cleaned["order_purchase_timestamp"].min().date())
end_date = st.sidebar.date_input("Tanggal Akhir", df_cleaned["order_purchase_timestamp"].max().date())

# Sidebar - Filtering berdasarkan provinsi
states = df_cleaned["customer_state"].unique()
selected_state = st.sidebar.multiselect("Pilih Provinsi", options=states, default=states)

# Filter data berdasarkan input pengguna
df_filtered = df_cleaned[
    (df_cleaned["order_purchase_timestamp"].dt.date >= start_date) &
    (df_cleaned["order_purchase_timestamp"].dt.date <= end_date) &
    (df_cleaned["customer_state"].isin(selected_state))
]

# Analisis Pelanggan yang Kembali Bertransaksi
repeat_customers = df_filtered["customer_unique_id"].value_counts()
repeat_count = (repeat_customers > 1).sum()
unique_customers = repeat_customers.count()
repeat_percentage = (repeat_count / unique_customers) * 100 if unique_customers > 0 else 0

# Analisis Distribusi Pelanggan Berdasarkan Kota
top_cities = df_filtered["customer_city"].value_counts().head(10)

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

# Visualisasi 2: Distribusi Pelanggan Berdasarkan Kota
st.subheader("2️⃣ Distribusi Pelanggan Berdasarkan Kota")
fig2, ax2 = plt.subplots(figsize=(10, 6))
sns.barplot(x=top_cities.values, y=top_cities.index, palette="coolwarm", ax=ax2)
ax2.set_xlabel("Jumlah Pelanggan")
ax2.set_ylabel("Kota")
ax2.set_title("Distribusi Pelanggan Berdasarkan Kota (Top 10)")
st.pyplot(fig2)

# Kesimpulan
st.subheader("📝 Kesimpulan")
st.write("✅ **Retensi pelanggan cukup rendah**, jadi strategi seperti program loyalitas bisa diterapkan.")
st.write("✅ **São Paulo masih menjadi pasar utama**, namun penting untuk memonitor tren di provinsi lain.")

st.success("Dashboard ini kini memiliki fitur filter berdasarkan tanggal dan provinsi untuk eksplorasi lebih mendalam!")
