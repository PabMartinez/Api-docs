=====================
Tariff
=====================

Request to retrieve the tariff info matching the filters.

TariffReport
--------------------------

**Example request**:
    
.. http:get:: /v1/tariff/getall


.. tabs::
    .. code-tab:: bash

        $ curl -X 'POST' \
            'https://localhost:5011/v1/tariff' \
            -H "Content-Type: application/json" \
            -H "Authorization: Bearer <token>"

**Example request Http**:

.. sourcecode:: json
    {
        "name": null,
        "contractNumber": "CL131839T",
        "delegationId": null,
        "fromDate": "2024-09-01T00:00:00.000Z",
        "toDate": "2024-09-02T00:00:00.000Z",
        "status": null
    }

The query params are like,

=====================   ===========   =============    ================================================================
Name                     Type         Constraint       Description
=====================   ===========   =============    ================================================================
ContractNumber           String        Mandatory         Contract number
Name                     String        Optional          Name
Status   	               Int           Optional          Status
FromDate                 DateTime      Mandatory         Starting date
ToDate                   DateTime      Optional          Finishing date
=====================   ===========   =============    ================================================================

**Example response**:

.. sourcecode:: json

  [
    {
        "documentId": "113175fb-44e5-433a-1935-08d9db648dd8",
        "contractName": "test",
        "carrier": "EGLV",
        "type": "SeaContainer",
        "rates": [
            {
                "id": "00000000-0000-0000-0000-000000000000",
                "pol": "ESVLC",
                "polServiceType": "",
                "pod": "BRPEC",
                "podServiceType": "",
                "startDate": "2022-01-01T00:00:00",
                "endDate": "2023-08-31T00:00:00",
                "timeInTransit": 24,
                "via": null,
                "containerType": 2,
                "costs": [
                    {
                        "commodity": null,
                        "chargeType": 0,
                        "chargeName": "ERS",
                        "chargeDescription": "Equipment Repositionning Surcharge",
                        "amount": 30000,
                        "currency": "EUR",
                        "chargeUnit": 0,
                        "criteria": null,
                        "extraInfo": ""
                    },
                    {
                        "commodity": null,
                        "chargeType": 1,
                        "chargeName": "ALF",
                        "chargeDescription": "Agency Logistic fee",
                        "amount": 1000,
                        "currency": "EUR",
                        "chargeUnit": 0,
                        "criteria": null,
                        "extraInfo": ""
                    },
                    {
                        "commodity": null,
                        "chargeType": 1,
                        "chargeName": "VGM",
                        "chargeDescription": "Verified Gross Mass",
                        "amount": 1000,
                        "currency": "EUR",
                        "chargeUnit": 0,
                        "criteria": null,
                        "extraInfo": ""
                    },
                    {
                        "commodity": null,
                        "chargeType": 0,
                        "chargeName": "PAL",
                        "chargeDescription": "Port additionals",
                        "amount": 5000,
                        "currency": "EUR",
                        "chargeUnit": 0,
                        "criteria": null,
                        "extraInfo": ""
                    },
                    {
                        "commodity": null,
                        "chargeType": 3,
                        "chargeName": "DOC",
                        "chargeDescription": "Documentation Fee",
                        "amount": 5000,
                        "currency": "EUR",
                        "chargeUnit": 0,
                        "criteria": null,
                        "extraInfo": ""
                    },
                    {
                        "commodity": null,
                        "chargeType": 1,
                        "chargeName": "THC",
                        "chargeDescription": "Terminal handling charge",
                        "amount": 23500,
                        "currency": "EUR",
                        "chargeUnit": 0,
                        "criteria": null,
                        "extraInfo": ""
                    },
                    {
                        "commodity": null,
                        "chargeType": 0,
                        "chargeName": "PSS",
                        "chargeDescription": "Peak Season Surcharge",
                        "amount": 60000,
                        "currency": "EUR",
                        "chargeUnit": 0,
                        "criteria": null,
                        "extraInfo": ""
                    },
                    {
                        "commodity": null,
                        "chargeType": 1,
                        "chargeName": "CSS",
                        "chargeDescription": "Carrier security surcharge (Carrier ISPS)",
                        "amount": 900,
                        "currency": "EUR",
                        "chargeUnit": 0,
                        "criteria": null,
                        "extraInfo": ""
                    },
                    {
                        "commodity": null,
                        "chargeType": 0,
                        "chargeName": "BAF",
                        "chargeDescription": "Bunker ajustement factor",
                        "amount": 31600,
                        "currency": "EUR",
                        "chargeUnit": 0,
                        "criteria": null,
                        "extraInfo": ""
                    },
                    {
                        "commodity": null,
                        "chargeType": 0,
                        "chargeName": "FRT",
                        "chargeDescription": "Seafreight",
                        "amount": 150000,
                        "currency": "EUR",
                        "chargeUnit": 0,
                        "criteria": null,
                        "extraInfo": ""
                    }
                ]
            },
            {
                "id": "00000000-0000-0000-0000-000000000000",
                "pol": "ESVLC",
                "polServiceType": "",
                "pod": "BRPEC",
                "podServiceType": "",
                "startDate": "2022-01-01T00:00:00",
                "endDate": "2023-08-31T00:00:00",
                "timeInTransit": 24,
                "via": null,
                "containerType": 3,
                "costs": [
                    {
                        "commodity": null,
                        "chargeType": 0,
                        "chargeName": "ERS",
                        "chargeDescription": "Equipment Repositionning Surcharge",
                        "amount": 30000,
                        "currency": "EUR",
                        "chargeUnit": 0,
                        "criteria": null,
                        "extraInfo": ""
                    },
                    {
                        "commodity": null,
                        "chargeType": 1,
                        "chargeName": "ALF",
                        "chargeDescription": "Agency Logistic fee",
                        "amount": 1000,
                        "currency": "EUR",
                        "chargeUnit": 0,
                        "criteria": null,
                        "extraInfo": ""
                    },
                    {
                        "commodity": null,
                        "chargeType": 1,
                        "chargeName": "VGM",
                        "chargeDescription": "Verified Gross Mass",
                        "amount": 1000,
                        "currency": "EUR",
                        "chargeUnit": 0,
                        "criteria": null,
                        "extraInfo": ""
                    },
                    {
                        "commodity": null,
                        "chargeType": 0,
                        "chargeName": "PAL",
                        "chargeDescription": "Port additionals",
                        "amount": 5000,
                        "currency": "EUR",
                        "chargeUnit": 0,
                        "criteria": null,
                        "extraInfo": ""
                    },
                    {
                        "commodity": null,
                        "chargeType": 3,
                        "chargeName": "DOC",
                        "chargeDescription": "Documentation Fee",
                        "amount": 5000,
                        "currency": "EUR",
                        "chargeUnit": 0,
                        "criteria": null,
                        "extraInfo": ""
                    },
                    {
                        "commodity": null,
                        "chargeType": 1,
                        "chargeName": "THC",
                        "chargeDescription": "Terminal handling charge",
                        "amount": 23500,
                        "currency": "EUR",
                        "chargeUnit": 0,
                        "criteria": null,
                        "extraInfo": ""
                    },
                    {
                        "commodity": null,
                        "chargeType": 0,
                        "chargeName": "PSS",
                        "chargeDescription": "Peak Season Surcharge",
                        "amount": 60000,
                        "currency": "EUR",
                        "chargeUnit": 0,
                        "criteria": null,
                        "extraInfo": ""
                    },
                    {
                        "commodity": null,
                        "chargeType": 1,
                        "chargeName": "CSS",
                        "chargeDescription": "Carrier security surcharge (Carrier ISPS)",
                        "amount": 900,
                        "currency": "EUR",
                        "chargeUnit": 0,
                        "criteria": null,
                        "extraInfo": ""
                    },
                    {
                        "commodity": null,
                        "chargeType": 0,
                        "chargeName": "BAF",
                        "chargeDescription": "Bunker ajustement factor",
                        "amount": 31600,
                        "currency": "EUR",
                        "chargeUnit": 0,
                        "criteria": null,
                        "extraInfo": ""
                    },
                    {
                        "commodity": null,
                        "chargeType": 0,
                        "chargeName": "FRT",
                        "chargeDescription": "Seafreight",
                        "amount": 150000,
                        "currency": "EUR",
                        "chargeUnit": 0,
                        "criteria": null,
                        "extraInfo": ""
                    }
                ]
            }            
        ]
    }
]

* Tariff model:

===========================   ====================   ===============================================
    Name                          Type                   Description
===========================   ====================   ===============================================
 Carrier                        String                 Carrier
 Name                           String                 Name 
 Type                           Int                    Tariff type (FCL/LCL)
 Rates	           	            List<Rate>             List of rates belonging to the tariff
===========================   ====================   ===============================================

* Tariff Rate model:

===========================   ====================   ===============================================
    Name                          Type                   Description
===========================   ====================   ===============================================
  POL                           String	               Origin Port
  POLServiceType                String?	               Origin service type
  POD           	            String	               Destination Port
  PODServiceType                String	               Destination service type
  StartDate                     DateTime               Starting date
  EndDate                       DateTime               Finishing date
  ContainerType                 DateTime               Finishing date
  Via                           DateTime               Finishing date
  TimeInTransit                 DateTime               Finishing date
  Costs                         List<Cost>             List of cost belonging to the rate 
===========================   ====================   ===============================================

* Tariff Cost model:

===========================   ====================   ===============================================
    Name                          Type                   Description
===========================   ====================   ===============================================
  Commodity                     String	               Commodity
  ChargeType                    Int?	                 Charge type
  ChargeName           	        String	               Charge name
  ChargeDescription             String	               Charge description
  Amount                        Long                   Cost price
  Currency                      String                 Currency
  ChargeUnit                    Int?                   Finishing date
  Criteria                      List<string>           List of criteria
  ExtraInfo                     String                 Extra info
===========================   ====================   ===============================================

.. autosummary::
   :toctree: generated
