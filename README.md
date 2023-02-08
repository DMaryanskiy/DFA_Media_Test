# DFA_Media_Test

## Installation

1. Create virtual environment `python -m venv venv` and activate it.
2. Install requirements via `pip install -r requirements.txt`
3. Change directory to DFA_Media_Test via `cd DFA_Media_Test`
4. Migrate and run server
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## Paths

1. Registration: `api/v1/users/register`
2. Login: `api/v1/users/login`
3. Get current active user: `api/v1/users/me`
4. Gallery CRUD: `api/v1/gallery`
5. Delete all images (for admins only): `api/v1/gallery/delete/all`