from flask import Flask, jsonify
from pymongo import MongoClient
from flask_cors import CORS


app = Flask(__name__)
cors = CORS(app, resources={r'/orders':{'origins': '*'}})

client = MongoClient("mongodb+srv://db_user_read:LdmrVA5EDEv4z3Wr@cluster0.n10ox.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client.RQ_Analytics

@app.route('/', methods=['GET'])
def get_data():
    data = list(db.shopifyOrders.find({}, {'_id': 0}))
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)