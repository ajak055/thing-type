from flask import jsonify


def success_response(data, code=None):
    status_code = None
    if code:
        status_code = code
    else:
        status_code = 200
    return jsonify(data), status_code


def failure_response(error):
   return jsonify({"message": error.message}), error.codes