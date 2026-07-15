# Authentication Guide

## JWT Flow
JSON Web Tokens (JWT) are used for secure authentication between the frontend client and our backend API.
1. The user provides their credentials (username & password) to the **Login API**.
2. The server verifies the credentials and returns two tokens: an **Access Token** (short-lived) and a **Refresh Token** (long-lived).
3. The client sends the Access Token in the `Authorization: Bearer <token>` header for all subsequent requests to **Protected APIs**.
4. When the Access Token expires, the client sends the Refresh Token to the **Refresh API** to securely get a new Access Token without requiring the user to log in again.

## Register API
**Endpoint:** `POST /api/v1/auth/register/`
Creates a new user account. 
- **Payload:** Accepts `username`, `password`, `email`, `first_name`, and `last_name`.

## Login API
**Endpoint:** `POST /api/v1/auth/login/`
Authenticates a user.
- **Payload:** Accepts `username` and `password`.
- **Response:** Returns an `access` and `refresh` token.

## Refresh Token API
**Endpoint:** `POST /api/v1/auth/refresh/`
Refreshes an expired access token.
- **Payload:** Accepts `refresh`.
- **Response:** Returns a new `access` token.

## Protected APIs
Endpoints that require a user to be logged in (such as the Profile API) are protected using Django REST Framework's `IsAuthenticated` permission class. You must include the `Authorization: Bearer <access_token>` header in your HTTP request to access them.

- **Profile API Endpoint:** `GET /api/v1/auth/profile/`
- **Response:** Returns the details of the currently authenticated user (ID, username, email, etc.).




# Authentication Guide

## Overview

The project uses a custom Django User model instead of Django's default authentication model.

The custom model supports:

- Email-based authentication
- JWT authentication
- Role-based authorization
- Django Admin integration
- Future OAuth providers
- Future Multi-Tenant support

---

## Authentication Architecture

```
Client
    │
    ▼
JWT Login API
    │
    ▼
Django REST Framework
    │
    ▼
JWT Authentication
    │
    ▼
Custom User Model
    │
    ▼
PostgreSQL
```

---

## Custom User Model

Location

```
backend/apps/users/models.py
```

The project replaces Django's default User model using:

```python
AUTH_USER_MODEL = "users.User"
```

---

## User Roles

| Role | Description |
|------|-------------|
| SUPER_ADMIN | Full platform access |
| ADMIN | Organization administration |
| DEVELOPER | Development features |
| SUPPORT | Customer support |
| USER | Standard application user |

---

## Permission Classes

Location

```
backend/apps/users/permissions/
```

Available permissions:

- IsSuperAdmin
- IsAdmin
- IsDeveloper
- IsSupport

Example:

```python
permission_classes = [IsAdmin]
```

---

## JWT Authentication

Configured in:

```
backend/config/settings/base.py
```

Authentication Class

```python
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
}
```

Clients authenticate using:

```
Authorization: Bearer <access_token>
```

---

## Django Admin

The custom User model is registered in:

```
backend/apps/users/admin.py
```

Admin Features

- Search users
- Filter by role
- Filter by active status
- Filter by staff
- Display created date
- Display role
- Read-only timestamps

---

## Database

Main authentication table:

```
users_user
```

Stores:

- Email
- Username
- Password
- Role
- Active status
- Staff status
- Superuser status
- Created timestamp
- Updated timestamp

---

## Future Enhancements

Planned features:

- User profile management
- Avatar upload
- Password reset
- Email verification
- Two-factor authentication (2FA)
- OAuth (Google/GitHub)
- Session management
- Audit logs

---

## Project Structure

```
backend/apps/users/

├── admin.py
├── apps.py
├── managers.py
├── migrations/
├── models.py
├── permissions/
├── serializers.py
├── urls.py
├── views.py
└── tests.py
```