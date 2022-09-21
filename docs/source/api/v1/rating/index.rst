===================
Rating
===================


Box Rating
----------------

Request to retrieve the rates for Box shipment(Terrestrial)

Returns a list containing the terrestrial rates for Boxes.

**Example request**:
    
.. http:post:: /v1/rates/boxes


.. tabs::

    .. code-tab:: bash

        $ curl -X POST \
            'https://<env>.freightol.com/v1/rates/boxes' \
            -H "Content-Type: application/json" \
            -H "Authorization: Bearer <token>" \
            -d @body.json
            

The content of ``body.json`` is like,
	
.. sourcecode:: json

	{
		"origin": {
			"postalCode": "24008",
			"country": "ES",
			"city": "León",
			"state": "CYL",
			"street": null,
			"coords": null
		},
		"destination": {
			"postalCode": "33001",
			"country": "ES",
			"city": "Ovieod",
			"state": "AST",
			"street": null,
			"coords": {
                "lat": 41.3006,
                "lng": 2.07976
            }
		},
		"pickUpDate": "2021-10-28T16:54:30.094Z",
		"goodsDescription": "string",
		"goodsValue": 100,
		"insurance": true,
		"customs": true,
		"currency": "EUR",
		"dangerousCargo": true,
		"boxes": [
			{
				"quantity": 1,
				"length": 10,
				"width": 10,
				"height": 10,
				"weight": 10,
				"measurementUnit": "CmKg"
			}
		]
	}

* Boxes Rating model:

==================   ===================   =============   ===============================================
Name                 Type                  Constraint      Description
==================   ===================   =============   ===============================================
Origin               Location              Mandatory       Object containing the origin info.
Destination          Location              Mandatory       Object containing the destination info.
Boxes                List<Box>      	   Mandatory       List of boxes for the shipment.
PickUpDate           DateTime              Mandatory       Requests pickup date
GoodsDescription     String                Mandatory       Goods description
GoodsValue           Long                  Mandatory       Goods value (last 2 digits are decimals)
Insurance            Boolean               Mandatory       True if insurance is requested
Customs              Boolean               Mandatory       True if customs is requered
Currency             String                Mandatory       Currency (Ex:EUR)
DangerousCargo       Boolean               Mandatory       Check if dangerous cargo is sent
==================   ===================   =============   ===============================================

* Location model:
  
=============     ========    =============      =======================================
Name              Type        Constraint         Description
=============     ========    =============      =======================================
PostalCode        String      Mandatory 	      PostalCode of the shipment
Country           String      Mandatory 	      Country ISO2 of the shipment
City              String      Mandatory 	      City of the shipment
State             String      Mandatory 	      State of the shipment
Street            String      Optional 	          Street of the shipment
Coords            Coord       Optional 	      	  Geolocation data
=============     ========    =============      =======================================

* Coord model:

=============     ========     =============    ======================================================
Name              Type         Constraint       Description
=============     ========     =============    ======================================================
Lat               Double       Mandatory     	Location latitude, precision is (3, 6).
Lng               Double       Mandatory 		Location longitude, precision is (3, 6).
=============     ========     =============    ======================================================

* Box model:
  
==================    =========    =============     =======================================
Name                  Type         Constraint        Description
==================    =========    =============     =======================================
Quantity              Integer      Mandatory 	  	 Quantity
Length                Double       Mandatory 	  	 Length of the box
Width                 Double       Mandatory 	  	 Width of the box
Height                Double       Mandatory	  	 Height of the box
Weight                Double       Mandatory  	  	 Weight of the box
MeasurementUnit       String       Mandatory 	  	 Measurement unit
==================    =========    =============     =======================================


**Example response**:
   
.. sourcecode:: json

	{
		"quoteId": "d929fedc-83e7-4a81-b274-938af067e662",
		"origin": {
			"postalCode": "24008",
			"country": "ES",
			"city": "Leon",
			"state": "CYL",
			"street": null,
			"coords": {
				"lat": 43.12345,
				"lng": -8.45678
			}
		},
		"destination": {
			"postalCode": "33001",
			"country": "ES",
			"city": "Oviedo",
			"state": "AST",
			"street": null,
			"coords": {
				"lat": null,
				"lng": null
			}
		},
		"pickUpDate": "2021-10-28T14:54:30.094",
		"rates": [
			{
				"id": "cacc83d3-de42-4148-ba8b-e52b5bdbd2cf",
				"agency": "UPS",
				"service": "UPS Standard",
				"pickUpDate": "2021-10-28T17:30:00",
				"deliveryDate": "2021-10-29T21:30:00",
				"transitDays": 2,
				"expirationDate": "2021-10-27T22:00:00",
				"price": 2003,
				"extraInfo": [
					"Services listed as guaranteed are backed by a money-back guarantee for transportation charges only. See Terms and Conditions in the Service Guide for details. Certain commodities and high value shipments may require additional transit time for customs clearance.",
					"Your invoice may vary from the displayed reference rates",
					"Horario de corte: 29/10/2021 23:30:00"
				]
			},
			{
				"id": "ab0fa27b-f207-4c39-adca-d8d34afc757c",
				"agency": "UPS",
				"service": "UPS Express Saver",
				"pickUpDate": "2021-10-28T17:30:00",
				"deliveryDate": "2021-10-29T21:30:00",
				"transitDays": 2,
				"expirationDate": "2021-10-27T22:00:00",
				"price": 4139,
				"extraInfo": [
					"Services listed as guaranteed are backed by a money-back guarantee for transportation charges only. See Terms and Conditions in the Service Guide for details. Certain commodities and high value shipments may require additional transit time for customs clearance.",
					"Your invoice may vary from the displayed reference rates",
					"Horario de corte: 29/10/2021 23:30:00"
				]
			},
			{
				"id": "2f59fcba-d195-4d72-9436-5830fdc163b6",
				"agency": "UPS",
				"service": "UPS Worldwide Express",
				"pickUpDate": "2021-10-28T17:30:00",
				"deliveryDate": "2021-10-29T08:30:00",
				"transitDays": 1,
				"expirationDate": "2021-10-27T22:00:00",
				"price": 4630,
				"extraInfo": [
					"Services listed as guaranteed are backed by a money-back guarantee for transportation charges only. See Terms and Conditions in the Service Guide for details. Certain commodities and high value shipments may require additional transit time for customs clearance.",
					"Your invoice may vary from the displayed reference rates",
					"Horario de corte: 29/10/2021 10:30:00"
				]
			},
			{
				"id": "f2a96a96-730d-471c-b0cb-f627d944f448",
				"agency": "UPS",
				"service": "UPS Worldwide Express Plus",
				"pickUpDate": "2021-10-28T17:30:00",
				"deliveryDate": "2021-10-29T07:00:00",
				"transitDays": 1,
				"expirationDate": "2021-10-27T22:00:00",
				"price": 10257,
				"extraInfo": [
					"Services listed as guaranteed are backed by a money-back guarantee for transportation charges only. See Terms and Conditions in the Service Guide for details. Certain commodities and high value shipments may require additional transit time for customs clearance.",
					"Your invoice may vary from the displayed reference rates",
					"Horario de corte: 29/10/2021 09:00:00"
				]
			}
		]
	}


* Box Quote model:

=============     =============    ======================================================
Name               Type            Description
=============     =============    ======================================================
QuoteId           Guid             Guid of the quote
Origin            Location         Object containing the origin info.
Destination       Location         Object containing the destination info.
PickUpDate        DateTime         Pickup date
Rates             List<BoxRate>    List containing the rates
=============     =============    ======================================================

* Location model:
  
=============     ========    =======================================
Name              Type        Description
=============     ========    =======================================
PostalCode        String      Zip code of the shipment
Country           String      Country ISO2 of the shipment
City              String      City of the shipment
State             String?     State of the shipment
Street            String?     Street of the shipment
Coords            Coord?      Geolocation data
=============     ========    =======================================

* Box Rate model:
  
===================    ====================    ==========================================================
	Name                    Type                    Description
===================    ====================    ==========================================================
Id                     Guid                    Guid of rate
Agency                 TransportOperator       Agency
Service                String                  Service
PickUpDate             DateTime                Pickup date
DeliveryDate           DateTime                Delivery date
TransitDays            Integer                 Transit days
ExpirationDate         DateTime                Expiration date
Price                  Long                    Price (Considering 2 last digits as decimals).      
ExtraInfo              List<String>?           List of extra info
===================    ====================    ==========================================================

     
    
Pallet Rating
----------------

Request to retrieve the rates for Pallet shipment(Terrestrial)

Returns a list containing the terrestrial rates for Pallets.

**Example request**:
    
.. http:post:: /v1/rates/pallets


.. tabs::

    .. code-tab:: bash

        $ curl -X POST \
            'https://<env>.freightol.com/v1/rates/pallets'
            -H "Content-Type: application/json" \
            -H "Authorization: Bearer <token>" \
            -d @body.json

The content of ``body.json`` is like,
        
.. sourcecode:: json

	{
		"origin": {
			"postalCode": "24008",
			"country": "ES",
			"city": "León",
			"state": "CYL",
			"street": null,
			"coords": {
                "lat": 41.3006,
                "lng": 2.07976
            }
		},
		"destination": {
			"postalCode": "33001",
			"country": "ES",
			"city": "Oviedo",
			"state": "AST",
			"street": null,
			"coords": {
                "lat": 41.3006,
                "lng": 2.07976
            }
		},
		"pickUpDate": "2021-10-28T16:54:30.094Z",
		"goodsDescription": "string",
		"goodsValue": 100,
		"insurance": true,
		"customs": true,
		"currency": "EUR",
		"dangerousCargo": true,
		"pallets": [
			{
				"quantity": 1,
				"length": 10,
				"width": 10,
				"height": 10,
				"weight": 10,
				"measurementUnit": "CmKg",
				"isStackable": false,
				"palletType": "Custom"
			}
		]
	}

* Pallets Rating model:
  
==================   ===================   =============   ===============================================
Name                 Type                  Constraint      Description
==================   ===================   =============   ===============================================
Origin               Location              Mandatory       Object containing the origin info.
Destination          Location              Mandatory       Object containing the destination info.
Pallets              List<Pallet>          Mandatory       List of pallets for the shipment.
PickUpDate           DateTime              Mandatory       Pickup date
GoodsDescription     String                Mandatory       Goods description
GoodsValue           Long                  Mandatory       Goods value (last 2 digits are decimals)
Insurance            Boolean               Mandatory       Has insurance
Customs              Boolean               Mandatory       Has customs
Currency             String                Mandatory       Currency (Ex:EUR)
DangerousCargo       Boolean               Mandatory       True if commodity include dangerous cargo
==================   ===================   =============   ===============================================

* Location model:

=============     ========    =============      =======================================
Name              Type        Constraint         Description
=============     ========    =============      =======================================
PostalCode        String      Mandatory 	      PostalCode of the shipment
Country           String      Mandatory 	      Country of the shipment
City              String      Mandatory 	      City of the shipment
State             String      Mandatory 	      State of the shipment
Street            String      Optional 	      	  Street of the shipment
Coords            Coord       Optional 	          Geolocation data
=============     ========    =============      =======================================

* Coord model:

=============     ========     =============    ======================================================
Name              Type         Constraint       Description
=============     ========     =============    ======================================================
Lat               Double       Mandatory        Location latitude, precision is (3, 6).
Lng               Double       Mandatory 	    Location longitude, precision is (3, 6).
=============     ========     =============    ======================================================

* Pallet:
  
==================    =============      ==============     ==========================================================
Name                  Type               Constraint         Description
==================    =============      ==============     ==========================================================
Quantity              Integer            Mandatory 	 		Quantity of pallet
Length                Double             Mandatory 	 		Length of the pallet
Width                 Double             Mandatory 	 		Width of the pallet
Height                Double             Mandatory	        Height of the pallet
Weight                Double             Mandatory  	 	Weight of the pallet
MeasurementUnit       String             Mandatory 	 		Measurement unit
IsStackable	          Boolean            Mandatory          True if pallet is stackable
PalletType            PalletType         Mandatory		 	Pallet Type
==================    =============      ==============     ==========================================================

* Pallet type model:
  
================     =======================================  
Name                  Description
================     =======================================  
Custom                Customs size
Euro1                 EURO1 size standard
Euro2                 EURO2 size standard
Uk      		      UK size standard
================     =======================================  


**Example response**:
   
.. sourcecode:: json

    {
		"quoteId": "065cbdf0-2bb8-48f0-a1f7-fc5a35c60592",
		"origin": {
			"postalCode": "24008",
			"country": "ES",
			"city": "Leon",
			"state": "CYL",
			"street": null,
			"coords": {
				"lat": null,
				"lng": null
			}
		},
		"destination": {
			"postalCode": "33001",
			"country": "ES",
			"city": "Oviedo",
			"state": "AST",
			"street": null,
			"coords": {
				"lat": null,
				"lng": null
			}
		},
		"pickUpDate": "2021-10-28T14:54:30.094",
		"rates": [
			{
				"id": "8d34a39b-d082-403c-931d-af7c42e901eb",
				"agency": "UPS",
				"service": "UPS Standard",
				"pickUpDate": "2021-10-28T17:30:00",
				"deliveryDate": "2021-10-29T21:30:00",
				"transitDays": 2,
				"expirationDate": "2021-10-27T22:00:00",
				"price": 2003,
				"extraInfo": [
					"Services listed as guaranteed are backed by a money-back guarantee for transportation charges only. See Terms and Conditions in the Service Guide for details. Certain commodities and high value shipments may require additional transit time for customs clearance.",
					"Your invoice may vary from the displayed reference rates",
					"Horario de corte: 29/10/2021 23:30:00"
				]
			},
			{
				"id": "31978773-3a22-44ac-b965-feb41bfc3a20",
				"agency": "UPS",
				"service": "UPS Express Saver",
				"pickUpDate": "2021-10-28T17:30:00",
				"deliveryDate": "2021-10-29T21:30:00",
				"transitDays": 2,
				"expirationDate": "2021-10-27T22:00:00",
				"price": 4139,
				"extraInfo": [
					"Services listed as guaranteed are backed by a money-back guarantee for transportation charges only. See Terms and Conditions in the Service Guide for details. Certain commodities and high value shipments may require additional transit time for customs clearance.",
					"Your invoice may vary from the displayed reference rates",
					"Horario de corte: 29/10/2021 23:30:00"
				]
			},
			{
				"id": "6ceff759-046f-4acf-9a4b-3c310324e533",
				"agency": "UPS",
				"service": "UPS Worldwide Express",
				"pickUpDate": "2021-10-28T17:30:00",
				"deliveryDate": "2021-10-29T08:30:00",
				"transitDays": 1,
				"expirationDate": "2021-10-27T22:00:00",
				"price": 4630,
				"extraInfo": [
					"Services listed as guaranteed are backed by a money-back guarantee for transportation charges only. See Terms and Conditions in the Service Guide for details. Certain commodities and high value shipments may require additional transit time for customs clearance.",
					"Your invoice may vary from the displayed reference rates",
					"Horario de corte: 29/10/2021 10:30:00"
				]
			},
			{
				"id": "167624bc-d698-4666-b6ba-12f360753766",
				"agency": "UPS",
				"service": "UPS Worldwide Express Plus",
				"pickUpDate": "2021-10-28T17:30:00",
				"deliveryDate": "2021-10-29T07:00:00",
				"transitDays": 1,
				"expirationDate": "2021-10-27T22:00:00",
				"price": 10257,
				"extraInfo": [
					"Services listed as guaranteed are backed by a money-back guarantee for transportation charges only. See Terms and Conditions in the Service Guide for details. Certain commodities and high value shipments may require additional transit time for customs clearance.",
					"Your invoice may vary from the displayed reference rates",
					"Horario de corte: 29/10/2021 09:00:00"
				]
			}
		]
	}

   
* Pallets Quote model: 

=============     ===================    ======================================================
Name               Type           		  Description
=============     ===================    ======================================================
QuoteId           Guid             			Guid of the quote
Origin            Location         			Object containing the origin info.
Destination       Location         			Object containing the destination info.
PickUpDate        DateTime         	  		Pickup date
Rates             List<PalletRate>       	List containing the rates
=============     ===================    ======================================================

* Location model:

=============     ========    =======================================
Name              Type        Description
=============     ========    =======================================
PostalCode        String      PostalCode of the shipment
Country           String      Country of the shipment
City              String      City of the shipment
State             String?     State of the shipment
Street            String?     Street of the shipment
Coords            Coord?      Geolocation data
=============     ========    =======================================

* Coord model:

=============     ========     ======================================================
Name              Type         Description
=============     ========     ======================================================
Lat               Double       Location latitude, precision is (3, 6).
Lng               Double       Location longitude, precision is (3, 6).
=============     ========     ======================================================

* Pallet Rate model:

===================    ====================    ==========================================================
Name                    Type                    Description
===================    ====================    ==========================================================
Id                     Int                     Quantity
Agency                 Double                  Agency
Service                Double                  Service
PickUpDate             Double                  Pickup date
DeliveryDate           Double                  Delivery date
TransitDays            Integer                 Transit days
ExpirationDate         DateTime                Expiration date
Price                  Long                    Price (Considering 2 last digits as decimals).      
ExtraInfo              List<String>?           List of extra info
===================    ====================    ==========================================================
    
FCL Sea Rating
----------------------------

Request to retrieve the rates for FCL sea shipment(Maritime)

Returns a list containing the Sea rates for FCL.

**Example request**:

.. http:post:: /v1/rates/sea/fcl


.. tabs::

    .. code-tab:: bash

        $ curl -X POST \
            'https://<env>.freightol.com/v1/rates/sea/fcl' \
            -H "Content-Type: application/json" \
            -H "Authorization: Bearer <token>" \
            -d @body.json

The content of ``body.json`` is like,

        
.. sourcecode:: json

	{
		"currency": "EUR",
		"customs": false,
		"goodsDescription": "PRODUCTOS ORIGEN ANIMAL",
		"goodsValue": 10,
		"pickUpDate": "2021-11-09T00:00:00.000Z",
		"insurance": false,
		"containers": [
			{
				"quantity": 1,
				"weight": 1000,
				"measurementUnit": "CmKg",
				"type": "DRY20",
				"isOwnedContainer": false,
				"isReeferContainer": false,
				"imoNumber": "1234"
			}
		],
		"originServiceType": "CY",
		"destinationServiceType": "SD",
		"origin": {
			"postalCode": "999077",
			"country": "HK",
			"city": "Hong Kong",
			"state": "Sai Kung",
			"street": null,
			"coords": null
		},
		"destination": {
			"postalCode": "08001",
			"country": "ES",
			"city": "Barcelona",
			"state": "Cataluña",
			"street": null,
			"coords": null
		},
		"originUnLocCode": "HKHKG",
		"originRkstCode": "HKHKG",
		"destinationUnLocCode": "ESBCN",
		"destinationRkstCode": "ESBCN"
	}

* FCL Quote model:

==========================   ==========================   ===============   ===============================================
Name                          Type                        Constraint         Description
==========================   ==========================   ===============   ===============================================
Origin                          Location                   Optional          Object containing the origin info.
Destination                     Location                   Optional          Object containing the destination info.
Containers                      List<Containers>           Mandatory         List of containers for the shipment.
PickUpDate                      DateTime                   Mandatory         Pickup date
GoodsDescription             	String                     Optional          Goods description
GoodsValue                      Long                       Optional          Goods value (last 2 digits are decimals)
Insurance                       Boolean                    Optional          Has insurance
Customs                         Boolean                    Optional          Has customs
OriginServiceType               ServiceType                Mandatory         Origin service type
DestinationServiceType          ServiceType                Mandatory         Destination service type
OriginUnLocCode                 String                     Mandatory         Origin UnLoc code
DestinationUnLocCode         	String                     Mandatory         Destination UnLoc code
==========================   ==========================   ===============   ===============================================

* Service type model:
  
=============     =======================================
Name			  Description
=============     =======================================
CY                Container Yard
SD                Store Door
=============     =======================================

* Location model:
  
=============     ========    =============      =======================================
Name              Type        Constraint         Description
=============     ========    =============      =======================================
PostalCode        String      Mandatory 	      PostalCode of the shipment
Country           String      Mandatory 	      Country of the shipment
City              String      Mandatory 	      City of the shipment
State             String      Mandatory 	      State of the shipment
Street            String      Optional 	      	  Street of the shipment
Coords            Coord       Optional 	          Geolocation data
=============     ========    =============      =======================================

* Coord model:
  
=============     ========     =============    ======================================================
Name              Type         Constraint       Description
=============     ========     =============    ======================================================
Lat               Double       Mandatory        Port latitude, precision is (3, 6).
Lng               Double       Mandatory 	    Port longitude, precision is (3, 6).
=============     ========     =============    ======================================================

* Container model:
  
======================    =============      =============     =======================================
Name                      Type                Constraint        Description
======================    =============      =============     =======================================
Quantity                  Integer             Mandatory 	    Quantity
Weight                    Double              Mandatory  	    Weight of the container
MeasurementUnit           String              Mandatory 	    Measurement unit: CmKg
Type                      ContainerType       Mandatory 	    Length of the container
IsOwnedContainer          Boolean             Mandatory 	    Ture if container is Owned
IsReeferContainer         Boolean             Mandatory	        True if container is Reefer (only RF) 
ImoNumber                 String	          Optional	        IMO number
======================    =============      =============     =======================================

* Container type model:
  
=============     =======================================
Name              Description
=============     =======================================
DRY20      			20' General purpose Standard    
DRY40      			40' General purpose Standard
HDRY40      		40' High Cube General purpose  
HDRY45      		45' High Cube General purpose  
NOR20      			20' Non-Operating Standard
NOR40      			40' Non-Operating Standard
HNOR40      		40' Non-Operating High Cube
HNOR45      		45' Non-Operating High Cube 
RF20      			20' Reefer Standard
RF40      			40' Reefer Standard
HRF40      			40' Reefer High Cube  
RF45      			45' Reefer Standard
OPENTOP20      		20' Open Top Standard
OPENTOP40      		40' Open Top Standard
HOPENTOP40      	40' Open Top High Cube
FLATRACK20      	20' Flat Rack Standard
FLATRACK40      	40' Flat Rack Standard
HFLATRACK40      	40' Flat Rack High Cube
=============     =======================================

**Example response**:
   
.. sourcecode:: json

    {
    "quoteId": "3a9f1340-7565-45b2-82bd-0cbfb8968481",
    "origin": {
        "postalCode": null,
        "country": "ES",
        "city": null,
        "state": null,
        "street": null,
        "coords": {
        "lat": null,
        "lng": null
        }
    },
    "destination": {
        "postalCode": null,
        "country": "HK",
        "city": null,
        "state": null,
        "street": null,
        "coords": {
        "lat": null,
        "lng": null
        }
    },
    "pickUpDate": "2022-09-26T00:00:00",
    "rates": [
        {
        "sealine": "MAEU009A",
        "scheduleDetails": [
            {
            "routeDetails": [
                {
                "fromLocation": {
                    "type": "TERMINAL",
                    "rkstCode": "ESBCNBS",
                    "unLocCode": "ESBCN",
                    "city": "Barcelona",
                    "countryCode": "ES",
                    "expectedDate": "2022-10-14T01:00:00"
                },
                "toLocation": {
                    "type": "TERMINAL",
                    "rkstCode": "SGSINPS",
                    "unLocCode": "SGSIN",
                    "city": "Singapore",
                    "countryCode": "SG",
                    "expectedDate": "2022-11-14T16:12:00"
                },
                "transport": {
                    "transportMode": "VESSEL",
                    "name": "MSC LENI",
                    "code": "9839454"
                }
                }
            ],
            "deadlines": [
                {
                "deadLineKey": "CY",
                "type": "Documentation",
                "deadLine": "2022-10-11T09:00:00",
                "name": "Commercial Cargo Cutoff"
                },
                {
                "deadLineKey": "SINONAMS",
                "type": "Documentation",
                "deadLine": "2022-10-10T15:00:00",
                "name": "Shipping Instructions Deadline"
                },
                {
                "deadLineKey": "VGM",
                "type": "Documentation",
                "deadLine": "2022-10-12T09:00:00",
                "name": "Commercial Verified Gross Mass Deadline"
                },
                {
                "deadLineKey": "LCD",
                "type": "Marine Services",
                "deadLine": "2022-10-10T11:00:00",
                "name": "Loadlist Closure Deadline"
                },
                {
                "deadLineKey": "CSPD",
                "type": "Marine Services",
                "deadLine": "2022-10-10T15:00:00",
                "name": "Coprar to Stowage Planners Deadline"
                },
                {
                "deadLineKey": "FLD",
                "type": "Marine Services",
                "deadLine": "2022-10-10T15:00:00",
                "name": "Final Loadlist Deadline"
                }
            ]
            },
            {
            "routeDetails": [
                {
                "fromLocation": {
                    "type": "TERMINAL",
                    "rkstCode": "SGSINPS",
                    "unLocCode": "SGSIN",
                    "city": "Singapore",
                    "countryCode": "SG",
                    "expectedDate": "2022-11-21T19:00:00"
                },
                "toLocation": {
                    "type": "TERMINAL",
                    "rkstCode": "HKHKGMO",
                    "unLocCode": "HKHKG",
                    "city": "Hong Kong",
                    "countryCode": "HK",
                    "expectedDate": "2022-11-25T08:00:00"
                },
                "transport": {
                    "transportMode": "VESSEL",
                    "name": "MAERSK LIMA",
                    "code": "9526875"
                }
                }
            ],
            "deadlines": [
                {
                "deadLineKey": "CY",
                "type": "Documentation",
                "deadLine": "2022-11-18T21:00:00",
                "name": "Commercial Cargo Cutoff"
                },
                {
                "deadLineKey": "SINONAMS",
                "type": "Documentation",
                "deadLine": "2022-11-17T15:00:00",
                "name": "Shipping Instructions Deadline"
                },
                {
                "deadLineKey": "VGM",
                "type": "Documentation",
                "deadLine": "2022-11-19T03:00:00",
                "name": "Commercial Verified Gross Mass Deadline"
                },
                {
                "deadLineKey": "LCD",
                "type": "Marine Services",
                "deadLine": "2022-11-18T04:00:00",
                "name": "Loadlist Closure Deadline"
                },
                {
                "deadLineKey": "CSPD",
                "type": "Marine Services",
                "deadLine": "2022-11-17T23:00:00",
                "name": "Coprar to Stowage Planners Deadline"
                },
                {
                "deadLineKey": "FLD",
                "type": "Marine Services",
                "deadLine": "2022-11-18T15:00:00",
                "name": "Final Loadlist Deadline"
                },
                {
                "deadLineKey": "SCDD",
                "type": "Marine Services",
                "deadLine": "2022-11-17T21:00:00",
                "name": "Special Cargo Documentation Deadline"
                }
            ]
            }
        ],
        "conditions": [
            {
            "chargeType": "Demurrage",
            "containerSizeType": "20DRY",
            "freeTimeStartEvent": "DISCHARGE",
            "freeTimeGrantInDays": 5,
            "commodity": "GENERAL CARGO",
            "price": {
                "value": 50000,
                "currency": "HKD"
            }
            },
            {
            "chargeType": "Detention",
            "containerSizeType": "20DRY",
            "freeTimeStartEvent": "DISCHARGE",
            "freeTimeGrantInDays": 7,
            "commodity": "GENERAL CARGO",
            "price": {
                "value": 25000,
                "currency": "HKD"
            }
            }
        ],
        "penalties": [
            {
            "containerSizeType": "20DRY",
            "charges": [
                {
                "penaltyType": "AmmendmentFee",
                "price": {
                    "value": 1800,
                    "currency": "USD"
                },
                "name": "Amendment Fee"
                },
                {
                "penaltyType": "AmmendmentFee",
                "price": {
                    "value": 2500,
                    "currency": "USD"
                },
                "name": "Cancellation Fee"
                },
                {
                "penaltyType": "AmmendmentFee",
                "price": {
                    "value": 5000,
                    "currency": "USD"
                },
                "name": "No Show Fee"
                },
                {
                "penaltyType": "AmmendmentFee",
                "price": {
                    "value": -2500,
                    "currency": "USD"
                },
                "name": "Compensation Fee"
                }
            ]
            }
        ],
        "surchages": {
            "surchargesPerFreight": [
            {
                "quantity": 1,
                "basis": "PER_CONTAINER",
                "type": "Freight",
                "chargeCode": "FRT",
                "description": "Basic Ocean Freight",
                "value": 40000,
                "currency": "USD",
                "containerSizeType": "DRY20"
            },
            {
                "quantity": 1,
                "basis": "PER_CONTAINER",
                "type": "Freight",
                "chargeCode": "EFF",
                "description": "Environmental Fuel Fee",
                "value": 15200,
                "currency": "USD",
                "containerSizeType": "DRY20"
            },
            {
                "quantity": 1,
                "basis": "PER_CONTAINER",
                "type": "Freight",
                "chargeCode": "asdad",
                "description": "asda",
                "value": 10000,
                "currency": "USD",
                "containerSizeType": "DRY20"
            }
            ],
            "surchargesAtOrigin": [
            {
                "quantity": 1,
                "basis": "PER_DOC",
                "type": "Origin",
                "chargeCode": "ODF",
                "description": "Documentation Fee Origin",
                "value": 5000,
                "currency": "EUR",
                "containerSizeType": null
            },
            {
                "quantity": 1,
                "basis": "PER_CONTAINER",
                "type": "Origin",
                "chargeCode": "PAE",
                "description": "Port Additionals / Port Dues Export",
                "value": 3500,
                "currency": "EUR",
                "containerSizeType": "DRY20"
            },
            {
                "quantity": 1,
                "basis": "PER_CONTAINER",
                "type": "Origin",
                "chargeCode": "MHE",
                "description": "Merchant Haulage Export",
                "value": 3500,
                "currency": "EUR",
                "containerSizeType": "DRY20"
            },
            {
                "quantity": 1,
                "basis": "PER_CONTAINER",
                "type": "Origin",
                "chargeCode": "VGM",
                "description": "Verified Gross Mass Charge",
                "value": 1800,
                "currency": "EUR",
                "containerSizeType": "DRY20"
            }
            ],
            "surchargesAtDestination": [
            {
                "quantity": 1,
                "basis": "PER_CONTAINER",
                "type": "Destination",
                "chargeCode": "DHC",
                "description": "Terminal Handling Service - Destination",
                "value": 220000,
                "currency": "HKD",
                "containerSizeType": "DRY20"
            },
            {
                "quantity": 1,
                "basis": "PER_DOC",
                "type": "Destination",
                "chargeCode": "DDF",
                "description": "Documentation fee - Destination",
                "value": 55000,
                "currency": "HKD",
                "containerSizeType": null
            }
            ]
        },
        "id": "280358e3-912b-4b0e-8765-34714d17ea80",
        "agency": "Maerks",
        "service": "Maersk Spot",
        "pickUpDate": "2022-10-14T00:00:00",
        "deliveryDate": "2022-11-25T08:00:00",
        "transitDays": 43,
        "expirationDate": "2022-09-22T06:39:47.7944899",
        "extraInfo": null
        },
        {
        "sealine": "MAEU009A",
        "scheduleDetails": [
            {
            "routeDetails": [
                {
                "fromLocation": {
                    "type": "TERMINAL",
                    "rkstCode": "ESBCNBS",
                    "unLocCode": "ESBCN",
                    "city": "Barcelona",
                    "countryCode": "ES",
                    "expectedDate": "2022-10-04T08:00:00"
                },
                "toLocation": {
                    "type": "TERMINAL",
                    "rkstCode": "SGSINPS",
                    "unLocCode": "SGSIN",
                    "city": "Singapore",
                    "countryCode": "SG",
                    "expectedDate": "2022-11-05T13:00:00"
                },
                "transport": {
                    "transportMode": "VESSEL",
                    "name": "MSC MINA",
                    "code": "9839260"
                }
                }
            ],
            "deadlines": [
                {
                "deadLineKey": "CY",
                "type": "Documentation",
                "deadLine": "2022-09-30T02:00:00",
                "name": "Commercial Cargo Cutoff"
                },
                {
                "deadLineKey": "SINONAMS",
                "type": "Documentation",
                "deadLine": "2022-09-29T08:00:00",
                "name": "Shipping Instructions Deadline"
                },
                {
                "deadLineKey": "VGM",
                "type": "Documentation",
                "deadLine": "2022-10-01T02:00:00",
                "name": "Commercial Verified Gross Mass Deadline"
                },
                {
                "deadLineKey": "LCD",
                "type": "Marine Services",
                "deadLine": "2022-09-29T08:00:00",
                "name": "Loadlist Closure Deadline"
                },
                {
                "deadLineKey": "CSPD",
                "type": "Marine Services",
                "deadLine": "2022-09-29T08:00:00",
                "name": "Coprar to Stowage Planners Deadline"
                },
                {
                "deadLineKey": "FLD",
                "type": "Marine Services",
                "deadLine": "2022-09-29T08:00:00",
                "name": "Final Loadlist Deadline"
                }
            ]
            },
            {
            "routeDetails": [
                {
                "fromLocation": {
                    "type": "TERMINAL",
                    "rkstCode": "SGSINPS",
                    "unLocCode": "SGSIN",
                    "city": "Singapore",
                    "countryCode": "SG",
                    "expectedDate": "2022-11-14T19:00:00"
                },
                "toLocation": {
                    "type": "TERMINAL",
                    "rkstCode": "HKHKGMO",
                    "unLocCode": "HKHKG",
                    "city": "Hong Kong",
                    "countryCode": "HK",
                    "expectedDate": "2022-11-18T08:00:00"
                },
                "transport": {
                    "transportMode": "VESSEL",
                    "name": "ATACAMA",
                    "code": "9718947"
                }
                }
            ],
            "deadlines": [
                {
                "deadLineKey": "CY",
                "type": "Documentation",
                "deadLine": "2022-11-11T21:00:00",
                "name": "Commercial Cargo Cutoff"
                },
                {
                "deadLineKey": "SINONAMS",
                "type": "Documentation",
                "deadLine": "2022-11-10T15:00:00",
                "name": "Shipping Instructions Deadline"
                },
                {
                "deadLineKey": "VGM",
                "type": "Documentation",
                "deadLine": "2022-11-12T03:00:00",
                "name": "Commercial Verified Gross Mass Deadline"
                },
                {
                "deadLineKey": "LCD",
                "type": "Marine Services",
                "deadLine": "2022-11-11T04:00:00",
                "name": "Loadlist Closure Deadline"
                },
                {
                "deadLineKey": "CSPD",
                "type": "Marine Services",
                "deadLine": "2022-11-10T23:00:00",
                "name": "Coprar to Stowage Planners Deadline"
                },
                {
                "deadLineKey": "FLD",
                "type": "Marine Services",
                "deadLine": "2022-11-11T15:00:00",
                "name": "Final Loadlist Deadline"
                },
                {
                "deadLineKey": "SCDD",
                "type": "Marine Services",
                "deadLine": "2022-11-10T21:00:00",
                "name": "Special Cargo Documentation Deadline"
                }
            ]
            }
        ],
        "conditions": [
            {
            "chargeType": "Demurrage",
            "containerSizeType": "20DRY",
            "freeTimeStartEvent": "DISCHARGE",
            "freeTimeGrantInDays": 5,
            "commodity": "GENERAL CARGO",
            "price": {
                "value": 50000,
                "currency": "HKD"
            }
            },
            {
            "chargeType": "Detention",
            "containerSizeType": "20DRY",
            "freeTimeStartEvent": "DISCHARGE",
            "freeTimeGrantInDays": 7,
            "commodity": "GENERAL CARGO",
            "price": {
                "value": 25000,
                "currency": "HKD"
            }
            }
        ],
        "penalties": [
            {
            "containerSizeType": "20DRY",
            "charges": [
                {
                "penaltyType": "AmmendmentFee",
                "price": {
                    "value": 1800,
                    "currency": "USD"
                },
                "name": "Amendment Fee"
                },
                {
                "penaltyType": "AmmendmentFee",
                "price": {
                    "value": 2500,
                    "currency": "USD"
                },
                "name": "Cancellation Fee"
                },
                {
                "penaltyType": "AmmendmentFee",
                "price": {
                    "value": 5000,
                    "currency": "USD"
                },
                "name": "No Show Fee"
                },
                {
                "penaltyType": "AmmendmentFee",
                "price": {
                    "value": -2500,
                    "currency": "USD"
                },
                "name": "Compensation Fee"
                }
            ]
            }
        ],
        "surchages": {
            "surchargesPerFreight": [
            {
                "quantity": 1,
                "basis": "PER_CONTAINER",
                "type": "Freight",
                "chargeCode": "FRT",
                "description": "Basic Ocean Freight",
                "value": 42000,
                "currency": "USD",
                "containerSizeType": "DRY20"
            },
            {
                "quantity": 1,
                "basis": "PER_CONTAINER",
                "type": "Freight",
                "chargeCode": "EFF",
                "description": "Environmental Fuel Fee",
                "value": 15200,
                "currency": "USD",
                "containerSizeType": "DRY20"
            },
            {
                "quantity": 1,
                "basis": "PER_CONTAINER",
                "type": "Freight",
                "chargeCode": "asdad",
                "description": "asda",
                "value": 10000,
                "currency": "USD",
                "containerSizeType": "DRY20"
            }
            ],
            "surchargesAtOrigin": [
            {
                "quantity": 1,
                "basis": "PER_DOC",
                "type": "Origin",
                "chargeCode": "ODF",
                "description": "Documentation Fee Origin",
                "value": 5000,
                "currency": "EUR",
                "containerSizeType": null
            },
            {
                "quantity": 1,
                "basis": "PER_CONTAINER",
                "type": "Origin",
                "chargeCode": "PAE",
                "description": "Port Additionals / Port Dues Export",
                "value": 3500,
                "currency": "EUR",
                "containerSizeType": "DRY20"
            },
            {
                "quantity": 1,
                "basis": "PER_CONTAINER",
                "type": "Origin",
                "chargeCode": "MHE",
                "description": "Merchant Haulage Export",
                "value": 3500,
                "currency": "EUR",
                "containerSizeType": "DRY20"
            },
            {
                "quantity": 1,
                "basis": "PER_CONTAINER",
                "type": "Origin",
                "chargeCode": "VGM",
                "description": "Verified Gross Mass Charge",
                "value": 1800,
                "currency": "EUR",
                "containerSizeType": "DRY20"
            }
            ],
            "surchargesAtDestination": [
            {
                "quantity": 1,
                "basis": "PER_CONTAINER",
                "type": "Destination",
                "chargeCode": "DHC",
                "description": "Terminal Handling Service - Destination",
                "value": 220000,
                "currency": "HKD",
                "containerSizeType": "DRY20"
            },
            {
                "quantity": 1,
                "basis": "PER_DOC",
                "type": "Destination",
                "chargeCode": "DDF",
                "description": "Documentation fee - Destination",
                "value": 55000,
                "currency": "HKD",
                "containerSizeType": null
            }
            ]
        },
        "id": "2727a2d6-ca16-4c03-9c9d-ebedcc06dc90",
        "agency": "Maerks",
        "service": "Maersk Spot",
        "pickUpDate": "2022-10-04T00:00:00",
        "deliveryDate": "2022-11-18T08:00:00",
        "transitDays": 46,
        "expirationDate": "2022-09-22T06:39:47.7739461",
        "extraInfo": null
        },
        {
        "sealine": "MAEU009A",
        "scheduleDetails": [
            {
            "routeDetails": [
                {
                "fromLocation": {
                    "type": "TERMINAL",
                    "rkstCode": "ESBCNBS",
                    "unLocCode": "ESBCN",
                    "city": "Barcelona",
                    "countryCode": "ES",
                    "expectedDate": "2022-09-29T03:00:00"
                },
                "toLocation": {
                    "type": "TERMINAL",
                    "rkstCode": "SGSINPS",
                    "unLocCode": "SGSIN",
                    "city": "Singapore",
                    "countryCode": "SG",
                    "expectedDate": "2022-10-29T06:00:00"
                },
                "transport": {
                    "transportMode": "VESSEL",
                    "name": "MSC SAMAR",
                    "code": "9839442"
                }
                }
            ],
            "deadlines": [
                {
                "deadLineKey": "CY",
                "type": "Documentation",
                "deadLine": "2022-09-23T11:00:00",
                "name": "Commercial Cargo Cutoff"
                },
                {
                "deadLineKey": "SINONAMS",
                "type": "Documentation",
                "deadLine": "2022-09-23T11:00:00",
                "name": "Shipping Instructions Deadline"
                },
                {
                "deadLineKey": "VGM",
                "type": "Documentation",
                "deadLine": "2022-09-23T11:00:00",
                "name": "Commercial Verified Gross Mass Deadline"
                },
                {
                "deadLineKey": "LCD",
                "type": "Marine Services",
                "deadLine": "2022-09-22T12:00:00",
                "name": "Loadlist Closure Deadline"
                },
                {
                "deadLineKey": "CSPD",
                "type": "Marine Services",
                "deadLine": "2022-09-22T15:00:00",
                "name": "Coprar to Stowage Planners Deadline"
                },
                {
                "deadLineKey": "FLD",
                "type": "Marine Services",
                "deadLine": "2022-09-22T15:00:00",
                "name": "Final Loadlist Deadline"
                }
            ]
            },
            {
            "routeDetails": [
                {
                "fromLocation": {
                    "type": "TERMINAL",
                    "rkstCode": "SGSINPS",
                    "unLocCode": "SGSIN",
                    "city": "Singapore",
                    "countryCode": "SG",
                    "expectedDate": "2022-11-07T19:00:00"
                },
                "toLocation": {
                    "type": "TERMINAL",
                    "rkstCode": "HKHKGMO",
                    "unLocCode": "HKHKG",
                    "city": "Hong Kong",
                    "countryCode": "HK",
                    "expectedDate": "2022-11-11T08:00:00"
                },
                "transport": {
                    "transportMode": "VESSEL",
                    "name": "MAERSK LANCO",
                    "code": "9527049"
                }
                }
            ],
            "deadlines": [
                {
                "deadLineKey": "CY",
                "type": "Documentation",
                "deadLine": "2022-11-04T21:00:00",
                "name": "Commercial Cargo Cutoff"
                },
                {
                "deadLineKey": "SINONAMS",
                "type": "Documentation",
                "deadLine": "2022-11-03T15:00:00",
                "name": "Shipping Instructions Deadline"
                },
                {
                "deadLineKey": "VGM",
                "type": "Documentation",
                "deadLine": "2022-11-05T03:00:00",
                "name": "Commercial Verified Gross Mass Deadline"
                },
                {
                "deadLineKey": "LCD",
                "type": "Marine Services",
                "deadLine": "2022-11-04T04:00:00",
                "name": "Loadlist Closure Deadline"
                },
                {
                "deadLineKey": "CSPD",
                "type": "Marine Services",
                "deadLine": "2022-11-03T23:00:00",
                "name": "Coprar to Stowage Planners Deadline"
                },
                {
                "deadLineKey": "FLD",
                "type": "Marine Services",
                "deadLine": "2022-11-04T15:00:00",
                "name": "Final Loadlist Deadline"
                },
                {
                "deadLineKey": "SCDD",
                "type": "Marine Services",
                "deadLine": "2022-11-03T21:00:00",
                "name": "Special Cargo Documentation Deadline"
                }
            ]
            }
        ],
        "conditions": [
            {
            "chargeType": "Demurrage",
            "containerSizeType": "20DRY",
            "freeTimeStartEvent": "DISCHARGE",
            "freeTimeGrantInDays": 5,
            "commodity": "GENERAL CARGO",
            "price": {
                "value": 50000,
                "currency": "HKD"
            }
            },
            {
            "chargeType": "Detention",
            "containerSizeType": "20DRY",
            "freeTimeStartEvent": "DISCHARGE",
            "freeTimeGrantInDays": 7,
            "commodity": "GENERAL CARGO",
            "price": {
                "value": 25000,
                "currency": "HKD"
            }
            }
        ],
        "penalties": [
            {
            "containerSizeType": "20DRY",
            "charges": [
                {
                "penaltyType": "AmmendmentFee",
                "price": {
                    "value": 1800,
                    "currency": "USD"
                },
                "name": "Amendment Fee"
                },
                {
                "penaltyType": "AmmendmentFee",
                "price": {
                    "value": 2500,
                    "currency": "USD"
                },
                "name": "Cancellation Fee"
                },
                {
                "penaltyType": "AmmendmentFee",
                "price": {
                    "value": 5000,
                    "currency": "USD"
                },
                "name": "No Show Fee"
                },
                {
                "penaltyType": "AmmendmentFee",
                "price": {
                    "value": -2500,
                    "currency": "USD"
                },
                "name": "Compensation Fee"
                }
            ]
            }
        ],
        "surchages": {
            "surchargesPerFreight": [
            {
                "quantity": 1,
                "basis": "PER_CONTAINER",
                "type": "Freight",
                "chargeCode": "FRT",
                "description": "Basic Ocean Freight",
                "value": 42000,
                "currency": "USD",
                "containerSizeType": "DRY20"
            },
            {
                "quantity": 1,
                "basis": "PER_CONTAINER",
                "type": "Freight",
                "chargeCode": "EFF",
                "description": "Environmental Fuel Fee",
                "value": 20300,
                "currency": "USD",
                "containerSizeType": "DRY20"
            },
            {
                "quantity": 1,
                "basis": "PER_CONTAINER",
                "type": "Freight",
                "chargeCode": "asdad",
                "description": "asda",
                "value": 10000,
                "currency": "USD",
                "containerSizeType": "DRY20"
            }
            ],
            "surchargesAtOrigin": [
            {
                "quantity": 1,
                "basis": "PER_DOC",
                "type": "Origin",
                "chargeCode": "ODF",
                "description": "Documentation Fee Origin",
                "value": 5000,
                "currency": "EUR",
                "containerSizeType": null
            },
            {
                "quantity": 1,
                "basis": "PER_CONTAINER",
                "type": "Origin",
                "chargeCode": "PAE",
                "description": "Port Additionals / Port Dues Export",
                "value": 3500,
                "currency": "EUR",
                "containerSizeType": "DRY20"
            },
            {
                "quantity": 1,
                "basis": "PER_CONTAINER",
                "type": "Origin",
                "chargeCode": "MHE",
                "description": "Merchant Haulage Export",
                "value": 3500,
                "currency": "EUR",
                "containerSizeType": "DRY20"
            },
            {
                "quantity": 1,
                "basis": "PER_CONTAINER",
                "type": "Origin",
                "chargeCode": "VGM",
                "description": "Verified Gross Mass Charge",
                "value": 1800,
                "currency": "EUR",
                "containerSizeType": "DRY20"
            }
            ],
            "surchargesAtDestination": [
            {
                "quantity": 1,
                "basis": "PER_CONTAINER",
                "type": "Destination",
                "chargeCode": "DHC",
                "description": "Terminal Handling Service - Destination",
                "value": 220000,
                "currency": "HKD",
                "containerSizeType": "DRY20"
            },
            {
                "quantity": 1,
                "basis": "PER_DOC",
                "type": "Destination",
                "chargeCode": "DDF",
                "description": "Documentation fee - Destination",
                "value": 55000,
                "currency": "HKD",
                "containerSizeType": null
            }
            ]
        },
        "id": "4d3b814d-cf82-4570-8c30-67dcb00f94af",
        "agency": "Maerks",
        "service": "Maersk Spot",
        "pickUpDate": "2022-09-29T00:00:00",
        "deliveryDate": "2022-11-11T08:00:00",
        "transitDays": 44,
        "expirationDate": "2022-09-22T06:39:47.5290864",
        "extraInfo": null
        }
    ]
    }
   
* FCL Quote model:

=============     ===============    ======================================================
 Name               Type             Description
=============     ===============    ======================================================
 QuoteId           Guid              Id of the quote
 Origin            Location          Object containing the origin info.
 Destination       Location          Object containing the destination info.
 PickUpDate        DateTime          Pickup date selected by client
 Rates             List<FCLRate>?    List containing the rates
=============     ===============    ======================================================

* Location model:
  
=============     ========    =======================================
 Name              Type       Description
=============     ========    =======================================
 PostalCode        String     PostalCode of the shipment
 Country           String     Country of the shipment
 City              String     City of the shipment
 State             String?    State of the shipment
 Street            String?    Street of the shipment
 Coords            Coord?     Geolocation data
=============     ========    =======================================

* Coord model:

=============     ========     ======================================================
Name              Type         Description
=============     ========     ======================================================
Lat               Double       Location latitude, precision is (3, 6).
Lng               Double       Location longitude, precision is (3, 6).
=============     ========     ======================================================

* FCL Rate model:
  
===================    ========================    ==========================================================
 Name                    Type                        Description
===================    ========================    ==========================================================
 Id                     Guid                        Rate ID
 Sealine 		        String		                Scas code
 Agency                 Double                      Agency
 Service                Double                      Service
 PickUpDate             DateTime?                   Pickup date (estimated)
 DeliveryDate           DateTime?                  Delivery date. Null if rate is a pre-booking.
 TransitDays            Integer?                    Transit days. Null or -1 if rate is a pre-booking.
 ExpirationDate         DateTime                    Expiration date
 Price                  Long                        Price (Considering 2 last digits as decimals).      
 ExtraInfo              List<String>                List of extra info
 ScheduleDetails        List<ScheduleDetails>	    List of schedule details
 Conditions	    	    List<Conditions>		    List of conditions
 Penalties	    	    List<Penalties>		        List of penalties
 Surchages	    	    List<Surchages>		        List of surchages     
===================    ========================    ==========================================================

* ScheduleDetails model:
  
===================    ========================    ==========================================================
 Name                    Type                        Description
===================    ========================    ==========================================================
 RouteDetails           List<RouteDetails>          Quantity
 Deadlines 		    	List<Deadlines>	            Rate deadlines   
===================    ========================    ==========================================================

* RouteDetails model:
  
===================    ========================    ==========================================================
 Name                    Type                        Description
===================    ========================    ==========================================================
 FromLocation           MaritimeLocation		     From Location
 ToLocation 	        MaritimeLocation 		     To Location
 Transport              Transport		             Transport
===================    ========================    ==========================================================

* MaritimeLocation model:

=====================    ========================    ==========================================================
 Name                     Type                        Description
=====================    ========================    ==========================================================
 RkstCode                 String?                     Rkst Code
 Type                     MaritimeLocationType		  Transport Type route
 UnLocCode                String                      UnLoc Code
 City                     String?                     City     
 CountryCode              String?                     Country Code
 ExpectedDate             String                      Expected Date
=====================    ========================    ==========================================================

* Transport model:
  
===================    ========================    ==========================================================
 Name                    Type                        Description
===================    ========================    ==========================================================
 Name                   String                      Name
 Code 		            String		                Code
 TransportMode          String	                    Transport Mode     
===================    ========================    ==========================================================

* Maritime location type model:
  
================     =======================================  
Name                  Description
================     =======================================  
VESSEL         		  Maritime location
TRUCK      			  Ground location
================     =======================================  

* Deadlines model:
  
===================    ========================    ==========================================================
 Name                    Type                        Description
===================    ========================    ==========================================================
 DeadLineKey            String                      DeadLine Key
 Type 		            String		                Type
 DeadLine               String                      DeadLine
 Name                   String                      Name
===================    ========================    ==========================================================

* Conditions model:

=======================    ========================    ==========================================================
 Name                       Type                        Description
=======================    ========================    ==========================================================
 ChargeType                 ConditionChargeType         Charge type
 ContainerSizeType 		    String			            Container size type
 FreeTimeStartEvent         String                      Free time start event
 FreeTimeGrantInDays        Integer                     Free time grant in days
 Commodity			        String                      Commodity
 Price			            Long                        Price (Considering 2 last digits as decimals).
=======================    ========================    ==========================================================

* Condition charge type model:
  
================     =======================================  
Name                  Description
================     =======================================  
Demurrage         	 Demurrage condition type
Detention      		 Detention condition type
Storage              Demurrage condition type
================     =======================================  

* Penalties model:
  
=======================    ========================    ==========================================================
 Name                       Type                        Description
=======================    ========================    ==========================================================
 ContainerSizeType 		    String			            Container size type
 Currency		            String                      Currency
 Charges        		    List<Charges>               Charges
=======================    ========================    ==========================================================
 
* Charges model:
  
=======================    ========================    ==========================================================
 Name                       Type                        Description
=======================    ========================    ==========================================================
 PenaltyType 		        PenaltyType			        Penalty type
 Name		                String                      Name
 Price        		        Long			            Price (Considering 2 last digits as decimals).
=======================    ========================    ==========================================================

* Penalty type model:
  
================     =======================================  
Name                  Description
================     =======================================  
AmmendmentFee         Modification cost
CancellationFee       Cancelation booking
NoShowFee             No show cost
CompensationFee       Compensation cost
================     =======================================  

* Surchages model:
  
=========================    ===============================    ==========================================================
 Name                         Type                        	     Description
=========================    ===============================    ==========================================================
 SurchargePerFreight 	      List<SurchargesItem> 	     		 Surcharges per freight
 SurchargesAtOrigin           List<SurchargesItem>               Surcharges at origin
 SurchargesAtOrigin           List<SurchargesItem>               Surcharges at destination
=========================    ===============================    ==========================================================

* SurchargesItem model:
  
=========================    ===============================    ==========================================================
 Name                         Type                        	     Description
=========================    ===============================    ==========================================================
 Quantity 	  	 	  	      Integer		 	     	         Quantity
 Basis            		      String	                         Basis
 Type            		      SurchargeType	                     Type
 ChargeCode            	      String?	                         Maritime standard charge code
 ChargeDescription            String?	                         Charge description
 Value            		      Long   		                     Value (Considering 2 last digits as decimals).
=========================    ===============================    ==========================================================
    
* Surcharge type model:
  
=============     =======================================     
Name               Description
=============     =======================================  
Freight            Surcharges relatives on Freight
Origin             Surcharges generated at Origin
Destination        Surcharges generated at Destination
=============     =======================================  

LCL Sea Rating
-----------------------------

Request to retrieve the rates for LCL sea shipment(Maritime)

Returns a list containing the Sea rates for LCL.

**Example request**:

.. http:post:: /v1/rates/sea/lcl


.. tabs::

    .. code-tab:: bash

        $ curl -X POST \
            'https://<env>.freightol.com/v1/rates/sea/lcl' \
            -H "Content-Type: application/json" \
            -H "Authorization: Bearer <token>" \
            -d @body.json

The content of ``body.json`` is like,
        
.. sourcecode:: json

	{
		"currency": "EUR",
		"customs": false,
		"goodsDescription": "PRODUCTOS ORIGEN ANIMAL",
		"goodsValue": 10,
		"pickUpDate": "2021-11-09T00:00:00.000Z",
		"insurance": false,
		"cargos": [
			{
				"quantity": 2,
				"weight": 1000,
				"measurementUnit": "CmKg",
				"CBM": 10
			}
		],
		"originServiceType": "SD",
		"destinationServiceType": "CY",
		"origin": {
			"postalCode": "999077",
			"country": "HK",
			"city": "Hong Kong",
			"state": "Sai Kung",
			"street": null,
			"coords": null
		},
		"destination": {
			"postalCode": "08001",
			"country": "ES",
			"city": "Barcelona",
			"state": "Cataluña",
			"street": null,
			"coords": null
		},
		"originUnLocCode": "HKHKG",
		"originRkstCode": "HKHKG",
		"destinationUnLocCode": "ESBCN",
		"destinationRkstCode": "ESBCN"
	}

* LCL Quote model:

==========================   ===================   =============   ===============================================
Name                 	     Type                  Constraint      Description
==========================   ===================   =============   ===============================================
Origin               	         Location            Optional        Object containing the origin info.
Destination               	 Location            Optional        Object containing the destination info.
Cargos               	     	 List<Cargos>        Mandatory       List of containers for the shipment.
PickUpDate               	 DateTime            Mandatory       Pickup date
GoodsDescription             	 String              Optional        Goods description
GoodsValue               	 Long                Optional        Goods value(last 2 digits are decimals)
Insurance               	 Boolean             Optional        Has insurance
Customs               	    	 Boolean             Optional        Has customs
Currency               	    	 String              Optional        Currency(Ex:EUR)
OriginServiceType           	 ServiceType         Mandatory       Origin service type
DestinationServiceType      	 ServiceType	     Mandatory       Destination service type
OriginUnLocCode       	    	 String              Mandatory       Origin UnLoc code
DestinationUnLocCode        	 String              Mandatory       Destination UnLoc code   
OriginRkstCode       	    	 String              Optional        Origin Rkst code
DestinationRkstCode       	 String              Optional        Destination Rkst code
==========================   ===================   =============   ===============================================
  
* Service type model:
  
=============     =======================================
Name			  Description
=============     =======================================
CY                Container Yard
SD                Store Door
=============     =======================================

* Location model:
  
=============     ========    =============      =======================================
Name              Type        Constraint         Description
=============     ========    =============      =======================================
PostalCode        String      Mandatory 	      PostalCode of the shipment
Country           String      Mandatory 	      Country of the shipment
City              String      Mandatory 	      City of the shipment
State             String      Mandatory 	      State of the shipment
Street            String      Optional 	          Street of the shipment
Coords            Coord       Optional 	          Geolocation data
=============     ========    =============      =======================================

* Coord model:
  
=============     ========     =============    ======================================================
Name              Type         Constraint       Description
=============     ========     =============    ======================================================
Lat               Double       Mandatory        Location latitude, precision is (3, 6).
Lng               Double       Mandatory 	    Location longitude, precision is (3, 6).
=============     ========     =============    ======================================================

* Cargo model:
  
======================    =========    =============     =======================================
Name                      Type         Constraint        Description
======================    =========    =============     =======================================
Quantity                  Int          Mandatory 	      Quantity
Weight                    Double       Mandatory  	      Weight of the cargo
MeasurementUnit           String       Mandatory 	      Measurement unit: CmKg
CBM                       Double       Mandatory 	      CBM of the cargo
======================    =========    =============     =======================================    

**Example response**:
   
   
   .. sourcecode:: json

      {
	    "quoteId": "cedb8248-ee94-4bfd-ae68-60d05073d460",
	    "origin": {
			"postalCode": "999077",
			"country": "HK",
			"city": "Hong Kong",
			"state": "Sai Kung",
			"street": null,
			"coords": {
				"lat": null,
				"lng": null
			}
	    },
	    "destination": {
			"postalCode": "08001",
			"country": "ES",
			"city": "Barcelona",
			"state": "Cataluña",
			"street": null,
			"coords": {
				"lat": null,
				"lng": null
			}
	    },
	    "pickUpDate": "2021-11-09T00:00:00",
	    "rates": [
			{
				"sealine": "MAEU",
				"scheduleDetails": [
				{
					"routeDetails": [
					{
						"fromLocation": {
							"type": "TERMINAL",
							"rkstCode": "HKHKGMO",
							"unLocCode": "HKHKG",
							"city": "Hong Kong",
							"countryCode": "HK",
							"expectedDate": "2021-11-10T12:00:00"
						},
						"toLocation": {
							"type": "TERMINAL",
							"rkstCode": "CNNANCT",
							"unLocCode": "CNNSA",
							"city": "Nansha New Port",
							"countryCode": "CN",
							"expectedDate": "2021-11-10T20:00:00"
						},
						"transport": {
							"transportMode": "VESSEL",
							"name": "SAN CHRISTOBAL",
							"code": "9699191"
						}
					},
					{
						"fromLocation": {
							"type": "TERMINAL",
							"rkstCode": "CNNANCT",
							"unLocCode": "CNNSA",
							"city": "Nansha New Port",
							"countryCode": "CN",
							"expectedDate": "2021-11-16T11:00:00"
						},
						"toLocation": {
							"type": "TERMINAL",
							"rkstCode": "ESBCNBS",
							"unLocCode": "ESBCN",
							"city": "Barcelona",
							"countryCode": "ES",
							"expectedDate": "2021-12-18T20:00:00"
						},
						"transport": {
							"transportMode": "VESSEL",
							"name": "MSC ARINA",
							"code": "9839284"
						}
					}
					],
					"deadlines": [
					{
						"deadLineKey": "CY",
						"type": "Documentation",
						"deadLine": "2021-11-08 17:00:00",
						"name": "Commercial Cargo Cutoff"
					},
					{
						"deadLineKey": "SIAMS",
						"type": "Documentation",
						"deadLine": "2021-11-06 16:00:00",
						"name": "Shipping Instructions Deadline for Advance Manifest Cargo"
					},
					{
						"deadLineKey": "VGM",
						"type": "Documentation",
						"deadLine": "2021-11-08 11:00:00",
						"name": "Commercial Verified Gross Mass Deadline"
					},
					{
						"deadLineKey": "LCD",
						"type": "Marine Services",
						"deadLine": "2021-11-08 11:00:00",
						"name": "Loadlist Closure Deadline"
					},
					{
						"deadLineKey": "CSPD",
						"type": "Marine Services",
						"deadLine": "2021-11-08 12:00:00",
						"name": "Coprar to Stowage Planners Deadline"
					},
					{
						"deadLineKey": "FLD",
						"type": "Marine Services",
						"deadLine": "2021-11-08 17:00:00",
						"name": "Final Loadlist Deadline"
					},
					{
						"deadLineKey": "SCDD",
						"type": "Marine Services",
						"deadLine": "2021-11-08 11:00:00",
						"name": "Special Cargo Documentation Deadline"
					}
					]
				},
				{
					"routeDetails": [
					{
						"fromLocation": {
							"type": "TERMINAL",
							"rkstCode": "HKHKGMO",
							"unLocCode": "HKHKG",
							"city": "Hong Kong",
							"countryCode": "HK",
							"expectedDate": "2021-11-10T12:00:00"
						},
						"toLocation": {
							"type": "TERMINAL",
							"rkstCode": "CNNANCT",
							"unLocCode": "CNNSA",
							"city": "Nansha New Port",
							"countryCode": "CN",
							"expectedDate": "2021-11-10T20:00:00"
						},
						"transport": {
							"transportMode": "VESSEL",
							"name": "SAN CHRISTOBAL",
							"code": "9699191"
						}
					},
					{
						"fromLocation": {
							"type": "TERMINAL",
							"rkstCode": "CNNANCT",
							"unLocCode": "CNNSA",
							"city": "Nansha New Port",
							"countryCode": "CN",
							"expectedDate": "2021-11-16T11:00:00"
						},
						"toLocation": {
							"type": "TERMINAL",
							"rkstCode": "ESBCNBS",
							"unLocCode": "ESBCN",
							"city": "Barcelona",
							"countryCode": "ES",
							"expectedDate": "2021-12-18T20:00:00"
						},
						"transport": {
							"transportMode": "VESSEL",
							"name": "MSC ARINA",
							"code": "9839284"
						}
					}
					],
					"deadlines": [
					{
						"deadLineKey": "CY",
						"type": "Documentation",
						"deadLine": "2021-11-16 12:00:00",
						"name": "Commercial Cargo Cutoff"
					},
					{
						"deadLineKey": "SIAMS",
						"type": "Documentation",
						"deadLine": "2021-11-13 22:00:00",
						"name": "Shipping Instructions Deadline for Advance Manifest Cargo"
					},
					{
						"deadLineKey": "VGM",
						"type": "Documentation",
						"deadLine": "2021-11-16 10:00:00",
						"name": "Commercial Verified Gross Mass Deadline"
					},
					{
						"deadLineKey": "LCD",
						"type": "Marine Services",
						"deadLine": "2021-11-15 16:00:00",
						"name": "Loadlist Closure Deadline"
					},
					{
						"deadLineKey": "CSPD",
						"type": "Marine Services",
						"deadLine": "2021-11-15 17:00:00",
						"name": "Coprar to Stowage Planners Deadline"
					},
					{
						"deadLineKey": "FLD",
						"type": "Marine Services",
						"deadLine": "2021-11-16 12:00:00",
						"name": "Final Loadlist Deadline"
					},
					{
						"deadLineKey": "SCDD",
						"type": "Marine Services",
						"deadLine": "2021-11-15 16:00:00",
						"name": "Special Cargo Documentation Deadline"
					}
					]
				}
				],
				"conditions": [
				{
					"chargeType": "Storage",
					"containerSizeType": "40DRY",
					"freeTimeStartEvent": "DISCHARGE",
					"freeTimeGrantInDays": 7,
					"commodity": "GENERAL CARGO",
					"price": 4308
				},
				{
					"chargeType": "Detention",
					"containerSizeType": "40DRY",
					"freeTimeStartEvent": "DISCHARGE",
					"freeTimeGrantInDays": 5,
					"commodity": "GENERAL CARGO",
					"price": 431
				}
				],
				"penalties": [
				{
					"containerSizeType": "40DRY",
					"currency": "EUR",
					"charges": [
					{
						"penaltyType": "AmmendmentFee",
						"price": 51692,
						"name": "Amendment Fee"
					},
					{
						"penaltyType": "CancellationFee",
						"price": 51692,
						"name": "Cancellation Fee"
					},
					{
						"penaltyType": "NoShowFee",
						"price": 103383,
						"name": "No Show Fee"
					}
					]
				}
				],
				"surchages": {
				"surchargePerDocs": [
					{
					"quantity": 1,
					"basis": "PER_DOC",
					"type": "Paid at Origin",
					"chargeCode": "ODF",
					"chargeDescription": "Documentation Fee Origin",
					"value": 6087
					},
					{
					"quantity": 1,
					"basis": "PER_DOC",
					"type": "Paid at Destination",
					"chargeCode": "DDF",
					"chargeDescription": "Documentation fee - Destination",
					"value": 4981
					}
				],
				"surchargesPerContainer": [
					{
					"containerSizeType": "40DRY",
					"surcharges": [
						{
						"quantity": 1,
						"basis": "PER_CONTAINER",
						"type": "Paid with Freight",
						"chargeCode": "PSS",
						"chargeDescription": "Peak Season Surcharge",
						"value": 172305
						},
						{
						"quantity": 1,
						"basis": "PER_CONTAINER",
						"type": "Paid with Freight",
						"chargeCode": "EFF",
						"chargeDescription": "Environmental Fuel Fee",
						"value": 19643
						},
						{
						"quantity": 1,
						"basis": "PER_CONTAINER",
						"type": "Paid at Destination",
						"chargeCode": "PAI",
						"chargeDescription": "Port Additionals / Port Dues Import",
						"value": 5479
						},
						{
						"quantity": 1,
						"basis": "PER_CONTAINER",
						"type": "Paid at Origin",
						"chargeCode": "OHC",
						"chargeDescription": "Terminal Handling Service - Origin",
						"value": 33199
						},
						{
						"quantity": 1,
						"basis": "PER_CONTAINER",
						"type": "Paid at Origin",
						"chargeCode": "EXP",
						"chargeDescription": "Export Service",
						"value": 664
						},
						{
						"quantity": 1,
						"basis": "PER_CONTAINER",
						"type": "Paid at Destination",
						"chargeCode": "DHC",
						"chargeDescription": "Terminal Handling Service - Destination",
						"value": 22914
						},
						{
						"quantity": 1,
						"basis": "PER_CONTAINER",
						"type": "Paid with Freight",
						"chargeCode": "BAS",
						"chargeDescription": "Basic Ocean Freight",
						"value": 1033830
						}
					]
					}
				]
				},
				"id": "a445119b-6fe4-4607-a976-7af8cdd71d5e",
				"agency": "Maerks",
				"service": "Maersk Spot",
				"pickUpDate": "2021-11-10T00:00:00",
				"deliveryDate": "2021-12-18T20:00:00",
				"transitDays": 39,
				"expirationDate": "2021-11-03T13:50:31.2957013",
				"price": 1299094,
				"extraInfo": null
			}
	    ]
	}
    
* LCL Quote model:


=============     ===============    ======================================================
 Name               Type             Description
=============     ===============    ======================================================
 QuoteId           Guid              Id of the quote
 Origin            Location          Object containing the origin info.
 Destination       Location          Object containing the destination info.
 PickUpDate        DateTime          Pickup date selected by client
 Rates             List<FCLRate>     List containing the rates
=============     ===============    ======================================================

* Location model:
  
=============     ========    =======================================
 Name              Type       Description
=============     ========    =======================================
 PostalCode        String     PostalCode of the shipment
 Country           String     Country of the shipment
 City              String     City of the shipment
 State             String     State of the shipment
 Street            String     Street of the shipment
 Coords            Coord      Geolocation data
=============     ========    =======================================

* Coord model:

=============     ========     ======================================================
Name              Type         Description
=============     ========     ======================================================
Lat               Double       Location latitude, precision is (3, 6).
Lng               Double       Location longitude, precision is (3, 6).
=============     ========     ======================================================

* LCL Rate model:
  
===================    ========================    ==========================================================
 Name                    Type                        Description
===================    ========================    ==========================================================
 Id                     Guid                        Rate ID
 Sealine 		        String		                Scas code
 Agency                 Double                      Agency
 Service                Double                      Service
 PickUpDate             DateTime?                   Pickup date (estimated)
 DeliveryDate           DateTuime?                  Delivery date. Null if rate is a pre-booking.
 TransitDays            Integer?                    Transit days. Null or -1 if rate is a pre-booking.
 ExpirationDate         DateTime                    Expiration date
 Price                  Long                        Price (Considering 2 last digits as decimals).      
 ExtraInfo              List<String>                List of extra info
 ScheduleDetails        List<ScheduleDetails>	    List of schedule details
 Conditions	    	    List<Conditions>		    List of conditions
 Penalties	    	    List<Penalties>		        List of penalties
 Surchages	    	    List<Surchages>		        List of surchages     
===================    ========================    ==========================================================

* ScheduleDetails model:
  
===================    ========================    ==========================================================
 Name                    Type                        Description
===================    ========================    ==========================================================
 RouteDetails           List<RouteDetails>          Quantity
 Deadlines 		    	List<Deadlines>	            Rate deadlines   
===================    ========================    ==========================================================

* RouteDetails model:
  
===================    ========================    ==========================================================
 Name                    Type                        Description
===================    ========================    ==========================================================
 FromLocation           MaritimeLocation		     From Location
 ToLocation 	        MaritimeLocation 		     To Location
 Transport              Transport		             Transport
===================    ========================    ==========================================================

* MaritimeLocation model:

=====================    ========================    ==========================================================
 Name                     Type                        Description
=====================    ========================    ==========================================================
 RkstCode                 String?                     Rkst Code
 Type                     MaritimeLocationType		  Transport Type route
 UnLocCode                String                      UnLoc Code
 City                     String                      City     
 CountryCode              String                      Country Code
 ExpectedDate             String                      Expected Date
=====================    ========================    ==========================================================

* Transport model:
  
===================    ========================    ==========================================================
 Name                    Type                        Description
===================    ========================    ==========================================================
 Name                   String                      Name
 Code 		            String		                Code
 TransportMode          String	                    Transport Mode     
===================    ========================    ==========================================================

* Maritime location type model:
  
================     =======================================  
Name                  Description
================     =======================================  
VESSEL         		  Maritime location
TRUCK      			  Ground location
================     =======================================  

* Deadlines model:
  
===================    ========================    ==========================================================
 Name                    Type                        Description
===================    ========================    ==========================================================
 DeadLineKey            String                      DeadLine Key
 Type 		            String		                Type
 DeadLine               String                      DeadLine
 Name                   String                      Name
===================    ========================    ==========================================================

* Conditions model:

=======================    ========================    ==========================================================
 Name                       Type                        Description
=======================    ========================    ==========================================================
 ChargeType                 ConditionChargeType         Charge type
 ContainerSizeType 		    String			            Container size type
 FreeTimeStartEvent         String                      Free time start event
 FreeTimeGrantInDays        Integer                     Free time grant in days
 Commodity			        String                      Commodity
 Price			            Long                        Price (Considering 2 last digits as decimals).
=======================    ========================    ==========================================================

* Condition charge type model:
  
================     =======================================  
Name                  Description
================     =======================================  
Demurrage         	 Demurrage condition type
Detention      		 Detention condition type
Storage              Demurrage condition type
================     =======================================  

* Penalties model:
  
=======================    ========================    ==========================================================
 Name                       Type                        Description
=======================    ========================    ==========================================================
 ContainerSizeType 		    String			            Container size type
 Currency		            String                      Currency
 Charges        		    List<Charges>               Charges
=======================    ========================    ==========================================================
 
* Charges model:
  
=======================    ========================    ==========================================================
 Name                       Type                        Description
=======================    ========================    ==========================================================
 PenaltyType 		        PenaltyType			        Penalty type
 Name		                String                      Name
 Price        		        Long			            Price (Considering 2 last digits as decimals).
=======================    ========================    ==========================================================

* Penalty type model:
  
================     =======================================  
Name                  Description
================     =======================================  
AmmendmentFee         Modification cost
CancellationFee       Cancelation booking
NoShowFee             No show cost
CompensationFee       Compensation cost
================     =======================================  

* Surchages model:
  
=========================    ===============================    ==========================================================
 Name                         Type                        	     Description
=========================    ===============================    ==========================================================
 SurchargePerFreight 	      List<SurchargesItem> 	     		 Surcharges per Freight
 SurchargesAtOrigin           List<SurchargesItem>               Surcharges at Origin
 SurchargesAtOrigin           List<SurchargesItem>               Surcharges at Destination
=========================    ===============================    ==========================================================

* SurchargesItem model:
  
=========================    ===============================    ==========================================================
 Name                         Type                        	     Description
=========================    ===============================    ==========================================================
 Quantity 	  	 	  	      Integer		 	     	         Quantity
 Basis            		      String	                         Basis
 Type            		      SurchargeType	                     Type
 ChargeCode            	      String?	                         Maritime standard charge code
 ChargeDescription            String?	                         Charge description
 Value            		      Long   		                     Value (Considering 2 last digits as decimals).
=========================    ===============================    ==========================================================
    
* Surcharge type model:
  
=============     =======================================     
Name               Description
=============     =======================================  
Freight            Surcharges relatives on Freight
Origin             Surcharges generated at Origin
Destination        Surcharges generated at Destination
=============     =======================================  


.. autosummary::
   :toctree:
