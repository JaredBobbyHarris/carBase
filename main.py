from flask import Flask
import pymongo
app = Flask(__name__)

try:
    mongo = pymongo.MongoClient(host = "localhost", port = 27017, serverSelectionTimeoutMS = 1500)
    mongo.server_info() #trigger exception if cannot connect to the db
except:
    print("ERROR - cannot connect to the database")

@app.route("/users", methods = ["POST"])
def create_user():
    return "Created user"

if __name__ == "__main__":
    app.run(port = 80, debug = True)

