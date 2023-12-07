import pandas as pd
from influxdb import InfluxDBClient

def connect_to_influxdb(database):
    """Initiates a InfluxDBClient and connects to Database

    Args:
        database (str): The database to connect to
    """
    client = InfluxDBClient(host="192.168.178.43", 
                            port="8086", 
                            username="grafana", 
                            password= "grafananana")
    client.switch_database(database)
    
def prepare_point_for_influxdb(date, value):
    measurement = "TEST_measurement"
    fields = 
    


def get_df_from_csv():
    df = pd.read_csv("HKV.csv", index_col="Datum")