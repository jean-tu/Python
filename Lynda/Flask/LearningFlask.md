# Learning Flask

We will be using virtualenv for the cases that we want to test out a new library, but don't want to mess up any of the other ones.

To be able to access the database from the command line for mine it is: `'/Applications/Postgres.app/Contents/Versions/9.6/bin'/psql -p5432`

To create an isolated environment: `virtualenv venv`. This command will run and create the new virtual environment for you.

To activate the environment you do `source venv/bin/activate`

To download Flask: `pip install flask`

## Folder Breakdown

The "static" folder is where all of the css, images, and javascript will go

## Notes

* The routes.py is what has the code that maps a URL to a python function
* Request-Response Cycle: The request first starts off in a peron's browser, then the routes.py, then to the templates folder to access the HTML, which then goes into the static folder that holds the css, javascript, and images.
