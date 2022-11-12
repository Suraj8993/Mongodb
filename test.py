import pymongo

client = pymongo.MongoClient("mongodb+srv://Suraj:Suraj143@cluster0.8qp0yum.mongodb.net/?retryWrites=true&w=majority")
db = client.test

data = {
    "name" : "sudhanshu",
    "mail_id" : "sudhanshu@ineuron.ai",
    "subject" : ["data scinece" , "big data " , "data analytics "]
}

database = client['myinfo']
collection = database["sudh"]
collection.insert_one(data)
