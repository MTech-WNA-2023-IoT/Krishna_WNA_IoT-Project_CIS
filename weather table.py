import mysql.connector

# Connect to MySQL database
db = mysql.connector.connect(
    host='0.0.0.0',
    user='krishna',
    password='KRISHNA',
    database='WeatherAPI'
)

# Execute the create table query
db_cursor = db.cursor()
create_table_query = """
CREATE TABLE weather_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    location_name VARCHAR(255),
    region VARCHAR(255),
    country VARCHAR(255),
    latitude FLOAT,
    longitude FLOAT,
    timezone_id VARCHAR(255),
    localtime_epoch BIGINT,
    local_time DATETIME,
    last_updated_epoch BIGINT,
    last_updated DATETIME,
    temp_c FLOAT,
    temp_f FLOAT,
    is_day INT,
    condition_text VARCHAR(255),
    condition_icon VARCHAR(255),
    condition_code INT,
    wind_mph FLOAT,
    wind_kph FLOAT,
    wind_degree INT,
    wind_dir VARCHAR(255),
    pressure_mb FLOAT,
    pressure_in FLOAT,
    precip_mm FLOAT,
    precip_in FLOAT,
    humidity INT,
    cloud INT,
    feelslike_c FLOAT,
    feelslike_f FLOAT,
    vis_km FLOAT,
    vis_miles FLOAT,
    uv FLOAT,
    gust_mph FLOAT,
    gust_kph FLOAT
);
"""
db_cursor.execute(create_table_query)

# Close the connection
db.close()

print("Table created successfully!")
