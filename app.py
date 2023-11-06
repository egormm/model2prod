import os

from flask import request, Flask, jsonify, Response, send_from_directory

from authentication import check_api_token_header
from image_transform import image_to_matrix
from model import predict
import dotenv

dotenv.load_dotenv()
app = Flask(__name__)
app.config['ALLOWED_API_TOKENS'] = os.getenv('API_TOKENS').split(',')


@app.route('/')
def index():
    return send_from_directory('static', 'index.html')


@app.route('/predict', methods=['POST'])
@check_api_token_header
def post_predict_handler() -> Response:
    if request.mimetype == 'application/json':
        features = request.json['images']
    else:
        file = request.files['image']
        features = image_to_matrix(file.read(), 32, 32)
    prediction = predict(features)
    return jsonify(prediction=prediction)


if __name__ == '__main__':
    app.run()
