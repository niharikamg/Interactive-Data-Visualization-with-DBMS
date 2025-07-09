import spacy
from transformers import pipeline

# Load NLP models if needed (placeholder here)
# nlp = spacy.load("en_core_web_sm")

# Simple logic to simulate SQL generation
def generate_sql_from_nl(nl_query):
    nl_query = nl_query.lower()

    if "sales" in nl_query and "region" in nl_query:
        return "SELECT region, SUM(sales) AS sales FROM sales_data GROUP BY region;"
    elif "sales" in nl_query:
        return "SELECT date, SUM(sales) AS sales FROM sales_data GROUP BY date;"
    else:
        return "SELECT * FROM sales_data LIMIT 10;"
