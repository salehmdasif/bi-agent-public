"""
Security utilities: password hashing, JWT creation/validation, AES-256 encryption.
"""
from datetime import timedelta
from typing import Optional


def hash_password(password: str) -> str:
    """
    Hash a plain-text password for storage.

    Note:
        Implementation is proprietary and not included in this public version.
    """
    raise NotImplementedError("Proprietary implementation")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verify a plain-text password against a stored hash.

    Note:
        Implementation is proprietary and not included in this public version.
    """
    raise NotImplementedError("Proprietary implementation")


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    """
    Create a short-lived JWT access token.

    Args:
        data: Payload to encode (must include 'sub' for user ID).
        expires_delta: Token lifetime. Defaults to JWT_ACCESS_TOKEN_EXPIRE_MINUTES.

    Returns:
        Encoded JWT string.

    Note:
        Implementation is proprietary and not included in this public version.
    """
    raise NotImplementedError("Proprietary implementation")


def create_refresh_token(data: dict) -> str:
    """
    Create a longer-lived JWT refresh token.

    Note:
        Implementation is proprietary and not included in this public version.
    """
    raise NotImplementedError("Proprietary implementation")


def decode_token(token: str) -> dict:
    """
    Decode and validate a JWT token.

    Raises HTTPException 401 if the token is expired or invalid.

    Note:
        Implementation is proprietary and not included in this public version.
    """
    raise NotImplementedError("Proprietary implementation")


def encrypt_value(plaintext: str) -> str:
    """
    Encrypt a string using AES-256 (Fernet).

    Used for storing third-party API credentials in the database.

    Args:
        plaintext: The sensitive value to encrypt.

    Returns:
        Base64-encoded encrypted string.

    Note:
        Implementation is proprietary and not included in this public version.
    """
    raise NotImplementedError("Proprietary implementation")


def decrypt_value(ciphertext: str) -> str:
    """
    Decrypt an AES-256 encrypted string.

    Args:
        ciphertext: The encrypted value from the database.

    Returns:
        Original plaintext string.

    Note:
        Implementation is proprietary and not included in this public version.
    """
    raise NotImplementedError("Proprietary implementation")
