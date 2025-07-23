from fastapi import HTTPException
from src.modules.auth.schemas import LoginRequest, LoginResponse
from fastapi import APIRouter
router = APIRouter()

@router.post("/login/")
def login(data: LoginRequest) -> LoginResponse:
    print(f"Login attempt with username: {data.username}")
    if data.username == "admin" and data.password == "password":
        return LoginResponse(access_token="fake-jwt-token")
    raise HTTPException(status_code=401, detail="Invalid credentials")