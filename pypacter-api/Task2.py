from flask import Flask, request, jsonify
from lang_detect import detect_language

app = Flask(__name__)

@app.route('/detect_language', methods=['POST'])
def api_detect_language():
    try:
        # Get code snippet from request
        code_snippet = request.json['code_snippet']
        
        # Detect language
        language = detect_language(code_snippet)
        
        # Return detected language
        return jsonify({'language': language}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
