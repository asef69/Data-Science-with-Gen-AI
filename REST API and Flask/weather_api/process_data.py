import pandas as pd

def process_weather_data(raw_data):
    if 'error' in raw_data:
        return raw_data, 400
    
    processed_data = {
        "City": raw_data.get("name"),
        "Temperature": raw_data.get("main", {}).get("temp"),
        "Humidity": raw_data.get("main", {}).get("humidity"),
        "Weather": raw_data.get("weather", [{}])[0].get("description")
    }
    
    df = pd.DataFrame([processed_data])
    df.fillna("Unknown", inplace=True)
    return df