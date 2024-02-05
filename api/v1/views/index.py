#!/usr/bin/python3
"""Create routes"""
from api.v1.views import app_views
from flask import jsonify

@app_views.route("/status", methods=["GET"], strict_slashes=False)
def status():
    """Get status"""
    return jsonify({"status": "OK"})
@app_views.route("/api/v1/stats", methods=["GET"], strict_slashes=False)
def number_of_objects():
    """ Retrieves the number of each objects by type """
    classes = [Amenity, City, Place, Review, State, User]
    names = ["amenities", "cities", "places", "reviews", "states", "users"]
    objs = {}
    for i in range(len(classes)):
        objs[names[i]] = storage.count(classes[i])
    return jsonify(objs)
