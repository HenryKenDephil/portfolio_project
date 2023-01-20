# portfolio_project



How To Run The SACCO Management System in Django


Step 1: gitclone this repository

Step 2: Go inside the project folder, open cmd and type the following commands to install Django Framework and run the webserver:

pip install virtualenv

virtualenv env

cd env/Scripts

activate

cd ../..

pip install django

pip install -r requirements.txt

pip freeze>requirements.txt

updating settings by connecting it to postgresql or sqlite3 or mysql; whatever you want

python manage.py migrate

python manage.py runserver

Step 3: Finally, open the browser and go to http://127.0.0.1:8000/





Authors: Henry Kennedy Ochieng' Omoloh

	Jon Achola
Inspirations for creating this app;
beisdes the academic qualifications, we are inspired to develop this app as our first entry level to the tech industry By the end of this course, we will be having a highly scalable system that will serve microfinance institutions and also act as our source of income. As future entrepreneur in tech industry, this app therefore marks one of our greatest milestone as an alternative tech service providers.
