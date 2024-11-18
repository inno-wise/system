#!/bin/bash

# Wait for database to be ready (optional for PostgreSQL)
# Uncomment the following if using PostgreSQL:
# while ! nc -z db 5432; do
#   sleep 0.1
# done

# Apply migrations
echo "Running migrations..."
python manage.py migrate

# Optionally, create the superuser if it doesn't exist
echo "Creating superuser if it doesn't exist..."
python manage.py shell <<EOF
from django.contrib.auth import get_user_model

User = get_user_model()

if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('inno', 'innocenty@admin.com', '@ddmein')
EOF

# Finally, start the server
echo "Starting the Django server..."
exec python manage.py runserver 0.0.0.0:8000

