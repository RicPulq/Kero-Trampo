from fastapi import APIRouter

from app import schema, models, db, auth, core

router = APIRouter(tags=["Login"])


@router.post("/login/", response_model=schema.LoginResponse)
def login(login: schema.Login):
    """Logar"""
    user = models.User.login(username=login.username, password=login.password)
    response = schema.LoginResponse(
        token=auth.encode_token(
            str(user.uuid), core.settings.ACCESS_TOKEN_EXPIRE_MINUTES
        ),
        user=user,
    )
    return response
