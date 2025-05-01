from flask import Flask, render_template, jsonify
import pandas as pd
from src.analysis import perform_analysis

app = Flask(__name__)

# Route für die Startseite
@app.route('/')
def home():
    try:
        # Lade die bereinigten Daten aus der CSV-Datei
        df = pd.read_csv('../data/cleaned_data.csv')
        # Konvertiere die Daten in ein JSON-Format
        return jsonify(df.to_dict(orient='records'))
    except Exception as e:
        return jsonify({"error": str(e)})

# Route für Visualisierungen
@app.route('/visualization')
def visualization():
    return "<h2>Hier könnten Visualisierungen eingebettet werden</h2>"

# Route für Analyseergebnisse
@app.route('/analysis')
def analysis():
    try:
        # Lade die bereinigten Daten
        df = pd.read_csv('../data/cleaned_data.csv')
        # Führe die Analyse durch
        results = perform_analysis(df)
        # Gebe die Ergebnisse im JSON-Format zurück
        return jsonify(results)
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)