import pandas as pd
import numpy as np

# 1. Baca data (PERBAIKAN NAMA FILE)
data = pd.read_csv("c:/Users/Qia/Downloads/calon_tni - titanic.csv.csv")

print("=== Data Calon TNI ===")
# Gunakan to_string() untuk memastikan semua baris ditampilkan (seperti yang diminta)
print(data.to_string())

# 2. Melihat informasi struktur dataset
print("\n=== Info Dataset ===")
data.info() # df.info() tidak perlu di print() lagi

# 3. Statistik dasar (PERBAIKAN NAMA KOLOM: 'Tinggi')
print("\n=== Statistik Tinggi Badan ===")
print(data['Tinggi'].describe().to_string())

# 4. Deteksi masalah data & Imputasi
print("\n=== Cek Missing Values ===")
print(data.isnull().sum())

print("\n=== Cek Data Duplikat ===")
print(data.duplicated().sum())

# pengecekan jika ada nilai kosong di kolom Tinggi
if data['Tinggi'].isnull().sum() > 0:
    rata2_imputasi = data['Tinggi'].mean()
    data['Tinggi'].fillna(rata2_imputasi, inplace=True)
    print(f"\nNilai kosong pada kolom Tinggi telah diganti dengan rata-rata: {rata2_imputasi:.2f}")
else:
    print("\nTidak ada data kosong yang perlu diimputasi.")

print("\n=== Data Setelah Imputasi ===")
print(data.to_string())


# 5. Analisis Tinggi & Handling Outlier (Menampilkan Rata-rata, Tertinggi, dll.)
rata2_tinggi = data['Tinggi'].mean()
tertinggi = data['Tinggi'].max()
terendah = data['Tinggi'].min()
median = data['Tinggi'].median()

print(f"\nRata-rata tinggi : {rata2_tinggi:.2f} cm")
print(f"Tertinggi        : {tertinggi} cm")
print(f"Terendah         : {terendah} cm")
print(f"Median           : {median:.1f} cm")


# 6. Calon di atas rata-rata tinggi
rata2 = data["Tinggi"].mean()
print("\n=== Calon di atas rata-rata tinggi ===")
# PERBAIKAN NAMA KOLOM: 'Nama', 'Alamat', 'Tinggi'
print(data[data["Tinggi"] > rata2][["Nama", "Alamat", "Tinggi"]].to_string())

# 7. Urutan dari Tertinggi ke Terendah
print("\n=== Urutan dari Tertinggi ke Terendah ===")
urut = data.sort_values(by="Tinggi", ascending=False)
# PERBAIKAN NAMA KOLOM: 'Nama', 'Alamat', 'Tinggi'
print(urut[["Nama", "Alamat", "Tinggi"]].to_string())

# 8. Tambah kategori tinggi (Disempurnakan agar sesuai output di PDF)
def kategori_tinggi(x):
    # Disesuaikan agar 180 masuk Tinggi, 178 masuk Sedang (sesuai hasil analisis sebelumnya)
    if x >= 180:
        return "Tinggi"
    elif 170 <= x <= 179: # Diubah range-nya agar 178 masuk Sedang
        return "Sedang"
    else: # x < 170
        return "Pendek"

data["kategori"] = data["Tinggi"].apply(kategori_tinggi)

print("\n=== Data dengan Kategori ===")
print(data.to_string())

# 9. Jumlah per kategori & Statistik Lanjutan
print("\n=== Jumlah Calon per Kategori ===")
print(data["kategori"].value_counts().to_string())

# Statistik lanjutan (Menggunakan ddof=1 untuk sample std/var, sesuai default Pandas)
std_dev = data["Tinggi"].std()
varian = data["Tinggi"].var()

print("\n=== Statistik Lanjutan ===")
print(f"Standar Deviasi : {std_dev:.2f}")
print(f"Variansi        : {varian:.2f}")

# 10. Calon dengan tinggi tertinggi
tertinggi = data.loc[data["Tinggi"].idxmax()]
# PERBAIKAN NAMA KOLOM: 'Nama', 'Alamat', 'Tinggi'
print("\n=== Calon dengan Tinggi Badan Tertinggi ===")
print(f"Nama   : {tertinggi['Nama']}")
print(f"Alamat : {tertinggi['Alamat']}")
print(f"Tinggi : {tertinggi['Tinggi']} cm")