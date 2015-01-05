#!/usr/bin/env python

import json

import argparse
from flask import Flask, render_template

import app_config
from render_utils import make_context, smarty_filter, urlencode_filter
import static

app = Flask(__name__)

app.jinja_env.filters['smarty'] = smarty_filter
app.jinja_env.filters['urlencode'] = urlencode_filter

# Example application views
@app.route('/')
def index():
    """
    Example view demonstrating rendering a simple HTML page.
    """
    context = make_context()

    with open('data/featured.json') as f:
        context['featured'] = json.load(f)

    return render_template('index.html', **context)

@app.route('/widget.html')
def widget():
    """
    Embeddable widget example page.
    """
    return render_template('widget.html', **make_context())

@app.route('/test_widget.html')
def test_widget():
    """
    Example page displaying widget at different embed sizes.
    """
    return render_template('test_widget.html', **make_context())

@app.route('/date.html')
def date_page():
    """
    Example page displaying widget at different embed sizes.
    """
    context = make_context()

    return render_template('date.html', **context)

@app.route('/date-oldest.html')
def date_oldest_page():
    """
    Example page displaying widget at different embed sizes.
    """
    context = make_context()

    return render_template('date-oldest.html', **context)

@app.route('/topic.html')
def topic_page():
    """
    Example page displaying widget at different embed sizes.
    """
    context = make_context()

    with open('data/featured.json') as f:
        context['featured'] = json.load(f)
    
    return render_template('topic.html', **context)
    
@app.route('/date_embed.html')
def date_embed_page():
    """
    Example page displaying widget at different embed sizes.
    """
    return render_template('date_embed.html', **make_context())
    
@app.route('/topic_embed.html')
def topic_embed_page():
    """
    Example page displaying widget at different embed sizes.
    """
    return render_template('topic_embed.html', **make_context())
    
@app.route('/map.html')
def map_page():
    """
    Example page displaying widget at different embed sizes.
    """
    return render_template('map.html', **make_context())
    
@app.route('/evidence.html')
def evidence_page():
    """
    Example page displaying widget at different embed sizes.
    """
    return render_template('evidence.html', **make_context())
    
@app.route('/photos.html')
def photos_page():
    """
    Example page displaying widget at different embed sizes.
    """
    return render_template('photos.html', **make_context())
    
@app.route('/audio.html')
def audio_page():
    """
    Example page displaying widget at different embed sizes.
    """
    return render_template('audio.html', **make_context())    
    
@app.route('/liveblog.html')
def liveblog_page():
    """
    Example page displaying widget at different embed sizes.
    """
    return render_template('liveblog.html', **make_context())        

app.register_blueprint(static.static)

# Boilerplate
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port')
    args = parser.parse_args()
    server_port = 8000

    if args.port:
        server_port = int(args.port)

    app.run(host='0.0.0.0', port=server_port, debug=app_config.DEBUG)
