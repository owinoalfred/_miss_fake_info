import os

class Config:
    MAX_LENGTH = 150
    MIN_LENGTH = 30
    API_KEY = os.getenv("API_KEY")
