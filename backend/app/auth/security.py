from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError
from passlib.context import CryptContext
import bcrypt
from fastapi import HTTPException, status
from app.config import settings

# Use bcrypt directly instead of passlib's bcrypt adapter.  That adapter is
# incompatible with newer bcrypt releases and caused registration-time 500s.
# The legacy context is retained only to migrate previous PBKDF2 hashes.
legacy_pwd = CryptContext(schemes=['pbkdf2_sha256'])

def _password_bytes(value):
    encoded=value.encode('utf-8')
    if len(encoded)>72: raise ValueError('Password must be at most 72 bytes')
    return encoded

def hash_password(value):
    return bcrypt.hashpw(_password_bytes(value), bcrypt.gensalt(rounds=12)).decode('utf-8')

def verify_password(value, hashed):
    if hashed.startswith(('$2a$', '$2b$', '$2y$')):
        return bcrypt.checkpw(_password_bytes(value), hashed.encode('utf-8'))
    return legacy_pwd.verify(value, hashed)

def password_needs_rehash(hashed): return not hashed.startswith(('$2a$', '$2b$', '$2y$'))
def create_token(subject):
    return jwt.encode({'sub': subject, 'exp': datetime.now(timezone.utc) + timedelta(minutes=settings.access_minutes)}, settings.jwt_secret, algorithm=settings.jwt_algorithm)
def decode_token(token):
    try: return jwt.decode(token, settings.jwt_secret, algorithms=[settings.jwt_algorithm])['sub']
    except (JWTError, KeyError): raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid or expired session')
