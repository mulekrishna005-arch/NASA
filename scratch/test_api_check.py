import urllib.request
import json

def test():
    req1 = urllib.request.urlopen('http://localhost:8000/api/countries')
    countries = json.loads(req1.read().decode())['countries']
    print(f"Countries loaded: {len(countries)}")
    for c in countries[:4]:
        print(f"  {c['code']}: {c['name']} (bbox: {c['bbox']})")

    req2 = urllib.request.urlopen('http://localhost:8000/api/regions?country=AUS')
    regions = json.loads(req2.read().decode())['regions']
    print(f"Australia regions: {len(regions)}")
    for r in regions:
        print(f"  {r['id']}: {r['name']} ({r['lat']}, {r['lon']})")

    req3 = urllib.request.urlopen('http://localhost:8000/api/firms-country?country=AUS&sensor=VIIRS_NOAA21_NRT&days=1')
    fire_aus = json.loads(req3.read().decode())
    print(f"Australia active fire pixels: {fire_aus.get('count', 0)}")

    req4 = urllib.request.urlopen('http://localhost:8000/api/agent-predict?country=AUS&sensor=VIIRS_NOAA21_NRT')
    pred_aus = json.loads(req4.read().decode())
    print(f"Australia prediction success: {pred_aus.get('success')}")
    print(f"Primary predicted target: {pred_aus.get('primary_predicted_target', {}).get('location_name')}")

if __name__ == '__main__':
    test()
