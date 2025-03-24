import os
from dotenv import load_dotenv

# Load environment variables from mongo.env file
load_dotenv("mongo.env")  

DATABASES = {
    'default': {
        'ENGINE': 'djongo',  # Use Djongo for MongoDB
        'NAME': os.getenv("MONGO_DB_NAME"),  # MongoDB database name
        'CLIENT': {
            'host': os.getenv("MONGO_HOST", "localhost"),  # MongoDB host
            'port': int(os.getenv("MONGO_PORT", 27017)),  # MongoDB port
            'username': os.getenv("MONGO_USER"),  # MongoDB username (if required)
            'password': os.getenv("MONGO_PASSWORD"),  # MongoDB password (if required)
            'authSource': os.getenv("MONGO_AUTH_DB", "admin"),  # Auth database (default is "admin")
        }
    }
}
