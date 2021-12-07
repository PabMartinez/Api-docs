===========================
Auth
===========================

Create a Authorization Token
-----------------------------
Create a JWT (Json Web Token) using a API Key and API Secret valid in public API. Token is valid for 12h.

**Example request**:

.. http:post:: /v1/auth/token


.. tabs::

    .. code-tab:: bash

        $ curl -X POST \
            'https://<env>.freightol.com/v1/auth/token' \
            -H "x-api-key: <api-key>" \
            -H "secret-api-key: <api-secret>"
            

=====================   =========  =============   ================================================================
Name                     Type      Constraint      Description
=====================   =========  =============   ================================================================
X-API-Key               String        Mandatory     API Key provided by Freightol staff
Secret-API-Key          String        Mandatory     API Secret provided by Freightol staff
=====================   =========  =============   ================================================================  
  
**Example response**:

.. sourcecode:: json

    {
        "token_type": "Bearer",
        "expires_in": 43200,
        "access_token": "eyJhbGciOiJSUzI1NiIsImtpZCI6I..."
    }

=====================   ========= ================================================================
Name                     Type      Description
=====================   ========= ================================================================
Token type               String    Token type
Expired in               Integer   Time until expiration 
Access token             String    Authentication token
=====================   ========= ================================================================  


.. autosummary::
   :toctree: generated