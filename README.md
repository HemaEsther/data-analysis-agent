# 🤖 Agentic AI Data Analysis System

## 📌 Overview

This project implements a **plug-and-play AI-powered Data Analysis Agent** that automates exploratory data analysis (EDA), generates insights, and produces professional reports.

Unlike traditional EDA scripts, this system simulates a **data analyst’s workflow** — from understanding the dataset to recommending next steps and generating shareable reports.

---

## 🚀 Key Features

### 🔍 Data Understanding

* 📊 Automatic dataset preview (`head`, `info`, shape)
* 🧾 Feature type detection (numerical & categorical)
* ⚠️ Missing value analysis with interpretation

### 🧠 Intelligent Analysis

* 📈 Distribution & skewness analysis
* 🔗 Correlation detection (strong relationships)
* 🧠 Human-readable insights generation

### ⚡ Smart System Capabilities

* 🔄 **Plug-and-Play** → works with any CSV dataset
* 📊 **Large dataset detection**
* 💡 **Smart sampling suggestion** (performance optimization)

### 🤖 Recommendations Engine

* 📌 Feature selection suggestions
* 🤖 Model recommendations (Regression / Classification)
* ⚖️ Data imbalance detection
* 🛠️ Preprocessing guidance

### 📄 Reporting System (NEW 🔥)

* 📊 Auto-generated **HTML dashboard report**
* 📈 Embedded visualizations (histograms, heatmaps)
* 🧠 Insights + recommendations in one place
* 🎯 Shareable output for stakeholders

---

## 🧠 What Makes It Unique?

This is not just an EDA tool — it's an **Agentic AI System**:

* Understands dataset structure
* Adapts to dataset size
* Interprets patterns
* Generates insights
* Recommends actions
* Produces professional reports

👉 It mimics how a **real data analyst thinks, decides, and communicates results**

---

## 🏗️ Project Structure

```
data-analysis-agent/
│
├── data/                 # Input datasets
│
├── src/
│   ├── data_loader.py     # Data loading & cleaning
│   ├── eda.py             # Statistical analysis
│   ├── insights.py        # Insight logic
│   ├── visualize.py       # Plot generation
│   ├── report.py          # Report generation
│   ├── agent.py           # Main agent (pipeline controller)
│   
│
├── app.py                 # Entry point (CLI interface)
├── requirements.txt
└── README.md
```

---

## ⚙️ Tech Stack

* Python 🐍
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone <your-repo-link>
cd data-analysis-agent
```

### 2. Create virtual environment

```bash
py -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
py -m pip install -r requirements.txt
```

### 4. Add dataset

Place your CSV file inside the `data/` folder.


### 5. Run the application

```bash
py app.py
```

---

## 📊 Output

After running, the agent will:

* Analyze your dataset
* Generate insights & recommendations
* Create a **dashboard-style report**

👉 Open report:

```bash
start report.html
```

---

## 💡 Example Use Cases

* Quick dataset understanding
* Automated EDA for ML projects
* Data preprocessing guidance
* Business insight generation
* Report generation for stakeholders

---

## 🧠 Future Enhancements

* 📊 Interactive dashboard (Streamlit)
* 🤖 LLM-based natural language querying
* 📄 PDF export support
* 📈 Advanced visual analytics

---

## 📌 Resume Highlight

> Built a plug-and-play AI-powered data analysis agent that performs automated EDA, generates insights, and produces interactive HTML reports with visualizations and intelligent recommendations.

---
