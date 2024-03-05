=========================
Digital Image Sensor Docs
=========================

Contributing
------------

Pull requests always welcome.

Local testing
-------------

- Clone the repo
- Set up a virtual environment 

``python -m venv img-venv``

- Activate the venv

``source img-venv/bin/activate``

- Install the dependencies

``pip install -r requirements.txt``

- Build the docs using ``make``
- View results by going to /docs and launching

``python -m http.server``

- Alternatively use ``sphinx-autobuild`` which will auto-reload any changes you make. 

``sphinx-autobuild source docs``

- This will host the build results at http://127.0.0.1:8000


Build to Github Pages
---------------------

This is managed automatically through a Github workflow, with an action on a push to the source directory.