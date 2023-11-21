====================
Digital Imaging Docs
====================



Build to Github Pages
---------------------

This is managed through Github workflow, with an action on a push to the source directory.


Contributing
============


Local testing
-------------

- Clone the repo
- Set up a virtual environment 

``pip install -r requirements.txt``

- Activate the venv

``source eee-venv/bin/activate``

- Build the docs using ``make``
- View results by going to /docs and launching

``python -m http.server``

- This will host the build results at http://127.0.0.1:8000