# MyAppDjango

A generated IBM Cloud application for test

[![](https://img.shields.io/badge/bluemix-powered-blue.svg)](https://bluemix.net)

## Run locally as Django application in development mode
```bash
pip install -r requirements.txt
gunicorn -b 0.0.0.0:3000 MyAppDjango.settings.development MyAppDjango.wsgi
```
## Run locally as Django application in release mode
```bash
pip install -r requirements.txt
gunicorn -b 0.0.0.0:3000 MyAppDjango.settings.production MyAppDjango.wsgi
```
## To test the Django Application
```bash
export PYTHONPATH=$(pwd)
python manage.py test
```
## To test the Django Application
```bash
export PYTHONPATH=$(pwd)
python manage.py test
```
## To debug the Django Application
```bash
export PYTHONPATH=$(pwd)
python manage.py runserver --settings MyAppDjango.settings.development --noreload
```

## Build, run, and deploy using IDT
```bash

# Install needed dependencies:
idt install
# Build the docker image for your app:
idt build
# Run the app locally through docker:
idt run
# Deploy your app to IBM Cloud using Cloud Foundry:
idt deploy
# Deploy your app to IBM Cloud using Kubernetes:
idt deploy --target container
```