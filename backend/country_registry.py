"""
Global Country Registry and Geospatial Boundary Catalog
Contains ISO 3166-1 alpha-3 country metadata, bounding boxes, centroids,
and default environmental fire baselines for worldwide NASA FIRMS & Copernicus ingestion.
"""

GLOBAL_COUNTRIES = [
    {
        "code": "DEFAULT", "name": "Global Default (Neutral Earth - No Hotspots)", "continent": "Global",
        "bbox": "-180.0,-85.0,180.0,85.0", "lat": 20.00, "lon": 0.00, "zoom": 2,
        "fire_regions": ["Global Default (No Active Region)"],
        "default_ndvi": 0.50, "default_elevation_m": 0, "typical_cloud_fraction": 0.0
    },
    {
        "code": "USA", "name": "United States of America", "continent": "North America",
        "bbox": "-124.78,24.74,-66.95,49.38", "lat": 39.50, "lon": -98.35, "zoom": 4,
        "fire_regions": ["California Sierra Nevada", "Pacific Northwest", "Texas Panhandle", "Florida Pine Barrens"],
        "default_ndvi": 0.42, "default_elevation_m": 760, "typical_cloud_fraction": 0.28
    },
    {
        "code": "CAN", "name": "Canada", "continent": "North America",
        "bbox": "-141.00,41.68,-52.62,83.11", "lat": 56.13, "lon": -106.35, "zoom": 3,
        "fire_regions": ["British Columbia Interior", "Alberta Boreal Belt", "Northwest Territories Taiga"],
        "default_ndvi": 0.48, "default_elevation_m": 480, "typical_cloud_fraction": 0.42
    },
    {
        "code": "BRA", "name": "Brazil", "continent": "South America",
        "bbox": "-73.98,-33.75,-34.79,5.27", "lat": -14.24, "lon": -51.93, "zoom": 4,
        "fire_regions": ["Amazon Basin Arc of Deforestation", "Cerrado Savanna", "Pantanal Wetlands"],
        "default_ndvi": 0.65, "default_elevation_m": 320, "typical_cloud_fraction": 0.35
    },
    {
        "code": "AUS", "name": "Australia", "continent": "Oceania",
        "bbox": "113.34,-43.63,153.57,-10.67", "lat": -25.27, "lon": 133.78, "zoom": 4,
        "fire_regions": ["New South Wales Blue Mountains", "Victoria Alpine Basin", "Northern Territory Savanna", "Western Australia Bush"],
        "default_ndvi": 0.24, "default_elevation_m": 330, "typical_cloud_fraction": 0.18
    },
    {
        "code": "IND", "name": "India", "continent": "Asia",
        "bbox": "68.18,6.75,97.40,35.50", "lat": 20.59, "lon": 78.96, "zoom": 5,
        "fire_regions": ["Punjab & Haryana Agricultural Plains", "Madhya Pradesh Teak Forests", "Odisha Eastern Ghats"],
        "default_ndvi": 0.45, "default_elevation_m": 450, "typical_cloud_fraction": 0.30
    },
    {
        "code": "IDN", "name": "Indonesia", "continent": "Asia",
        "bbox": "95.01,-11.01,141.02,5.91", "lat": -0.79, "lon": 113.92, "zoom": 5,
        "fire_regions": ["Sumatra Peatland Corridor", "Kalimantan Tropical Rainforest", "Papua Lowlands"],
        "default_ndvi": 0.72, "default_elevation_m": 220, "typical_cloud_fraction": 0.55
    },
    {
        "code": "ESP", "name": "Spain", "continent": "Europe",
        "bbox": "-9.30,36.00,3.32,43.79", "lat": 40.46, "lon": -3.75, "zoom": 6,
        "fire_regions": ["Galicia Eucalyptus Forests", "Sierra de Gredos", "Andalusia Sierra Nevada", "Valencia Scrub"],
        "default_ndvi": 0.32, "default_elevation_m": 660, "typical_cloud_fraction": 0.22
    },
    {
        "code": "PRT", "name": "Portugal", "continent": "Europe",
        "bbox": "-9.53,36.96,-6.19,42.15", "lat": 39.40, "lon": -8.22, "zoom": 7,
        "fire_regions": ["Pedrógão Grande Basin", "Serra da Estrela", "Monchique Algarve"],
        "default_ndvi": 0.38, "default_elevation_m": 370, "typical_cloud_fraction": 0.25
    },
    {
        "code": "GRC", "name": "Greece", "continent": "Europe",
        "bbox": "19.37,34.80,28.24,41.75", "lat": 39.07, "lon": 21.82, "zoom": 6,
        "fire_regions": ["Attica Pine Forests", "Evia Island Ridge", "Peloponnese Maquis", "Rhodes Highlands"],
        "default_ndvi": 0.30, "default_elevation_m": 490, "typical_cloud_fraction": 0.19
    },
    {
        "code": "ITA", "name": "Italy", "continent": "Europe",
        "bbox": "6.63,35.49,18.52,47.09", "lat": 41.87, "lon": 12.57, "zoom": 6,
        "fire_regions": ["Sicily Madonie Foothills", "Sardinia Gallura", "Calabria Aspromonte"],
        "default_ndvi": 0.44, "default_elevation_m": 530, "typical_cloud_fraction": 0.26
    },
    {
        "code": "FRA", "name": "France", "continent": "Europe",
        "bbox": "-4.79,41.33,9.56,51.09", "lat": 46.23, "lon": 2.21, "zoom": 5,
        "fire_regions": ["Gironde Maritime Pine Belt", "Var Massif des Maures", "Corsica Scrub"],
        "default_ndvi": 0.52, "default_elevation_m": 375, "typical_cloud_fraction": 0.36
    },
    {
        "code": "RUS", "name": "Russian Federation", "continent": "Europe/Asia",
        "bbox": "19.64,41.19,-169.05,81.86", "lat": 61.52, "lon": 105.32, "zoom": 3,
        "fire_regions": ["Siberian Taiga (Yakutia)", "Krasnoyarsk Boreal Belt", "Amur River Basin"],
        "default_ndvi": 0.46, "default_elevation_m": 600, "typical_cloud_fraction": 0.45
    },
    {
        "code": "CHL", "name": "Chile", "continent": "South America",
        "bbox": "-75.64,-55.98,-66.96,-17.50", "lat": -35.68, "lon": -71.54, "zoom": 4,
        "fire_regions": ["Biobío Plantation Foothills", "Valparaíso Coastal Hills", "Araucanía Forests"],
        "default_ndvi": 0.36, "default_elevation_m": 1200, "typical_cloud_fraction": 0.28
    },
    {
        "code": "ARG", "name": "Argentina", "continent": "South America",
        "bbox": "-73.58,-55.06,-53.64,-21.78", "lat": -38.42, "lon": -63.62, "zoom": 4,
        "fire_regions": ["Corrientes Wetlands", "Córdoba Sierras", "Patagonian Andean Forests"],
        "default_ndvi": 0.39, "default_elevation_m": 590, "typical_cloud_fraction": 0.27
    },
    {
        "code": "ZAF", "name": "South Africa", "continent": "Africa",
        "bbox": "16.45,-34.83,32.89,-22.13", "lat": -30.56, "lon": 22.94, "zoom": 5,
        "fire_regions": ["Western Cape Fynbos", "Mpumalanga Highveld Grasslands", "KwaZulu-Natal Drakensberg"],
        "default_ndvi": 0.28, "default_elevation_m": 900, "typical_cloud_fraction": 0.22
    },
    {
        "code": "COD", "name": "Democratic Republic of the Congo", "continent": "Africa",
        "bbox": "12.21,-13.46,31.31,5.39", "lat": -4.04, "lon": 21.76, "zoom": 5,
        "fire_regions": ["Katanga Savanna", "Congo Basin Margin", "Kivu Highlands"],
        "default_ndvi": 0.62, "default_elevation_m": 720, "typical_cloud_fraction": 0.48
    },
    {
        "code": "AGO", "name": "Angola", "continent": "Africa",
        "bbox": "11.68,-18.04,24.08,-4.39", "lat": -11.20, "lon": 17.87, "zoom": 5,
        "fire_regions": ["Bié Plateau Miombo Woodland", "Moxico Dry Woodlands", "Huíla Escarpment"],
        "default_ndvi": 0.41, "default_elevation_m": 1100, "typical_cloud_fraction": 0.31
    },
    {
        "code": "MEX", "name": "Mexico", "continent": "North America",
        "bbox": "-118.40,14.53,-86.71,32.72", "lat": 23.63, "lon": -102.55, "zoom": 5,
        "fire_regions": ["Sierra Madre Occidental", "Jalisco Pine-Oak", "Oaxaca Highlands", "Chiapas Selva"],
        "default_ndvi": 0.38, "default_elevation_m": 1100, "typical_cloud_fraction": 0.25
    },
    {
        "code": "TUR", "name": "Turkey", "continent": "Europe/Asia",
        "bbox": "25.66,35.81,44.82,42.11", "lat": 38.96, "lon": 35.24, "zoom": 6,
        "fire_regions": ["Antalya Mediterranean Pine Belt", "Muğla Aegean Coast", "Marmaris Highlands"],
        "default_ndvi": 0.34, "default_elevation_m": 850, "typical_cloud_fraction": 0.20
    },
    {
        "code": "DZA", "name": "Algeria", "continent": "Africa",
        "bbox": "-8.67,18.98,11.99,37.09", "lat": 28.03, "lon": 1.66, "zoom": 5,
        "fire_regions": ["Kabylie Cork Oak Mountains", "Tizi Ouzou Forests", "Atlas Tellien"],
        "default_ndvi": 0.18, "default_elevation_m": 800, "typical_cloud_fraction": 0.15
    },
    {
        "code": "COL", "name": "Colombia", "continent": "South America",
        "bbox": "-79.02,-4.23,-66.85,12.46", "lat": 4.57, "lon": -74.30, "zoom": 5,
        "fire_regions": ["Llanos Orientales Grasslands", "Amazon Fringe", "Andean Paramo"],
        "default_ndvi": 0.61, "default_elevation_m": 1200, "typical_cloud_fraction": 0.45
    },
    {
        "code": "THA", "name": "Thailand", "continent": "Asia",
        "bbox": "97.34,5.61,105.64,20.46", "lat": 15.87, "lon": 100.99, "zoom": 6,
        "fire_regions": ["Chiang Mai Highland Deciduous", "Nan Basin", "Khao Yai Margin"],
        "default_ndvi": 0.58, "default_elevation_m": 350, "typical_cloud_fraction": 0.38
    },
    {
        "code": "VNM", "name": "Vietnam", "continent": "Asia",
        "bbox": "102.14,8.56,109.46,23.39", "lat": 14.06, "lon": 108.28, "zoom": 6,
        "fire_regions": ["Central Highlands (Tay Nguyen)", "Northwest Mountain Scrub", "U Minh Peat Forest"],
        "default_ndvi": 0.62, "default_elevation_m": 420, "typical_cloud_fraction": 0.46
    },
    {
        "code": "PHL", "name": "Philippines", "continent": "Asia",
        "bbox": "116.93,4.64,126.60,21.12", "lat": 12.88, "lon": 121.77, "zoom": 6,
        "fire_regions": ["Benguet Cordillera Pine", "Mindanao Grasslands", "Palawan Scrub"],
        "default_ndvi": 0.68, "default_elevation_m": 310, "typical_cloud_fraction": 0.52
    },
    {
        "code": "KEN", "name": "Kenya", "continent": "Africa",
        "bbox": "33.91,-4.68,41.91,5.03", "lat": -0.02, "lon": 37.91, "zoom": 6,
        "fire_regions": ["Rift Valley Escarpment", "Aberdare Range Foothills", "Tsavo Savanna"],
        "default_ndvi": 0.34, "default_elevation_m": 1150, "typical_cloud_fraction": 0.32
    },
    {
        "code": "DEU", "name": "Germany", "continent": "Europe",
        "bbox": "5.87,47.27,15.04,55.06", "lat": 51.17, "lon": 10.45, "zoom": 6,
        "fire_regions": ["Brandenburg Pine Forests", "Harz Mountains", "Saxon Switzerland"],
        "default_ndvi": 0.56, "default_elevation_m": 290, "typical_cloud_fraction": 0.44
    },
    {
        "code": "GBR", "name": "United Kingdom", "continent": "Europe",
        "bbox": "-8.65,49.86,1.77,60.86", "lat": 55.38, "lon": -3.44, "zoom": 5,
        "fire_regions": ["Scottish Highlands Moorland", "Pennines Heather Peat", "Dorset Heathlands"],
        "default_ndvi": 0.54, "default_elevation_m": 210, "typical_cloud_fraction": 0.58
    },
    {
        "code": "JPN", "name": "Japan", "continent": "Asia",
        "bbox": "122.93,20.43,153.99,45.52", "lat": 36.20, "lon": 138.25, "zoom": 5,
        "fire_regions": ["Hokkaido Wildlands", "Nagano Alpine Foothills", "Kyushu Volcanic Slopes"],
        "default_ndvi": 0.63, "default_elevation_m": 480, "typical_cloud_fraction": 0.48
    }
]

SPECIFIC_REGIONS = {
    "DEFAULT": [
        {"id": "DEFAULT", "name": "Global Default (No Active Region)", "lat": 20.00, "lon": 0.00, "zoom": 2, "bbox": "-180.0,-85.0,180.0,85.0", "elevation_m": 0, "desc": "Neutral Earth view without active fire hotspots"}
    ],
    "USA": [
        {"id": "USA-CA", "name": "California Sierra Nevada Foothills", "lat": 39.76, "lon": -121.42, "zoom": 9, "bbox": "-124.5,37.5,-119.5,41.5", "elevation_m": 840, "desc": "High-risk chimney canyon wildfire corridor, Butte & Plumas counties"},
        {"id": "USA-PNW", "name": "Pacific Northwest Cascades (OR/WA)", "lat": 44.50, "lon": -121.80, "zoom": 7, "bbox": "-124.5,42.0,-119.0,48.5", "elevation_m": 920, "desc": "Dense conifer timber belt, lightning ignition zones"},
        {"id": "USA-SOCAL", "name": "Southern California Chaparral", "lat": 34.20, "lon": -117.80, "zoom": 8, "bbox": "-119.5,33.5,-116.5,35.5", "elevation_m": 650, "desc": "Santa Ana wind corridor, Angeles & San Bernardino National Forests"},
        {"id": "USA-ROCKY", "name": "Rocky Mountains & Intermountain West", "lat": 44.00, "lon": -113.50, "zoom": 6, "bbox": "-116.5,40.0,-108.0,48.0", "elevation_m": 1850, "desc": "Subalpine lodgepole pine & beetle-kill fuel complexes"},
        {"id": "USA-TEXAS", "name": "Texas Panhandle & Edwards Plateau", "lat": 32.50, "lon": -100.50, "zoom": 6, "bbox": "-106.0,28.0,-94.0,36.0", "elevation_m": 620, "desc": "Dry prairie grassland & cedar scrub wildfire corridor"},
        {"id": "USA-FLORIDA", "name": "Florida Pine Flatwoods & Everglades", "lat": 27.50, "lon": -81.50, "zoom": 7, "bbox": "-85.0,25.0,-80.0,31.0", "elevation_m": 25, "desc": "Palmetto understory & subtropical peatlands"},
        {"id": "USA-SW", "name": "Southwest Mogollon Rim & Tonto (AZ/NM)", "lat": 34.20, "lon": -111.00, "zoom": 7, "bbox": "-114.5,31.5,-108.5,36.5", "elevation_m": 1400, "desc": "Ponderosa pine forests & desert chaparral interface"}
    ],
    "CAN": [
        {"id": "CAN-BC", "name": "British Columbia Interior & Fraser Canyon", "lat": 50.80, "lon": -121.50, "zoom": 7, "bbox": "-125.0,49.0,-119.0,54.0", "elevation_m": 780, "desc": "Dry interior Douglas fir & ponderosa pine belt"},
        {"id": "CAN-AB", "name": "Alberta Boreal Belt & Fort McMurray", "lat": 56.70, "lon": -111.40, "zoom": 6, "bbox": "-119.0,53.0,-110.0,59.0", "elevation_m": 420, "desc": "Dense black spruce muskeg & peatland taiga"},
        {"id": "CAN-NWT", "name": "Northwest Territories Taiga Shield", "lat": 62.45, "lon": -114.37, "zoom": 5, "bbox": "-125.0,60.0,-110.0,68.0", "elevation_m": 220, "desc": "Subarctic jack pine taiga & lichen woodland"}
    ],
    "BRA": [
        {"id": "BRA-AMZ", "name": "Amazon Basin Arc of Deforestation", "lat": -9.50, "lon": -55.00, "zoom": 6, "bbox": "-62.0,-13.0,-48.0,-6.0", "elevation_m": 240, "desc": "Tropical rainforest fringe, high fuel loading slash burns"},
        {"id": "BRA-PAN", "name": "Pantanal Wetlands Basin", "lat": -17.50, "lon": -56.50, "zoom": 7, "bbox": "-59.0,-21.0,-54.0,-15.0", "elevation_m": 110, "desc": "Seasonal wetland marshes & dry grass savannah"},
        {"id": "BRA-CER", "name": "Cerrado Savanna Agricultural Belt", "lat": -14.00, "lon": -48.00, "zoom": 6, "bbox": "-53.0,-18.0,-44.0,-10.0", "elevation_m": 480, "desc": "Deep-rooted scrubland, intense dry-season burns"}
    ],
    "AUS": [
        {"id": "AUS-NSW", "name": "New South Wales Blue Mountains", "lat": -33.70, "lon": 150.30, "zoom": 8, "bbox": "149.0,-34.5,151.5,-32.5", "elevation_m": 750, "desc": "Eucalyptus oil vapor crown fires, steep sandstone gorges"},
        {"id": "AUS-VIC", "name": "Victoria Alpine National Park", "lat": -37.00, "lon": 146.80, "zoom": 8, "bbox": "145.0,-38.5,148.5,-36.0", "elevation_m": 1250, "desc": "Mountain ash & snow gum alpine forests"},
        {"id": "AUS-QLD", "name": "Queensland Savanna & Atherton", "lat": -18.50, "lon": 144.00, "zoom": 6, "bbox": "140.0,-23.0,149.0,-15.0", "elevation_m": 420, "desc": "Tropical grassland & open woodland"},
        {"id": "AUS-WA", "name": "Western Australia Pilbara & Bush", "lat": -22.50, "lon": 120.00, "zoom": 6, "bbox": "115.0,-32.0,128.0,-18.0", "elevation_m": 350, "desc": "Spinifex hummock grasslands & acacia scrub"}
    ],
    "IND": [
        {"id": "IND-UK", "name": "Uttarakhand Himalayan Pine Foothills", "lat": 29.80, "lon": 79.20, "zoom": 8, "bbox": "77.5,28.5,81.0,31.5", "elevation_m": 1450, "desc": "Chir pine forests, steep slope chimney effect"},
        {"id": "IND-WG", "name": "Western Ghats & Bandipur Escarpment", "lat": 13.50, "lon": 75.50, "zoom": 7, "bbox": "74.0,10.0,77.5,16.5", "elevation_m": 880, "desc": "Moist deciduous to dry scrub transition corridor"},
        {"id": "IND-ODI", "name": "Odisha & Simlipal Sal Reserve", "lat": 21.80, "lon": 86.30, "zoom": 8, "bbox": "84.0,19.5,87.5,23.0", "elevation_m": 520, "desc": "Sal tree canopy, heavy dry leaf litter accumulation"},
        {"id": "IND-MP", "name": "Madhya Pradesh & Satpura Teak Belt", "lat": 22.50, "lon": 78.00, "zoom": 7, "bbox": "75.0,20.5,81.5,25.0", "elevation_m": 610, "desc": "Central Indian dry deciduous teak forest"}
    ],
    "ESP": [
        {"id": "ESP-GAL", "name": "Galicia Eucalyptus Highlands", "lat": 42.60, "lon": -8.00, "zoom": 8, "bbox": "-9.3,41.8,-6.8,43.8", "elevation_m": 580, "desc": "Fast-growing flammable eucalyptus plantations"},
        {"id": "ESP-AND", "name": "Andalusia Sierra Nevada", "lat": 37.10, "lon": -3.35, "zoom": 8, "bbox": "-5.5,36.0,-1.8,38.5", "elevation_m": 1600, "desc": "Mediterranean scrub & dry mountain conifers"},
        {"id": "ESP-GRE", "name": "Sierra de Gredos Central Ridge", "lat": 40.30, "lon": -5.20, "zoom": 8, "bbox": "-6.5,39.5,-4.0,41.0", "elevation_m": 1300, "desc": "High central plateau pine & heath"}
    ],
    "PRT": [
        {"id": "PRT-PED", "name": "Pedrógão Grande Basin & Pinhal", "lat": 39.90, "lon": -8.15, "zoom": 9, "bbox": "-8.7,39.5,-7.6,40.4", "elevation_m": 420, "desc": "Maritime pine & eucalyptus valley fire funnel"},
        {"id": "PRT-EST", "name": "Serra da Estrela Mountain Ridge", "lat": 40.30, "lon": -7.60, "zoom": 9, "bbox": "-8.1,40.0,-7.1,40.7", "elevation_m": 1150, "desc": "High granite plateau scrub & pine"}
    ],
    "GRC": [
        {"id": "GRC-ATT", "name": "Attica & Parnitha Pine Corridor", "lat": 38.15, "lon": 23.70, "zoom": 9, "bbox": "23.2,37.8,24.2,38.5", "elevation_m": 620, "desc": "Aleppo pine forests near urban wildland interface"},
        {"id": "GRC-EVI", "name": "Evia Island Forest Ridge", "lat": 38.55, "lon": 23.90, "zoom": 8, "bbox": "23.4,38.0,24.6,39.1", "elevation_m": 710, "desc": "Rugged island topography, meltemi gale winds"}
    ],
    "FRA": [
        {"id": "FRA-GIR", "name": "Gironde Maritime Pine Belt", "lat": 44.70, "lon": -0.80, "zoom": 8, "bbox": "-1.5,44.2,-0.2,45.3", "elevation_m": 65, "desc": "Dense planted resinous maritime pine on sandy soils"},
        {"id": "FRA-VAR", "name": "Var & Massif des Maures", "lat": 43.30, "lon": 6.50, "zoom": 8, "bbox": "5.8,43.0,7.0,43.7", "elevation_m": 480, "desc": "Cork oak & chestnut maquis, mistral wind hazard"}
    ],
    "ITA": [
        {"id": "ITA-CAL", "name": "Calabria & Aspromonte Wildlands", "lat": 38.20, "lon": 15.90, "zoom": 8, "bbox": "15.3,37.8,16.8,39.5", "elevation_m": 720, "desc": "Steep Mediterranean valleys and dry mountain scrub"},
        {"id": "ITA-SIC", "name": "Sicily Madonie & Mount Etna", "lat": 37.80, "lon": 14.80, "zoom": 8, "bbox": "12.4,36.6,15.7,38.4", "elevation_m": 850, "desc": "Volcanic soil shrublands, high summer sirocco heat"}
    ],
    "RUS": [
        {"id": "RUS-YAK", "name": "Siberian Taiga Basin (Yakutia)", "lat": 62.00, "lon": 129.70, "zoom": 5, "bbox": "120.0,58.0,140.0,68.0", "elevation_m": 190, "desc": "Continuous permafrost larch taiga, zombie peat fires"},
        {"id": "RUS-KRA", "name": "Krasnoyarsk Boreal Belt", "lat": 56.00, "lon": 92.80, "zoom": 5, "bbox": "85.0,52.0,105.0,62.0", "elevation_m": 310, "desc": "Dense southern taiga spruce-fir forest"}
    ]
}

def _generate_default_regions_for_country(c: dict) -> list:
    """Generates geographically distinct northern, central, and southern regional zones for any country."""
    try:
        parts = [float(x.strip()) for x in c["bbox"].split(",")]
        min_lon, min_lat, max_lon, max_lat = parts[0], parts[1], parts[2], parts[3]
    except Exception:
        min_lon, min_lat, max_lon, max_lat = c["lon"] - 3, c["lat"] - 3, c["lon"] + 3, c["lat"] + 3

    lat_step = (max_lat - min_lat) / 3.0
    lon_mid = (min_lon + max_lon) / 2.0
    c_code = c["code"]
    c_name = c["name"]

    return [
        {
            "id": f"{c_code}-NORTH",
            "name": f"{c_name} Northern Forest Basin",
            "lat": round(max_lat - lat_step * 0.5, 4),
            "lon": round(lon_mid, 4),
            "zoom": c.get("zoom", 5) + 1,
            "bbox": f"{min_lon:.2f},{(max_lat - lat_step):.2f},{max_lon:.2f},{max_lat:.2f}",
            "elevation_m": c.get("default_elevation_m", 450) + 150,
            "desc": f"Northern wildfire risk division for {c_name}"
        },
        {
            "id": f"{c_code}-CENTRAL",
            "name": f"{c_name} Central Foothills Corridor",
            "lat": round(c["lat"], 4),
            "lon": round(c["lon"], 4),
            "zoom": c.get("zoom", 5) + 1,
            "bbox": f"{min_lon:.2f},{(min_lat + lat_step):.2f},{max_lon:.2f},{(max_lat - lat_step):.2f}",
            "elevation_m": c.get("default_elevation_m", 450),
            "desc": f"Central core administrative and wildland division for {c_name}"
        },
        {
            "id": f"{c_code}-SOUTH",
            "name": f"{c_name} Southern Plains & Savanna",
            "lat": round(min_lat + lat_step * 0.5, 4),
            "lon": round(lon_mid, 4),
            "zoom": c.get("zoom", 5) + 1,
            "bbox": f"{min_lon:.2f},{min_lat:.2f},{max_lon:.2f},{(min_lat + lat_step):.2f}",
            "elevation_m": max(50, c.get("default_elevation_m", 450) - 100),
            "desc": f"Southern border and agricultural scrub frontier for {c_name}"
        }
    ]

# Populate rich regions on every country object
for c in GLOBAL_COUNTRIES:
    code = c["code"]
    if code in SPECIFIC_REGIONS:
        c["regions"] = SPECIFIC_REGIONS[code]
    else:
        c["regions"] = _generate_default_regions_for_country(c)

GLOBAL_COUNTRIES_BY_CODE = {c["code"]: c for c in GLOBAL_COUNTRIES}

def get_country_by_code(code: str):
    """Retrieve country metadata by ISO-3 alpha code or return USA default."""
    if not code:
        return GLOBAL_COUNTRIES_BY_CODE.get("USA")
    clean_code = str(code).strip().upper()
    return GLOBAL_COUNTRIES_BY_CODE.get(clean_code, GLOBAL_COUNTRIES_BY_CODE.get("USA"))

def get_regions_for_country(code: str):
    """Retrieve structured list of fire regions for the specified country."""
    c = get_country_by_code(code)
    return c.get("regions", [])
