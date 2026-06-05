import os
import sys

from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL=os.getenv("MONGO_DB_URL")

import certifi
ca=certifi.where()

import numpy as np
import pandas as pd
import pymongo
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def csv_to_json_conerter(self, file_path):
        try:
            df=pd.read_csv(file_path)
            df.reset_index(drop=True, inplace=True)

            records=df.to_dict(orient='records')

            return records
        
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def insert_data_to_mongodb(self, records, database, collection):
        try:
            self.collection=collection
            self.database=database
            self.records=records

            self.mogo_client = pymongo.MongoClient(MONGO_DB_URL, tlsCAFile=ca)
            self.database = self.mogo_client[self.database]
            self.collection = self.database[self.collection]

            self.collection.insert_many(self.records)

            return len(self.records)

        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
if __name__ == '__main__':
    FILE_PATH = r'Network_Data\phisingData.csv'
    Databse = 'HiteshAI'
    Collection = 'NetworkData'
    networkobj=NetworkDataExtract()
    records=networkobj.csv_to_json_conerter(FILE_PATH)
    print(records)
    no_of_records=networkobj.insert_data_to_mongodb(records, Databse, Collection)
    print(no_of_records)
