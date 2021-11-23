=====================
Shipping
=====================

Box Shipping
----------------

**Example request**:
    
.. http:post:: /v1/shipping/boxes


.. tabs::

    .. code-tab:: bash

        $ curl \
            -X POST \
            -H "Content-Type: application/json" \
            -H "Authorization: Bearer <token>" \
            -d @body.json \
            https://<env>.freightol.com/v1/shipping/boxes

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

* Box Shipping model:

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
TrackingCode              String       Tracking code
ExternalTrackingUrl       Url          External tracking url
BookingCode               String       Booking code
=======================   ==========   ===============================================
   

Pallet Shipping
----------------

**Example request**:
    
.. http:post:: /v1/shipping/pallets


.. tabs::

    .. code-tab:: bash

        $ curl \
            -X POST \
            -H "Content-Type: application/json" \
            -H "Authorization: Bearer <token>" \
            -d @body.json \
            https://<env>.freightol.com/v1/shipping/pallets

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

* Pallet Shipping model:

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
TrackingCode              String       Tracking code
ExternalTrackingUrl       Url          External tracking url
BookingCode               String       Booking code
=======================   ==========   ===============================================
    

FCL Sea Shipping
-------------------

.. warning::

   This endpoint is working in progress.

**Example request**:
    
.. http:post:: /v1/shipping/sea/fcl


.. tabs::

    .. code-tab:: bash

        $ curl \
            -X POST \
            -H "Content-Type: application/json" \
            -H "Authorization: Bearer <token>" \
            -d @body.json \
            https://<env>.freightol.com/v1/shipping/sea/fcl

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
        "incotermCode": "EBW"
    }

* Sea FCL Shipping model:

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
IncotermCode            String      Mandatory        Inconterm code, requires a valid code
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
        "externalTrackingUrl": "http://dummy",
        "bookingCode": "dummy"
    }

* Sea FCL Booking model:

=======================   ==========   ===============================================
Name                      Type         Description
=======================   ==========   ===============================================
ShipmentId                Guid         Guid of the processed shipment
ShipmentCode              String       Code of the processed shipment
TrackingCode              String       Tracking code
ExternalTrackingUrl       Url          External tracking url
BookingCode               String       Booking code
=======================   ==========   ===============================================
 
LCL Sea Shipping
-------------------------------

.. warning::

   This project is working in progress.

**Example request**:
    
.. http:post:: /v1/shipping/sea/lcl


.. tabs::

    .. code-tab:: bash

        $ curl \
            -X POST \
            -H "Content-Type: application/json" \
            -H "Authorization: Bearer <token>" \
            -d @body.json \
            https://<env>.freightol.com/v1/shipping/sea/lcl

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
        "incotermCode": "FOB"
    }

* Sea LCL Shipping model:

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
IncotermCode            String      Mandatory        Inconterm code, requires a valid code
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
        "externalTrackingUrl": "http://dummy",
        "bookingCode": "dummy"
    }

* Sea LCL Booking model:

=======================   ==========   ===============================================
Name                      Type         Description
=======================   ==========   ===============================================
ShipmentId                Guid         Guid of the processed shipment
ShipmentCode              String       Code of the processed shipment
TrackingCode              String       Tracking code
ExternalTrackingUrl       Url          External tracking url
BookingCode               String       Booking code
=======================   ==========   ===============================================

Air Shipping
----------------------------

**Example request**:
    
.. http:post:: /v1/shipping/air


.. tabs::

    .. code-tab:: bash

        $ curl \
            -X POST \
            -H "Content-Type: application/json" \
            -H "Authorization: Bearer <token>" \
            -d @body.json \
            https://<env>.freightol.com/v1/shipping/air

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
        "trackingCode": "1S51S1S56816301289",
        "externalTrackingUrl": "dummy",
        "bookingCode": "1S51S1S56816301289"
    }

* Air Booking model:

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