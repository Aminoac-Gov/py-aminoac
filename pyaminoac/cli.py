"""
Command-line interface for PyAminoac.
"""

import click
import sys
import logging
from .server import run_server
from .translator import translate_text

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@click.group()
@click.version_option()
def main():
    """PyAminoac - A tool for translating Chinese to Aminoac."""
    pass

@main.command()
@click.argument('text', required=False)
@click.option('--file', '-f', type=click.Path(exists=True), help='Input file path')
@click.option('--output', '-o', type=click.Path(), help='Output file path')
def translate(text, file, output):
    """Translate text from Chinese to reversed pinyin."""
    # Get input text from file or argument
    input_text = ""
    if file:
        try:
            with open(file, 'r', encoding='utf-8') as f:
                input_text = f.read()
        except Exception as e:
            logger.error(f"Error reading file: {str(e)}")
            sys.exit(1)
    elif text:
        input_text = text
    else:
        # Read from stdin if no text or file is provided
        try:
            input_text = sys.stdin.read()
        except KeyboardInterrupt:
            sys.exit(0)
    
    # Translate the text
    try:
        translated_text = translate_text(input_text)
    except Exception as e:
        logger.error(f"Error translating text: {str(e)}")
        sys.exit(1)
    
    # Output the translated text
    if output:
        try:
            with open(output, 'w', encoding='utf-8') as f:
                f.write(translated_text)
            click.echo(f"Translation saved to {output}")
        except Exception as e:
            logger.error(f"Error writing to file: {str(e)}")
            sys.exit(1)
    else:
        click.echo(translated_text)

@main.command()
@click.option('--host', '-h', default='0.0.0.0', help='Host to bind to')
@click.option('--port', '-p', default=8963, help='Port to bind to')
@click.option('--debug', is_flag=True, help='Enable debug mode')
def serve(host, port, debug):
    """Start the REST API server."""
    run_server(host=host, port=port, debug=debug)

if __name__ == '__main__':
    main()