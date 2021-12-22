=============================
PickUp Time
=============================

PickUp Time
----------------
Receives the Id of the shipment, and returns a list valid PickUp times.

**Example request**:
    
.. http:get:: /v1/shipping/pickUpTime/(guid: shipmentId)

.. tabs::
    .. code-tab:: bash

        $ curl \
            -H "Content-Type: application/json" \
            -H "Authorization: Bearer <token>" \
            https://<env>.freightol.com/v1/shipping/pickUpTime/fd67ff6e-4c47-4f85-8cc4-92833724338a

=============  =======  =================================================
Name            Type    Description
=============  =======  =================================================
ShipmentId      Guid    Shipment or Rate ID
=============  =======  =================================================

**Example response**:

.. sourcecode:: json

	{
        "from": [
            "11:00:00",
            "11:30:00",
            "12:00:00",
            "12:30:00",
            "13:00:00",
            "13:30:00",
            "14:00:00",
            "14:30:00",
            "15:00:00",
            "15:30:00",
            "16:00:00",
            "16:30:00",
            "17:00:00",
            "17:30:00",
            "18:00:00",
            "18:30:00"
        ],
        "to": [
            "12:00:00",
            "12:30:00",
            "13:00:00",
            "13:30:00",
            "14:00:00",
            "14:30:00",
            "15:00:00",
            "15:30:00",
            "16:00:00",
            "16:30:00",
            "17:00:00",
            "17:30:00",
            "18:00:00",
            "18:30:00"
        ],
        "minRangeInMinutes": 60
    }

==================  ===============  ======================================================
Name                 Type             Description
==================  ===============  ======================================================
From                 List<String>    Valid times for start pickup time
To                   List<String>    Valid times for end pickup time
MinRangeInMinutes    int             Minimum interval in minutes
==================  ===============  ======================================================

.. autosummary::
   :toctree: generated
