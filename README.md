# 🌫️ Ahmedabad AQI Dashboard

> End-to-end Air Quality Index monitoring, analysis, 
> and prediction system for Ahmedabad city — built 
> using 3.5 years of real daily data.

**🔗 Live Dashboard → [Click Here](https://lalitkumar-7.github.io/AQI_Ahmedabad_Monitoring/dashboard/overview.html)**  
**📁 Dataset → [Zenodo](https://zenodo.org/records/14891822)**

---

## 📌 Project Overview

This project performs a complete data science pipeline 
on Ahmedabad's air quality data — from raw CSV to 
trained ML models to a fully interactive web dashboard.

| | |
|---|---|
| **City** | Ahmedabad, Gujarat, India |
| **Data Range** | Aug 1, 2022 → Feb 18, 2026 |
| **Total Records** | 1,298 daily rows |
| **Pollutants Tracked** | 9 (PM2.5, PM10, NO2, SO2, CO, O3, AOD, Dust, UV) |
| **Target Variable** | US AQI (0–500 scale) |

---

## 📊 Dashboard Pages

| Page | Description |
|---|---|
| 🏠 Overview | Metric cards, 3.5-year AQI trend, pollutant summary |
| 📅 Date Explorer | Filter any date range, see AQI + pollutant breakdown |
| 📈 Monthly Trends | Year-wise monthly bar chart, seasonal comparison |
| 💨 Pollutant Explorer | Per-pollutant trend, scatter vs AQI, correlation ranking |
| 🤖 AQI Predictor | Input sliders → real-time AQI prediction + health advice |
| 🔗 Correlation Insights | Weekday vs weekend, lag analysis, pollution fingerprint |

---

## 🗂️ Project Structure
```
AQI_Ahmedabad_Monitoring/
│
├── 📁 data/
│   ├── air_quality_historical.csv
│   └── clean_data.csv
│
├── 📁 models/
│   ├── aqi_model.pkl
│   └── aqi_classifier.pkl
│
├── 📁 notebooks/
│   ├── 01_EDA.ipynb
│   ├── 02_Preprocessing.ipynb
│   ├── 03_AQI_Prediction.ipynb
│   ├── 04_AQI_Classification.ipynb
│   └── 05_Correlation_Study.ipynb
│
├── 📁 dashboard/
│   ├── overview.html
│   ├── date_explorer.html
│   ├── monthly_trends.html
│   ├── pollutant.html
│   ├── predictor.html
│   └── correlation.html
│
└── README.md
```


---

## 🔬 Notebooks Summary

### 01 — EDA
- Distribution analysis of all 9 pollutants
- AQI trend over 3.5 years
- Monthly and seasonal patterns
- Festival spike detection (Diwali, Uttarayan)
- Correlation heatmap
- Outlier analysis — worst AQI days
- AOD and UV special analysis

### 02 — Preprocessing
- Missing value handling (forward fill)
- Date parsing and feature extraction
  (month, year, day of week, season)
- AQI category labeling (5 classes)
- Feature scaling (StandardScaler)
- Saves `clean_data.csv`

### 03 — AQI Prediction (Regression)
- Models trained: Linear Regression, 
  Random Forest, XGBoost
- Evaluation: MAE, RMSE, R² Score
- Best model saved as `aqi_model.pkl`
- Feature importance chart

### 04 — AQI Classification
- 5 classes: Good / Moderate / 
  Unhealthy for Sensitive / Unhealthy / Very Unhealthy
- Models: Logistic Regression, 
  Random Forest, XGBoost
- Confusion matrix, Classification report
- Best model saved as `aqi_classifier.pkl`

### 05 — Correlation Study
- Weekday vs weekend industrial pollutant analysis
- Pollutant pair scatter plots with trendlines
  (CO vs NO2, UV vs Ozone, Dust vs PM10)
- Lag correlation (does yesterday's PM2.5 
  predict today's AQI?)
- Worst AQI days breakdown
- Pollution source fingerprint 
  (Winter = vehicular, Summer = natural dust)
- Year-over-year AQI trend

---
---

## 🤖 ML Models

| Model | Task | Algorithm | Metric |
|---|---|---|---|
| `aqi_model.pkl` | Predict AQI value | Random Forest Regressor | R², RMSE |
| `aqi_classifier.pkl` | Predict AQI category | Random Forest Classifier | Accuracy, F1 |

---

## 📦 Dataset Details

| Field | Value |
|---|---|
| Source | Zenodo — Open Data Repository |
| Authors | Nitiraj Kulkarni, Jagadish Tawade |
| Coverage | Ahmedabad city, Gujarat, India |
| Frequency | Daily |
| API Source | Open-Meteo CAMS Global |

**Columns:**

| Column | Description | Unit |
|---|---|---|
| `date` | Daily date | YYYY-MM-DD |
| `pm2_5` | Fine particulate matter | µg/m³ |
| `pm10` | Coarse particulate matter | µg/m³ |
| `carbon_monoxide` | CO levels | µg/m³ |
| `nitrogen_dioxide` | NO2 levels | µg/m³ |
| `sulphur_dioxide` | SO2 levels | µg/m³ |
| `ozone` | Ground-level ozone | µg/m³ |
| `aerosol_optical_depth` | Sky haze indicator | 0–2 |
| `dust` | Dust particle concentration | µg/m³ |
| `uv_index` | UV radiation level | 0–3 |
| `us_aqi` | US EPA AQI score (target) | 0–500 |
| `european_aqi` | European AQI score | 0–100+ |

---

## 🛠️ Tech Stack

**Data & ML**
- Python 3.x
- Pandas, NumPy
- Scikit-learn
- Matplotlib, Seaborn
- Jupyter Notebook

**Dashboard**
- HTML5 + CSS3
- Tailwind CSS
- Chart.js (interactive charts)
- PapaParse (CSV parsing in browser)

**Hosting**
- GitHub Pages (live, free)

---

## 🚀 How to Run Locally

```bash
# Clone the repo
git clone https://github.com/Lalitkumar-7/AQI_Ahmedabad_Monitoring.git

cd AQI_Ahmedabad_Monitoring

# Install dependencies
pip install pandas numpy scikit-learn 
    matplotlib seaborn jupyter

# Run notebooks in order
jupyter notebook notebooks/01_EDA.ipynb

# Open dashboard locally
# Open dashboard/overview.html in any browser
# (serve via live server for CSV to load correctly)
```

---

## 👤 Author

**Lalit Kumar**  
BTech CSE (Data Science) — VGEC, Ahmedabad  
[GitHub](https://github.com/Lalitkumar-7) • [LinkedIn](www.linkedin.com/in/lalit-patadiya)

---

## 📄 License

This project is open source.

Dataset is publicly available on Zenodo 
under open access.
