#!/usr/bin/env python3
"""
Function that returns all students sorted by average score from a MongoDB collection.
"""

from pymongo import MongoClient

def top_students(mongo_collection):
    """
    Returns all students sorted by average score.

    :param mongo_collection: The pymongo collection object
    :return: List of students sorted by average score
    """
    pipeline = [
        {
            "$project": {
                "name": 1,
                "averageScore": { "$avg": "$scores.score" }
            }
        },
        {
            "$sort": { "averageScore": -1 }
        }
    ]
    return list(mongo_collection.aggregate(pipeline))

if __name__ == "__main__":
    client = MongoClient('mongodb://localhost:27017/')
    db = client.students_db
    collection = db.students
    for student in top_students(collection):
        print(student)

