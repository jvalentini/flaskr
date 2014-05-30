from flask import Flask
from flask.ext.restful import Resource, Api, reqparse
import json
import unittest

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['TESTING'] = True

api = Api(app)

class FlaskrController(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        # I don't want to use action='append' because the order of the tasks matter
        parser.add_argument('tasks',
                            required=True, location='json',
                            help='Missing tasks')
        args = parser.parse_args()

        print args['tasks'].__class__
        return 'test'


api.add_resource(FlaskrController, '/')


class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = True
        self.app = app.test_client()

    def test_simple(self):
        params = {'tasks': 1}
        response = self.app.post('/', data=json.dumps(params), content_type='application/json')
        print response.data
        assert response.status_code == 200

    def test_example(self):
        task1 = {'key': 1}
        task2 = {'key': 2}
        params = {'tasks': [task1, task2]}
        response = self.app.post('/', data=json.dumps(params), content_type='application/json')
        print response.data
        assert response.status_code == 200


if __name__ == '__main__':
    unittest.main()
