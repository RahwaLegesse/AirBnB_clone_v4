#!/usr/bin/python3
""" begining of flash """
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place
import uuid
from models.city import City
app = Flask(__name__)


@app.teardown_appcontext
def close_db(error):
    """Session deleting """
    storage.close()


@app.route('/101-hbnb/', strict_slashes=False)
def hbnb():
    """ waiting """
    states = storage.all(State).values()
    states = sorted(states, key=lambda k: k.name)
    st_ct = []

    for state in states:
        st_ct.append([state, sorted(state.cities, key=lambda k: k.name)])

    amenities = storage.all(Amenity).values()
    amenities = sorted(amenities, key=lambda k: k.name)
    cache_id = str(uuid.uuid4())
    places = storage.all(Place).values()
    places = sorted(places, key=lambda k: k.name)

    return render_template('101-hbnb.html',
                           states=st_ct,
                           amenities=amenities,
                           places=places,
                           cache_id=cache_id)


if __name__ == "__main__":
    """ first part"""
    app.run(host='0.0.0.0', port=5000)