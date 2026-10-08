import json
import pycountry
from pathlib import Path

fixture = []

for pk, country in enumerate(pycountry.countries, start=1):
    fixture.append({
        "model": "taller.pais",
        "pk": pk,
        "fields": {
            "nombre": country.name,
            "nacionalidad": "",
            "iso_2": country.alpha_2,
            "iso_3": country.alpha_3
        }
    })

script_dir = Path(__file__).parent.resolve() 
real_file_path = script_dir / "data_paises.json"

with open(real_file_path, "w", encoding="utf-8") as f:
    json.dump(fixture, f, ensure_ascii=False, indent=4)
    
    print(fixture)