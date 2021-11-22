===================
Rating
===================


Box Rating
----------------

**Example request**:
    
.. http:post:: /v1/rating/boxes


.. tabs::

    .. code-tab:: bash

        $ curl \
            -X POST \
            -H "Content-Type: application/json" \
            -H "Authorization: Bearer <token>" \
            -d @body.json \
            https://<env>.freightol.com/v1/rating/boxes

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
			"coords": null
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
PickUpDate           DateTime              Mandatory       Pickup date
GoodsDescription     String                Mandatory       Goods description
GoodsValue           Long                  Mandatory       Goods value (last 2 digits are decimals)
Insurance            Boolean               Mandatory       True if insurance is requested
Customs              Boolean               Mandatory       True if customs is requered
Currency             String                Mandatory       Currency(Ex:EUR)
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
Quantity              Int          Mandatory 	  	 Quantity
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


* Box quote model:

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
  
=============     ========    =============      =======================================
Name              Type        Constraint          Description
=============     ========    =============      =======================================
PostalCode        String      Mandatory 	      Zip code of the shipment
Country           String      Mandatory 	      Country ISO2 of the shipment
City              String      Mandatory 	      City of the shipment
State             String      Mandatory 	      State of the shipment
Street            String      Optional 	     	  Street of the shipment
Coords            Coord       Optional 	      	  Geolocation data
=============     ========    =============      =======================================

* Box Rate model:
  
===================    ====================    ==========================================================
	Name                    Type                    Description
===================    ====================    ==========================================================
Id                     Integer                 Guid of rate
Agency                 Double                  Agency
Service                String                  Service
PickUpDate             DateTime                Pickup date
DeliveryDate           DateTime                Delivery date
TransitDays            Integer                 Transit days
ExpirationDate         DateTime                Expiration date
Price                  Long                    Price  (Considering 2 last digits as decimals).      
ExtraInfo              List<String>            List of extra info
===================    ====================    ==========================================================

     
    
Pallet Rating
----------------

**Example request**:
    
.. http:post:: /v1/rating/pallets


.. tabs::

    .. code-tab:: bash

        $ curl \
            -X POST \
            -H "Content-Type: application/json" \
            -H "Authorization: Bearer <token>" \
            -d @body.json \
            https://<env>.freightol.com/v1/rating/pallets

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
			"city": "Oviedo",
			"state": "AST",
			"street": null,
			"coords": null
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
				"palletType": 2
			}
		]
	}

* Pallets Rating model:
  
==================   ===================   =============   ===============================================
Name                 Type                  Constraint      Description
==================   ===================   =============   ===============================================
Origin               Location              Mandatory       Object containing the origin info.
Destination          Location              Mandatory       Object containing the destination info.
Boxes                List<Containers>      Mandatory       List of containers for the shipment.
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
coords            Coord       Optional 	          Geolocation data
=============     ========    =============      =======================================

* Coord model:

=============     ========     =============    ======================================================
Name              Type         Constraint       Description
=============     ========     =============    ======================================================
lat               Double       Mandatory        Location latitude, precision is (3, 6).
lng               Double       Mandatory 	    Location longitude, precision is (3, 6).
=============     ========     =============    ======================================================

* Container:
  
==================    =============      ==============     ==========================================================
Name                  Type               Constraint         Description
==================    =============      ==============     ==========================================================
Quantity              Integer            Mandatory 	 		Quantity of pallet (same type)
Length                Double             Mandatory 	 		Length of the pallet
Width                 Double             Mandatory 	 		Width of the pallet
Height                Double             Mandatory	        Height of the pallet
Weight                Double             Mandatory  	 	Weight of the pallet
MeasurementUnit       String             Mandatory 	 		Measurement unit
IsStackable	          Boolean            Mandatory          True if pallet is stackable
PalletType            Integer            Mandatory		 	Pallet Type(0-Other,1-Euro1,2-Euro2,3-UK)
==================    =============      ==============     ==========================================================


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
QuoteId           Guid             			Id of the quote
Origin            Location         			Object containing the origin info.
Destination       Location         			Object containing the destination info.
PickUpDate        DateTime         	  		Pickup date
Rates             List<PalletRate>       	List containing the rates
=============     ===================    ======================================================

* Location model:

=============     ========    =============      =======================================
Name              Type        Constraint          Description
=============     ========    =============      =======================================
PostalCode        String      Mandatory 	      PostalCode of the shipment
Country           String      Mandatory 	      Country of the shipment
City              String      Mandatory 	      City of the shipment
State             String      Mandatory 	      State of the shipment
Street            String      Optional 	      	  Street of the shipment
Coords            Coord       Optional 	      	  Geolocation data
=============     ========    =============      =======================================

* Coord model:

=============     ========     =============    ======================================================
Name              Type         Constraint       Description
=============     ========     =============    ======================================================
Lat               Double       Mandatory        Location latitude, precision is (3, 6).
Lng               Double       Mandatory 	    Location longitude, precision is (3, 6).
=============     ========     =============    ======================================================

* Pallet Rate model:

===================    ====================    ==========================================================
Name                    Type                    Description
===================    ====================    ==========================================================
Id                     Int                     Quantity
Agency                 Double                  Agency
Service                Double                  Service
PickUpDate             Double                  Pickup date
DeliveryDate           Double                  Delivery date
TransitDays            String                  Transit days
ExpirationDate         DateTime                Expiration date
Price                  Long                    Price (Considering 2 last digits as decimals).      
ExtraInfo              List<String>            List of extra info
===================    ====================    ==========================================================
    
.. include:: sea/index.rst


Air Rating
-----------------------


**Example request**:
    
.. http:post:: /v1/rating/air


.. tabs::

    .. code-tab:: bash

        $ curl \
            -X POST \
            -H "Content-Type: application/json" \
            -H "Authorization: Bearer <token>" \
            -d @body.json \
            https://<env>.freightol.com/v1/rating/air

The content of ``body.json`` is like,
        
.. sourcecode:: json

	{
		"arrivalAirportCode": "BCN",
		"departureAirportCode": "HKG",
		"origin": {
			"postalCode": "24008",
			"country": "ES",
			"city": "Barcelona",
			"state": "CAT",
			"street": null,
			"coords": null
		},
		"destination": {
			"postalCode": "33001",
			"country": "CN",
			"city": "Hong Kong",
			"state": "HK",
			"street": null,
			"coords": null
		},
		"pickUpDate": "2021-11-18T16:54:30.094Z",
		"goodsDescription": "string",
		"goodsValue": 100,
		"insurance": true,
		"customs": true,
		"currency": "EUR",
		"cargos": [
			{
				"quantity": 10,
				"length": 10,
				"width": 30,
				"height": 20,
				"weight": 40,
				"measurementUnit": "CmKg",
				"isStackable": true,
				"isTiltable": true,
				"isTopLoadable": true,
				"chargeableWeight": 20,
				"weightType": "TOTAL"
			}
		]
	}

* Air Quote model:

==========================   ===================   =============   ===============================================
Name                 	  	 Type                  Constraint      Description
==========================   ===================   =============   ===============================================
Origin               	  	 Location              Mandatory       Object containing the origin info.
Destination               	 Location              Mandatory       Object containing the destination info.
Cargos               	 	 List<Cargos>      	   Mandatory       List of containers for the shipment.
PickUpDate               	 DateTime              Mandatory       Pickup date
GoodsDescription             String                Mandatory       Goods description
GoodsValue               	 Long                  Mandatory       Goods value(last 2 digits are decimals)
Insurance               	 Boolean               Mandatory       Has insurance
Customs               	  	 Boolean               Mandatory       Has customs
DangerousCargo               Boolean               Mandatory       True if dangerous cargo is sent
Arrival airport code		 String   	           Mandatory       Arrival airport ISO code
Destination airport code	 String				   Mandatory	   Destination airport ISO code
==========================   ===================   =============   ===============================================

* Location model:
  
=============     ========    =============      =======================================
Name              Type        Constraint       	 Description
=============     ========    =============      =======================================
PostalCode        String      Mandatory 	      PostalCode of the shipment
Country           String      Mandatory 	      Country of the shipment
City              String      Mandatory 	      City of the shipment
State             String      Mandatory 	      State of the shipment
Street            String      Optional 	      	  Street of the shipment
coords            Coord       Optional 	      	  Geolocation data
=============     ========    =============      =======================================

* Coord model:
  
=============     ========     =============    ======================================================
Name              Type         Constraint       Description
=============     ========     =============    ======================================================
Lat               Double       Mandatory        Airport latitude, precision is (3, 6).
Lng               Double       Mandatory 	     Airport longitude, precision is (3, 6).
=============     ========     =============    ======================================================

* Cargos model:
  
======================    =========    =============     =======================================
Name                      Type         Constraint        Description
======================    =========    =============     =======================================
Quantity                  Integer      Mandatory 	      Quantity
Length                    Double       Mandatory  	      Length of the cargo
Width                     Double       Mandatory  	      Width of the cargo
Weight                    Double       Mandatory  	      Weight of the cargo
Height                    Double       Mandatory  	      Height of the cargo
MeasurementUnit           String       Mandatory 	      Measurement unit
IsStackable               Boolean      Mandatory 	      Is stackable
IsTiltable                Boolean      Mandatory	      Is tiltable
IsTopLoadable             Boolean	   Mandatory	      Is top loadable
ChargeableWeight          Integer      Mandatory	      Chargeable weight
WeightType                String       Mandatory	      Weight type
======================    =========    =============     =======================================


**Example response**:
    
.. sourcecode:: json

	{
		"quoteId": "7f938132-10ac-40d2-9dc8-4e176fe8378d",
		"origin": {
			"postalCode": "24008",
			"country": "ES",
			"city": "Barcelona",
			"state": "CAT",
			"street": null,
			"coords": {
				"lat": null,
				"lng": null
			}
		},
		"destination": {
			"postalCode": "33001",
			"country": "CN",
			"city": "Hong Kong",
			"state": "HK",
			"street": null,
			"coords": {
				"lat": null,
				"lng": null
			}
		},
		"pickUpDate": "2021-11-18T15:54:30.094",
		"rates": [
			{
				"airlineCode": "GF",
				"airlineIATACode": 72,
				"arrivalAirportCode": "BKK",
				"departureAirportCode": "CDG",
				"netRate": 22,
				"allInRate": 22,
				"chargeableWeight": 1.000002,
				"freightPrice": 4500,
				"legs": [
					{
						"flightNumber": "GF016",
						"aircraftCode": "320",
						"departureTime": "2021-11-18T08:35:00",
						"arrivalTime": "2021-11-18T17:00:00",
						"arrivalAirportCode": "BAH",
						"departureAirportCode": "CDG",
						"bodyType": "UNKNOWN",
						"cO2": {
							"value": 0,
							"isEstimation": false
						}
					},
					{
						"flightNumber": "GF165",
						"aircraftCode": "789",
						"departureTime": "2021-11-20T22:05:00",
						"arrivalTime": "2021-11-21T09:20:00",
						"arrivalAirportCode": "BKK",
						"departureAirportCode": "BAH",
						"bodyType": "UNKNOWN",
						"cO2": {
							"value": 0,
							"isEstimation": false
						}
					}
				],
				"surchages": null,
				"id": "95565227-9281-4cdf-b247-515d13e108d7",
				"agency": "GulfAir",
				"service": "GF016-GF165",
				"pickUpDate": "2021-11-18T07:35:00",
				"deliveryDate": "2021-11-21T08:20:00",
				"transitDays": 4,
				"expirationDate": "2021-11-17T23:00:00",
				"price": 4500,
				"extraInfo": [
					"SCC : Barème FCH\nCHC ; 29.50€\nFrais déchargement 0.060€/kg si remise coté ville  - Minimum de perception par opération : 19.00€ (loose cargo)\nRAC : 115.50€ \nTAXE DGR navette : 16.00€\nCCA : 75.00€\nFrais de contrôle Dry Ice / batterie au lithium / quantité exempté et pharma : 17.00€ / contrôle\nTaxe aéroportuaire : 2.40€/LTA\nFrais de transmission de données aux douanes :  8.60€/LTA",
					"1-\tOffre sous réserve de capacité lors de la réservation.\n2-\tRéférence cotation à rappeler impérativement lors de la réservation.\n3-\tCette cotation est valable pour le colisage indiqué uniquement, en cas de modification, merci de procéder à une nouvelle demande auprès du service commercial. \n4-\tTaxes (IRC – MYC –  etc…) susceptibles de modification sans préavis.\n5-\tEn cas d’annulation ou de no show, nous nous réservons le droit de vous répercuter tout ou une partie des frais \n-\tAnnulation 72heures avant le départ du camion et/ou du vol (heures ouvrées) : facturation 50% du montant du fret\n-\tAnnulation 48heures avant le départ du camion et/ou du vol (heures ouvrées) : facturation 75% du montant du fret\n-\tAnnulation 24heures avant le départ du camion et/ou du vol (heures ouvrées) : facturation 100% du montant du fret\n-\tDans le cas d’un no show (non présentation du fret) : facturation 100% du montant du fret \n-\tDans le cas d’un low show (remise inferieure de 50% au poids taxable réservé) : facturation 75% du poids taxable réservé\n"
				]
			},
			{
				"airlineCode": "MS",
				"airlineIATACode": 77,
				"arrivalAirportCode": "BKK",
				"departureAirportCode": "CDG",
				"netRate": 35,
				"allInRate": 35,
				"chargeableWeight": 1.000002,
				"freightPrice": 7000,
				"legs": [
					{
						"flightNumber": "MS800",
						"aircraftCode": "789",
						"departureTime": "2021-11-18T15:45:00",
						"arrivalTime": "2021-11-18T19:05:00",
						"arrivalAirportCode": "CAI",
						"departureAirportCode": "CDG",
						"bodyType": "UNKNOWN",
						"cO2": {
							"value": 0,
							"isEstimation": false
						}
					},
					{
						"flightNumber": "MS507",
						"aircraftCode": "33Y",
						"departureTime": "2021-11-20T09:00:00",
						"arrivalTime": "2021-11-20T17:10:00",
						"arrivalAirportCode": "BKK",
						"departureAirportCode": "CAI",
						"bodyType": "UNKNOWN",
						"cO2": {
							"value": 0,
							"isEstimation": false
						}
					}
				],
				"surchages": null,
				"id": "ee3d57d0-7b30-4370-b8a8-eb4535299579",
				"agency": "Egyptair",
				"service": "MS800-MS507",
				"pickUpDate": "2021-11-18T14:45:00",
				"deliveryDate": "2021-11-20T16:10:00",
				"transitDays": 3,
				"expirationDate": "2021-11-17T23:00:00",
				"price": 7000,
				"extraInfo": [
					"1.\tTarif ALL IN : Fret, fuel, IRC\n2.\tSi frais de navettes applicables : se référer aux coûts de navettes de la grille général Egyptair\n3.\tHS code obligatoire pour tout envoi à destination de la Chine,…\n4.\tTaxe de transmission de données : 3.00 EUR par MAWB et HAWB\n5.      La fumigation des palettes bois est obligatoire pour toutes les destinations\n",
					"1.\tLa référence de cotation indiquée ci-dessus doit être fournie au moment de la réservation, et doit obligatoirement apparaître sur la copie de la LTA. \n2.\tLa cotation est soumise à la disponibilité de l&rsquo;espace au moment de la prise de réservation.\n3.\tLa cotation est soumise aux conditions générales d’application et/ou particulières de la compagnie si mentionné.\n4.\tLa cotation est valide un mois à compter de la date de cotation sauf si une date particulière est mentionnée.\n5.\tLe tarif indiqué est basé sur les détails de l&rsquo;envoi (colisage) fournis au moment de la cotation.\n6.\tUne variation importante du poids ou du volume brut de l&rsquo;envoi peut entraîner un changement tarifaire.\n7.\tLa validité du tarif est basée sur la première date de vol.\n8.\tLes surcharges carburant-fuel  (MYC) et de sécurité (IRC), si applicables, sont susceptibles de changer en fonction de la date de vol effective de l&rsquo;expédition.\n9.\tLa liste OCDC (Other Charges Due Carrier) mentionnée ci-dessus n&rsquo;est pas exhaustive.\nD&rsquo;autres frais supplémentaires dus par le transporteur (OCDC) peuvent s&rsquo;appliquer en fonction des caractéristiques de l&rsquo;expédition finale, de sa destination finale, et selon les conditions générales et/ou locales."
				]
			},
			{
				"airlineCode": "QY",
				"airlineIATACode": 615,
				"arrivalAirportCode": "BKK",
				"departureAirportCode": "CDG",
				"netRate": 110,
				"allInRate": 110,
				"chargeableWeight": 1.000002,
				"freightPrice": 22000,
				"legs": [
					{
						"flightNumber": "QY1261",
						"aircraftCode": "75F",
						"departureTime": "2021-11-18T21:15:00",
						"arrivalTime": "2021-11-18T22:50:00",
						"arrivalAirportCode": "LEJ",
						"departureAirportCode": "CDG",
						"bodyType": "UNKNOWN",
						"cO2": {
							"value": 0,
							"isEstimation": false
						}
					},
					{
						"flightNumber": "QY9446",
						"aircraftCode": "747",
						"departureTime": "2021-11-19T20:40:00",
						"arrivalTime": "2021-11-19T23:40:00",
						"arrivalAirportCode": "DME",
						"departureAirportCode": "LEJ",
						"bodyType": "UNKNOWN",
						"cO2": {
							"value": 0,
							"isEstimation": false
						}
					},
					{
						"flightNumber": "QY9403A",
						"aircraftCode": "77F",
						"departureTime": "2021-11-21T06:10:00",
						"arrivalTime": "2021-11-21T15:10:00",
						"arrivalAirportCode": "BKK",
						"departureAirportCode": "DME",
						"bodyType": "UNKNOWN",
						"cO2": {
							"value": 0,
							"isEstimation": false
						}
					}
				],
				"surchages": null,
				"id": "06f49d04-b1f9-4eb1-8ebe-549b892c645c",
				"agency": "EuropeanAirTransport",
				"service": "QY1261-QY9446-QY9403A",
				"pickUpDate": "2021-11-18T20:15:00",
				"deliveryDate": "2021-11-21T14:10:00",
				"transitDays": 3,
				"expirationDate": "2021-11-17T23:00:00",
				"price": 22000,
				"extraInfo": [
					"SCC : Barème FH\nFrais déchargement 0.060€/kg si remise coté ville  - Minimum de perception par opération : 19.00€ (loose cargo)\nRAC : 115.00€ - Frais de 2ème présentation DGR : 125.00€ \nTaxe DGR navette : 16.00€\nCCA : 75.00€\nFrais de contrôle Dry Ice / batterie au lithium / quantité exempté et pharma : 25.00€ / contrôle\n2eme présentation pour les batteries au lithium ion and metal : 25.00€\nRRY : 57.50€ en sus de la RAC\nAVI : 53.00€\nFrais de transmission messages électroniques.\nL’envoi des FHL/FWB est obligatoire sur TOUTES les destinations depuis le 01 janvier 2021 \nSi vous n’avez pas la possibilité d’assurer la transmission via votre système d’exploitation, cette prestation sera assurée par France Handling et facturée selon le barème suivant : \n15€ / MAWB - 8.50€ / HAWB avec un minimum de 17€.\nSi vous rencontrez des difficultés veuillez contacter ACS.Data.Quality@dhl.com avec une description détaillée du problème (en anglais)\n\n- Le 11 avril 2021, une palette traitée par Hong Kong Air Cargo chargée de smartphones a pris feu à l&rsquo;aéroport international de Hong Kong. \nSuite à cet incident, avec effet immédiat, DHL Aviation n&rsquo;acceptera ni ne transportera les appareils électroniques VIVO nulle part dans le réseau jusqu&rsquo;à nouvel ordre.\nVeuillez communiquer ces informations d&rsquo;interdiction temporaire à vos collaborateurs, clients, afin de n&rsquo;acceptez aucune expédition pouvant contenir de tels éléments.\n\n\n\n\n",
					"1-\tVol confirmé uniquement lors de la réservation et sous réserve de capacité au moment du booking.\n2-\tRéférence cotation à rappeler impérativement lors de la réservation.\n3-\tCette cotation est valable pour le colisage indiqué uniquement, en cas de modification, merci de procéder à une nouvelle demande auprès du service commercial. \n4-\tTaxes (IRC – MYC –  etc…) susceptibles de modification sans préavis.\n5-\tEn cas d’annulation ou de no show, nous nous réservons le droit de vous répercuter tout ou une partie des frais\nAnnulation 72heures avant le départ du camion et/ou du vol (heures ouvrées) : facturation 50% du montant du fret\nAnnulation 48heures avant le départ du camion et/ou du vol (heures ouvrées) : facturation 75% du montant du fret\nAnnulation 24heures avant le départ du camion et/ou du vol (heures ouvrées) : facturation 100% du montant du fret\n\n"
				]
			}
		]
	}

* Air Quote model: 

=============     =============    ======================================================
Name               Type            Description
=============     =============    ======================================================
QuoteId           Guid             Id of the quote
Origin            Location         Object containing the origin info.
Destination       Location         Object containing the destination info.
PickUpDate        DateTime         Pickup date
Rates             List<AirRate>    List containing the rates
=============     =============    ======================================================

* Location model:
  
=============     ========    =============      =======================================
Name              Type        Constraint         Description
=============     ========    =============      =======================================
PostalCode        String      Mandatory 	      PostalCode of the shipment
Country           String      Mandatory 	      Country of the shipment
City              String      Mandatory 	      City of the shipment
State             String      Mandatory 	      State of the shipment
Street            String      Optional 	      	  Street of the shipment
coords            Coord       Optional 	      	  Geolocation data
=============     ========    =============      =======================================

* Coord model:

=============     ========     =============    ======================================================
Name              Type         Constraint       Description
=============     ========     =============    ======================================================
Lat               Double       Mandatory        Location latitude, precision is (3, 6).
Lng               Double       Mandatory 	    Location longitude, precision is (3, 6).
=============     ========     =============    ======================================================


* Air Rate model:
  
=======================    ========================    ==========================================================
Name                       Type                        Description
=======================    ========================    ==========================================================
Id                         Integer                     Guid of rate
AirlineCode                String			    	   Airline code
AirlineIATACode            String                      Airline IATA code
ArrivalAirportCode         String			    	   Arrival Airport Code
DepartureAirportCode       String                      Departure Airport Code
NetRate					   Integer			    	   Net rate
AllInRate				   Integer			    	   All in rate
ChargeableWeight		   Decimal			    	   Chargeable weight
FreightPrice			   Double			    	   Freight price
Agency                     Double                      Agency
Service                    Double                      Service
PickUpDate                 Double                      Pickup date
DeliveryDate               Double                      Delivery date
TransitDays                String                      Transit days
ExpirationDate             DateTime                    Expiration date
Price                      Long                        Price  (Considering 2 last digits as decimals)     
ExtraInfo                  List<String>                List of extra info
Legs                       List<Leg>				   Legs through which it is estimated that it will pass
=======================    ========================    ==========================================================


* Leg model:
  
=====================    ========================    ==========================================================
Name                     Type                        Description
=====================    ========================    ==========================================================
FlightNumber             String                      Flight number
AircraftCode 	      	 String			  	         Aircraft code
DepartureTime            DateTime                    Departure time
ArrivalTime              DateTime                    Arrival time     
ArrivalAirportCode       String                      Arrival airport code
DepartureAirportCode     String                      Departure airport code
BodyType                 String                      Body type
CO2             	     CO2                         CO2
=====================    ========================    ==========================================================   


* CO2 model:
  
=====================    ========================    ==========================================================
Name                     Type                        Description
=====================    ========================    ==========================================================
Value             		 Integer                      CO2 quantity
IsEstimation 	      	 Boolean			  	      True if value is a estimation
=====================    ========================    ==========================================================   
    

.. autosummary::
   :toctree: