"""
License system — RS256 JWT-based deployment authorization.

Two-layer validation:
  Layer 1: RS256 JWT signature and expiry
  Layer 2: licensed_domain must match FRONTEND_URL

Note:
    The full license system implementation is proprietary and not included
    in this public version.
"""
from typing import Optional


class LicenseStatus:
    VALID         = "valid"
    EXPIRED       = "expired"
    INVALID       = "invalid"
    NOT_ACTIVATED = "not_activated"


class LicenseInfo:
    """
    Holds the result of a license verification check.

    Attributes:
        status: One of LicenseStatus values.
        licensed_to: Email of the licensee.
        company: Company name on the license.
        license_type: 'trial' or 'lifetime'.
        allowed_modules: List of permitted module names. Empty = all allowed.
        allowed_users: User seat limit. None = unlimited.
        expires_at: ISO date string for the expiry date.
        is_valid: True only if status is VALID.
    """

    def __init__(
        self,
        status: str,
        licensed_to: Optional[str] = None,
        licensed_domain: Optional[str] = None,
        company: Optional[str] = None,
        license_type: Optional[str] = None,
        allowed_modules: Optional[list] = None,
        allowed_users: Optional[int] = None,
        issued_at: Optional[str] = None,
        expires_at: Optional[str] = None,
        message: str = "",
    ):
        self.status          = status
        self.licensed_to     = licensed_to
        self.licensed_domain = licensed_domain
        self.company         = company
        self.license_type    = license_type
        self.allowed_modules = allowed_modules or []
        self.allowed_users   = allowed_users
        self.issued_at       = issued_at
        self.expires_at      = expires_at
        self.message         = message

    @property
    def is_valid(self) -> bool:
        return self.status == LicenseStatus.VALID


def verify_license_key(license_key: str) -> LicenseInfo:
    """
    Verify a license JWT against the deployment's public key and domain.

    Args:
        license_key: The license JWT string from the database.

    Returns:
        LicenseInfo with the verification result.

    Note:
        Verification logic is proprietary and not included in this public version.
    """
    raise NotImplementedError("Proprietary implementation")


def is_module_allowed_by_license(module_name: str, license_info: LicenseInfo) -> bool:
    """
    Check if a module is permitted by the current license.

    An empty allowed_modules list means all modules are permitted.

    Note:
        Implementation is proprietary and not included in this public version.
    """
    raise NotImplementedError("Proprietary implementation")


def is_users_allowed_by_license(current_count: int, license_info: LicenseInfo) -> bool:
    """
    Check if adding another user is within the license seat limit.

    Note:
        Implementation is proprietary and not included in this public version.
    """
    raise NotImplementedError("Proprietary implementation")


async def check_license_with_cache(redis, db) -> str:
    """
    Full license check with Redis caching (1-hour TTL).

    Returns the license status string without hitting the database on every request.

    Note:
        Implementation is proprietary and not included in this public version.
    """
    raise NotImplementedError("Proprietary implementation")
