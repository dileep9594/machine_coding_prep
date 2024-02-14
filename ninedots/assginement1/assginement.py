from datetime import datetime, timedelta
import pandas as pd
from pymongo import MongoClient

from subscriptionanalyzer import SubscriptionAnalyzer


if __name__ == '__main__':
    # Connect to MongoDB
    client = MongoClient("mongodb+srv://root:root@cluster0.upi4ff4.mongodb.net/?retryWrites=true&w=majority")
    db = client["assginements"]
    collection = db["ninedots"]

    # analyzer = SubscriptionAnalyzer(client, db, collection)

    # # 1. How many active subscriptions were present as of 3/1/2020?
    # count = analyzer.active_subscriptions_count(datetime(2020, 3, 1))
    # print(f"1. Active Subscriptions Count: {count}")

    # # 2. What were the expected renewal dates associated with the active subscriptions in (1)?
    # renewal_dates = analyzer.expected_renewal_dates(datetime(2020, 3, 1))
    # print(f"2. Expected Renewal Dates: {renewal_dates}")

    # # 3. How many of the subscriptions identified in (1) renewed?
    # renewed_count = analyzer.renewed_subscriptions_count(datetime(2020, 3, 1))
    # print(f"3. Renewed Subscriptions Count: {renewed_count}")

    # 4. What potential issues do you see with identifying renewals using your method in (3) vs. actually identifying the renewal subscription version with a unique key?
    # analyzer.potential_issues()

    # Convert date strings to ISODate format
    # for document in collection.find({}):
    #     start_date = datetime.strptime(document["EFFECTIVE_START_DATE"], "%m/%d/%y")
    #     end_date = datetime.strptime(document["EFFECTIVE_END_DATE"], "%m/%d/%y")

        # Update the document with the new date format
        # collection.update_one(
        #     {"_id": document["_id"]},
        #     {"$set": {"EFFECTIVE_START_DATE": start_date, "EFFECTIVE_END_DATE": end_date}}
        # )

    # Load data from CSV to DataFrame
    # file_path = "/Users/dileeppandey/Downloads/Subscriptions_Snapshot_Dataset.csv"
    # df = pd.read_csv(file_path)

    # Convert DataFrame to list of dictionaries (MongoDB format)
    # data = df.to_dict(orient="records")

    # Insert data into MongoDB
    # collection.insert_many(data)

    # Close MongoDB connection
    # client.close()

    # Now you can use the SQL-like queries on MongoDB data
    # You can use pymongo or other libraries to run the queries, but make sure to adjust the queries accordingly

    # Find the maximum date
    # max_date_query = [
    #     {"$group": {"_id": None, "max_date": {"$max": "$EFFECTIVE_END_DATE"}}}
    # ]
    # max_date_result = list(collection.aggregate(max_date_query))
    # max_date = max_date_result[0]["max_date"] if max_date_result else None
    # print(f"Maximum date: {max_date}")

    # # Find the minimum date
    # min_date_query = [
    #     {"$group": {"_id": None, "min_date": {"$min": "$EFFECTIVE_END_DATE"}}}
    # ]
    # min_date_result = list(collection.aggregate(min_date_query))
    # min_date = min_date_result[0]["min_date"] if min_date_result else None
    # print(f"Minimum date: {min_date}")
    

    pipeline_count = [
    {
        "$match": {
            "EFFECTIVE_END_DATE": {"$gte": datetime(2020, 3, 1)},
            "EFFECTIVE_START_DATE": {"$lt": datetime(2020, 3, 1)}
        }
    },
    {
        "$group": {
            "_id": "$Subscription_ID"
        }
    },
    {
        "$group": {
            "_id": None,
            "no_of_sub_till_march20": {"$sum": 1}
        }
    }
]

    result_count = list(collection.aggregate(pipeline_count))
    print(result_count)

    query_distinct = {
    "EFFECTIVE_END_DATE": {"$gte": datetime(2020, 3, 1)},
    "EFFECTIVE_START_DATE": {"$lt": datetime(2020, 3, 1)}
}

    result_distinct = collection.find(query_distinct).distinct("Subscription_ID")
    print(result_distinct)


    # MongoDB query equivalent to SQL
    query = [
        {"$match": {
            "EFFECTIVE_END_DATE": {"$gte": datetime(2020, 3, 1)},
            "EFFECTIVE_START_DATE": {"$lt": datetime(2020, 3, 1)}
        }},
        {"$group": {
            "_id": "$Subscription_ID",
            "EFFECTIVE_END_DATE": {"$first": "$EFFECTIVE_END_DATE"}
        }},
        {"$match": {
            "EFFECTIVE_END_DATE": {"$gte": datetime(2020, 3, 1)}
        }},
        {"$sort": {"_id": 1}}
    ]

    # Execute the query
    result = list(collection.aggregate(query))

    # Print the result
    for doc in result:
        print(doc)

    days_30_seconds = 30*24*60*60*1000

    query = [
    {"$match": {
        "EFFECTIVE_END_DATE": {"$gte": datetime(2020, 3, 1)},
        "EFFECTIVE_START_DATE": {"$lt": datetime(2020, 3, 1)}
    }},
    {"$group": {
        "_id": "$Subscription_ID",
        "EXPECT_RENEW_DATE_FROM": {"$first": "$EFFECTIVE_END_DATE"}
    }},
    {"$match": {
        "EXPECT_RENEW_DATE_FROM": {"$gte": datetime(2020, 3, 1)}
    }},
    {"$project": {
        "Subscription_ID": "$_id",
        "EXPECT_RENEW_DATE_FROM": 1,
        "EXPECT_RENEW_DATE_TO": {"$add": ["$EXPECT_RENEW_DATE_FROM", days_30_seconds]}
    }},
    {"$sort": {"Subscription_ID": 1}}
]

    # Execute the query
    result = list(collection.aggregate(query))

    # Print the result
    for doc in result:
        print(doc)

    query = [
    {"$match": {
        "EFFECTIVE_END_DATE": {"$gt": datetime(2020, 3, 1)},
        "EFFECTIVE_START_DATE": {"$not": {"$regex": "^2021"}},
        "Subscription_ID": {"$in": [
            doc["_id"] for doc in collection.aggregate([
                {"$match": {
                    "EFFECTIVE_END_DATE": {"$gte": datetime(2020, 3, 1)},
                    "EFFECTIVE_START_DATE": {"$lt": datetime(2020, 3, 1)}
                }},
                {"$group": {
                    "_id": "$Subscription_ID",
                    "EFFECTIVE_END_DATE": {"$max": "$EFFECTIVE_END_DATE"}
                }},
                {"$match": {
                    "EFFECTIVE_END_DATE": {"$gte": datetime(2020, 3, 1)}
                }}
            ])
        ]}
    }},
    {"$group": {
        "_id": "$Subscription_ID",
        "EFFECTIVE_START_DATE": {"$first": "$EFFECTIVE_START_DATE"}
    }},
    {"$sort": {"_id": 1}}
]

    # Execute the query
    result = list(collection.aggregate(query))

    # Print the result
    for doc in result:
        print(doc)

