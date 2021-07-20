from flask import Flask
from flask_restful import Resource, Api, reqparse
import yamlModels.hostname
import yamlModels.statics
import InputData
app = Flask(__name__)
api = Api(app)

class Users(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('infrastructureKey', required=True)
        parser.add_argument('projectKey', required=True)
        parser.add_argument('projectName', required=True)
        args = parser.parse_args() 
        dataAsClass = InputData.GetInputDataFromJson(args)
        yamlData = yamlModels.hostname.Hostname.CreateHostname(dataAsClass.infrastructureKey, dataAsClass.projectKey,dataAsClass.projectName)
        print(yamlData)
        return yamlData, 200
    pass

api.add_resource(Users, '/users') 

if __name__ == '__main__':
    app.run()  # run our Flask app