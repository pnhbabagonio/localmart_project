"""
Settings module - loads the appropriate settings based on environment.
"""
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Determine which settings to use
ENVIRONMENT = os.getenv('DJANGO_ENV', 'development')

if ENVIRONMENT == 'production':
    from .production import *
else:
    from .development import *