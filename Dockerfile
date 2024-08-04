FROM python:3.10
WORKDIR /site
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY backend/ .
ENV PYTHONUNBUFFERED 1
RUN python manage.py migrate
RUN python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@mail.ru', '12345')"

CMD ["python", "manage.py", "runserver", "0.0.0.0:8081"]
