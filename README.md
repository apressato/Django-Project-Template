# Django-Project-Template
A small skeleton of Django Project for begin my project with most of the settings already set.
This skeleton contains:
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
  git clone https://github.com/apressato/Django-Project-Template.git
```
```bash
  cd Django-Project-Template
```
```bash
  python -m venv .venv
```
```bash
  .venv/script/activate
```
```bash
  python -m pip install --upgrade pip
```
```bash
  pythin -m pip install -r @requirements.txt
```
```bash
  python -m manage makemigrations
```
```bash  
  python -m manage migrate
```
```bash
  python -m createsuperuser
```
```bash
  wget https://github.com/mdbootstrap/mdb-ui-kit/archive/refs/heads/master.zip
```
```bash
  unzip master.zip ./static/MDB5UIKIT
```