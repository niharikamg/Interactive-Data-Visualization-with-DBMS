from flask import Flask, request, jsonify
from nlp import generate_sql_from_nl
from visualizer import visualize_data
import config
import pandas as pd
import sqlalchemy

app = Flask(__name__)
engine = sqlalchemy.create_engine(config.DB_URI)

@app.route("/query", methods=["POST"])
def query():
    data = request.get_json()
    input_text = data.get("query")

    sql_query = generate_sql_from_nl(input_text)
    df = pd.read_sql_query(sql_query, engine)
    chart_path = visualize_data(df)

    return jsonify({"sql": sql_query, "chart": chart_path})

if __name__ == "__main__":
    app.run(debug=True)
