============================
Courier
============================

Postal Codes
----------------

Receives the name of the city or postal code, and returns a list of locations.

**Example request**:
    
.. http:get:: /v1/postalcode?countryCode=(string: iso2Code)&loc=(string: text)

.. tabs::
    .. code-tab:: bash

        $ curl \
            -H "Content-Type: application/json" \
            -H "Authorization: Bearer <token>" \
            https://<env>.freightol.com/v1/postalcode?countryCode=ES&loc=Barcelona

=============  =======  ===========  =========================================
Name            Type     Constraint             Description
=============  =======  ===========  =========================================
CountryCode    String    Mandatory   Country ISO 3166-1 alfa-2 code.
Loc            String    Mandatory   Name of city or postal code.
=============  =======  ===========  =========================================

**Example response**:

.. sourcecode:: json

    [
        {
            "latitude": 41.380002,
            "longitude": 2.168131,
            "country": "España",
            "countryCode": "ES",
            "city": "Barcelona",
            "region": "Cataluña",
            "regionCode": null,
            "postalCode": "08001"
        },
        {
            "latitude": 41.380665,
            "longitude": 2.177762,
            "country": "España",
            "countryCode": "ES",
            "city": "Barcelona",
            "region": "Cataluña",
            "regionCode": null,
            "postalCode": "08002"
        },
        {
            "latitude": 41.384247,
            "longitude": 2.176349,
            "country": "España",
            "countryCode": "ES",
            "city": "Barcelona",
            "region": "Cataluña",
            "regionCode": null,
            "postalCode": "08003"
        }
    ]

**Example response**:

=============  =======  ======================================================
Name            Type    Description
=============  =======  ======================================================
Latitude        Double   Latitude, precision is (3, 6).
Longitude       Double   longitude precision is (3, 6).
Country         String   Country name.
CountryCode     String   Country ISO 3166-1 alfa-2 code.
City            String   City name.
Region          Model    Region name.
RegionCode      Model    Region code.
PostalCode      Model    Postal code.
=============  =======  ======================================================


Pallet Types
----------------

Retrieves the list of supported pallet types.

**Example request**:

.. http:get:: /v1/courier/pallets

.. tabs::
    .. code-tab:: bash

        $ curl \
            -H "Content-Type: application/json" \
            -H "Authorization: Bearer <token>" \
            https://<env>.freightol.com/v1/courier/pallets


**Example response**:

.. sourcecode:: json

    [
        {
            "type": "Custom",
            "length": null,
            "width": null,
            "height": null,
            "unit": null
        },
        {
            "type": "Euro",
            "length": 120,
            "width": 80,
            "height": 145,
            "unit": "CM"
        },
        {
            "type": "American",
            "length": 120,
            "width": 100,
            "height": null,
            "unit": "CM"
        }
    ]
    

=======================   ==========   ===============================================
Name                      Type         Description
=======================   ==========   ===============================================
Type                        String       Pallet type
Length                      Double       Pallet length
Width                       Double       Pallet width
Height                      Double       Pallet height
Unit                        String       Unit of measurement
=======================   ==========   ===============================================

.. autosummary::
   :toctree: generated

   lumache