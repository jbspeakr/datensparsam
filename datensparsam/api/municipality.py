# -*- coding: utf-8 -*-
from flask import Blueprint, jsonify


blueprint = Blueprint('municipality', __name__, url_prefix='/municipality')


@blueprint.route('/ping', methods=['GET'])
def ping():
    return jsonify(ping='pong')
