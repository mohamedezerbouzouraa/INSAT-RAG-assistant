from flask import Flask
from flask_cors import CORS
from routes.chat_routes import chat_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(chat_bp)
if __name__ == "__main__":
    app.run(debug=False, port=5000)
