# Simple Web Scraping & JSON to CSV Converter

## 📌 Deskripsi
Proyek ini merupakan kombinasi dari web scraping API Astra OtoShop dan konversi data hasil scraping dari JSON ke format CSV. Proses ini mencakup pengambilan data menggunakan metode POST, menyimpan hasil dalam file JSON, serta mengonversinya menjadi file CSV agar lebih mudah diolah dan dianalisis.

## ⚙️ Fitur
- Melakukan web scraping menggunakan API Astra OtoShop.
- Menyimpan data hasil scraping dalam format JSON.
- Mengonversi data JSON menjadi CSV dengan ekspansi data nested.
- Menangani data produk beserta media, atribut, dan kategori terkait.

## 🚀 Tahapan Proses
### 1️⃣ Web Scraping dengan Python
Skrip ini mengambil data produk dari API Astra OtoShop dengan metode POST dan menyimpan hasilnya dalam file `output.json`.

#### 🔹 Endpoint API:
```
https://api.astraotoshop.com/v1/product-service/search/v2
```
#### 🔹 Headers:
```json
{
  "accept": "application/json",
  "content-type": "application/json",
  "origin": "https://astraotoshop.com",
  "referer": "https://astraotoshop.com/",
  "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}
```

#### 🔹 Body Request:
```json
{
  "text": "",
  "page": 1,
  "pageSize": 2207,
  "sort": null,
  "filter": {
    "priceMin": 0,
    "priceMax": 1000000000,
    "vehicleId": "c5c80ff6-7302-4bc2-9aa2-0850d57a7294"
  }
}
```

### 2️⃣ Menyimpan Hasil Scraping ke JSON
Setelah request berhasil, data akan disimpan ke dalam file `output.json` untuk diproses lebih lanjut.

### 3️⃣ Konversi JSON ke CSV
Skrip Python membaca `output.json`, mengekstrak data utama serta informasi nested seperti `product_media`, `attribute_detail`, dan `product_categories`, kemudian menyimpannya dalam `output.csv` dengan format yang lebih terstruktur.

## 📂 Struktur Data JSON
```json
{
    "data": [
        {
            "id": "uuid",
            "name": "Nama Produk",
            "price": 100000,
            "product_media": [
                {"url": "https://example.com/image1.jpg", "is_main": true},
                {"url": "https://example.com/image2.jpg", "is_main": false}
            ],
            "attribute_detail": [
                {"name": "Warna", "value": "Merah"},
                {"name": "Ukuran", "value": "L"}
            ],
            "product_categories": [
                {"categories_name": "Ban Mobil"},
                {"categories_name": "Aksesoris Kendaraan"}
            ]
        }
    ]
}
```

## 📂 Format CSV yang Dihasilkan
```csv
id,name,price,media_url_main,media_url_secondary,attribute_warna,attribute_ukuran,category_1,category_2
uuid,Nama Produk,100000,https://example.com/image1.jpg,https://example.com/image2.jpg,Merah,L,Ban Mobil,Aksesoris Kendaraan
```

## 🔧 Cara Menggunakan
### 1️⃣ Instalasi
Pastikan Python telah terinstal, lalu instal dependensi:
```sh
pip install requests pandas
```

### 2️⃣ Jalankan Web Scraping
```sh
python scrape_api.py
```
Ini akan menghasilkan file `output.json` yang berisi data produk.

### 3️⃣ Konversi JSON ke CSV
```sh
python convert_json_to_csv.py output.json output.csv
```
Dimana:
- `output.json` adalah file hasil scraping.
- `output.csv` adalah file hasil konversi.

## 📌 Catatan Tambahan
- Jika ada lebih dari satu item dalam array `product_media`, `attribute_detail`, atau `product_categories`, data akan di-duplikasi di CSV untuk mempertahankan struktur yang jelas.
- Pastikan file JSON memiliki format yang sesuai agar tidak terjadi error dalam konversi.

## 📜 Lisensi
Proyek ini dilisensikan di bawah MIT License - silakan lihat file `LICENSE` untuk detail lebih lanjut.

