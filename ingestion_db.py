# import pandas as pd
# import os
# from sqlalchemy import create_engine
# # import mysql.connector

# # isse pta lge kitne time mein load
# import time
# import logging

# logging.basicConfig(
#     filename="logs/ingestion_db.log",
#     level=logging.DEBUG,
#     format= "%(asctime)s - %(levelname)s - %(message)s",
#     # a means append
#     filemode ="a"
# )

# engine=create_engine('sqlite:///inventory.db')
# def ingest_db(df,table_name,engine):
#     # dataframe into database table
#     df.to_sql(table_name,con=engine,if_exists='replace',index=False)
    
# def load_raw_data():
#     # this function will load csv as dataframe and ingest into db
    
#     start=time.time()
#     for file in os.listdir('data'):
#     if '.csv' in file:
#         df=pd.read_csv('data/'+file)
#         logging.info(f'Ingesting {file} in db')
#         ingest_db(df,file[:-4],engine)
#      end=time.time()
#      total_time= (end-start)/60
#      logging.info('---------------Ingestion complete------------------')    

#      logging.info(f'\ntotal time taken: {total_time} minutes')

# if __name__ == '__main__':
#     load_raw_data()





import pandas as pd
import os
from sqlalchemy import create_engine
# import mysql.connector

# isse pta lge kitne time mein load
import time
import logging

logging.basicConfig(
    filename="logs/ingestion_db.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a"   # append mode
)

engine = create_engine('sqlite:///inventory.db')


def ingest_db(df, table_name, engine):
    # dataframe into database table
    df.to_sql(table_name, con=engine, if_exists='replace', index=False)


def load_raw_data():
    # this function will load csv as dataframe and ingest into db

    start = time.time()

    for file in os.listdir('data'):
        if '.csv' in file:
            df = pd.read_csv('data/' + file)
            logging.info(f'Ingesting {file} in db')
            ingest_db(df, file[:-4], engine)

    end = time.time()

    total_time = (end - start) / 60

    logging.info('---------------Ingestion complete------------------')
    logging.info(f'\nTotal time taken: {total_time:.2f} minutes')


if __name__ == '__main__':
    load_raw_data()