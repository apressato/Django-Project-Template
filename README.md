# Django-Project-Template
 A small starter Django's Skeleton Project with all settings already set.

#### This project contains:
 * Extended User Structure
 * Login / Logout
 * Profile editing (to be fixed)
 * django-info (corresponding to PHPInfo)
 * A small About that display the licence (or whatever you want)
 * An example og UI with toolbar and searchbar
 * Custom Error Handlers for 500 and 400
 * All Settings already configured for static path like Avatar and use uploaded files


## How to use this template
```bash
  # Create et access project folder
  mkdir project_name
  cd project_name
  wget https://github.com/apressato/Django-Project-Template/archive/refs/heads/master.zip
```
```bash
  # Create Python virtual env 
  python3 -m venv .venv
```
```bash
  # Activate virtual env
  source .venv/bin/activate
```
```bash
  # Upgrade pip
  python -m pip install --upgrade pip
```
```bash
  # Install all requirements
  python -m pip install -r @requirements.txt
```
```bash
  # Create Django Project
  django-admin startproject project_name  
```
Extract the file _unzipgithubhelper.py_ from _master.zip_ then execute the command below:
```bash
  # Extract template
  python .\unzipgithubhelper.py -f .\master.zip -o .\ -p {your project name} 
```
```bash
  # Clean folder
  del master.zip
```
```bash
  # Generate migration files
  python -m manage makemigrations
```
```bash  
  # Apply Migration file 
  python -m manage migrate
```
```bash
  # Create Super User
  python -m createsuperuser
```
```bash
  # Download Free version of Material Design Bootstrap UI Kit
  wget https://github.com/mdbootstrap/mdb-ui-kit/archive/refs/heads/master.zip
  # Extract UI KIT
  python .\unzipgithubhelper.py -f .\master.zip -o /static/MDB5UIKIT
  ```

You can add more functions to your site by using the Django command _startapp_:
```bash
  .venv/script/activate
```
```bash
  # Create App
  python manage.py startapp app_name
```

don't forget to add the new function in _settings.py_

```python
# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    ...,
    'app_name',
]
```
