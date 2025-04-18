# FACILITY_NETWORK

## 🚀 Introduction
FACILITY_NETWORK is a UI automation testing project using **Playwright** and **pytest**. This project also integrates **Allure** for generating detailed test reports.

---

## ⚙️ Installation Guide

### 1️⃣ Clone the Repository
Ensure you have **Git** installed, then run:
```sh
git clone https://github.com/Celcius1910/FACILITY_NETWORK.git
cd FACILITY_NETWORK
```

### 2️⃣ Create a Virtual Environment (Optional but Recommended)
```sh
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate  # Windows
```

### 3️⃣ Install Dependencies
Run the following command to install all required dependencies:
```sh
pip install -r requirements.txt
```

### 4️⃣ Install Playwright & Browsers
```sh
playwright install
playwright install-deps  # For Linux/Mac
```

---

## ✅ Running Tests
To execute tests using **pytest**:
```sh
pytest tests/test_UI.py
```

For **headless mode** (without opening the browser):
```sh
pytest tests/test_UI.py --headless
```

To run tests with **Allure reporting**:
```sh
pytest --alluredir=reports/allure-results
allure serve reports/allure-results
```

---

## 📊 Generate Allure Report
To generate a test result report:
```sh
allure generate reports/allure-results -o reports/allure-report --clean
```

To open the generated report:
```sh
allure open reports/allure-report
```

---

## 🔧 Troubleshooting
If Playwright fails to detect browsers, try:
```sh
playwright install
```

If there are dependency issues on Linux:
```sh
playwright install-deps
```

To clear pytest cache:
```sh
pytest --cache-clear
```

---

## 📬 Contact
For any questions or assistance, feel free to reach out:
📧 Email: naufalazizmaulana19@gmail.com
📌 GitHub: https://github.com/Celcius1910

---

🎯 **Happy Testing and Automation! 🚀**

