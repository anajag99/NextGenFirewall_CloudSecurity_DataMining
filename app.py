import streamlit as st
import pandas as pd
import requests
from io import BytesIO

# Simulate the firewall's decision
def simulate_firewall_decision(prediction):
    return 'Safe' if prediction == 0 else 'Unsafe'

# Process CSV data and log decisions
def process_csv_data(data, url):
    files = {'file': ('data.csv', data, 'text/csv')}
    try:
        response = requests.post(url, files=files)
        print("Sending request to URL:", url)
        if response.status_code == 200:
            predictions = response.json()
            return [f"Transaction {i+1} is {('safe','unsafe')[p]}" for i, p in enumerate(predictions)]
        else:
            return [f"Failed to get a response from the server: {response.status_code} - {response.text}"]
    except requests.exceptions.RequestException as e:
        return [f"Request failed: {str(e)}"]


# Streamlit user interface
def main():
    st.title('Firewall Decision Simulator')
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file is not None:
        if st.button('Process Data'):
            # Convert the uploaded file to bytes for transmission
            data = BytesIO(uploaded_file.getvalue())
            results = process_csv_data(data, 'http://localhost:5000/predict')
            for result in results:
                st.write(result)

if __name__ == "__main__":
    main()
