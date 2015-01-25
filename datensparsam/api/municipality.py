# -*- coding: utf-8 -*-
from flask import Blueprint, jsonify


municipality = Blueprint('municipality', __name__, url_prefix='/municipality')


@municipality.route('/ping', methods=['GET'])
def ping():
    return jsonify(ping='pong')
