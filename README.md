# Sparkify Data Mart
This project aims at building a datamart to help Sparkify(a music streaming company) analyze their user data.Since data resides in json log and song data files, the team decides to build a schema to contain this data locaded from the json logs.


Since the analytics queries are read heavy, a schema which better suits the faster read performance would be STAR schema as described in the schema design diagram below.Columns marked as **bold** in the diagram are Primary keys for those tables/entities. Lines connecting entities represents Foreign key relationships between tables
![Sparkify Star Schema](https://github.com/bhosalem/SparkifyDataWarehouse/blob/bhosalem-patch-1/Sparkify_Star_schema.png)


## 1. Data files:
     There are two data feed files
### Song Data file:
      Type : json
      contains : This file contains data columns for dimensions songs and artists
      Sample Data: {"num_songs": 1, "artist_id": "ARJIE2Y1187B994AB7", "artist_latitude": null, "artist_longitude": null, "artist_location": "", "artist_name": "Line Renaud", "song_id": "SOUPIRU12A6D4FA1E1", "title": "Der Kleine Dompfaff", "duration": 152.92036, "year": 0}
### Log data:
      Type : json
      contains : This file contains data columns for dimensions users and time
      Sample Data:
 bhosalem-patch-1
![Log data](https://github.com/bhosalem/SparkifyDataWarehouse/blob/bhosalem-patch-1/log-data.png)

## 2. Dimension tables:
   Songs, users, artists and time are the four dimesion tables as seen n the schema diagram. Refer the [DDL](https://github.com/bhosalem/SparkifyDataWarehouse/blob/bhosalem-patch-1/Sparkify_DDL.sql) for the columns and datatypes
   for each of the dimension tables. 
   All the dimension tables are of type **Slowly Changing Dimension Type -1**. It means that each of the dimensions will maintain only the latest information for the files loaded.
E.g: If User A was opting the for free subscription till 21st April 2019 and switched to paid at a later data then table user will reflect 'level' as 'Paid'. Earlier record for that user gets overwritten to Paid. This avoids any dupliaction as well in the dimensions.

## 3. Fact Table:
     The fact table songplays contains dimensional keys from dimensions ae well as few events. It essentially is an events table.
     E.g Number of users which change to paid subscription in given period of time and vice-versa. This table will be used to derive different insights for anlytics.
  
# Run Instructions:
1. Run "python create_tables.py" file from command line
   Creates tables, sequences required for building schema
2. Run "python etl.py" from command line
   Extracts data from song data and log data files and loads them in respective tables.

   
=======
![Log-Data](https://github.com/bhosalem/SparkifyDataWarehouse/blob/master/log-data.png)
      

# Sample Analytics Queries
## 1. Paid subscription users location wise
![Paid User Subscriptions Locationwise](https://github.com/bhosalem/SparkifyDataWarehouse/blob/bhosalem-patch-1/Paid_users_count_locationwise.PNG)
