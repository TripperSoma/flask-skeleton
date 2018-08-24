from flask import Blueprint, render_template, request, jsonify
from SDIC import ALLOWED_EXTENSIONS, app
import uuid, os
import random

bp = Blueprint('index', __name__)
tests = {}


@app.route('/taste', methods=['GET'])
def Message():
    dataSend = {
        "data" : "data"
    }
    return jsonify(dataSend)
