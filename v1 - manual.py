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
    
    payload = {
        "text": "",
        "page": 1,
        "pageSize": 3,
        "sort": None,
        "filter": {
            "priceMin": 0,
            "priceMax": 1000000000,
            "rating": None,
            "brandIds": [],
            "mainCategoryIds": [],
            "vehicleId": "c5c80ff6-7302-4bc2-9aa2-0850d57a7294",
            "myGarageId": "",
            "categoryId": ""
        }
    }
    
    response = requests.post(url, headers=headers, json=payload)
    
    if response.status_code == 200:
        data = response.json()
        with open("scraped_data_test.json", "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        print("Data berhasil disimpan ke scraped_data_test.json")
    else:
        print(f"Gagal mengambil data! Status code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    scrape_data()
