mkdir -p form_builder_files
mkdir -p form_builder_uploads
pip install -r requirements.txt
cp env_example .env
python manage.py migrate
python manage.py collectstatic

