#Deployment instructions
=========================================================================
For the deployment, we'll be using a digital ocean droplet running Ubuntu 16.04.

I will be making the following assumptions:
 You know how to create a droplet (reference: https://www.digitalocean.com/community/tutorials/how-to-create-your-first-digitalocean-droplet-virtual-server)

 You know how to set up a server (reference: https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-16-04)

 You already have a domain name (you can get one at https://www.gandi.net/en)

 You know how to bind a domain name to a webserver using DNS (reference: https://www.digitalocean.com/community/tutorials/how-to-point-to-digitalocean-nameservers-from-common-domain-registrars)

 You know how to setup Git (reference: https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup)

 You know how to generate SSH keys and add them to github (reference: https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/)

 You know how to add a github remote (reference: https://help.github.com/articles/adding-a-remote/)

--------------------------------------------------------------------------
##Requirements:
- A postgres database
- A gunicorn application server
- Nginx
- Our django application
- Git

--------------------------------------------------------------------------
##Package installation
In your terminal run the following commands: (Don't include the $)
  $ sudo apt-get update

  $ sudo apt-get install python-pip python-dev libpq-dev postgresql postgresql-contrib nginx supervisor

--------------------------------------------------------------------------
##Create the PostgreSQL database and user
Log into an interactive Postgres session:
  $ sudo -u postgres psql

The terminal will change from having $ to having postgres=#

NOTE: myproject should be substituted with the name of your database
      myprojectuser with the name of your database user
      password with the password you select for the database user

Create your database: (Remember to include the semi-colons at the end. They are part of SQL syntax)
  postgres=# CREATE DATABASE myproject;

Create a database user for our project with a secure password:
  postgres=# CREATE USER myprojectuser WITH PASSWORD 'password';

Set the default encoding to UTF-8:
  postgres=# ALTER ROLE myprojectuser SET client_encoding TO 'utf8';

Block reads from uncommitted transactions by setting the default transaction isolation scheme to "read committed":
  postgres=# ALTER ROLE myprojectuser SET default_transaction_isolation TO 'read committed';

Set the time-zone for your Django project to 'Africa/Nairobi'.
This is the same as 'UTC+3'
  postgres=# ALTER ROLE myprojectuser SET timezone TO 'Africa/Nairobi';

Give our user administrative access to our database:
  postgres=# GRANT ALL PRIVILEGES ON DATABASE myproject TO myprojectuser;

To see all the databases present, enter:
  postgres=# \l

To exit out of the PostgreSQL prompt, enter:
  postgres=# \q

---------------------------------------------------------------------------
##Create a python VirtualEnvironment for your project
These instructions are for Python2

Upgrade pip to the most current version:
  $ sudo -H pip install --upgrade pip

Install virtualenv:
  $ sudo -H pip install virtualenv

While still in the home directory(/home/user) activate your virtualenv
  $ virtualenv .

Activate the virtualenvironment:
  $ source bin/activate

Create a new git repository
  $ git init

Add a remote:
  $ git remote add origin git@github.com:username/repository.git

Clone your project repository from github:
  $ git clone git@github.com:username/repository.git

Tree representation:

        ├── mabrands          <-- django project
        │   ├── brands        <-- django app
        │   ├── brands_admin
        │   ├── mabrands      <-- Project directory
        │   ├── manage.py
        │   ├── Notes.md
        │   ├── README.md
        │   ├── requirements.txt
        │   └── templates

-----------------------------------------------------------------------
##Setup the project for deployment
cd into the project and install the requirements:
  $ cd mabrands
  $ pip install -r requirements.txt

Install Gunicorn and the psycopg2 PostgreSQL adator using pip
  $ pip install gunicorn psycopg2

The next 3 tasks will be executed in the project settings file
Add ALLOWED_HOSTS:

        ALLOWED_HOSTS = ['your_server_domain_or_IP', ]

Configure your database:

        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql_psycopg2',
                'NAME': 'myproject',
                'USER': 'myprojectuser',
                'PASSWORD': 'password',
                'HOST': 'localhost',
                'PORT': '',
            }
        }


Add a static root directory (https://docs.djangoproject.com/en/1.11/howto/static-files/#deployment):

        STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


Exit your settings file.

Make migrations:
  $ python manage.py makemigrations

Migrate the database:
  $ python manage.py migrate

Collect all the static files to the static root directory:
  $ python manage.py collectstatic

-------------------------------------------------------------------------
##Configure Gunicorn
Create the gunicorn_start script in the virtualenv bin directory:
  $ vim bin/gunicorn_start

Add the following information and save it:

        #!/bin/bash

        NAME="your-project-name"
        DIR=/home/urban/your-project-name
        USER=your-server-user
        GROUP=your-server-user
        WORKERS=3
        BIND=unix:/home/urban/run/gunicorn.sock
        DJANGO_SETTINGS_MODULE=your-project-name.settings
        DJANGO_WSGI_MODULE=your-project-name.wsgi
        LOG_LEVEL=error

        cd $DIR
        source ../bin/activate

        export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
        export PYTHONPATH=$DIR:$PYTHONPATH

        exec ../bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
          --name $NAME \
          --workers $WORKERS \
          --user=$USER \
          --group=$GROUP \
          --bind=$BIND \
          --log-level=$LOG_LEVEL \
          --log-file=-

    **substitute your-project-name with the name of your project
    **substitute your-server-user with the name of the user on your server

Make the gunicorn_start file executable:
  $ chmod u+x bin/gunicorn_start

Create a run directory form the unix socket file
  $ mkdir -v run

Create a logs directory inisde the virtualenv at the same level as run:
  $ mkdir -v logs

Create a file to be used to log application errors
  $ touch logs/gunicorn-error.log

-------------------------------------------------------------------------
##Configure supervisor to take care of running the gunicorn server
Create a new Supervisor configuration file:
  $ sudo vim /etc/supervisor/conf.d/your-project-name.conf

Add the following to it:
        [program:your-project-name]
        command=/home/urban/bin/gunicorn_start
        user=urban
        autostart=true
        autorestart=true
        redirect_stderr=true
        stdout_logfile=/home/urban/logs/gunicorn-error.log

Reread the Supervisor configuration files and make the new program available:
  $ sudo supervisorctl reread
  $ sudo supervisorctl update

Check the status:
  $ sudo supervisorctl status your-project-name

It should return something like this:

    your-project-name              RUNNING   pid 23381, uptime 0:00:15

To update the source code fo your application, pull the source code from github and restart the process
  $ sudo supervisorctl restart your-project-name

-------------------------------------------------------------------------
##Configure Nginx
Add a new configuration file named your-project-name inside /etc/nginx/sites-available/
  $ sudo vim /etc/nginx/sites-available/your-project-name

Add the following to it:

        server {
            listen 80;
            server_name domain/ip-address;


            root /home/dan/mabrands;

            # Add index.php to the list if you are using PHP
            index index.html index.htm index.nginx-debian.html;


            location = /favicon.ico { access_log off; log_not_found off; }
            location /static {
                alias /path/to/STATIC_ROOT;
            }


            location / {
                include proxy_params;
                proxy_pass http://unix:/home/user/run/gunicorn.sock;
            }
        }


Create a symbolic link to the sites-enabled directory:
  $ sudo ln -s /etc/nginx/sites-available/your-project-name /etc/nginx/sites-enabled/your-project-name

Remove the Nginx default websites from sites-enabled:
  $ sudo rm /etc/nginx/sites-enabled/default

Test your Nginx configuration for syntax errors:
  $ sudo nginx -t

If no errors are reported restart Nginx:
  $ sudo systemctl restart nginx

Open up our firewall to traffic on port 80:
  $ sudo ufw allow 'Nginx Full'


Congratulate yourself, your deployment should be visible on a url
