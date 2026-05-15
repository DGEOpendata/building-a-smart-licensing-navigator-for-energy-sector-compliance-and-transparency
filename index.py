python
from flask import Flask, request, jsonify
import pandas as pd
import json

app = Flask(__name__)

# Load the dataset
dataset = pd.read_csv('Licenses_Permits_Energy_Sector_2025.csv')

@app.route('/search', methods=['POST'])
def search_licenses():
    # Parse JSON request data
    query_params = request.json
    
    # Filter dataset based on query
    results = dataset
    for key, value in query_params.items():
        if key in dataset.columns:
            results = results[results[key].str.contains(value, case=False, na=False)]

    # Convert results to JSON and return
    results_json = results.to_json(orient='records')
    return jsonify(json.loads(results_json))

if __name__ == '__main__':
    app.run(debug=True)
