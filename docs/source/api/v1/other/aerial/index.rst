Aerial
------

Retrieve the name of a city or an IATA code, and returns a list of airports that meet the value received. 

**Example request**:

.. http:get:: /v1/aerial?nameCityuIata=(string: text) 

.. tabs::
    .. code-tab:: bash

        $ curl \
            -H "Content-Type: application/json" \
            -H "Authorization: Bearer <token>" \
            https://<env>.freightol.com/v1/aerial?NameCityIata=barcelona

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
name            String   Name of the airport. 
city            String   Airport city.
state           String   Airport state. 
country         String   Airport country.
iataCode        String   Airport IATA code. 
iso             String   Country ISO code.
geoloc          Model    Airport geolocation.
=============  =======  ======================================================

* Geoloc model:

=============  =======  ======================================================
Name            Type    Description
=============  =======  ======================================================
lat             Double   Airport latitude, precision is (3, 6).
lng             Double   Airport longitude, precision is (3, 6).
=============  =======  ======================================================

