import json
import csv

def convert_json_to_csv(json_filename, csv_filename):
    try:
        # Load JSON data
        with open(json_filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        # Define field names
        fieldnames = [
            "id", "urlKey", "name", "isProductBundling", "isProductGroup", "productTypeId", "productType",
            "priceOriginal", "price", "availableQty", "discountPercentage", "brandId", "brandName", "currency",
            "isAstraotoservice", "isInsurance", "isMotoquick", "isFlashsale", "isSnd", "isVoucher", "mainCategoryID",
            "merchantId", "merchantName", "rating", "sku", "status", "stock_status", "total_sold", "updated_at", 
            "created_at", "remaining_stock", "stock", "periode_start", "periode_end"
        ]
        
        # Additional fields for nested arrays
        media_fields = ["media_id", "media_url", "media_alt_text", "media_type", "media_is_main"]
        attribute_fields = ["attribute_name", "attribute_value"]
        category_fields = ["category_id", "category_name"]
        
        # Extend fieldnames
        fieldnames.extend(media_fields + attribute_fields + category_fields)
        
        # Open CSV file for writing
        with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            
            for item in data.get("data", []):
                row = {key: item.get(key, "") for key in fieldnames if key not in media_fields + attribute_fields + category_fields}
                
                # Handle nested product_media (taking the first entry for simplicity)
                if item.get("product_media"):
                    media = item["product_media"][0]
                    row.update({
                        "media_id": media.get("id", ""),
                        "media_url": media.get("url", ""),
                        "media_alt_text": media.get("alt_text", ""),
                        "media_type": media.get("type", ""),
                        "media_is_main": media.get("is_main", "")
                    })
                
                # Handle nested attribute_detail (taking the first entry for simplicity)
                if item.get("attribute_detail"):
                    attribute = item["attribute_detail"][0]
                    row.update({
                        "attribute_name": attribute.get("name", ""),
                        "attribute_value": attribute.get("value", "")
                    })
                
                # Handle nested product_categories (taking the first entry for simplicity)
                if item.get("product_categories"):
                    category = item["product_categories"][0]
                    row.update({
                        "category_id": category.get("categories_id", ""),
                        "category_name": category.get("categories_name", "")
                    })
                
                writer.writerow(row)
        
        print(f"CSV file '{csv_filename}' has been created successfully!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    json_filename = input("Masukkan nama file JSON: ")
    csv_filename = input("Masukkan nama file CSV hasil konversi: ")
    convert_json_to_csv(json_filename, csv_filename)
