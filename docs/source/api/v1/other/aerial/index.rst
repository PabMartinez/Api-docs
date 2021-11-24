===========================
Aerial
===========================

Airports
--------

Retrieve the name of a city or an IATA code, and returns a list of airports that meet the value received. 

**Example request**:

.. http:get:: /v1/aerial/airports

.. tabs::
    .. code-tab:: bash

        $ curl -X 'GET' \
            'https://<env>.freightol.com/v1/aerial/airports?nameCityIata=barcelona' \
            -H "Content-Type: application/json" \
            -H "Authorization: Bearer <token>"

=============  =======  ===========  =========================================
Name            Type     Constraint  Description
=============  =======  ===========  =========================================
nameCityIata   String    Mandatory   Name of city or IATA airport code.
=============  =======  ===========  =========================================

**Example response**:

.. sourcecode:: json

    [
        {
            "name": "Barcelona International Airport",
            "city": "El Prat de Llobregat",
            "state": "Catalonia",
            "country": "Spain",
            "iataCode": "BCN",
            "iso": "ES",
            "geoloc": {
                "lat": 41.3006,
                "lng": 2.07976
            }
        }
    ]

* Airport model:

=============  =======  ======================================================
Name            Type    Description
=============  =======  ======================================================
Name            String   Name of the airport. 
City            String   Airport city.
State           String   Airport state. 
Country         String   Airport country.
IataCode        String   Airport IATA code. 
Iso             String   Country ISO code.
Geoloc          Model    Airport geolocation.
=============  =======  ======================================================

* Geoloc model:

=============  =======  ======================================================
Name            Type    Description
=============  =======  ======================================================
Lat             Double   Airport latitude, precision is (3, 6).
Lng             Double   Airport longitude, precision is (3, 6).
=============  =======  ======================================================

.. autosummary::
   :toctree: generated