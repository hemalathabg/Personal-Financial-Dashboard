The Personal Financial Dashboard is a web application designed to help users track, visualize, and manage their finances in one place. With a simple interface, users can view spending patterns, categorize expenses, and gain insights into their financial habits. Powered by the Plaid API, this dashboard connects with your bank accounts to pull transaction data and displays spending patterns using charts.

Features
Transaction Tracking: Automatically fetches and categorizes transactions from your bank accounts.
Spending Analysis: Provides total spending and category-wise breakdowns, helping users understand their spending habits.
Visualizations: Includes interactive charts for easy visualization of financial data.
Secure API Integration: Uses Plaid API to securely access transaction data.
Tech Stack
Backend: Flask (Python)
Frontend: HTML, CSS, JavaScript (with Chart.js)
Database: SQLite (for local data storage)
API Integration: Plaid API for accessing bank transaction data
Project Structure
php
Copy code
personal_financial_dashboard/
├── app.py                 # Main Flask application
├── config.py              # Configuration file for API keys and settings
├── templates/
│   └── index.html         # HTML template for the main dashboard
├── static/
│   └── style.css          # CSS styling for the frontend
├── finance_data.py        # Logic for data processing and analysis
├── requirements.txt       # Dependencies file
└── README.md              # Project readme
Getting Started
Prerequisites
Python 3.6 or later
Plaid API account with sandbox access (for testing)
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/hemalathabg/personal_financial_dashboard.git
cd personal_financial_dashboard
Set up the virtual environment:

bash
Copy code
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Configure Plaid API:

Add your Plaid API keys in the config.py file.
Run the application:

bash
Copy code
python app.py
Access the app: Open your web browser and go to http://127.0.0.1:5000.

Usage
Connect to Plaid: Use your Plaid sandbox credentials to connect and authorize transactions.
Fetch Transactions: Click "Fetch Transactions" to pull transaction data.
View Insights: The dashboard will display a total spending summary and a categorized spending chart.
Future Enhancements
Budget Tracking: Enable users to set budgets and track spending against targets.
Notifications: Send alerts when spending exceeds a specified threshold in any category.
Multiple Account Support: Allow users to track finances across multiple accounts for a consolidated view.
