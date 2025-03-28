import csv
from pymongo import MongoClient

class User:
    def __init__(self):
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client["survey_db"]
        self.collection = self.db["user_data"]

    def export_to_csv(self, filename="data.csv"):
        users = self.collection.find()
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Age", "Gender", "Total Income", "Category", "Amount"])

            for user in users:
                for category, amount in user.get("expenses", {}).items():
                    writer.writerow([
                        user["age"],
                        user["gender"],
                        user["total_income"],
                        category,
                        amount
                    ])

# Run this file to export data
if __name__ == "__main__":
    u = User()
    u.export_to_csv()
    print("Data exported to data.csv")
