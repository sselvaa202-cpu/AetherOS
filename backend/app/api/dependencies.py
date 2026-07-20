from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.core.security import verify_access_token
from app.models.user import User

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/login"
)

def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
):
    print("=" * 60)
    print("TOKEN RECEIVED:", token)
    print("=" * 60)

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
    )

    payload = verify_access_token(token)

    print(payload)

    email = payload.get("sub")

    user = db.query(User).filter(
        User.email == email
    ).first()

    print(user)

    if user is None:
        raise credentials_exception

    return user
