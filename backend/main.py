from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

from functions import analyze_file

app = Flask(__name__)

app.config.from_object(__name__)

CORS(app, resources={r"/*": {"origins": "*"}})  # Allow all origins


@app.route('/analyze', methods=['POST'])
@cross_origin(supports_credentials=True)
def analyze():
    print(' - - - - -  - - - -  - - - -  - - - - - - - - - - - -  - - - - - - - -')
  
    if 'file' not in request.files:
        return jsonify(message='No file provided'), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify(message='No selected file'), 400

    # Process the file or form data here
    # For demonstration, you can access the file name:
    # print('Uploaded File Name:', file.filename)
    
    analyze_file(file)
    return 'passed'
    
    
@app.route('/values', methods=['GET'])
def get_values():
    # Retrieve the previously analyzed values
    # For demonstration, we'll return a dummy response
    analyzed_values = { "value1": 123, "value2": 456 }
    return jsonify(analyzed_values)

if __name__ == "__main__":
       app.run(debug=True,host='0.0.0.0', port=3000)