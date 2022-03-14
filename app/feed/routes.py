from flask import Blueprint, render_template

feed = Blueprint('feed', __name__, template_folder='feed_templates')

@feed.route('/browse')
def browse():
    return render_template('browse.html')