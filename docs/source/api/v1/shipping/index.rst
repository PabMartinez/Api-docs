=====================
Shipping
=====================

Box Shipping
----------------

**Example request**:
    
    .. sourcecode::

        https://api.freightol.com/v1/shipping/boxes
        
    .. sourcecode:: json

       {
        "id": "cacc83d3-de42-4148-ba8b-e52b5bdbd2cf",
        "origin": {
		"contactPerson": "DO NOT COLLECT",
		"companyName": "DO NOT COLLECT",
		"contactMail": "test@test.com",
		"address": "DO NOT COLLECT",
		"phonePrefix": "676226090",
		"phone": "34"
        },
        "destination": {
		"contactPerson": "DO NOT COLLECT",
		"companyName": "DO NOT COLLECT",
		"contactMail": "test@test.com",
		"address": "DO NOT COLLECT",
		"phonePrefix": "676226090",
		"phone": "34"
        },
        "pickupTimeFrom": "10:10",
        "pickupTimeTo": "20:20",
        "pickupDescription": null,
        "deliveryDescription": null,
        "incotermCode": null
        }

**Example response**:

    .. sourcecode:: json

        {
		"shipmentId": "215bcdxe-b3df-4400-52e4-08d999fb141c",
		"shipmentCode": "FR9999FD",
		"trackingCode": "1S51S1S56816301289",
		"externalTrackingUrl": "dummy",
		"bookingCode": "1S51S1S56816301289"
        }

Parameters
~~~~~~~~~~

    =====================   =========   =============    ================================================================
     Name                     Type       Constraint       Description
    =====================   =========   =============    ================================================================
     Id                      Guid        Mandatory        Id of selected the quote
     Origin                  Address     Mandatory        Object containing the origin info.
     Destination             Address     Mandatory        Object containing the destination info.
     PickupTimeFrom          String      Mandatory        PickUp start time, timeSpan as string (hh:mm or hh:mm:ss) 
     PickupTimeTo            String      Mandatory        PickUp end time, timeSpan as string (hh:mm or hh:mm:ss)
     PickupDescription       String      Optional         Desription for the pickup
     DeliveryDescription     String      Optional         Desription for the delivery
     IncotermCode            String      Optional         Inconterm code, requires a valid code
    =====================   =========   =============    ================================================================

     * Address:
    =================    ==========   =============    =======================================
     Name                 Type         Constraint       Description
    =================    ==========   =============    =======================================
     ContactPerson        String       Mandatory        Contact person
     CompanyName          String       Mandatory        Company name
     ContactMail          String       Mandatory        Contact mail
     Address              String       Mandatory        Address
     PhonePrefix          String       Optional         Phone prefix (without "+")
     Phone                String       Mandatory        Phone
    =================    ==========   =============    =======================================
    
Response
~~~~~~~~

    =======================   ==========   ===============================================
     Name                      Type         Description
    =======================   ==========   ===============================================
     ShipmentId                Guid         Guid of the processed shipment
     ShipmentCode              String       Code of the processed shipment
     TrackingCode              String       Tracking code
     ExternalTrackingUrl       Url          External tracking url
     BookingCode               String       Booking code
    =======================   ==========   ===============================================
   

Pallet Shipping
----------------


Example request
~~~~~~~~~~~~~~~
    
    .. sourcecode::

        https://api.freightol.com/v1/shipping/pallets
        
    .. sourcecode:: json

     {
	"id": "8d34a39b-d082-403c-931d-af7c42e901eb",
	"origin": {
		"contactPerson": "DO NOT COLLECT",
		"companyName": "DO NOT COLLECT",
		"contactMail": "test@test.com",
		"address": "DO NOT COLLECT",
		"phonePrefix": "999999999",
		"phone": "34"
	},
	"destination": {
		"contactPerson": "DO NOT COLLECT",
		"companyName": "DO NOT COLLECT",
		"contactMail": "test@test.com",
		"address": "DO NOT COLLECT",
		"phonePrefix": "999999999",
		"phone": "34"
	},
	"pickupTimeFrom": "10:10",
	"pickupTimeTo": "20:20",
	"pickupDescription": null,
	"deliveryDescription": null,
	"incotermCode": null
    }



Example response
~~~~~~~~~~~~~~~~

    .. sourcecode:: json

        {
        "shipmentId": "215bcdxe-b3df-4400-52e4-08d999fb141c",
        "shipmentCode": "FR9999FD",
        "trackingCode": "1S51S1S56816301289",
        "externalTrackingUrl": "dummy",
        "bookingCode": "1S51S1S56816301289"
        }

Parameters
~~~~~~~~~~

    =====================   =========   =============    ================================================================
     Name                     Type       Constraint       Description
    =====================   =========   =============    ================================================================
     Id                      Guid        Mandatory        Id of selected the quote
     Origin                  Address     Mandatory        Object containing the origin info.
     Destination             Address     Mandatory        Object containing the destination info.
     PickupTimeFrom          String      Mandatory        PickUp start time, timeSpan as string (hh:mm or hh:mm:ss) 
     PickupTimeTo            String      Mandatory        PickUp end time, timeSpan as string (hh:mm or hh:mm:ss)
     PickupDescription       String      Optional         Desription for the pickup
     DeliveryDescription     String      Optional         Desription for the delivery
     IncotermCode            String      Optional         Inconterm code, requires a valid code
    =====================   =========   =============    ================================================================

     * Address:
    =================    ==========   =============    =======================================
     Name                 Type         Constraint       Description
    =================    ==========   =============    =======================================
     ContactPerson        String       Mandatory        Contact person
     CompanyName          String       Mandatory        Company name
     ContactMail          String       Mandatory        Contact mail
     Address              String       Mandatory        Address
     PhonePrefix          String       Optional         Phone prefix (without "+")
     Phone                String       Mandatory        Phone
    =================    ==========   =============    =======================================
    
Response
~~~~~~~~

    =======================   ==========   ===============================================
     Name                      Type         Description
    =======================   ==========   ===============================================
     ShipmentId                Guid         Guid of the processed shipment
     ShipmentCode              String       Code of the processed shipment
     TrackingCode              String       Tracking code
     ExternalTrackingUrl       Url          External tracking url
     BookingCode               String       Booking code
    =======================   ==========   ===============================================
    

FCL Sea Shipping
-------------------

Example request
~~~~~~~~~~~~~~~
    
    .. sourcecode::

        https://api.freightol.com/v1/shipping/sea/fcl
        
    .. sourcecode:: json

       {
	"id": "a445119b-6fe4-4607-a976-7af8cdd71d5e",
	"origin": {
		"contactPerson": "DO NOT COLLECT",
		"companyName": "DO NOT COLLECT",
		"contactMail": "test@test.com",
		"address": "DO NOT COLLECT",
		"phonePrefix": "999999999",
		"phone": "34"
	},
	"destination": {
		"contactPerson": "DO NOT COLLECT",
		"companyName": "DO NOT COLLECT",
		"contactMail": "test@test.com",
		"address": "DO NOT COLLECT",
		"phonePrefix": "999999999",
		"phone": "34"
	},
	"pickupTimeFrom": "10:10",
	"pickupTimeTo": "20:20",
	"pickupDescription": null,
	"deliveryDescription": null,
	"incotermCode": null
	}

Example response
~~~~~~~~~~~~~~~~

    .. sourcecode:: json

        {
        "shipmentId": "215bcdxe-b3df-4400-52e4-08d999fb141c",
        "shipmentCode": "FR9999FD",
        "trackingCode": "1S51S1S56816301289",
        "externalTrackingUrl": "dummy",
        "bookingCode": "1S51S1S56816301289"
        }

Parameters
~~~~~~~~~~

    =====================   =========   =============    ================================================================
     Name                     Type       Constraint       Description
    =====================   =========   =============    ================================================================
     Id                      Guid        Mandatory        Id of selected the quote
     Origin                  Address     Mandatory        Object containing the origin info.
     Destination             Address     Mandatory        Object containing the destination info.
     PickupTimeFrom          String      Mandatory        PickUp start time, timeSpan as string (hh:mm or hh:mm:ss) 
     PickupTimeTo            String      Mandatory        PickUp end time, timeSpan as string (hh:mm or hh:mm:ss)
     PickupDescription       String      Optional         Desription for the pickup
     DeliveryDescription     String      Optional         Desription for the delivery
     IncotermCode            String      Optional         Inconterm code, requires a valid code
    =====================   =========   =============    ================================================================

     * Address:
    =================    ==========   =============    =======================================
     Name                 Type         Constraint       Description
    =================    ==========   =============    =======================================
     ContactPerson        String       Mandatory        Contact person
     CompanyName          String       Mandatory        Company name
     ContactMail          String       Mandatory        Contact mail
     Address              String       Mandatory        Address
     PhonePrefix          String       Optional         Phone prefix (without "+")
     Phone                String       Mandatory        Phone
    =================    ==========   =============    =======================================
    
Response
~~~~~~~~

    =======================   ==========   ===============================================
     Name                      Type         Description
    =======================   ==========   ===============================================
     ShipmentId                Guid         Guid of the processed shipment
     ShipmentCode              String       Code of the processed shipment
     TrackingCode              String       Tracking code
     ExternalTrackingUrl       Url          External tracking url
     BookingCode               String       Booking code
    =======================   ==========   ===============================================
 
LCL Sea Shipping - HTTPPOST
-------------------------------

Example request
~~~~~~~~~~~~~~~
    
    .. sourcecode::

        https://api.freightol.com/v1/shipping/sea/lcl
        
    .. sourcecode:: json

     {
	"id": "8d34a39b-d082-403c-931d-af7c42e901eb",
	"origin": {
	"contactPerson": "DO NOT COLLECT",
	"companyName": "DO NOT COLLECT",
	"contactMail": "test@test.com",
	"address": "DO NOT COLLECT",
	"phonePrefix": "999999999",
	"phone": "34"
	},
	"destination": {
	"contactPerson": "DO NOT COLLECT",
	"companyName": "DO NOT COLLECT",
	"contactMail": "test@test.com",
	"address": "DO NOT COLLECT",
	"phonePrefix": "999999999",
	"phone": "34"
	},
	"pickupTimeFrom": "10:10",
	"pickupTimeTo": "20:20",
	"pickupDescription": null,
	"deliveryDescription": null,
	"incotermCode": null
    }



Example response
~~~~~~~~~~~~~~~~

    .. sourcecode:: json

        {
          "shipmentId": "215bcdxe-b3df-4400-52e4-08d999fb141c",
          "shipmentCode": "FR9999FD",
          "trackingCode": "1S51S1S56816301289",
          "externalTrackingUrl": "dummy",
          "bookingCode": "1S51S1S56816301289"
        }

Parameters
~~~~~~~~~~

    =====================   =========   =============    ================================================================
     Name                     Type       Constraint       Description
    =====================   =========   =============    ================================================================
     Id                      Guid        Mandatory        Id of selected the quote
     Origin                  Address     Mandatory        Object containing the origin info.
     Destination             Address     Mandatory        Object containing the destination info.
     PickupTimeFrom          String      Mandatory        PickUp start time, timeSpan as string (hh:mm or hh:mm:ss) 
     PickupTimeTo            String      Mandatory        PickUp end time, timeSpan as string (hh:mm or hh:mm:ss)
     PickupDescription       String      Optional         Desription for the pickup
     DeliveryDescription     String      Optional         Desription for the delivery
     IncotermCode            String      Optional         Inconterm code, requires a valid code
    =====================   =========   =============    ================================================================

     * Address:
    =================    ==========   =============    =======================================
     Name                 Type         Constraint       Description
    =================    ==========   =============    =======================================
     ContactPerson        String       Mandatory        Contact person
     CompanyName          String       Mandatory        Company name
     ContactMail          String       Mandatory        Contact mail
     Address              String       Mandatory        Address
     PhonePrefix          String       Optional         Phone prefix (without "+")
     Phone                String       Mandatory        Phone
    =================    ==========   =============    =======================================
    
Response
~~~~~~~~

    =======================   ==========   ===============================================
     Name                      Type         Description
    =======================   ==========   ===============================================
     ShipmentId                Guid         Guid of the processed shipment
     ShipmentCode              String       Code of the processed shipment
     TrackingCode              String       Tracking code
     ExternalTrackingUrl       Url          External tracking url
     BookingCode               String       Booking code
    =======================   ==========   ===============================================

Air Shipping - HTTPPOST
----------------------------


Example request
~~~~~~~~~~~~~~~
    
    .. sourcecode::

        https://api.freightol.com/v1/shipping/air
        
    .. sourcecode:: json
    
	{
	"id": "dc518d27-0f3d-4bdc-ab4d-3fce1baaee87",
	"origin": {
		"contactPerson": "DO NOT COLLECT",
		"companyName": "DO NOT COLLECT",
		"contactMail": "test@test.com",
		"address": "DO NOT COLLECT",
		"phonePrefix": "676226090",
		"phone": "34"
	},
	"destination": {
		"contactPerson": "DO NOT COLLECT",
		"companyName": "DO NOT COLLECT",
		"contactMail": "test@test.com",
		"address": "DO NOT COLLECT",
		"phonePrefix": "676226090",
		"phone": "34"
	},
	"pickupTimeFrom": "10:10",
	"pickupTimeTo": "20:20",
	"pickupDescription": null,
	"deliveryDescription": null,
	"incotermCode": null
	}

Example response
~~~~~~~~~~~~~~~~

    .. sourcecode:: json

        {
          "shipmentId": "215bcdxe-b3df-4400-52e4-08d999fb141c",
          "shipmentCode": "FR9999FD",
          "trackingCode": "1S51S1S56816301289",
          "externalTrackingUrl": "dummy",
          "bookingCode": "1S51S1S56816301289"
        }

Parameters
~~~~~~~~~~

    =====================   =========   =============    ================================================================
     Name                     Type       Constraint       Description
    =====================   =========   =============    ================================================================
     Id                      Guid        Mandatory        Id of selected the quote
     Origin                  Address     Mandatory        Object containing the origin info.
     Destination             Address     Mandatory        Object containing the destination info.
     PickupTimeFrom          String      Mandatory        PickUp start time, timeSpan as string (hh:mm or hh:mm:ss) 
     PickupTimeTo            String      Mandatory        PickUp end time, timeSpan as string (hh:mm or hh:mm:ss)
     IncotermCode            String      Mandatory        Inconterm code, requires a valid code
     PickupDescription       String      Optional         Desription for the pickup
     DeliveryDescription     String      Optional         Desription for the delivery
    =====================   =========   =============    ================================================================

     * Address:
    =================    ==========   =============    =======================================
     Name                 Type         Constraint       Description
    =================    ==========   =============    =======================================
     ContactPerson        String       Mandatory        Contact person
     CompanyName          String       Mandatory        Company name
     ContactMail          String       Mandatory        Contact mail
     Address              String       Mandatory        Address
     PhonePrefix          String       Optional         Phone prefix (without "+")
     Phone                String       Mandatory        Phone
    =================    ==========   =============    =======================================
    
Response
~~~~~~~~

    =======================   ==========   ===============================================
     Name                      Type         Description
    =======================   ==========   ===============================================
     ShipmentId                Guid         Guid of the processed shipment
     ShipmentCode              String       Code of the processed shipment
     TrackingCode              String       Tracking code
     ExternalTrackingUrl       Url          External tracking url
     BookingCode               String       Booking code
    =======================   ==========   ===============================================


.. autosummary::
   :toctree: generated

   lumache