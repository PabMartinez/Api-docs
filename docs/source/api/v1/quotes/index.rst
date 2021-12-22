=====================
Quotes
=====================

Save Box Quote
----------------

Request to save the Box rate, using the Id obtained in the Box Rating Request.

**Example request**:
    
.. http:post:: /v1/quotes


.. tabs::
    .. code-tab:: bash

        $ curl -X 'POST' \
            'https://<env>.freightol.com/v1/quotes/box/3d86df83-0ffa-4bc3-b6cc-37c7d4058c0f'
            -H "Content-Type: application/json" \
            -H "Authorization: Bearer <token>"

**Example response**:


.. sourcecode:: json

    {
        "shipmentId": "f5daefae-d5e2-44cc-8b5e-92ade14abab7",
        "success": true,
        "message": "Success"
    }


Save Pallet Quote
----------------

Request to save the Pallet rate, using the Id obtained in the Pallet Rating Request.

**Example request**:
    
.. http:post:: /v1/quotes


.. tabs::
    .. code-tab:: bash

        $ curl -X 'POST' \
            'https://<env>.freightol.com/v1/quotes/pallet/86d1cf93-26cd-4352-80bf-1a50aa4ae045'
            -H "Content-Type: application/json" \
            -H "Authorization: Bearer <token>"

**Example response**:


.. sourcecode:: json

    {
        "shipmentId": "45b0c812-7cee-457a-97ce-0df1a4017ba9",
        "success": true,
        "message": "Success"
    }


Save Sea FCL Quote
----------------

Request to save the FCL rate, using the Id obtained in the Sea FCL Rating Request.

**Example request**:
    
.. http:post:: /v1/quotes


.. tabs::
    .. code-tab:: bash

        $ curl -X 'POST' \
            'https://<env>.freightol.com/v1/quotes/sea/fcl/27f62ac9-5768-457c-a870-9bfcece5fd5b'
            -H "Content-Type: application/json" \
            -H "Authorization: Bearer <token>"

**Example response**:


.. sourcecode:: json

    {
        "shipmentId": "7e117a17-d566-4bdc-9037-cf7f345dc394",
        "success": true,
        "message": "Success"
    }


Save Sea LCL Quote
----------------

Request to save the LCL rate, using the Id obtained in the Sea LCL Rating Request.

**Example request**:
    
.. http:post:: /v1/quotes


.. tabs::
    .. code-tab:: bash

        $ curl -X 'POST' \
            'https://<env>.freightol.com/v1/quotes/sea/lcl/4df3e744-63ec-4440-8aad-717e912fa652'
            -H "Content-Type: application/json" \
            -H "Authorization: Bearer <token>"

**Example response**:


.. sourcecode:: json

    {
        "shipmentId": "6bfd464b-6e02-4d5a-bc6a-7da0010a36f8",
        "success": true,
        "message": "Success"
    }

Save Air Quote
----------------

Request to save the Air rate, using the Id obtained in the Air Rating Request.

**Example request**:
    
.. http:post:: /v1/quotes


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
