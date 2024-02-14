import pymongo
from datetime import datetime, timedelta

class SubscriptionAnalyzer:
    def __init__(self, client, database_name, collection_name):
        self.client = client
        self.db = database_name
        self.collection = collection_name

    def active_subscriptions_count(self, as_of_date):
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
        result_count = list(self.collection.aggregate(pipeline_count))
        result_count
        query_distinct = {
        "EFFECTIVE_END_DATE": {"$gte": datetime(2020, 3, 1)},
        "EFFECTIVE_START_DATE": {"$lt": datetime(2020, 3, 1)}
    }
        result_distinct = self.collection.find(query_distinct).distinct("Subscription_ID")
        print(result_distinct)
        return result_count
    def expected_renewal_dates(self, as_of_date, renewal_window=30):
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
        result = list(self.collection.aggregate(query))

        # Print the result
        for doc in result:
            print(doc)

    def renewed_subscriptions_count(self, as_of_date, renewal_window=30):
       query = [
                {"$match": {
                    "EFFECTIVE_END_DATE": {"$gt": datetime(2020, 3, 1)},
                    "EFFECTIVE_START_DATE": {"$not": {"$regex": "^2021"}},
                    "Subscription_ID": {"$in": [
                        doc["_id"] for doc in self.collection.aggregate([
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
        # Execute the quer
       result = list(self.collection.aggregate(query))
       for doc in result:
           print(doc)
    