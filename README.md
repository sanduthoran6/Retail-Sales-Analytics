# Retail Sales Analytics Dashboard

This Streamlit website is the interactive version of the Jupyter project **Retail Sales Data Analysis and Visualization Using Python**.

## Data consistency
- Uses the same reproducible synthetic dataset logic as the notebook (`numpy.random.seed(42)`, 500 transactions, same products, prices, regions, dates and payment methods).
- Includes the same 11 prepared columns: `Order_ID`, `Order_Date`, `Product`, `Category`, `Region`, `Quantity`, `Unit_Price`, `Payment_Method`, `Total_Sales`, `Month`, `Year`.
- The dashboard's default (unfiltered) KPIs use the same calculations as the notebook.
- Dataset is synthetic and for educational demonstration only.

## Run locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy a public website with Streamlit Community Cloud
1. Create/sign in to GitHub and create a **public** repository (for example `retail-sales-analytics`).
2. Upload `app.py`, `retail_sales_data.csv`, and `requirements.txt` to the repository root.
3. Open https://share.streamlit.io/ and sign in with GitHub.
4. Choose **Create app**, select the repository and branch, and set the main file path to `app.py`.
5. Deploy. Streamlit will provide the public website URL to submit.

The public website URL is created only after deployment from your GitHub account.
