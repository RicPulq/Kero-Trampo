from app import core

core.settings.FIRST_SUPERUSER



admin = {
    "username": core.settings.FIRST_SUPERUSER,
    "password": core.settings.FIRST_SUPERUSER_PASSWORD
}