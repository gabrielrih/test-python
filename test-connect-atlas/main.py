'''
    MongoDB Atlas connection test
    References:
        https://www.mongodb.com/docs/drivers/pymongo/
'''
from pymongo import MongoClient
from arguments import get_arguments

# Getting information for connection
endpoint, username, password, database, collection = get_arguments()
conn_str_model = 'mongodb+srv://<username>:<password>@<endpoint>/<database>?retryWrites=true&w=majority'
conn_str = conn_str_model.replace('<username>', username).replace('<password>', password).replace('<endpoint>', endpoint).replace('<database>', database)

# Try connection
# set a 5-second connection timeout
client = MongoClient(conn_str, serverSelectionTimeoutMS=5000)
try:
    print("Success!")
    #print(client.server_info())
except Exception:
    print("Unable to connect to the server.")

print("(+) Setting namespace " + database + "." + collection)
try:
    db = client[database]
    collection = db[collection]
except Exception as ex:
    print(str(ex))
    exit(1)

print("(+) Inserting document")
try:
    collection.insert_one({"message": "We're here for tech and beer! \o/"})
except Exception as ex:
    print(str(ex))
    exit(1)

print("(+) Retriving data on database")
try: 
    data = collection.find_one()
    print(data)
except Exception as ex:
    print(str(ex))
    exit(1)

print("(+) Deleting data on database")
try:
    collection.delete_one({"_id": data["_id"]})
except Exception as ex:
    print(str(ex))
    exit(1)