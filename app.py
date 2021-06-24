from flask import Flask, request
from flask_restful import Resource, Api
import pickle

app = Flask(__name__)
api = Api(app)

def params():
    funding = float(request.args['funding'])
    Emp_count = float(request.args['Emp_count'])
    N_advisor = float(request.args['N_advisor'])
    part_start = float(request.args['part_start'])
    worked_top = float(request.args['worked_top'])
    bothps = float(request.args['bothps'])
    product = float(request.args['product'])
    service = float(request.args['service'])
    part_suc_strt = float(request.args['part_suc_strt'])
    bachelors = float(request.args['bachelors'])
    masters = float(request.args['masters'])
    nodegree = float(request.args['nodegree'])
    phd = float(request.args['phd'])
    model=pickle.load(open('newm.pkl','rb'))
    prediction=model.predict([[funding,Emp_count,N_advisor,part_start,worked_top,bothps,product,service,part_suc_strt,bachelors,masters,nodegree,phd]])
    return str(prediction[0]) 
class HelloWorld(Resource):
    def get(self):
        

        return params()

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)