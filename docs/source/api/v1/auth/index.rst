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

        $ curl \
            -X POST \
            -H "Content-Type: application/json" \
            -H "x-api-key: <api-key>" \
            -H "secret-api-key: <api-secret>" \
            https://<env>.freightol.com/v1/auth/token

=====================   =========  =============   ================================================================
Name                     Type      Constraint      Description
=====================   =========  =============   ================================================================
X-API-Key               String        Mandatory     API Key provider by Freightol staff
Secret-API-Key          String        Mandatory     API Secret provider by Freightol staff
=====================   =========  =============   ================================================================  
  
**Example response**:

.. sourcecode:: json

    {
        "token_type": "Bearer",
        "expires_in": 43200,
        "access_token": "eyJhbGciOiJSUzI1NiIsImtpZCI6I..."
    }


.. autosummary::
   :toctree: generated