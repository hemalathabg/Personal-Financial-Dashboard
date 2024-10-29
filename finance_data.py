# finance_data.py

import pandas as pd

def process_transactions(transactions):
    # Load transactions into a DataFrame
    df = pd.DataFrame(transactions)
    
    # Example: Categorize by spending category
    df['amount'] = df['amount'].astype(float)
    category_summary = df.groupby('category').sum()['amount'].reset_index()
    
    # Format data for frontend
    data = {
        'total_spent': df['amount'].sum(),
        'category_summary': category_summary.to_dict(orient='records')
    }
    return data
