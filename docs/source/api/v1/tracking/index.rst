=====================
Tracking
=====================


Tracking - Shipments Query
--------------------------

Example request
~~~~~~~~~~~~~~~
    
    .. sourcecode::

        https://api.freightol.com/v1/tracking/shipments
        
    .. sourcecode:: json
    
	{
        "destination": "",
        "origin": "",
        "FR": "",
        "transportOperator": "",
        "startDate": null,
        "endDate": null
	}

Example response
~~~~~~~~~~~~~~~~

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
            "originState": "PV",
            "originCountry": "ES",
            "originCountryName": "Spain",
            "originCity": "Galdácano",
            "originPostalCode": "48960",
            "destinationState": "CT",
            "destinationCountry": "ES",
            "destinationCountryName": "Spain",
            "destinationCity": "La Garriga",
            "destinationPostalCode": "08530",
            "hasInvoice": false
        },
        {
            "shipmentId": "4b5a254c-6735-474f-81ea-08d7523e7fee",
            "agency": "TNT",
            "pickUpDate": "2019-10-21T06:26:00",
            "deliveryDate": "2019-10-22T16:00:00",
            "transitDays": 1,
            "clientPrice": 1637,
            "currency": "EUR",
            "shipmentCode": "FR00061C",
            "currencyExchangedApplied": null,
            "customs": false,
            "insurance": false,
            "shipmentType": "Box",
            "trackingStatus": 0,
            "customsStatus": null,
            "originState": "Cantabria",
            "originCountry": "ES",
            "originCountryName": "Spain",
            "originCity": "Torrelavega",
            "originPostalCode": "39300",
            "destinationState": "País Vasco",
            "destinationCountry": "ES",
            "destinationCountryName": "Spain",
            "destinationCity": "Sestao",
            "destinationPostalCode": "48910",
            "hasInvoice": true
        },
        {
            "shipmentId": "cfab8e81-d328-4d4c-81eb-08d7523e7fee",
            "agency": "TNT",
            "pickUpDate": "2019-10-21T07:07:00",
            "deliveryDate": "2019-10-23T16:00:00",
            "transitDays": 2,
            "clientPrice": 2869,
            "currency": "EUR",
            "shipmentCode": "FR00061D",
            "currencyExchangedApplied": null,
            "customs": false,
            "insurance": false,
            "shipmentType": "Box",
            "trackingStatus": 0,
            "customsStatus": null,
            "originState": "England",
            "originCountry": "GB",
            "originCountryName": "United Kingdom of Great Britain and Northern Ireland (the)",
            "originCity": "Midlands Occidentales",
            "originPostalCode": "B65 0QW",
            "destinationState": "País Vasco",
            "destinationCountry": "ES",
            "destinationCountryName": "Spain",
            "destinationCity": "Itziar",
            "destinationPostalCode": "20829",
            "hasInvoice": true
        }
      ]
    }

Parameters
~~~~~~~~~~

    =====================   ===========   =============    ================================================================
     Name                     Type         Constraint       Description
    =====================   ===========   =============    ================================================================
     Origin                  String        Optional         Origin
     Destination             String        Optional         Destination
     FR             	     String        Optional         FR
     TransportOperator       String        Optional         Transport Operator
     StartDate       	     DateTime      Optional         Start date
     EndDate		     DateTime      Optional         End date
    =====================   ===========   =============    ================================================================
    
Response
~~~~~~~~

    ===========================   ==========   ===============================================
     Name                          Type         Description
    ===========================   ==========   ===============================================
     ShipmentId                    Guid         Guid of the processed shipment
     ShipmentCode                  String       Shipment code
     Agency                        String       Agency
     PickUpDate                    Double       Pickup date
     DeliveryDate                  Double       Delivery date
     TransitDays                   Int          Transit days
     ExpirationDate                DateTime     Expiration date
     ClientPrice                   Long         ClientPrice(Considering 2 last digits as decimals).      
     Currency		           String	Currency
     CurrencyExchangedApplied      Double?	Currency exchanged applied
     Customs		           Boolean	Customs
     Insurance		           Boolean	Insurance
     ShipmentType	           String	Shipment type
     TrackingStatus	           Int		Tracking status
     CustomsStatus	           String	Customs status
     OriginState	           String	Origin state
     OriginCountry	           String	Origin country
     OriginCountryName	           String	Origin countryName
     OriginCity	           	   String	Origin city
     OriginPostalCode	           String	Origin postalCode
     DestinationState	           String	Destination state
     DestinationCountry	           String	Destination country
     DestinationCountryName	   String	Destination country name
     DestinationCity	           String	Destination city
     DestinationPostalCode	   String	Destination postal code
     HasInvoice	           	   Boolean	Has invoice
    ===========================   ==========   ===============================================


Tracking - Shipment details - HTTPGET
------------------------------------------

Example request
~~~~~~~~~~~~~~~
    
    .. sourcecode::

        https://api.freightol.com/v1/tracking/shipment/details/shipmentId=339d8158-ca3d-4ed7-ac21-08d6ee8277b7
        
    
Example response
~~~~~~~~~~~~~~~~

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
	    "pickupHours": " - "
	}
    
Response
~~~~~~~~

    ===========================   ====================   ===============================================
     Name                          Type         	  Description
    ===========================   ====================   ===============================================
     CommodityId                   Guid         	  Guid of the shipment
     UserId                    	   Guid         	  Guid of the user
     CommodityType	           String		  Commodity type
     CommodityUnits	           List<Commodities>      Commodity type
     CommodityDescription	   String		  Commodity description
     CommodityValue	           Int   		  Commodity value
     ServiceName	           String		  Service name
     Reference	           	   String		  Reference
     BookingReference	           String		  Booking reference
     ExternalTrackingURL	   String		  External tracking URL
     TrackingReference	           String		  Tracking reference
     PaymentType	           String		  Payment type
     PaymentStatus	           String		  Payment status
     Customs		           Boolean		  Customs
     Insurance		           Boolean		  Insurance
     OriginAddress	           String		  Origin address
     OriginState	           String		  Origin state
     OriginCountryCode	           String		  Origin country code
     OriginCountryName	           String		  Origin country name
     OriginCity	           	   String		  Origin city
     OriginPostalCode	           String		  Origin postalCode
     OriginCompany	           String		  Origin company
     OriginContact	           String		  Origin contact	 
     OriginMail	         	   String		  Origin mail
     OriginPhone	           String		  Origin phone     
     DestinationAddress	           String		  Destination address
     DestinationState	           String		  Destination state
     DestinationCountryCode        String		  Destination country code
     DestinationCountryName	   String		  Destination country name
     DestinationCity	           String		  Destination city
     DestinationPostalCode	   String		  Destination postal code
     DestinationCompany	           String		  Destination company
     DestinationContact	           String		  Destination contact	 
     DestinationMail	           String		  Destination mail
     DestinationPhone	           String		  Destination phone
     PickupDescription	           String		  Pickup description
     DeliveryDescription           String		  Delivery description
     PickupHours	           String		  Pickup hours
    ===========================   ====================   ===============================================

     * Commodities:
    ====================    ==========  =======================================
     Name                    Type        Description
    ====================    ==========  =======================================
     CommodityId             String      Shipment Id
     CommodityUnitId         String      Commodity Id
     UnitType                String      Unit type
     MeasurementUnit         String      Measurement unit
     Quantity                String      Quantity
     Weight                  String      Weight
     Length                  String      Length
     Width                   String      Width
     Height                  String      Height
     IsStackable             String      Is stackable
     PalletType              String      Pallet type
     ContainerType           String      Container type
     IsOwnedContainer        String      Is ownedContainer
     IsReeferContainer       String      Is reefer container
     ImoNumber               String      Imo number
    ====================    ==========  =======================================

Tracking - Tracking Messages - HTTPGET
---------------------------------------


Example request
~~~~~~~~~~~~~~~
    
    .. sourcecode::

        https://api.freightol.com/v1/tracking/cfab8e81-d328-4d4c-81eb-08d7523e7fee
        
    
Example response
~~~~~~~~~~~~~~~~

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
         
Response
~~~~~~~~

    ===========================   ==========   ===============================================
     Name                          Type         Description
    ===========================   ==========   ===============================================
     ShipmentId                    Guid         Guid of the shipment
     Message                       String       Message
     UpdatedDate                   DateTime     Updated date
     Status	                   String       Status
     GroupIndex 	           String       Group index
     CountryCode                   String       Country code  
     CountryName		   String	Country name
     City			   String	City
     Address		           String	Address
    ===========================   ==========   ===============================================

.. autosummary::
   :toctree: generated

   lumache