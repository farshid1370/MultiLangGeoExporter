import os
import json
import unicodedata
from collections import defaultdict

# Helpers
def remove_diacritics(text):
    return ''.join(c for c in unicodedata.normalize('NFD', text) if unicodedata.category(c) != 'Mn')

def parse_alternate_names(file_path):
    name_map = defaultdict(dict)
    with open(file_path, encoding='utf-8') as f:
        for line in f:
            parts = line.strip().split('\t')
            if len(parts) < 4:
                continue
            geonameid, lang, name = parts[1], parts[2], parts[3]
            if lang in ['fa', 'ar'] and lang not in name_map[geonameid]:
                name_map[geonameid][lang] = remove_diacritics(name)
    return name_map

# Load translations
alt_names = parse_alternate_names("alternateNames.txt")

# Step 1: Countries
countries = {}
country_id_map = {}
with open("countryInfo.txt", encoding='utf-8') as f:
    for line in f:
        if line.startswith('#'): continue
        parts = line.strip().split('\t')
        if len(parts) < 17: continue
        iso = parts[0]
        name_en = parts[4]
        phone_code = parts[12]
        culture = parts[15]
        geonameid = parts[16]
        country_id_map[iso] = geonameid
        countries[iso] = {
            "Id": str(geonameid),
            "Code": iso,
            "Cultures": culture,
            "Name_EN": name_en,
            "Name_FA": alt_names.get(geonameid, {}).get('fa') or "",
            "Name_AR": alt_names.get(geonameid, {}).get('ar') or "",
            "PhoneCode": phone_code,
            "Latitude": 0,
            "Longitude": 0,
        }

# Step 2: States
states = {}
state_id_map = {}
with open("admin1CodesASCII.txt", encoding='utf-8') as f:
    for line in f:
        parts = line.strip().split('\t')
        if len(parts) < 4: continue
        code = parts[0]  # e.g., IR.07
        name_en = parts[1]
        geonameid = parts[3]
        country_iso, state_code = code.split('.')
        country_id = country_id_map.get(country_iso)
        if not country_id: continue
        state_id_map[code] = geonameid
        states[code] = {
            "Id": str(geonameid),
            "Code": code,
            "CountryId": str(country_id),
            "CountryCode": country_iso,
            "Name_EN": name_en,
            "Name_FA": alt_names.get(geonameid, {}).get('fa') or "",
            "Name_AR": alt_names.get(geonameid, {}).get('ar') or "",
            "Latitude": 0,
            "Longitude": 0
        }

# Step 3: Cities
cities = []
state_coords = defaultdict(list)
country_coords = defaultdict(list)

with open("cities500.txt", encoding='utf-8') as f:
    for line in f:
        parts = line.strip().split('\t')
        if len(parts) < 19: continue
        geonameid = parts[0]
        name_en = parts[2]
        lat = float(parts[4])
        lon = float(parts[5])
        country_iso = parts[8]
        admin1 = parts[10]
        timezone = parts[17]
        code = f"{country_iso}.{admin1}"
        country_id = country_id_map.get(country_iso)
        state_id = state_id_map.get(code)
        if not state_id: continue

        city = {
            "Id": str(geonameid),
            "StateId": str(state_id),
            "StateCode": code,
            "CountryId": str(country_id),
            "CountryCode": country_iso,
            "Name_EN": name_en,
            "Name_FA": alt_names.get(geonameid, {}).get('fa') or "",
            "Name_AR": alt_names.get(geonameid, {}).get('ar') or "",
            "Latitude": lat,
            "Longitude": lon,
            "TimeZone": timezone
        }
        cities.append(city)
        state_coords[code].append((lat, lon))
        country_coords[country_iso].append((lat, lon))

# Step 4: Average lat/lon for states and countries
for code, coords in state_coords.items():
    if code in states:
        lats, lons = zip(*coords)
        states[code]["Latitude"] = sum(lats) / len(lats)
        states[code]["Longitude"] = sum(lons) / len(lons)

for iso, coords in country_coords.items():
    if iso in countries:
        lats, lons = zip(*coords)
        countries[iso]["Latitude"] = sum(lats) / len(lats)
        countries[iso]["Longitude"] = sum(lons) / len(lons)

# Step 5: Write JSON files
OUTPUT_DIR = "jsonFiles"
os.makedirs(OUTPUT_DIR, exist_ok=True)
with open(os.path.join(OUTPUT_DIR,"countries.json"), "w", encoding='utf-8') as f:
    json.dump(list(countries.values()), f, ensure_ascii=False, indent=2)

with open(os.path.join(OUTPUT_DIR,"states.json"), "w", encoding='utf-8') as f:
    json.dump(list(states.values()), f, ensure_ascii=False, indent=2)

with open(os.path.join(OUTPUT_DIR,"cities.json"), "w", encoding='utf-8') as f:
    json.dump(cities, f, ensure_ascii=False, indent=2)

print("Done.")
