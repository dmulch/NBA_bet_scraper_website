#!/usr/bin/env bash
# exit on error
set -o errexit
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
printf "admin\ndmulcahy24@gsb.columbia.edu\n1234qwer1234qwer" | python manage.py createsuperuser
#echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin1',
#'admin@example.com', 'pass')" | python manage.py shell