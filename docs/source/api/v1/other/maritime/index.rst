=============================
Maritime
=============================

Containers Types
----------------
Retrieves the list of supported containers types

**Example request**:

.. http:get:: /v1/maritime

.. tabs::
    .. code-tab:: bash

        $ curl \
            -H "Content-Type: application/json" \
            -H "Authorization: Bearer <token>" \
            https://<env>.freightol.com/v1/maritime
  
  
**Example response**:

.. sourcecode:: json

	[
	    {
		"size": "20",
		"type": "DRY",
		"name": "20DRY",
		"label": "40 Dry Standard",
		"isReefer": false
	    },
	    {
		"size": "40",
		"type": "DRY",
		"name": "40DRY",
		"label": "40 Dry Standard",
		"isReefer": false
	    },
	    {
		"size": "40",
		"type": "HDRY",
		"name": "40HDRY",
		"label": "40 Dry High",
		"isReefer": false
	    },
	    {
		"size": "45",
		"type": "HDRY",
		"name": "45HDRY",
		"label": "45 Dry High",
		"isReefer": false
	    },
	    {
		"size": "20",
		"type": "OPENTOP",
		"name": "20OPENTOP",
		"label": "20 Open Top Standard",
		"isReefer": false
	    },
	    {
		"size": "40",
		"type": "OPENTOP",
		"name": "40OPENTOP",
		"label": "40 Open Top Standard",
		"isReefer": false
	    },
	    {
		"size": "40",
		"type": "HOPENTOP",
		"name": "40HOPENTOP",
		"label": "45 Open Top High",
		"isReefer": false
	    },
	    {
		"size": "40",
		"type": "FLATRACK",
		"name": "40FLATRACK",
		"label": "40 Flat Rack Standard",
		"isReefer": false
	    },
	    {
		"size": "40",
		"type": "HFLATRACK",
		"name": "40HFLATRACK",
		"label": "45 Flat Rack High",
		"isReefer": false
	    },
	    {
		"size": "40",
		"type": "HNOR",
		"name": "40HNOR",
		"label": "40 Non Operating Reefer High",
		"isReefer": false
	    },
	    {
		"size": "45",
		"type": "HNOR",
		"name": "45HNOR",
		"label": "45 Non Operating Reefer High",
		"isReefer": false
	    },
	    {
		"size": "20",
		"type": "RF",
		"name": "20RF",
		"label": "20 Reefer Standard",
		"isReefer": true
	    },
	    {
		"size": "40",
		"type": "RF",
		"name": "40RF",
		"label": "40 Reefer Standard",
		"isReefer": true
	    },
	    {
		"size": "40",
		"type": "HRF",
		"name": "40HRF",
		"label": "45 Reefer High",
		"isReefer": false
	    },
	    {
		"size": "45",
		"type": "RF",
		"name": "45RF",
		"label": "45 Reefer Standard",
		"isReefer": true
	    },
	    {
		"size": "20",
		"type": "FLATRACK",
		"name": "20FLATRACK",
		"label": "20 Flat Rack Standard",
		"isReefer": false
	    }
	]

**Example response**:

=======================   ==========   ===============================================
Name                      Type         Description
=======================   ==========   ===============================================
Size		       			Double	     Size
Type		      			String       Type
Name		       			String       Name
Label		       			String       Label
IsReefer		       		Boolean      Is reefer
=======================   ==========   ===============================================

Maritime Ports
----------------
Receives the name of the city, and returns a list of ports.

**Example request**:
    
.. http:get:: /v1/maritime/ports?cityName=(string: port)

.. tabs::
    .. code-tab:: bash

        $ curl \
            -H "Content-Type: application/json" \
            -H "Authorization: Bearer <token>" \
            https://<env>.freightol.com/v1/maritime/ports?CityName=barcelona

=============  =======  =================================================
Name            Type    Description
=============  =======  =================================================
CityName       String    Mandatory   Name of city or IATA airport code.
=============  =======  =================================================

**Example response**:

.. sourcecode:: json

	[
		{
			"unLocCode": "ESBCN",
			"country": "ES",
			"city": "Barcelona",
			"rkstCode": "ESBCN"
		},
		{
			"unLocCode": "VEBLA",
			"country": "VE",
			"city": "Barcelona",
			"rkstCode": "VEBCA"
		}
	]

=============  =======  ======================================================
Name            Type    Description
=============  =======  ======================================================
unLocCode      String   UN/LOCODE 
country        String   Country ISO 3166-1 alfa-2 code.
city           String   City name.
rkstCode       String   Code used internally in Maersk network
=============  =======  ======================================================


