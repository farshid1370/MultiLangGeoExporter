# 🗺️ Extracting Countries, States, and Cities Data from GeoNames

This project extracts information about countries, states, and cities from GeoNames files and saves them in structured JSON format.

---

## 📥 Download GeoNames Data Files

This script processes GeoNames data files to generate JSON files for countries, states (admin1), and cities with translations in English, Persian (Farsi), and Arabic.

### Required Data Files

Download and place the following files in the same folder as `App.py`:

- [countryInfo.txt](http://download.geonames.org/export/dump/countryInfo.txt)
- [admin1CodesASCII.txt](http://download.geonames.org/export/dump/admin1CodesASCII.txt)
- [cities500.txt](http://download.geonames.org/export/dump/cities500.zip) (or any cities file)
- [alternateNamesV2.txt](http://download.geonames.org/export/dump/alternateNamesV2.zip)

### How It Works

- Loads alternate names from `alternateNamesV2.txt` for Persian (`fa`) and Arabic (`ar`).
- Reads countries from `countryInfo.txt`, applying translations and fixing phone codes and timezone for Iran.
- Reads states from `admin1CodesASCII.txt` and links them to countries.
- Reads cities from `cities500.txt` and links them to states.
- Calculates average latitude and longitude for states and countries based on cities and states respectively.
- Outputs JSON files: `countries.json`, `states.json`, and `cities.json`.




### ⚖️ Difference Between `cities500.txt` and `cities15000.txt`

| File               | Min Population | Approx Size | Description |
|--------------------|----------------|-------------|-------------|
| `cities500.txt`    | 500            | ~20MB       | Includes most towns, cities, and even large villages |
| `cities15000.txt`  | 15000          | ~3MB        | Only includes large and highly populated cities |

> If you want more comprehensive data (e.g., for Iran), use `cities500.txt`.

---

## 🧾 Output Format

Three JSON files will be generated:

- `countries.json` ✅ Country information
- `states.json` ✅ States or provinces
- `cities.json` ✅ Cities

### JSON Structure:

#### `countries.json`
```json
{
  "Id": "GUID",
  "Name_EN": "Iran",
  "Name_FA": "ایران",
  "Name_AR": "إيران",
  "TimeZone": "Asia/Tehran",
  "PhoneCode": "98",
  "Latitude": 32.0,
  "Longitude": 53.0
}
```

#### `states.json`
```json
{
  "Id": "GUID",
  "Name_EN": "Tehran",
  "Name_FA": "تهران",
  "Name_AR": "طهران",
  "CountryId": "GUID of the country",
  "Latitude": 35.6892,
  "Longitude": 51.3890
}
```

#### `cities.json`
```json
{
  "Id": "GUID",
  "Name_EN": "Shiraz",
  "Name_FA": "شیراز",
  "Name_AR": "شيراز",
  "StateId": "GUID of the state",
  "Latitude": 29.5918,
  "Longitude": 52.5836
}
```

---

## ▶️ How to Run

1. Make sure Python 3 is installed on your system.

2. Open terminal or CMD and navigate to the folder containing `app.py`.

3. Run the script using:

```bash
python App.py
```

4. Output files `countries.json`, `states.json`, and `cities.json` will be created in the same directory.

---

## 💬 Suggestions

- If you're interested in one specific country (like Iran), you can modify the script to filter only that country.
- If performance is a concern, use `cities15000.txt` for smaller and faster processing.

---

## 🧑‍💻 Author

This project was built by Farshid and is open for personal or organizational use.