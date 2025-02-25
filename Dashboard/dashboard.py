import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime

# Identitas
st.sidebar.title("📌 Proyek Akhir Analisis Data dengan Python")
st.sidebar.write("**Nama:** Radithya Fawwaz Aydin")
st.sidebar.write("🔗 [LinkedIn](https://www.linkedin.com/in/radithya-fawwaz-/)")
st.sidebar.write("🐙 [GitHub](https://github.com/wingscode123)")

# Load data dengan path yang sesuai
df_cleaned = pd.read_csv("Dashboard/customers_dataset_v2_cleaned.csv")

# Konversi kolom tanggal ke format datetime
df_cleaned['order_purchase_timestamp'] = pd.to_datetime(df_cleaned['order_purchase_timestamp'])

# Sidebar - Filtering Data
st.sidebar.header("🔍 Filter Data")

# Filter berdasarkan rentang tanggal
date_min = df_cleaned['order_purchase_timestamp'].min().date()
date_max = df_cleaned['order_purchase_timestamp'].max().date()
selected_date = st.sidebar.date_input("Pilih Rentang Tanggal", (date_min, date_max), date_min, date_max)
df_filtered = df_cleaned[(df_cleaned['order_purchase_timestamp'].dt.date >= selected_date[0]) &
                         (df_cleaned['order_purchase_timestamp'].dt.date <= selected_date[1])]

# Filter berdasarkan kategori produk
product_categories = df_cleaned['product_category_name'].unique()
selected_category = st.sidebar.multiselect("Pilih Kategori Produk", product_categories, product_categories)
df_filtered = df_filtered[df_filtered['product_category_name'].isin(selected_category)]

# Filter berdasarkan state
states = df_cleaned['customer_state'].unique()
selected_state = st.sidebar.multiselect("Pilih State", states, states)
df_filtered = df_filtered[df_filtered['customer_state'].isin(selected_state)]

# Analisis Pelanggan yang Kembali Bertransaksi
repeat_customers = df_filtered["customer_unique_id"].value_counts()
repeat_count = (repeat_customers > 1).sum()
unique_customers = repeat_customers.count()
repeat_percentage = (repeat_count / unique_customers) * 100

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
st.write("\n📌 **Mayoritas pelanggan hanya bertransaksi sekali**, menunjukkan bahwa retensi pelanggan cukup rendah. Program loyalitas bisa menjadi solusi!")

# Visualisasi 2: Distribusi Pelanggan Berdasarkan Kota
st.subheader("2️⃣ Distribusi Pelanggan Berdasarkan Kota")
fig2, ax2 = plt.subplots(figsize=(10, 6))
sns.barplot(x=top_cities.values, y=top_cities.index, palette="coolwarm", ax=ax2)
ax2.set_xlabel("Jumlah Pelanggan")
ax2.set_ylabel("Kota")
ax2.set_title("Distribusi Pelanggan Berdasarkan Kota (Top 10)")
st.pyplot(fig2)

st.write("📌 **Kota dengan pelanggan terbanyak bisa menjadi target utama pemasaran**")

# Kesimpulan
st.subheader("📝 Kesimpulan")
st.write("✅ **Retensi pelanggan cukup rendah**, jadi strategi seperti program loyalitas dan pemasaran ulang bisa diterapkan.")
st.write("✅ **Beberapa kota memiliki pelanggan lebih banyak**, bisa dijadikan prioritas dalam strategi pemasaran.")

st.success("Dashboard ini sekarang memiliki fitur interaktif yang memungkinkan eksplorasi lebih dalam!")
