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
  "Id": "6252001",
  "Code": "US",
  "languages": "en-US,es-US,haw,fr",
  "Name_EN": "United States",
  "Name_FA": "ایالات متحده امریکا",
  "Name_AR": "الاولايات المتحدة الامريكية",
  "PhoneCode": "1",
  "Latitude": 38.55309931506852,
  "Longitude": -90.55750630367564
}
```

#### `states.json`
```json
{
  "Id": "4155751",
  "Code": "US.FL",
  "CountryId": "6252001",
  "CountryCode": "US",
  "Name_EN": "Florida",
  "Name_FA": "فلوریدا",
  "Name_AR": "فلوريدا",
  "Latitude": 27.976960150637286,
  "Longitude": -81.96234544611828
}
```

#### `cities.json`
```json
{
  "Id": "4145941",
  "StateId": "4155751",
  "StateCode": "US.FL",
  "CountryId": "6252001",
  "CountryCode": "US",
  "Name_EN": "Altamonte Springs",
  "Name_FA": "التامونت اسپرینگز، فلوریدا",
  "Name_AR": "التامونت سبرنغز",
  "Latitude": 28.66111,
  "Longitude": -81.36562,
  "TimeZone": "America/New_York"
}
```

---

## ▶️ How to Run

1. Make sure Python 3 is installed on your system.

2. Open terminal or CMD and navigate to the folder containing `app.py`.

3. Run the script using:

```bash
python app.py
```

4. Output files `countries.json`, `states.json`, and `cities.json` will be created in the same directory.

---

## 💬 Suggestions

- If you're interested in one specific country (like Iran), you can modify the script to filter only that country.
- If performance is a concern, use `cities15000.txt` for smaller and faster processing.

---

## 🧑‍💻 Author

This project was built by Farshid Amirkhani and is open for personal or organizational use.