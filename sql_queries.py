# DROP TABLES
songplay_table_drop = "DROP TABLE IF EXISTS songplays;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs;"
artist_table_drop = "DROP TABLE IF EXISTS artists;"
time_table_drop = "DROP TABLE IF EXISTS time;"

#DROP sequences 
songplay_seq_drop ="""DROP SEQUENCE IF EXISTS songplay_seq;"""
time_seq_drop = """DROP SEQUENCE IF EXISTS time_seq;"""

#CREATE SEQUENCE FOR FACT TABLE
create_songplay_seq = ("""CREATE SEQUENCE songplay_seq
START 1 INCREMENT 1 NO MAXVALUE CACHE 1;""")

#Time key for time dimension
create_time_seq = ("""CREATE SEQUENCE time_seq
START 1 INCREMENT 1 NO MAXVALUE CACHE 1;""")

# CREATE TABLES

song_table_create = ("""CREATE TABLE IF NOT EXISTS songs 
  ( 
     song_id            VARCHAR PRIMARY KEY NOT NULL, 
     title              VARCHAR, 
     artist_id          VARCHAR, 
     year               INT, 
     duration           NUMERIC, 
     create_timestamp   TIMESTAMP, 
     modified_timestamp TIMESTAMP 
  );""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists 
  ( 
     artist_id          VARCHAR PRIMARY KEY NOT NULL, 
     name               VARCHAR, 
     location           VARCHAR, 
     latitude           VARCHAR, 
     longitude          VARCHAR, 
     create_timestamp   TIMESTAMP, 
     modified_timestamp TIMESTAMP 
  );""")


user_table_create = ("""CREATE TABLE IF NOT EXISTS users 
  ( 
     user_id            INT PRIMARY KEY NOT NULL, 
     first_name         VARCHAR, 
     last_name          VARCHAR, 
     gender             CHAR(1), 
     level              VARCHAR NOT NULL, 
     create_timestamp   TIMESTAMP, 
     modified_timestamp TIMESTAMP 
  );""")


time_table_create = ("""CREATE TABLE IF not EXISTS TIME 
  ( 
     time_key   INT NOT NULL, 
     start_time TIME without TIME zone NOT NULL, 
     hour       INT, 
     day        INT, 
     week       INT, 
     month      INT, 
     year       INT, 
     weekday    INT, 
     create_timestamp timestamp, 
     modified_timestamp timestamp,
     PRIMARY KEY(time_key,start_time)
  );""")

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays 
  ( 
     songplay_id        INT PRIMARY KEY NOT NULL, 
     start_time         TIMESTAMP, 
     user_id            INT, 
     level              VARCHAR, 
     song_id            VARCHAR REFERENCES songs (song_id), 
     artist_id          VARCHAR REFERENCES artists (artist_id), 
     session_id         INT, 
     location           VARCHAR, 
     user_agent         VARCHAR, 
     create_timestamp   TIMESTAMP, 
     modified_timestamp TIMESTAMP 
  );""")

# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO songplays 
            (songplay_id, 
             start_time, 
             user_id, 
             level, 
             song_id, 
             artist_id, 
             session_id, 
             location, 
             user_agent, 
             create_timestamp, 
             modified_timestamp) 
VALUES      (NEXTVAL('songplay_seq'), 
             %s, 
             %s, 
             %s, 
             %s, 
             %s, 
             %s, 
             %s, 
             %s, 
             LOCALTIMESTAMP, 
             NULL);""")

user_table_insert = ("""INSERT INTO users 
            ( 
                        user_id, 
                        first_name, 
                        last_name, 
                        gender, 
                        level, 
                        create_timestamp, 
                        modified_timestamp 
            ) 
            VALUES 
            ( 
                        %s, 
                        %s, 
                        %s, 
                        %s, 
                        %s, 
                        localtimestamp, 
                        NULL 
            ) 
            ON conflict(user_id)
                     DO UPDATE 
            set level=excluded.level, 
                modified_timestamp=localtimestamp;""")

song_table_insert = ("""INSERT INTO songs 
            ( 
                        song_id, 
                        title, 
                        artist_id, 
                        year, 
                        duration, 
                        create_timestamp, 
                        modified_timestamp 
            ) 
            VALUES 
            ( 
                        %s, 
                        %s, 
                        %s, 
                        %s, 
                        %s, 
                        localtimestamp, 
                        NULL 
            ) 
            ON conflict(song_id)
            DO nothing;""")

artist_table_insert = ("""INSERT INTO artists 
            ( 
                        artist_id, 
                        name, 
                        location, 
                        latitude, 
                        longitude, 
                        create_timestamp, 
                        modified_timestamp 
            ) 
            VALUES 
            ( 
                        %s, 
                        %s, 
                        %s, 
                        %s, 
                        %s, 
                        localtimestamp, 
                        NULL 
            ) 
            ON conflict(artist_id) 
                     DO 
            UPDATE 
            SET     location=excluded.location, 
                    latitude=excluded.latitude, 
                    longitude=excluded.longitude, 
                    modified_timestamp=localtimestamp;""")


time_table_insert = ("""INSERT INTO TIME 
            ( 
                        time_key, 
                        start_time, 
                        hour, 
                        day, 
                        week, 
                        month, 
                        year, 
                        weekday, 
                        create_timestamp, 
                        modified_timestamp 
            ) 
            VALUES 
            ( 
                        NEXTVAL('time_seq'), 
                        %s, 
                        %s, 
                        %s, 
                        %s, 
                        %s, 
                        %s, 
                        %s, 
                        localtimestamp, 
                        NULL 
            ) 
            ON conflict(time_key,start_time) 
            DO nothing;""")

# FIND SONGS

song_select = ("""SELECT s.song_id, 
       s.artist_id 
FROM   songs s 
       join artists a 
         ON a.artist_id = s.artist_id 
WHERE  s.title =%s 
       AND a.name =%s 
       AND s.duration =%s;""")

# QUERY LISTS

create_table_queries = [user_table_create, song_table_create, artist_table_create, time_table_create,songplay_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
drop_sequence_queries = [songplay_seq_drop,time_seq_drop]
