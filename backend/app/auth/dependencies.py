from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.auth.security import decode_token
from app.database.store import store

bearer=HTTPBearer(auto_error=False)
def current_user(credentials: HTTPAuthorizationCredentials=Depends(bearer)):
 if not credentials: raise HTTPException(401,'Authentication required')
 user=store.user_by_id(decode_token(credentials.credentials))
 if not user: raise HTTPException(401,'User not found')
 return user
