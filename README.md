# NASA Environmental Hotspot Activity Forecast

An Earth Observation & Machine Learning full-stack pipeline forecasting next-day satellite active-fire hotspot detections based on NASA FIRMS (VIIRS 375m NOAA-21/20 & MODIS), GPM precipitation, MODIS NDVI, MERRA-2 weather, and SRTM topography data.

---

## 📁 Connected Full-Stack Architecture

The backend and frontend environments in this project are unified and communicate bi-directionally via REST APIs, real-time satellite telemetry ingestion, and shared `.env` configurations:

```
NASA/
├── run.py                        # Unified full-stack launcher (auto-starts server & browser)
├── start.bat                     # 1-Click Windows execution script
├── .env                          # Root environment config (NASA_FIRMS_MAP_KEY, SENSOR, BBOX)
├── README.md                     # Documentation
│
├── frontend/                     # Web Application (UI / Visualization)
│   ├── index.html                # Main interface, mission control telemetry & modals
│   ├── style.css                 # Mission-control NASA dark theme stylesheet
│   ├── app.js                    # Interactive Leaflet map, Chart.js, HUD & API connectors
│   └── forecast_data.json        # Structured forecast telemetry consumed by UI
│
├── backend/                      # Data Science & Machine Learning Engine
│   ├── model_pipeline.py         # Pure NumPy training, baseline benchmarks & FIRMS ingestion
│   ├── server.py                 # Threading HTTP server & REST API (serves frontend & executes pipeline)
│   ├── forecast_data.json        # Output export from latest model run
│   ├── requirements.txt          # Python dependencies (numpy, pandas)
│   └── .env                      # Synced environment configuration
│
├── .vscode/                      # Editor configuration
│   ├── settings.json             # Workspace interpreter & linter settings
│   ├── launch.json               # Debugging configurations for full-stack and pipeline
│   └── tasks.json                # VS Code Build & Retrain tasks
│
└── venv/                         # Python Virtual Environment (NumPy & Pandas)
```

---

## ⚡ 1-Click Launch (Recommended)

### Option A: Double-Click `start.bat`
Double-click `start.bat` in File Explorer or run in terminal:
```cmd
start.bat
```
This automatically selects the virtual environment, verifies dependencies, starts the backend REST API server, and opens your browser.

### Option B: Run `run.py`
```bash
python run.py
```
Or using the virtual environment:
```powershell
.\venv\Scripts\python.exe run.py
```

The application will be live at:
- **Web Dashboard**: [http://localhost:8000/](http://localhost:8000/)
- **API Status**: [http://localhost:8000/api/status](http://localhost:8000/api/status)
- **Forecast JSON**: [http://localhost:8000/api/forecast](http://localhost:8000/api/forecast)
- **Config Info**: [http://localhost:8000/api/config](http://localhost:8000/api/config)

---

## 🔄 How Backend and Frontend Are Connected

1. **Integrated Server**: `backend/server.py` hosts the static files in `frontend/` on `http://localhost:8000/` while routing all `/api/*` endpoints to backend logic.
2. **Real-Time Retraining**: Clicking **Retrain Model** in the web interface calls `POST /api/retrain`, which triggers `backend/model_pipeline.py` in the background, pulls live NASA FIRMS detections, trains the model, and updates the map and charts in real time without refreshing.
3. **NASA Key Synchronization**: When a user inputs their `NASA_FIRMS_MAP_KEY` in the frontend modal, it calls `POST /api/set-firms-key`, which persists the key to both `d:\NASA\.env` and `backend/.env`, and updates active telemetry.
4. **Resilient Data Loading**: `frontend/app.js` queries `http://localhost:8000/api/forecast` first with a cache-busting timestamp, then falls back to `forecast_data.json`, and finally falls back to scientific benchmark data if opened offline or via `file://`.
5. **CORS Enabled**: The backend server supports `OPTIONS` preflights and CORS headers so other local dev servers can query the API without restriction.

---

## 🛰️ Supported Satellite Sensors

- **VIIRS NOAA-21 (375m)** (`VIIRS_NOAA21_NRT`) — Primary next-generation JPSS-2 sensor *(Default)*
- **VIIRS NOAA-20 (375m)** (`VIIRS_NOAA20_NRT`) — High-resolution JPSS-1 sensor
- **VIIRS Suomi-NPP (375m)** (`VIIRS_SNPP_NRT`) — Afternoon orbit sensor
- **MODIS Terra/Aqua (1km)** (`MODIS_NRT`) — Long-term baseline thermal anomaly sensor

---

## 🚨 Emergency Numbers & Respected Calling System

The platform integrates a real-time emergency dispatch registry supporting the **Indian Numbering System** (`+91 XXXXX XXXXX`, `112` ERSS, `101` Fire Control) and country-specific emergency contacts:

1. **In-Dashboard Emergency Configuration**:
   * Add and manage country-number pairs directly from the In-Dashboard Sidebar, the Floating Dashboard Card, or the Emergency Management Modal.
   * Auto-formats 10-digit mobile inputs into standard Indian format (`+91 98765 43210`) and validates emergency shortcodes (`112`, `101`).
2. **Respected Emergency Responder Calling**:
   * When fire predictions are active, the system automatically routes emergency voice notifications and real-time satellite telemetry reports to the designated respected responder for that country (e.g., India: `+91 90599 57974`, USA: `+91 63013 85741`).
3. **Sudden Prediction Change & Escalation Detection**:
   * Stored baseline data (`backend/prediction_history.json` and client-side storage) is continuously cross-referenced with live incoming satellite and ML forecast metrics.
   * If a sudden spike occurs ($\Delta \text{Risk} \ge 14\%$, $\Delta \text{Pixels} \ge 10$, or risk transitions from Moderate to Critical):
     * The system **bypasses standard cooldowns** to immediately alert responders.
     * Displays a glowing red/amber **Sudden Prediction Shift Banner** on the dashboard.
     * Dials the country's respected emergency number with synthesized voice alerts.
     * Generates a detailed incident report with a dedicated comparison breakdown comparing stored baselines against the updated forecast.

---

## 🛠️ VS Code Integration

Use `Ctrl+Shift+B` in VS Code to trigger **Start Full-Stack NASA App**, or open the Run & Debug pane (`Ctrl+Shift+D`) to run:
- **Launch Full-Stack System (run.py)**
- **Debug Backend Server (server.py)**
- **Run Model Pipeline (Pure NumPy Engine)**
- **Run Model Pipeline (Sync Live NASA FIRMS)**

