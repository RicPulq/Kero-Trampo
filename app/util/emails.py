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
import ssl

from app.core.config import settings


def send_email(email_reciver: str, subject: str, body=str) -> any:
    try:
        conteudo = f"{body}"
        password = core.config.settings.SMTP_PASSWORD
        msg = MIMEMultipart()
        msg["Subject"] = f"{subject}"
        msg["From"] = core.config.settings.EMAILS_FROM_EMAIL
        msg["To"] = email_reciver
        msg.attach(MIMEText(conteudo, "html"))

        context = ssl.create_default_context()
        
        with smtplib.SMTP_SSL(
            host=core.config.settings.SMTP_HOST, timeout=5, port=core.config.settings.SMTP_PORT, context=context
        ) as smtp:
            smtp.ehlo()
            smtp.starttls
            smtp.login(msg["From"], password)
            smtp.sendmail(msg["From"], [msg["To"]], msg.as_string())
            smtp.quit()
    # except smtplib.SMTPException as e:
    #     raise HTTPException(
    #         status_code=400,
    #         detail=f"Não foi possível enviar o email para {email_reciver}",
    #     )
    finally:
        pass


def send_reset_password_email(email_reciver: str, code: str) -> None:
    project_name = settings.PROJECT_NAME
    body = f"""
    <html>
    <h3 style="font-weight:700;font-family:Ubuntu, Helvetica, Arial, sans-serif;font-size:16px;line-height:1;text-align:left;color:#555555;">
        <b>{project_name}</b> - Recuperar Senha
    </h3>
    <p style="font-family:Ubuntu, Helvetica, Arial, sans-serif;font-size:16px;line-height:1;text-align:left;color:#555555;">
        Recebemos um pedido de recuperação de senha do(a) usuário(a) {email_reciver}
    </p>
    <p style="font-family:Ubuntu, Helvetica, Arial, sans-serif;font-size:16px;line-height:1;text-align:left;color:#555555;">
        Código de verificação:
    </p>
    <h4 align="center" style="padding:50px 0px;">{code}</h2>
    </html>
    """
    send_email(email_reciver, project_name, body)


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
