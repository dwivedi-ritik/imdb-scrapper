from flask import Flask , jsonify

from flask_restful import Api , Resource

from flask_cors import CORS

from webscrap import Movie

app = Flask(__name__)

cors = CORS(app , resources = {r"/*": {"origins": "*" , "Access-Control-Allow-Origin" :"*"}})

api = Api(app)

class Output(Resource):
	def get(self , movie_id):
		try:
			res = Movie(movie_id)
			return jsonify({"data": res.render()})
		except:
			return {"error": "Either IMDB changed their html element or You are trying to acces a movies which is not realesed yet" , "apology": "Sorry :("}

class Error(Resource):
	def get(self):
		return {"error":"Bad request/id is missing" , "eg":"/get_movie/id=your_movie_id/"}

class Error1(Resource):
	def get(self):
		return {"error":"Bad request/id is missing" , "eg":"/get_movie/id=your_movie_id/"}

class Error2(Resource):
	def get(self):
		return {"error":"Bad request/id is missing" , "eg":"/get_movie/id=your_movie_id/"}

api.add_resource(Output , "/get_movie/id=<string:movie_id>/")

api.add_resource(Error , "/get_movie/")

api.add_resource(Error1, "/get_movie/id")

api.add_resource(Error2 , "/")

if __name__ == '__main__':
	app.run()
