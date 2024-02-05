#!/usr/bin/python3
"""Create routes"""
from api.v1.views import app_views
from flask import jsonify
@app.views.route("/status", methods=["GET"], strict_slashes=False)
def status():
    """Get status"""
    return jsonify({"status": "OK"})
