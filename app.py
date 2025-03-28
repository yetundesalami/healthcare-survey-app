from flask import Flask, render_template, request, redirect
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client["survey_db"]
collection = db["user_data"]

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = {
        "age": int(request.form["age"]),
        "gender": request.form["gender"],
        "total_income": float(request.form["income"]),
        "expenses": {}
    }

    for category in ["utilities", "entertainment", "school_fees", "shopping", "healthcare"]:
        if request.form.get(category):
            amount = float(request.form.get(f"{category}_amount", 0))
            data["expenses"][category] = amount

    collection.insert_one(data)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
