"""
Flask server for PyAminoac REST API.
"""

from flask import Flask, request, jsonify, render_template
import logging
import datetime
from .translator import translate_text

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Create Flask app
app = Flask(__name__, 
            template_folder='templates')

@app.route('/')
def index():
    """
    Main page of the API.
    
    Returns:
        Rendered HTML template
    """
    current_year = datetime.datetime.now().year
    
    return render_template(
        'index.html', 
        title='PyAminoac REST API',
        service_name='PyAminoac Translation Service',
        api_title='PyAminoac Translation Service',
        api_subtitle='A REST API for text translation',
        api_description='This service provides an API for translating text via the PyAminoac system. Use the interface below to test the API endpoints.',
        port=app.config.get('PORT', 8963),
        year=current_year
    )

@app.route('/translate', methods=['GET'])
def translate():
    """
    Endpoint to translate text.
    
    Query parameters:
        text: The text to translate
        
    Returns:
        JSON with translated text
    """
    text = request.args.get('text', '')
    
    if not text:
        return jsonify({
            'error': 'No text provided',
            'status': 'error'
        }), 400
    
    try:
        translated = translate_text(text)
        return jsonify({
            'original': text,
            'translated': translated,
            'status': 'success'
        })
    except Exception as e:
        logger.error(f"Error translating text: {str(e)}")
        return jsonify({
            'error': str(e),
            'status': 'error'
        }), 500

@app.route('/health', methods=['GET'])
def health():
    """
    Health check endpoint.
    
    Returns:
        Status of the service
    """
    return jsonify({
        'status': 'healthy',
        'service': 'pyaminoac'
    })

def run_server(host='0.0.0.0', port=8963, debug=False):
    """
    Run the Flask server.
    
    Args:
        host: Host to bind to
        port: Port to bind to
        debug: Whether to run in debug mode
    """
    # Store port in app config to make it available to templates
    app.config['PORT'] = port
    
    logger.info(f"Starting PyAminoac server on {host}:{port}")
    app.run(host=host, port=port, debug=debug)

if __name__ == '__main__':
    run_server(debug=True)