CREATE TABLE "songplays" (
  "songplay_id" INT PRIMARY KEY NOT NULL,
  "time_key" INT,
  "user_id" INT,
  "level" VARCHAR,
  "song_id" VARCHAR,
  "artist_id" VARCHAR,
  "session_id" INT,
  "location" VARCHAR,
  "user_agent" VARCHAR,
  "create_timestamp" timestamp,
  "modified_timestamp" timestamp
);

CREATE TABLE "users" (
  "user_id" INT PRIMARY KEY NOT NULL,
  "first_name" VARCHAR,
  "last_name" VARCHAR,
  "gender" CHAR(1),
  "level" VARCHAR NOT NULL,
  "create_timestamp" timestamp,
  "modified_timestamp" timestamp
);

CREATE TABLE "songs" (
  "song_id" VARCHAR PRIMARY KEY NOT NULL,
  "title" VARCHAR,
  "artist_id" VARCHAR NOT NULL,
  "year" INT,
  "duration" NUMERIC,
  "create_timestamp" timestamp,
  "modified_timestamp" timestamp
);

CREATE TABLE "artists" (
  "artist_id" VARCHAR PRIMARY KEY NOT NULL,
  "name" VARCHAR,
  "location" VARCHAR,
  "latitude" VARCHAR,
  "longitude" VARCHAR,
  "create_timestamp" timestamp,
  "modified_timestamp" timestamp
);

CREATE TABLE "TIME" (
  "time_key" INT PRIMARY KEY NOT NULL,
  "start_time" TIME NOT NULL,
  "hour" INT,
  "day" INT,
  "week" INT,
  "month" INT,
  "year" INT,
  "weekday" INT,
  "create_timestamp" timestamp,
  "modified_timestamp" timestamp
);

ALTER TABLE "songplays" ADD FOREIGN KEY ("time_key") REFERENCES "TIME" ("time_key");

ALTER TABLE "songplays" ADD FOREIGN KEY ("user_id") REFERENCES "users" ("user_id");

ALTER TABLE "songplays" ADD FOREIGN KEY ("song_id") REFERENCES "songs" ("song_id");

ALTER TABLE "songplays" ADD FOREIGN KEY ("artist_id") REFERENCES "artists" ("artist_id");
