import os

from dotenv import load_dotenv, dotenv_values

from fastcampus_note.settings.settings import BASE_DIR

ENV_LOC = BASE_DIR / "fastcampus_note/settings/.env"
ENV_LOAD = load_dotenv(ENV_LOC)

if ENV_LOAD:
    config = dotenv_values(ENV_LOC)
    GMAIL_PW = config.get("GMAIL_PW")
else:
    GMAIL_PW = os.environ.get("GMAIL_PW")

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "abc@gmail.com"
EMAIL_HOST_PASSWORD = GMAIL_PW
