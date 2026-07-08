# Migration Report

## 1. Legacy Architecture Overview

The original system followed a monolithic architecture where all business logic was contained in a single application.

---

## 2. C4 Level 2 Container Diagram

```text
                +------------------------+
                |        User            |
                +-----------+------------+
                            |
                            v
                +------------------------+
                |      Main Service      |
                +-----------+------------+
                            |
            +---------------+---------------+
            |                               |
            v                               v
+------------------------+      +------------------------+
| Encryption Service     |      | Compression Service    |
+------------------------+      +------------------------+
```

---

## 3. Code Smells Identified

1. God Object
   - Multiple responsibilities handled by one class.

2. Hardcoded Coupling
   - Components directly instantiate dependencies.

3. Tight Coupling
   - Business logic depends directly on implementation classes.

---

## 4. Refactoring

The application was migrated into a lightweight microservice-inspired structure by separating processing services into independent modules.

Factory Pattern was implemented to dynamically create processing services.

Strategy Pattern was implemented to allow interchangeable data-processing algorithms.

---

## 5. Manual Verification of AI Output

- Verified imports manually.
- Corrected module organization.
- Confirmed Factory Pattern returns the correct service.
- Confirmed Strategy Pattern delegates processing correctly.
- Executed the program successfully.

---

# JWT Authentication Handshake

The authentication service uses JSON Web Tokens (JWT) with the HS256 algorithm.

Authentication Flow:

1. User submits login credentials.
2. Server validates the credentials.
3. Server generates a JWT containing the username and expiration timestamp.
4. The JWT is signed using the server's secret key.
5. The client stores the JWT.
6. Every protected request includes the JWT.
7. The server verifies the signature and expiration before granting access.

This approach ensures message integrity because any modification of the token invalidates its signature.