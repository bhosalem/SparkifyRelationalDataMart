# Sparkify Data warehouse
This project aims at building a datamart to help Sparkify(a music streaming company) analyze their user data.Since data resides in json log and song data files, the team decides to build a schema to contain this data locaded from the json logs.

Since the analytics queries are read heavy, a schema which better suits the faster read performance would be STAR schema as described in the schema design diagram below.
![Sparkify Star Schema]()

## 1. Data files:
     There are two data feed files
### Song Data file:
      Type : json
      file location: song_data/*/*/*/*.json
      Sample Data: {"num_songs": 1, "artist_id": "ARJIE2Y1187B994AB7", "artist_latitude": null, "artist_longitude": null, "artist_location": "", "artist_name": "Line Renaud", "song_id": "SOUPIRU12A6D4FA1E1", "title": "Der Kleine Dompfaff", "duration": 152.92036, "year": 0}
### Log data:
      Type : json
      file location : log_data/*/1*/*-events.json
      Sample Data:
      ![Log data]()
      
# Sample Analytics Queries
## 1. Paid subscription users location wise
    ![Paid User Subscriptions Locationwise](/home/workspace/Paid_users_count_locationwise.png)
