import logging
from datetime import datetime, timedelta
from fastapi.templating import Jinja2Templates
from pathlib import Path
from typing import Any, Dict, Optional


import emails
from emails.template import JinjaTemplate
from fastapi import HTTPException
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from app import core
import smtplib

from app.core.config import settings


def send_email(email_reciver: str, subject: str, body=str) -> any:
    try:
        conteudo = f"{body}"
        password = core.config.settings.SMTP_PASSWORD
        msg = MIMEMultipart()
        msg["Subject"] = f"{subject}"
        msg["From"] = core.config.settings.SMTP_USER
        msg["To"] = email_reciver
        msg.attach(MIMEText(conteudo, "html"))

        with smtplib.SMTP_SSL(
            host="smtp.gmail.com", timeout=5, port=core.config.settings.SMTP_PORT
        ) as smtp:
            smtp.ehlo()
            smtp.starttls
            smtp.login(msg["From"], password)
            smtp.sendmail(msg["From"], [msg["To"]], msg.as_string().encode("utf-8"))
            smtp.quit()
    except smtplib.SMTPException as e:
        raise HTTPException(
            status_code=400,
            detail=f"Não foi possível enviar o email para {email_reciver}",
        )


def send_reset_password_email(email_to: str, email: str, token: str) -> None:
    project_name = settings.PROJECT_NAME
    subject = f"{project_name} - Recuperação de senha para {email}"
    with open(Path(settings.EMAIL_TEMPLATES_DIR) / "reset_password.html") as f:
        template_str = f.read()
    server_host = settings.REDEFINIR_SENHA_ENDPOINT
    link = f"{server_host}/?{token}"
    print(link)
    send_email(
        email_to=email_to,
        subject_template=subject,
        html_template=template_str,
        environment={
            "project_name": settings.PROJECT_NAME,
            "username": email,
            "email": email_to,
            "valid_hours": settings.EMAIL_RESET_TOKEN_EXPIRE_HOURS,
            "link": link,
        },
    )


def send_new_account_email(email_to: str, username: str, token: str) -> None:
    # project_name = settings.PROJECT_NAME
    subject = f"{settings.PROJECT_NAME} - Nova conta para {username.capitalize()}"
    with open(Path(settings.EMAIL_TEMPLATES_DIR) / "new_account.html") as f:
        template_str = f.read()
    link = f"{settings.SERVER_HOST}{settings.API_URL_PREFIX}/registration/{token}"
    send_email(
        email_to=email_to,
        subject_template=subject,
        html_template=template_str,
        environment={
            "project_name": settings.PROJECT_NAME,
            "username": username.capitalize(),
            "email": email_to,
            "link": link,
        },
    )
