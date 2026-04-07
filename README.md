# 🤖 Agentic AI Data Analysis System

## 📌 Overview

This project implements an **AI-powered Data Analysis Agent** that automates exploratory data analysis (EDA), generates insights, and provides intelligent recommendations for data preprocessing and modeling.

Unlike traditional EDA scripts, this system simulates a **data analyst's thinking process** by not only analyzing data but also suggesting actionable next steps.

---

## 🚀 Key Features

- 📊 Automated Exploratory Data Analysis (EDA)
- 🔍 Missing Value Detection
- 📈 Distribution & Skewness Analysis
- 🔗 Correlation Detection
- 🧠 Insight Generation (Human-readable)
- 📌 Feature Selection Recommendations
- 🤖 Model Suggestions (Regression / Classification)
- ⚖️ Data Imbalance Detection
- 🛠️ Preprocessing Recommendations

---

## 🧠 What Makes It Unique?

This project goes beyond basic analysis by acting as an **Agentic AI System**:

- Understands dataset structure  
- Interprets patterns  
- Generates insights  
- Recommends actions  

👉 It mimics how a **real data analyst thinks and works**

---

## 🏗️ Project Structure

data-analysis-agent/
│

├── data/

│ └── AirQualityUCI.csv

│

├── src/

│ ├── data_loader.py # Data loading & cleaning

│ ├── eda.py # Statistical analysis functions

│ ├── insights.py # Insight & recommendation logic

│ ├── agent.py # Main agent orchestration

│ └── init.py

│

├── app.py # Entry point

├── requirements.txt

└── README.md


---

## ⚙️ Tech Stack

- Python 🐍  
- Pandas  
- NumPy  
- Matplotlib  
- Seaborn  
- Scikit-learn  

---

## 📊 Dataset

- Air Quality Dataset (Sensor-based environmental data)
- Contains:
  - Gas concentrations (CO, NOx, etc.)
  - Temperature, humidity
  - Time-based readings

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone <your-repo-link>
cd data-analysis-agent

### 2. Install dependencies

```bash
pip install -r requirements.txt

### 3. Run the application
py app.py

