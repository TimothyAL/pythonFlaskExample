import os

from flask import  Flask, Blueprint, request, Response
from flask_socketio import SocketIO
from flask_cors import CORS
import werkzeug



app = Flask(__name__, instance_relative_config=True)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.cors_allowed_origins=os.environ['FRONTEND_URL']
from views.functions import functions
app.register_blueprint(functions)

@app.route('/back')
def test():
    return("this is a test")

 
if __name__ == '__main__':
    app.run(host='0.0.0.0', use_reloader=True, debug=True, port=5000)