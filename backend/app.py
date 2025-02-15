from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
from dotenv import load_dotenv
import logging

# Load environment variables first
load_dotenv('../.env')

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Import utils
try:
    from utils.ocr import extract_text_from_image
    from utils.code_generator import generate_code
except ImportError as e:
    logger.error(f"Import error: {e}")
    raise

app = Flask(__name__, static_folder='../frontend', static_url_path='/')
CORS(app)

# Verify paths
frontend_path = os.path.abspath(app.static_folder)
logger.debug(f"Final static path: {frontend_path}")

@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/styles/<path:filename>')
def serve_styles(filename):
    return send_from_directory(os.path.join(app.static_folder, 'styles'), filename)

@app.route('/scripts/<path:filename>')
def serve_scripts(filename):
    return send_from_directory(os.path.join(app.static_folder, 'scripts'), filename)

@app.route('/api/convert', methods=['POST'])
def convert_image():
    try:
        if not request.is_json:
            return jsonify({'error': 'Request must be JSON'}), 400
            
        data = request.get_json()
        image_data = data.get('image')
        framework = data.get('framework', 'react')
        
        if not image_data:
            logger.warning("No image data in request")
            return jsonify({'error': 'No image provided'}), 400
            
        extracted_text = extract_text_from_image(image_data)
        generated_code = generate_code(extracted_text, framework)
        
        if "Error" in generated_code:
            return jsonify({'error': generated_code}), 500
            
        return jsonify({
            'text': extracted_text,
            'code': generated_code
        })
        
    except Exception as e:
        logger.error(f"Error in conversion: {str(e)}", exc_info=True)
        return jsonify({'error': str(e)}), 500

# This MUST be at the base indentation level
if __name__ == '__main__':
    if not os.path.exists(frontend_path):
        logger.error(f"Missing frontend at: {frontend_path}")
        raise FileNotFoundError("Frontend directory not found")
        
    app.run(host='0.0.0.0', port=5000, debug=True)