# Sparkify Data warehouse
1. Sparkify analytical team wants to analyze the data to understand the user behaviour like what songs their users are listening to from the json logs available from their music streaming app. Since the data is not readily available for the 
analysis, the team decides to build a schema to contain this data locaded from the json logs.

2. Since the analytics queries are read heavy, a schema which better suits the faster read performance would be STAR schema as described in the schema design diagram below.
![Sparkify Star Schema](/home/workspace/star_schema.png)

# Sample Analytics Queries
## 1. Paid subscription users location wise
    ![Paid User Subscriptions Locationwise](/home/workspace/Paid_users_count_locationwise.png)
