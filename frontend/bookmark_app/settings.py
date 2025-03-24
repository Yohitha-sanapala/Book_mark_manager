import os
from dotenv import load_dotenv

load_dotenv("mongo.env")

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': os.getenv("MONGO_DB_NAME"),
        'CLIENT': {
            'host': os.getenv("MONGO_URI"),
        }
    }
}
