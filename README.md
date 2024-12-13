# Project Set Up


 
![image](https://realpython.com/cdn-cgi/image/width=960,format=auto/https://files.realpython.com/media/building_with_python_watermark.2ebe5beb5b1e.jpg)

## 1. Clone repo

    git clone https://github.com/minkova-diyana/health-assist.git

## 2. Install dependencies

    pip install requirements.txt
    
## 3. Set up the Settings
. SECRET_KEY = 'django-insecure-generate-your-secret_key'

    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": "mydatabase",
            "USER": "mydatabaseuser",
            "PASSWORD": "mypassword",
            "HOST": "127.0.0.1",
            "PORT": "5432",
        }
    }

. Set up email settings to email host of your choice

EMAIL_HOST = os.getenv('EMAIL_HOST', config('EMAIL_HOST'))

EMAIL_PORT = os.getenv('EMAIL_PORT', config('EMAIL_PORT'))

EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS', config('EMAIL_USE_TLS')) == "True"

EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER', config('EMAIL_HOST_USER'))

EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD', config('EMAIL_HOST_PASSWORD'))

## 4. Run migrations

    python manage.py migrate
    
    
## 5. Run project

    python manage.py runserver
    

### If you want to register and login as a health assist user you need the uc_id_number of existing employee profile 
. get to the accounts migration 0013 adn choose one of the two 

