from flask import Flask, redirect, url_for, jsonify,send_file
from fetch_data import fetch_weather_data
from process_data import process_weather_data
from config import CSV_FILE, EXCEL_FILE, XML_FILE
from convert_data import convert_to_csv, convert_to_excel, convert_to_xml

app = Flask(__name__)

@app.route("/get_weather_data",methods=["GET"])
def get_weather_data():
    weather_data = fetch_weather_data()
    if "error" in weather_data:
        return jsonify(weather_data), 400
    processed_data = process_weather_data(weather_data)
    if isinstance(processed_data, tuple):
        error_body, status_code = processed_data
        return jsonify(error_body), status_code
    csv_file = convert_to_csv(processed_data)
    excel_file = convert_to_excel(processed_data)
    xml_file = convert_to_xml(processed_data)
    return jsonify({
        "message": "Weather data fetched and processed successfully.",
        "csv_file": csv_file,
        "excel_file": excel_file,
        "xml_file": xml_file
    })
    
@app.route("/download_csv",methods=["GET"])
def download_csv():
    return send_file(CSV_FILE, as_attachment=True)   

@app.route("/download_excel",methods=["GET"])
def download_excel():
    return send_file(EXCEL_FILE, as_attachment=True)
    
@app.route("/download_xml",methods=["GET"])
def download_xml():
    return send_file(XML_FILE, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
    
