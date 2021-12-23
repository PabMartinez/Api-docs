=====================
Tracking
=====================

Request to retrieve the tracking info of the shipments matching the filters.

Shipments
--------------------------

**Example request**:
    
.. http:get:: /v1/tracking/shipments


.. tabs::
    .. code-tab:: bash

        $ curl -X 'GET' \
            'https://<env>.freightol.com/v1/tracking/shipments' \
            -H "Content-Type: application/json" \
            -H "Authorization: Bearer <token>"


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
                "price": 7943,
                "currency": "EUR",
                "shipmentCode": "FR000002",
                "customs": true,
                "insurance": true,
                "shipmentType": "Box",
                "trackingStatus": "None",
                "customsStatus": null,
                "origin": {
                    "state": "PV",
                    "countryCode": "ES",
                    "city": "Galdácano",
                    "postalCode": "48960"
                },
                "destination": {
                    "state": "CT",
                    "countryCode": "ES",
                    "city": "La Garriga",
                    "postalCode": "08530"
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
Price                         Long                    Total price
Currency                      String	              Currency ISO code
Customs                       Boolean	              Customs
Insurance                     Boolean	              Insurance
ShipmentType                  String	              Shipment type
TrackingStatus                String?		          Tracking status
CustomsStatus                 String?	              Customs status
Origin                        ShipmentLocation	      Origin location
Destination                   ShipmentLocation	      Destination location
HasInvoice	           	      Boolean	              True if shipment has invoice saved
===========================   ====================   ===============================================

* Shipment location model:

===========================   ====================   ===============================================
    Name                          Type                   Description
===========================   ====================   ===============================================
Country code                   String	              Origin country ISO-2 code
State	                       String?	              Origin state 
City	           	           String	              Origin city
PostalCode	                   String	              Origin postalCode
===========================   ====================   ===============================================


Shipment Info
------------------------------------------

.. warning::

   This endpoint is working in progress.

**Example request**:
    
    .. http:get:: /v1/tracking/shipment/(guid: shipmentId)/detail


.. tabs::
    .. code-tab:: bash

        $ curl -X 'GET' \
            'https://<env>.freightol.com/v1/tracking/shipment/339d8158-ca3d-4ed7-ac21-08d6ee8277b7' \
            -H "Content-Type: application/json" \
            -H "Authorization: Bearer <token>"
            
        
    
**Example response**:

.. sourcecode:: json

    {
        "shipmentId": "cfab8e81-d328-4d4c-81eb-08d7523e7fee",
        "commodityType": "Box",
        "serviceName": "TNT Economy Express",
        "shipmentCode": null,
        "bookingCode": "XHB  835745",
        "externalTracking": "511706288",
        "externalTrackingURL": "https://www.tnt.com/express/es_es/site/herramientas-envio/seguimiento.html?searchType=con&cons=511706288",
        "customs": null,
        "insurance": null,
        "origin": {
            "address": "CAKEMORE ROAD, ROWLEY REGIS, WEST MIDLANDS",
            "state": "Inglaterra",
            "city": "Midlands Occidentales",
            "postalCode": "B65 0QW",
            "countryCode": "GB",
            "company": "CUBE PRECISION ENGINEERING LTD",
            "contact": "SID HICKMAN",
            "mail": "s.hickman@cubeprecision.com",
            "phone": "00441 - 215593096"
        },
        "destination": {
            "address": "POLIGONO IND. PARCELA M 4.1",
            "state": "PV",
            "city": "Itziar-Deba",
            "postalCode": "20829",
            "countryCode": "ES",
            "company": "MACHINE TOOL ENGINEERING, S.A.",
            "contact": "Esteban",
            "mail": "esteban@mtemachine.com",
            "phone": "34 - 943606383"
        },
        "commodity": {
            "commodityDescription": "NIVEL TCP",
            "commodityValue": 0,
            "commodityUnits": [
                {
                "commodityId": "cfab8e81-d328-4d4c-81eb-08d7523e7fee",
                "commodityUnitId": "ec794362-100f-496b-96eb-08d93cd24e74",
                "unitType": "Box",
                "measurementUnit": 1,
                "quantity": 1,
                "weight": 16,
                "length": 37,
                "width": 37,
                "height": 40,
                "isStackable": null,
                "palletType": null,
                "containerType": null,
                "isOwnedContainer": null,
                "isReeferContainer": null,
                "imoNumber": null
                }
            ]
        }
    }
        

===========================   ====================   ===============================================
Name                          Type         	            Description
===========================   ====================   ===============================================
ShipmentId                      Guid         	        Guid of the shipment
ShipmentType	                String		            Commodity type
Commodity                       Commodity               Commodity info
ServiceName	                    String		            Service name
Reference	           	        String		            Reference
BookingCode        	            String		            Booking reference
ExternalTrackingURL	            String		            External tracking URL
ExternalTracking	            String		            Tracking reference
Customs		                    Boolean		            Customs
Insurance		                Boolean		            Insurance
Origin                          ShipmentLocation        Origin address
Destination                     ShipmentLocation        Destination address
PickupDescription	            String		            Pickup description
DeliveryDescription             String		            Delivery description
PickupHours	                    String		            Pickup hours
===========================   ====================   ===============================================

* Shipment location model:
  
====================    ==========  =======================================
Name                    Type        Description
====================    ==========  =======================================
Address	                String		 Street adress
State	                String		 State
CountryCode	            String		 Country code
City	           	    String		 City
PostalCode	            String		 PostalCode
Company	                String		 Company
Contact	                String		 Contact	 
Mail	         	    String		 Mail
Phone	                String		 Phone    
====================    ==========  =======================================

* Commodity info model:
  
====================    ==================  =======================================
Name                    Type                Description
====================    ==================  =======================================
CommodityUnits	        List<Commodities>   Commodity type
CommodityDescription	String		        Commodity description
CommodityValue	        Integer  	        Commodity value   
====================    ==================  =======================================

* Commodities item model:
  
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
    
    .. http:get:: /v1/tracking/shipment/(string: shipmentCode)/messages


.. tabs::
    .. code-tab:: bash

        $ curl -X 'GET' \
            'https://<env>.freightol.com/v1/tracking/shipment/FR00061D/detail' \
            -H "Content-Type: application/json" \
            -H "Authorization: Bearer <token>"
        
    
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
