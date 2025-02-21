import requests
import json

def scrape_data():
    url = "https://api.astraotoshop.com/v1/product-service/search/v2"
    
    headers = {
        "accept": "application/json",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "undefined",
        "content-type": "application/json",
        "origin": "https://astraotoshop.com",
        "referer": "https://astraotoshop.com/",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"
    }
    
    # Input dari pengguna
    page_size = int(input("Masukkan jumlah data per halaman (pageSize): "))
    vehicle_id = input("Masukkan vehicleId: ")
    file_name = input("Masukkan nama file output (misal: output.json): ")
    
    payload = {
        "text": "",
        "page": 1,
        "pageSize": page_size,
        "sort": None,
        "filter": {
            "priceMin": 0,
            "priceMax": 1000000000,
            "rating": None,
            "brandIds": [],
            "mainCategoryIds": [],
            "vehicleId": vehicle_id,
            "myGarageId": "",
            "categoryId": ""
        }
    }
    
    response = requests.post(url, headers=headers, json=payload)
    
    if response.status_code == 200:
        data = response.json()
        with open(file_name, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        print(f"Data berhasil disimpan ke {file_name}")
    else:
        print(f"Gagal mengambil data! Status code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    scrape_data()
