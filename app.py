from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb+srv://Database:Starboy%4025@cluster0.vkyiq.mongodb.net/")  # Connect to MongoDB
db = client["survey_database"]  
collection = db["responses"] 

@app.route("/")
def index():

    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    # get form data

        data = {
            "age": request.form["age"],
            "gender": request.form["gender"],
            "total_income": float(request.form["total_income"]),
            "expenses": {
                "utilities": float(request.form.get("utilities", 0)),
                "entertainment": float(request.form.get("entertainment", 0)),
                "school_fees": float(request.form.get("school_fees", 0)),
                "shopping": float(request.form.get("shopping", 0)),
                "healthcare": float(request.form.get("healthcare", 0)),
            },
        }
        collection.insert_one(data)  # Save data to MongoDB

        return jsonify({'message': 'Data submitted sucessfully:'}), 200


if __name__ == "__main__":
    app.run(debug=True)
