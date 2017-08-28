# mabrands
Backend API for enabling Brands to gather product insights

-------------------------------------------------------------------------------
This project uses postgres for local development

To get a working local installation follow the instructions here https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-16-04

For security reasons values like the secret key, the database name, user and password are not explicitly set rather imported using os.getenv.

Set these variables at the bottom of the virtual environment bin/activate script
The format is as follows:
  export BRANDS_SECRET_KEY='your-secret-key'
  export BRANDS_DB_NAME='your-database-name'
  export BRANDS_DB_USER='your-database-user'
  export BRANDS_DB_PASSWORD='your-database-user's-password'

Deactivate the virtualenv and reactivate it for the variables to take effect

The reason these are set in the activate script is because they are only needed when we are working on the project hence you only need to access them when the virtualenv is activated.

Instead of a settings.py I have a settings directory with a local.py and a production.py
This is for ease of deployment and updating the repository in the production server.
Because of this the DJANGO_SETTINGS_MODULE in manage.py is set to mabrands.settings.local
If it was production it would be mabrands.settings.production

At this point you should be good to go.


