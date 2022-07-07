# Rumah.com-Web-Scraping-with-Python
Scraping information from Rumah.com with several filters and parsers using Python programming language

# Attributes to be scraped:
1. Property Name (Nama Properti)
2. Property Price (Harga Properti)
3. Number of bedrooms (Jumlah Kamar Tidur)
4. Number of bathrooms (Jumlah Kamar Mandi)
5. Price per meter squared (Harga per meter persegi)
6. Property Type (Tipe Properti)
7. Property's Land Area (Luas Tanah Properti)
8. Property's Building Area (Luas Bangunan Properti)
8. Property's Interior (Interior Properti)
9. Number of Floors (Jumlah Lantai)
10. Parking Spaces (Jumlah Tempat Parkir)
11. Property's Year of Construction (Tahun Konstruksi Properti)
12. Property's Listing Date (Tanggal Listing Properti)
13. Property's Latitude (Latitude Properti)
14. Property's Longitude (Longitude Properti)
15. Property's Developer (Pengembang Properti)
16. URL to Property's Page (URL Properti)

# The following is the filter for the property type and information. Only properties that match the filter will be scraped.
1. Listed on the website in the last month
2. Is a house (not apartment or any other type of property)
3. Is located in either of the following districts:
- Kecamatan Cakung
- Kecamatan Kelapa Gading
- Kecamatan Cilincing

# Notes about Output
1. Format listing dan pembangunan dalam DATETIME
2. Kalau N/A, ganti jadi NULL atau kosong
3. Deskripsi buang headernya
4. Interior ambil opsi yang lebih atas
5. Harga per meter pakai angka aja
6. Per kecamatan dipisah