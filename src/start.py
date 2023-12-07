# onboard imports
from datetime import date, datetime

# user imports
from secret_credentials import *

# 3rd party imports
import pandas as pd
from influxdb import InfluxDBClient


def main():
    new_sample = SampleHandler().new_sample()
    
    print(new_sample) 


class SampleHandler():
    def __init__(self) -> None:
        pass
      
            
    def new_sample(self):        
        sample = {"Datum" : date.today(),
                  "Bad" : "",
                  "Schlafzimmer" : "",
                  "Kinderzimmer" : "",
                  "Wohnzimmer" : "",
                  "Esszimmer" : "",
                  "Buero" : ""}
        
        for key in sample:
            if not key == "Datum":
                sample[key] = input(f"Set value for {key}: ")
        print("Current sample: ")
        for key in sample:
            print(key, ": ", sample[key])
        print("")
        sample = self.__accept_sample(sample)
        return sample    
        

    def __accept_sample(self, sample):
        user_accepts = input("Accept current sample? (y/n)")
        if user_accepts == ("y" or "j" or "yes"):
            return sample
        elif user_accepts == ("n" or "no"):
            sample = self.change_sample(sample)        
            return sample
        else:
            self.__accept_sample(sample)
        

    def change_sample(self, sample):
        change_key = input("Type key to change: ")
        if not change_key in sample:
            # TODO: avoid recursion
            print("\nKey is not in sample. Try again!\n")
            self.change_sample(sample)
            return
        change_value = input("Type new value: ")
        if change_key == "Datum":      
            # TODO: catch ValueError exception
            change_value = datetime.strptime(change_value, "%d.%m.%Y").date()
        sample[change_key] = change_value
        return sample
    

class HomeDBClient():
    def __init__(self) -> None:
        pass
     
    
    def connect_to_influxdb(self, database, host=influx_host, 
                            port=influx_port, username=influx_user, 
                            password=influx_pw):
        """connects to given InfluxDB database via client

        Args:
            database (str): the database to connect to
            host (str, optional): host ip address. Defaults to influx_host.
            port (int, optional): host ip port. Defaults to influx_port.
            username (str, optional): 
                username for influx client. Defaults to influx_user.
            password (str, optional): 
                password for influx client. Defaults to influx_pw.
        """
        client = InfluxDBClient(host=host, port=port, username=username, 
                                password=password)
        client.switch_database(database)
      
      
if __name__ == "__main__":
    main()