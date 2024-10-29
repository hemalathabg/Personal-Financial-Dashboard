# app.py

from flask import Flask, render_template, request, jsonify
import plaid
from config import PLAID_CLIENT_ID, PLAID_SECRET, PLAID_ENV, PLAID_PRODUCTS, PLAID_COUNTRY_CODES
from finance_data import process_transactions
import pandas as pd

app = Flask(__name__)

# Initialize Plaid client
client = plaid.Client(client_id=PLAID_CLIENT_ID, secret=PLAID_SECRET, environment=PLAID_ENV)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_access_token', methods=['POST'])
def get_access_token():
    public_token = request.form.get('public_token')
    exchange_response = client.Item.public_token.exchange(public_token)
    access_token = exchange_response['access_token']
    return jsonify(access_token=access_token)

@app.route('/transactions', methods=['GET'])
def get_transactions():
    access_token = request.args.get('access_token')
    response = client.Transactions.get(access_token, start_date="2022-01-01", end_date="2022-12-31")
    transactions = response['transactions']
    
    # Process transactions for frontend display
    data = process_transactions(transactions)
    return jsonify(data=data)

if __name__ == '__main__':
    app.run(debug=True)
