# SauceDemo Automation Project

This repository contains an end-to-end automation testing framework built for the [SauceDemo](https://www.saucedemo.com/) e-commerce demo website. It uses *python*, *Selenium*, and the *Pytest* framework following the *Page Object Model (POM)* architecture with support for *Data Driven Testing (DDT)*.
---

# Objective

To verify the functionality of a demo e-commerce site using automated test cases that simulate real user interactions. Tests cover both **positive and negative scenarios**, and generate **HTML reports** for results.

---

# Key Features

-  Complete test coverage for 8 use cases (login, cart, checkout, etc.)
-  Modular design using Page Object Model (POM)
-  Data Driven Testing (CSV-based)
-  Screenshot capture during checkout
-  Pytest-based HTML report generation
-  Structured with Python OOPS and exception handling
-  Logs and cookie-based session validation
-  Cross-browser capable (via `webdriver-manager`)

---

# Tools & Technologies Used

| Tool                | Purpose                                |
|---------------------|----------------------------------------|
| Python              | Programming language                   |
| Selenium WebDriver  | Browser automation                     |
| Pytest              | Testing framework                      |
| Pytest-HTML         | HTML test reporting                    |
| Webdriver Manager   | Auto-manages browser drivers           |
| POM Design Pattern  | Code structure for UI automation       |
| CSV / YAML          | Data / Keyword-Driven Testing          |

---

# Test Case Summary

| Test Case | Description |
|-----------|-------------|
| TC1 | Valid login with multiple users and session validation via cookies |
| TC2 | Invalid login using non-registered user (`guvi_user`) |
| TC3 | Logout button visibility and functionality |
| TC4 | Cart button visibility after login |
| TC5 | Random product selection (4 of 6) and data fetch |
| TC6 | Add 4 products to cart and verify cart badge |
| TC7 | Fetch product details from cart |
| TC8 | Complete checkout, capture screenshot, and verify summary |

---

# Project Structure
saucedemo_capstone/
│
├── data/
│   └── login_data.csv
│
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   ├── checkout_page.py
│
├── tests/
│   ├── test_login_valid_users.py
│   ├── test_login_invalid_user.py
│   ├── test_logout.py
│   ├── test_cart_visibility.py
│   ├── test_random_product_fetch.py
│   ├── test_add_products_to_cart.py
│   ├── test_cart_verification.py
│   ├── test_checkout_process.py
│
├── utils/
│   ├── driver_factory.py
│   ├── read_csv_data.py
│
├── screenshots/
│   └── (generated at runtime)
│
├── reports/
│   └── (pytest-html report will be stored here)
│
├── requirements.txt
├── pytest.ini
├── README.md



---

# How to Run the Tests

Step 1: Install dependencies
in the output terminal:
pip install -r requirements.txt

Step 2: Run all tests with HTML report
in the output terminal:
pytest -vs tests/ --html=reports/report.html --self-contained-html

Step 3: View the report
Open reports/report.html in your browser after execution.

📸 Screenshots
Checkout overview screenshots are saved in /screenshots/ folder during Test Case 8.

                     Login Credentials Used
User Type	     Username	                   Password
Standard User	     standard_user	          secret_sauce
Problem User	     problem_user	          secret_sauce
Performance Glitch   performance_glitch_user	  secret_sauce
Locked Out User	     locked_out_user	          secret_sauce
Invalid User	     guvi_user	                  Secret@123




