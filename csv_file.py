from flask import Flask, request, jsonify
import csv

app = Flask(index.html)

# Define CSV file path
CSV_FILE = "reviews.csv"

# Ensure CSV file has a header
with open(CSV_FILE, "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Review"])

@app.route("/submit_review", methods=["POST"])
def submit_review():
    data = request.json
    review = data.get("review")

    if not review:
        return jsonify({"message": "Review cannot be empty!"}), 400

    with open(CSV_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([review])

    return jsonify({"message": "Review submitted successfully!"})

if __name__ == "__main__":
    app.run(debug=True)
