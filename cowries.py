import uuid,random,time
from flask import Flask
from flask_restful import Resource, Api

app= Flask(__name__)  #initializing flask app
api = Api(app)
Timestamp_UUID = []
 
class Item(Resource):  #creating a get resource
    def get(self):
        rnd = random.Random()   
        new_uuid = uuid.UUID(int=rnd.getrandbits(128), version=4)
        Time = time.time()
        timestamp = time.ctime(Time)
        print(timestamp)
        new_data = {timestamp:str(new_uuid)}
        Timestamp_UUID.append(new_data)
        return Timestamp_UUID, 201

api.add_resource(Item, "/")   #route to home page "127.0.0.1:5000/"
if __name__== "__main__":
    app.run(debug=True) 





