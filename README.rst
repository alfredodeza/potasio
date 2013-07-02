potasio
=======
After attempting to deploy `tasseo <https://github.com/obfuscurity/tasseo>`_ in
production and failing to compile with all kinds of Ruby errors (not tasseo's
fault for sure) I decided to port everything to Python.

All of the JavaScript and static assets come from the tasseo project, hence the
license for this application is BSD.

configuration
-------------
Set the Graphite url in ``config.py`` and place your dashboard JS files in
``public/dashboards/``.

There is an example dashboard that you can see and alter to get a dashboard up
and running.

License
-------
3 clause BSD, see ``LICENSE`` in this repository
