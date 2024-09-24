from flask import Flask, request, jsonify
from DataXtractor import DataXtractor
import base64
import io

app = Flask(__name__)
extractor = DataXtractor()

@app.route('/extract', methods=['POST'])
def extract_data():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected for uploading'}), 400
    
    # Read the file
    file_bytes = file.read()
    file_obj = io.BytesIO(file_bytes)
    
    # Extract data
    result = extractor.extract(file_obj)
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
