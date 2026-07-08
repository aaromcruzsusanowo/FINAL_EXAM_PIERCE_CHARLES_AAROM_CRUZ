# SECURITY.md

## Dependency Pinning

The application uses exact dependency versions in `requirements.txt`.

### Third-Party Packages

- Flask==3.1.0
- PyJWT==2.10.1
- requests==2.32.3

## Mock Vulnerability Scan

Potential vulnerabilities:

- Hardcoded secrets
- Missing HTTPS
- Weak passwords
- Missing rate limiting
- Token replay attacks

## Recommended Mitigations

- Store secrets in environment variables.
- Use HTTPS.
- Rotate JWT secrets.
- Validate all user input.
- Enable rate limiting.

---

# JWT Authentication Handshake

The authentication service uses JSON Web Tokens (JWT) with the HS256 algorithm.

Authentication Process:

1. User enters credentials.
2. Server validates credentials.
3. Server creates a JWT containing the username and expiration timestamp.
4. The token is digitally signed using the server secret.
5. The client stores the token.
6. Every protected request includes the token.
7. The server verifies the signature and expiration before allowing access.

This protects the integrity of the authentication token because any modification invalidates the signature.