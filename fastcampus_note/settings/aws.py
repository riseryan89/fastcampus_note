from fastcampus_note.settings.settings import DEBUG, BASE_DIR
import boto3
from storages.backends.s3boto3 import S3Boto3Storage
from dotenv import load_dotenv, dotenv_values

ENV_LOC = BASE_DIR / "fastcampus_note/settings/.env"
ENV_LOAD = load_dotenv(ENV_LOC)

if ENV_LOAD:
    config = dotenv_values(ENV_LOC)
    AWS_ACCESS_KEY_ID = config.get("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = config.get("AWS_SECRET_ACCESS_KEY")

DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"


AWS_STORAGE_BUCKET_NAME = "django-note"
AWS_S3_REGION_NAME = "ap-northeast-2"
AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"
AWS_S3_SECURE_URLS = True
STATICFILES_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"


class StaticStorage(S3Boto3Storage):
    location = "static"
