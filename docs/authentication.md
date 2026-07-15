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
