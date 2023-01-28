import pandas as pd
from sqlalchemy import create_engine
import os

#assign directory
directory = '/home/sakabuana31/training/create_data/source/'
for files in os.listdir(directory):
    file_path = os.path.join(directory,files)
    #create file name
    file_name = os.path.basename(file_path).split('.')[0]

    if os.path.isfile(file_path):
        print(file_name)
        #create data framework
        df=pd.read_csv(file_path, sep=',')
        #create engine
        engine = create_engine('postgresql://postgres:postgres@localhost:5432/postgres')
        df.to_sql(file_name, engine, if_exists='replace')
        