from fastapi import APIRouter

from app import schema, models, db, auth, core

router = APIRouter(tags=["Login"])


@router.post("/login/", response_model=schema.LoginResponse)
def login(login: schema.Login):
    """Logar"""
    # print(login.username, login.password)
    user = models.User.login(username=login.username, password=login.password)
    sub = {"user_uuid": str(user.uuid), "key": [user.role.permission_level]}
    
    for i in range(1, user.role.permission_level):
        sub["key"].append(i)

    response = schema.LoginResponse(
        token=auth.encode_token(
            sub,
            core.settings.ACCESS_TOKEN_EXPIRE_MINUTES,
        ),
        user=user.username,
    )

    return response
