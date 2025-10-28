
# Django + MongoDB on AWS (2 EC2s)

**Web**: Django (Amazon Linux 2023)  
**DB**: MongoDB 7 (Amazon Linux 2023)  
**Network**: SG-Mongo allows 27017 only from SG-Web.

## Run (local or EC2)

```bash
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
export DJANGO_ALLOWED_HOSTS="*"
export MONGO_HOST="127.0.0.1"   # set to Mongo PRIVATE IP on AWS, e.g. 172.31.X.Y
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```

Open: `http://<your-host>:8000`

## Verify Mongo data
On the Mongo host:
```bash
mongosh
use mydatabase
db.interactive_submission.find().pretty()
```

## Project structure
- `interactive/` – app with form + conditional logic and persistence
- `webapp/` – Django project (settings, urls, wsgi)
- `requirements.txt` – pinned deps to work with djongo
# django-mongodb-AWS
