=====================
Quotes
=====================

Saved quotes
----------------


Example request
~~~~~~~~~~~~~~~
    
    .. sourcecode::

        https://api.freightol.com/v1/quotes
        

Example response
~~~~~~~~~~~~~~~~

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

Parameters
~~~~~~~~~~
    
Response
~~~~~~~~

    =======================   ==================   ===========================================================
     Name                      Type                 Description
    =======================   ==================   ===========================================================
     QuoteId                   Guid                 Guid of saved quote
     Agency                    String               Transport operator name
     PickupDate                DateTime?            Pickup date (estimated), can be null on Maritime
     DeliveryDate              DateTime?            Delivery date (estimated), can be null on Maritime
     ExpirationDate            DateTime             Expiration date when quote will not be valid
     TransitDays               int                  Days in transit (estimated), if delivery date has value
     TotalPrice                MoneyModel           Total price 
     Surcharges                List<Surcharge>      List with all surcharges relatives with this quote
    =======================   ==================   ===========================================================

     * Surcharge:
    =======================   ==================   ===========================================================
     Name                      Type                 Description
    =======================   ==================   ===========================================================
     Description               String               Surcharge description 
     Price                     MoneyModel           Surcharge price
    =======================   ==================   ===========================================================

     * Moneymodel:
    =======================   ==================   ===========================================================
     Name                      Type                 Description
    =======================   ==================   ===========================================================
     Value                     Long                 Surcharge value (last 2 digits are decimals)
     Currency                  String               Surcharge currency
    =======================   ==================   ===========================================================

Delete Boxes quote
----------------


Example request
~~~~~~~~~~~~~~~
    
    .. sourcecode::

        https://api.freightol.com/v1/quotes/boxes/{quoteId}
        


Delete Pallets quote
----------------


Example request
~~~~~~~~~~~~~~~
    
    .. sourcecode::

        https://api.freightol.com/v1/quotes/pallets/{quoteId}
	

Delete FCL quote
----------------


Example request
~~~~~~~~~~~~~~~
    
    .. sourcecode::

        https://api.freightol.com/v1/quotes/sea/fcl/{quoteId}
	

Delete LCL quote
----------------


Example request
~~~~~~~~~~~~~~~
    
    .. sourcecode::

        https://api.freightol.com/v1/quote/boxes/{quoteId}
	

Delete Air quote
----------------


Example request
~~~~~~~~~~~~~~~
    
    .. sourcecode::

        https://api.freightol.com/v1/quotes/air/{quoteId}


.. autosummary::
   :toctree: generated

   lumache