=====================
Tracking
=====================


Shipments
--------------------------

**Example request**:
    
.. http:get:: /v1/tracking/shipments


.. tabs::
    .. code-tab:: bash

        $ curl \
            -H "Content-Type: application/json" \
            -H "Authorization: Bearer <token>" \
            https://<env>.freightol.com/v1/tracking/shipments

The query params are like,

=====================   ===========   =============    ================================================================
Name                     Type         Constraint       Description
=====================   ===========   =============    ================================================================
Origin                  String        Optional         Origin
Destination             String        Optional         Destination
ShipmentCode   	        String        Optional         ShipmentCode
TransportOperator       String        Optional         Transport Operator
StartDate               DateTime      Optional         Start date
EndDate                 DateTime      Optional         End date
=====================   ===========   =============    ================================================================

**Example response**:

    .. sourcecode:: json

        {
            "shipments": [
                {
                    "shipmentId": "339d8158-ca3d-4ed7-ac21-08d6ee8277b7",
                    "agency": "CorreosExpress",
                    "pickUpDate": "2019-06-12T09:28:00",
                    "deliveryDate": "2019-06-13T09:28:00",
                    "transitDays": 1,
                    "clientPrice": 7943,
                    "currency": "EUR",
                    "shipmentCode": "FR000002",
                    "currencyExchangedApplied": null,
                    "customs": true,
                    "insurance": true,
                    "shipmentType": "Box",
                    "trackingStatus": 0,
                    "customsStatus": null,
                    "origin": {
                        "state": "PV",
                        "countryCode": "ES",
                        "city": "Galdácano",
                        "postalCode": "48960",
                    },
                    "destination": {
                        "state": "CT",
                        "countryCode": "ES",
                        "city": "La Garriga",
                        "postalCode": "08530",
                    },
                    "hasInvoice": false
                }
            ],
            totalElements: 1
        }

 * Shipment model:

===========================   ====================   ===============================================
    Name                          Type                   Description
===========================   ====================   ===============================================
ShipmentId                    Guid                   Shipment ID
ShipmentCode                  String                 Shipment code
Agency                        String                 Agency
PickUpDate                    DateTime?              Pickup date
DeliveryDate                  DateTime?              Delivery date
TransitDays                   Integer                Transit days
ExpirationDate                DateTime               Expiration date
ClientPrice                   Longer                 Total price
Currency                      String	              Currency ISO code
CurrencyExchangedApplied      Double?	              Currency exchanged applied
Customs                       Boolean	              Customs
Insurance                     Boolean	              Insurance
ShipmentType                  String	              Shipment type
TrackingStatus                String		          Tracking status
CustomsStatus                 String	              Customs status
Origin                        ShipmentLocation	      Origin location
Destination                   ShipmentLocation	      Destination location
HasInvoice	           	       Boolean	              True if shipment has invoice saved
===========================   ====================   ===============================================

* Shipment location model:

===========================   ====================   ===============================================
    Name                          Type                   Description
===========================   ====================   ===============================================
Country code                   String	              Origin country ISO-2 code
State	                       String	              Origin state 
City	           	           String	              Origin city
PostalCode	                   String	              Origin postalCode
===========================   ====================   ===============================================


Shipment Info
------------------------------------------

.. warning::

   This endpoint is working in progress.

**Example request**:
    
    .. http:get:: /v1/tracking/shipments/(guid: shipmentId)


.. tabs::
    .. code-tab:: bash

        $ curl \
            -H "Content-Type: application/json" \
            -H "Authorization: Bearer <token>" \
            https://<env>.freightol.com/v1/tracking/shipments/339d8158-ca3d-4ed7-ac21-08d6ee8277b7
        
    
**Example response**:

    .. sourcecode:: json

     {
	    "commodityId": "339d8158-ca3d-4ed7-ac21-08d6ee8277b7",
	    "userId": "2b1d55e2-ce72-4ba3-12ca-08d93ca29348",
	    "commodityType": "Box",
	    "commodityDescription": "silla",
	    "commodityValue": 100,
	    "serviceName": "CorreosExpress CorreosExpress 24",
	    "reference": "FR000002",
	    "bookingReference": null,
	    "externalTrackingURL": null,
	    "trackingReference": null,
	    "commodityUnits": [
            {
                "commodityId": "339d8158-ca3d-4ed7-ac21-08d6ee8277b7",
                "commodityUnitId": "6050254f-ce83-4ab5-3c91-08d93cc1b5e4",
                "unitType": "Box",
                "measurementUnit": 1,
                "quantity": 1,
                "weight": 25,
                "length": 58,
                "width": 62,
                "height": 66,
                "isStackable": null,
                "palletType": null,
                "containerType": null,
                "isOwnedContainer": null,
                "isReeferContainer": null,
                "imoNumber": null
            }
	    ],
	    "paymentStatus": "Paid",
	    "paymentType": "TPV",
	    "customs": "True",
	    "insurance": "True",
	    "originAddress": "Pol in erletxes plataforma e nave 5",
	    "originState": "PV",
	    "originCountryCode": "ES",
	    "originCountryName": "Spain",
	    "originCity": "Galdácano",
	    "originPostalCode": "48960",
	    "originCompany": "Xayglobal ",
	    "originContact": "Aitor",
	    "originMail": "Peluquerianorte@hotmail.com",
	    "originPhone": "34 - 699660583",
	    "destinationAddress": "divina infantita Nº6",
	    "destinationState": "AL",
	    "destinationCountryCode": "ES",
	    "destinationCountryName": "Spain",
	    "destinationCity": "El Ejido/Almeria ",
	    "destinationPostalCode": "04700",
	    "destinationCompany": "Dreams salon sl",
	    "destinationContact": "Antonio",
	    "destinationMail": "peluquerianorte@hotmail.com",
	    "destinationPhone": "34 - 695733174",
	    "pickupDescription": null,
	    "deliveryDescription": null,
	    "pickupHours": "12:00 - 14:00"
	}
    

===========================   ====================   ===============================================
Name                          Type         	            Description
===========================   ====================   ===============================================
CommodityId                     Guid         	        Guid of the shipment
UserId                    	    Guid         	        Guid of the user
CommodityType	                String		            Commodity type
CommodityUnits	                List<Commodities>       Commodity type
CommodityDescription	        String		            Commodity description
CommodityValue	                Int   		            Commodity value
ServiceName	                    String		            Service name
Reference	           	        String		            Reference
BookingReference	            String		            Booking reference
ExternalTrackingURL	            String		            External tracking URL
TrackingReference	            String		            Tracking reference
PaymentType	                    String		            Payment type
PaymentStatus	                String		            Payment status
Customs		                    Boolean		            Customs
Insurance		                Boolean		            Insurance
OriginAddress	                String		            Origin address
OriginState	                    String		            Origin state
OriginCountryCode	            String		            Origin country code
OriginCountryName	            String		            Origin country name
OriginCity	           	        String		            Origin city
OriginPostalCode	            String		            Origin postalCode
OriginCompany	                String		            Origin company
OriginContact	                String		            Origin contact	 
OriginMail	         	        String		            Origin mail
OriginPhone	                    String		            Origin phone     
DestinationAddress	            String		            Destination address
DestinationState	            String		            Destination state
DestinationCountryCode          String		            Destination country code
DestinationCountryName	        String		            Destination country name
DestinationCity	                String		            Destination city
DestinationPostalCode	        String		            Destination postal code
DestinationCompany	            String		            Destination company
DestinationContact	            String		            Destination contact	 
DestinationMail	                String		            Destination mail
DestinationPhone	            String		            Destination phone
PickupDescription	            String		            Pickup description
DeliveryDescription             String		            Delivery description
PickupHours	                    String		            Pickup hours
===========================   ====================   ===============================================

* Commodities:
  
====================    ==========  =======================================
Name                    Type        Description
====================    ==========  =======================================
CommodityId             String      Shipment Id
CommodityUnitId         String      Commodity Id
UnitType                String      Unit type
MeasurementUnit         String      Measurement unit
Quantity                Integer     Quantity
Weight                  Double      Weight
Length                  Double      Dimensions: Length
Width                   Double      Dimensions: Width
Height                  Double      Dimensions: Height
IsStackable             String      True if pallets is stackable (only pallets)
PalletType              String      Pallet type (only Pallets)
ContainerType           String      Container type (only FCL)
IsOwnedContainer        String      True if container is owner (only FCL)
IsReeferContainer       String      True if container is reefer (only FCL)
ImoNumber               String      IMO number (only FCL)
====================    ==========  =======================================

Tracking messages
---------------------------------------

**Example request**:
    
    .. sourcecode::

        https://api.freightol.com/v1/tracking/cfab8e81-d328-4d4c-81eb-08d7523e7fee
        
    
**Example response**:

.. sourcecode:: json

	[
	   {
            "shipmentId": "cfab8e81-d328-4d4c-81eb-08d7523e7fee",
            "message": "Shipment Received At Transit Point.",
            "updatedDate": null,
            "status": "None",
            "groupIndex": null,
            "countryCode": null,
            "countryName": null,
            "city": "MV9",
            "address": null
	    },
	    {
            "shipmentId": "cfab8e81-d328-4d4c-81eb-08d7523e7fee",
            "message": "Shipment Received At Origin Depot.",
            "updatedDate": null,
            "status": "None",
            "groupIndex": null,
            "countryCode": null,
            "countryName": null,
            "city": "Korntal Muenchingen",
            "address": null
	    }
    ]
         

===========================   ==========   ===============================================
Name                          Type         Description
===========================   ==========   ===============================================
ShipmentId                      Guid         Guid of the shipment
Message                         String       Message
UpdatedDate                    DateTime?    Updated date
Status	                        String       Status
GroupIndex                      Integer?     Allows group massages when value is not null
CountryCode                     String       Country code  
CountryName                     String	     Country name
City                            String	     City
Address                         String	     Street address
===========================   ==========   ===============================================

.. autosummary::
   :toctree: generated