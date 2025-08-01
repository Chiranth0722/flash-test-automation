# ⚡ Flash Test Automation

Automated test suite built with `pytest` to simulate and verify the behavior of a flash memory device. It includes both basic functional tests and advanced simulations such as capacity limits, hardware failures, and device busy states.

![Python](https://img.shields.io/badge/Python-3.12-blue.svg)
![Pytest](https://img.shields.io/badge/Tested_with-Pytest-green.svg)
[![CI](https://github.com/Chiranth0722/flash-test-automation/actions/workflows/python-tests.yml/badge.svg)](https://github.com/Chiranth0722/flash-test-automation/actions)
[![codecov](https://codecov.io/gh/Chiranth0722/flash-test-automation/branch/main/graph/badge.svg)](https://codecov.io/gh/Chiranth0722/flash-test-automation)

---

## 🚀 Features

- ✅ Unit testing with `pytest`
- 🔁 Parameterized test coverage
- 🧪 Advanced edge-case testing:
  - Capacity limits
  - Random hardware failures
  - Busy device simulation
- 📈 Code coverage reports (via `pytest-cov` & Codecov)
- ☁️ CI/CD with GitHub Actions

---

## 🛠️ Setup & Usage

1️⃣ Create Virtual Environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Run Tests with Coverage
pytest --cov=flash_device --cov-report=term --cov-report=html
📝 Coverage report will be available in test-reports/htmlcov/index.html.
🔄 Continuous Integration
GitHub Actions automatically runs the test suite and uploads coverage to Codecov on every push and pull request to the main branch.

📊 Code Coverage Dashboard
View coverage reports on Codecov.
