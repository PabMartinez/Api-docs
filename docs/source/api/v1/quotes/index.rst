=====================
Quotes
=====================

Saved Quotes
----------------

Request to retrieve the quotes currently stored.

**Example request**:
    
.. http:get:: /v1/quotes


.. tabs::
    .. code-tab:: bash

        $ curl -X 'GET' \
            'https://<env>.freightol.com/v1/quotes'
            -H "Content-Type: application/json" \
            -H "Authorization: Bearer <token>"

**Example response**:

.. sourcecode:: json

    [
        {
            "quoteId": "a11e7c54-0d79-4898-fc6f-08d981bf0c29",
            "agency": "ASM",
            "shipmentType": "Box",
            "pickUpDate": "2021-09-29T00:00:00",
            "deliveryDate": "2021-10-02T00:00:00",
            "expirationDate": "2021-09-29T00:00:00",
            "transitDays": 3,
            "totalPrice": {
                "value": 668,
                "currency": "EUR"
            },
            "surcharges": [
                {
                    "description": "Transport",
                    "price": {
                        "value": 668,
                        "currency": "EUR"
                    },
                    "taxPercent": 0
                }
            ]
        }
    ]


* Quote model    

=======================   ==================   ===========================================================
Name                      Type                 Description
=======================   ==================   ===========================================================
QuoteId                   Guid                 Guid of saved quote
Agency                    String               Transport operator name
PickupDate                DateTime?            Pickup date (estimated), can be null on Maritime
DeliveryDate              DateTime?            Delivery date (estimated), can be null on Maritime
ExpirationDate            DateTime             Expiration date when quote will not be valid
TransitDays               Integer?             Days in transit (estimated), if delivery date has value
TotalPrice                Money                Total price 
Surcharges                List<Surcharge>      List with all surcharges relatives with this quote
=======================   ==================   ===========================================================

* Surcharge model:

=======================   ==================   ===========================================================
Name                      Type                 Description
=======================   ==================   ===========================================================
Description               String               Surcharge description (ISO code or text)
Price                     Money                Surcharge price object
=======================   ==================   ===========================================================

* Money model:

=======================   ==================   ===========================================================
Name                      Type                 Description
=======================   ==================   ===========================================================
Value                     Long                 Surcharge value (last 2 digits are decimals)
Currency                  String               Surcharge currency ISO code
=======================   ==================   ===========================================================

Save Quote
----------------

Request to save the rate, using the Id obtained in the Rating Requests.

**Example request**:
    
.. http:post:: /v1/quotes/(string: type)/(guid: rateId)


.. tabs::
    .. code-tab:: bash

        $ curl -X 'POST' \
            'https://<env>.freightol.com/v1/quotes/air/c3f74c81-819b-4671-a1d1-ad27c818dd6a'
            -H "Content-Type: application/json" \
            -H "Authorization: Bearer <token>"

**Example response**:


.. sourcecode:: json

    {
        "shipmentId": "a9e657c0-0d2d-44f3-bbf0-b70488065315",
        "success": true,
        "message": "Success"
    }

* Quote model    

=======================   ==================   ===========================================================
Name                      Type                 Description
=======================   ==================   ===========================================================
ShipmentId                Guid                  Guid of saved quote
Success                   Boolean               Boolean if operation was completed succesfully
Message                   String                Message if any error was happened
=======================   ==================   ===========================================================

Delete Quote
----------------

Request to delete a quote thats currently stored.


**Example request**:
        
.. http:delete:: /v1/quotes/(string: type)/(guid: quoteId)


.. tabs::

    .. code-tab:: bash

        $ curl -X DELETE \
            'https://<env>.freightol.com/v1/quotes/sea/fcl/c7ef9573-59df-4da0-0983-08d95c96c463 ' \
            -H "Content-Type: application/json" \
            -H "Authorization: Bearer <token>" \
            -d @body.json

* Query params

=====================   =============  =============   ================================================================
Name                     Type           Constraint      Description
=====================   =============  =============   ================================================================
Type                    ShipmentType    Mandatory       Shipment type
QuoteId                 Guid            Mandatory       Guid of quote ID
=====================   =============  =============   ================================================================

* Shipment type model:

+-----------+-------+---------+---------+---------+---------+
| Type      | Boxes | Pallets | Sea FCL | Sea LCL | Aerial  |
+===========+=======+=========+=========+=========+=========+
| **Param** | boxes | pallets | sea/fcl | sea/lcl | air     |
+-----------+-------+---------+---------+---------+---------+



.. autosummary::
   :toctree: generated
