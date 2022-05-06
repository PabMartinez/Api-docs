=====================
Booking
=====================

Box Booking
----------------

Request for Box shipment, it receives the data of the shipment and returns the shipmentCode, bookingCode and trackingCode.

**Example request**:
    
.. http:post:: /v1/shipping/boxes


.. tabs::

    .. code-tab:: bash

        $ curl '-X POST' \
            'https://<env>.freightol.com/v1/shipping/boxes' \
            -H "Content-Type: application/json" \
            -H "Authorization: Bearer <token>" \
            -d @body.json

The content of ``body.json`` is like,
	
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

* Box Booking model:

=====================   =========   =============    ================================================================
Name                     Type       Constraint       Description
=====================   =========   =============    ================================================================
Id                      Guid        Mandatory        Guid of selected the quote
Origin                  Address     Mandatory        Object containing the origin info.
Destination             Address     Mandatory        Object containing the destination info.
PickupTimeFrom          String      Mandatory        PickUp start time, timeSpan as string (hh:mm or hh:mm:ss) 
PickupTimeTo            String      Mandatory        PickUp end time, timeSpan as string (hh:mm or hh:mm:ss)
PickupDescription       String      Optional         Desription for the pickup
DeliveryDescription     String      Optional         Desription for the delivery
IncotermCode            String      Optional         Incoterm code, requires a valid standard code
=====================   =========   =============    ================================================================

* Address model:
  
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


**Example response**:

.. sourcecode:: json

    {
        "shipmentId": "215bcdxe-b3df-4400-52e4-08d999fb141c",
        "shipmentCode": "FR9999FD",
        "trackingCode": "dummy",
        "externalTrackingUrl": "http://dummy.io",
        "bookingCode": "dummy"
    }

* Box Booking model:

=======================   ==========   ===============================================
Name                      Type         Description
=======================   ==========   ===============================================
ShipmentId                Guid         Guid of the processed shipment
ShipmentCode              String       Code of the processed shipment
TrackingCode              String?      Tracking code
ExternalTrackingUrl       String?      External tracking url
BookingCode               String?      Booking code
=======================   ==========   ===============================================
   

Pallet Booking
----------------

Request for Pallet shipment, it receives the data of the shipment and returns the shipmentCode, bookingCode and trackingCode.

**Example request**:
    
.. http:post:: /v1/shipping/pallets


.. tabs::

    .. code-tab:: bash

        $ curl -X POST \
            'https://<env>.freightol.com/v1/shipping/pallets' \
            -H "Content-Type: application/json" \
            -H "Authorization: Bearer <token>" \
            -d @body.json
            

The content of ``body.json`` is like,
	
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

* Pallet Booking model:

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

**Example response**:

.. sourcecode:: json

    {
        "shipmentId": "215bcdxe-b3df-4400-52e4-08d999fb141c",
        "shipmentCode": "FR9999FD",
        "trackingCode": "dummy",
        "externalTrackingUrl": "http://dummy.io",
        "bookingCode": "dummy"
    }

* Pallet Booking model:

=======================   ==========   ===============================================
Name                      Type         Description
=======================   ==========   ===============================================
ShipmentId                Guid         Guid of the processed shipment
ShipmentCode              String       Code of the processed shipment
TrackingCode              String?      Tracking code
ExternalTrackingUrl       String?      External tracking url
BookingCode               String?      Booking code
=======================   ==========   ===============================================
    

FCL Sea Booking
-------------------

Request for Sea FCL shipment, it receives the data of the shipment and returns the shipmentCode, bookingCode and trackingCode.

.. warning::

   This endpoint is working in progress.

**Example request**:
    
.. http:post:: /v1/shipping/sea/fcl


.. tabs::

    .. code-tab:: bash

        $ curl -X POST \
            'https://<env>.freightol.com/v1/shipping/sea/fcl' \
            -H "Content-Type: application/json" \
            -H "Authorization: Bearer <token>" \
            -d @body.json

The content of ``body.json`` is like,
	
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
        "incotermCode": "EXW",
        "containers": [
			{
				"sequentialNumber": 0,
				"cargos": [
					{
						"quantity": 2,
						"weight": 100.0,
						"cbm": 5,
						"description": "Motor",
						"ediType": "204",
						"hsCode": "8601",
						"indexContainer": 0
					},
					{
						"quantity": 1,
						"weight": 500.0,
						"cbm": 1.5,
						"description": "Motor",
						"ediType": "214",
						"hsCode": "8401",
						"indexContainer": 1
					}
				]
			}
    }

* Sea FCL Booking model:

=====================   =================   =============    ================================================================
Name                     Type                Constraint       Description
=====================   =================   =============    ================================================================
Id                      Guid                 Mandatory        Id of selected the quote
Origin                  Address              Mandatory        Object containing the origin info.
Destination             Address              Mandatory        Object containing the destination info.
PickupTimeFrom          String               Mandatory        PickUp start time, timeSpan as string (hh:mm or hh:mm:ss) 
PickupTimeTo            String               Mandatory        PickUp end time, timeSpan as string (hh:mm or hh:mm:ss)
PickupDescription       String               Optional         Desription for the pickup
DeliveryDescription     String               Optional         Desription for the delivery
IncotermCode            String               Mandatory        Incoterm code, requires a valid code
Containers              List<Container>      Mandatory        List container-cargos commodity details.
=====================   =================   =============    ================================================================

* Address model:

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

* Container model:

=================    ==============   =============    ==================================================================================================================
Name                 Type             Constraint       Description
=================    ==============   =============    ==================================================================================================================
SequentialNumber      Integer         Mandatory        Container sequential number, starting at 0. 
Cargos                List<Cargo>     Mandatory        Cargo packages in FCL container
=================    ==============   =============    ==================================================================================================================

* Cargo model:

=================    ==========   =============    ==================================================================================================================
Name                 Type         Constraint       Description
=================    ==========   =============    ==================================================================================================================
Quantity              Integer      Mandatory        Cargo quantity
Weight                Double       Mandatory        Cargo weight
CBM                   Double       Mandatory        Cargo CBM
Description           String       Mandatory        Cargo description
EDIType               String       Mandatory        EDI description
HSCode                String       Mandatory        HS Code (https://www.tariffnumber.com/). No pre-validation. If code is invalid, booking will never confirm.
IndexContainer        Integer      Mandatory        Cargo index using Container quantity. It must be lower than quantity and start at 0.
=================    ==========   =============    ==================================================================================================================

**Example response**:

.. sourcecode:: json

    {
        "shipmentId": "215bcdxe-b3df-4400-52e4-08d999fb141c",
        "shipmentCode": "FR9999FD",
        "trackingCode": "dummy",
        "externalTrackingUrl": "http://dummy",
        "bookingCode": "dummy"
    }

* Sea FCL Booking model:

=======================   ==========   ===============================================
Name                      Type         Description
=======================   ==========   ===============================================
ShipmentId                Guid         Guid of the processed shipment
ShipmentCode              String       Code of the processed shipment
TrackingCode              String?      Tracking code
ExternalTrackingUrl       String?      External tracking url
BookingCode               String?      Booking code
=======================   ==========   ===============================================
 
LCL Sea Booking
-------------------------------

Request for Sea LCL shipment, it receives the data of the shipment and returns the shipmentCode, bookingCode and trackingCode.

.. warning::

   This endpoint is working in progress.

**Example request**:
    
.. http:post:: /v1/shipping/sea/lcl


.. tabs::

    .. code-tab:: bash

        $ curl -X POST \
            'https://<env>.freightol.com/v1/shipping/sea/lcl' \
            -H "Content-Type: application/json" \
            -H "Authorization: Bearer <token>" \
            -d @body.json
            

The content of ``body.json`` is like,
	
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
        "incotermCode": "FOB",
        "cargos": [
            {
                "description": "Motor",
                "ediType": "204",
                "hsCode": "8601"
            },
            {
                "description": "Motor",
                "ediType": "214",
                "hsCode": "8401"
            }
        ]
    }

* Sea LCL Booking model:

=====================   =================   =============    ================================================================
Name                     Type                Constraint       Description
=====================   =================   =============    ================================================================
Id                      Guid                 Mandatory        Id of selected the quote
Origin                  Address              Mandatory        Object containing the origin info.
Destination             Address              Mandatory        Object containing the destination info.
PickupTimeFrom          String               Mandatory        PickUp start time, timeSpan as string (hh:mm or hh:mm:ss) 
PickupTimeTo            String               Mandatory        PickUp end time, timeSpan as string (hh:mm or hh:mm:ss)
PickupDescription       String               Optional         Desription for the pickup
DeliveryDescription     String               Optional         Desription for the delivery
IncotermCode            String               Mandatory        Inconterm code, requires a valid code
Cargos                  List<Cargo>          Mandatory        List cargos commodity details.
=====================   =================   =============    ================================================================

* Address model:

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

* Cargo model:

=================    ==========   =============    ==================================================================================================================
Name                 Type         Constraint       Description
=================    ==========   =============    ==================================================================================================================
Description           String       Mandatory        Cargo description
EDIType               String       Mandatory        EDI description
HSCode                String       Mandatory        HS Code (https://www.tariffnumber.com/). No pre-validation. If code is invalid, booking will never confirm.
=================    ==========   =============    ==================================================================================================================

**Example response**:

.. sourcecode:: json

    {
        "shipmentId": "215bcdxe-b3df-4400-52e4-08d999fb141c",
        "shipmentCode": "FR9999FD",
        "trackingCode": "dummy",
        "externalTrackingUrl": "http://dummy",
        "bookingCode": "dummy"
    }

* Sea LCL Booking model:

=======================   ==========   ===============================================
Name                      Type         Description
=======================   ==========   ===============================================
ShipmentId                Guid         Guid of the processed shipment
ShipmentCode              String       Code of the processed shipment
TrackingCode              String?      Tracking code
ExternalTrackingUrl       String?      External tracking url
BookingCode               String?      Booking code
=======================   ==========   ===============================================

/*Air Booking
----------------------------

Request for Air shipment, it receives the data of the shipment and returns the shipmentCode, bookingCode and trackingCode.


**Example request**:
    
.. http:post:: /v1/shipping/air


.. tabs::

    .. code-tab:: bash

        $ curl -X POST \
            'https://<env>.freightol.com/v1/shipping/air' \
            -H "Content-Type: application/json" \
            -H "Authorization: Bearer <token>" \
            -d @body.json

The content of ``body.json`` is like,
	
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

* Air Shipping model:

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

* Address model:

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
    

**Example response**:

.. sourcecode:: json

    {
        "shipmentId": "215bcdxe-b3df-4400-52e4-08d999fb141c",
        "shipmentCode": "FR9999FD",
        "trackingCode": "http://dummy",
        "externalTrackingUrl": "dummy",
        "bookingCode": "dummy"
    }

* Air Booking model:

=======================   ==========   ===============================================
Name                      Type         Description
=======================   ==========   ===============================================
ShipmentId                Guid         Guid of the processed shipment
ShipmentCode              String       Code of the processed shipment
TrackingCode              String?      Tracking code
ExternalTrackingUrl       String?      External tracking url
BookingCode               String?      Booking code
=======================   ==========   ===============================================
*/
.. autosummary::
   :toctree: generated
