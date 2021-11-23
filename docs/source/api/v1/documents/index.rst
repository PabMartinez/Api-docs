===========================
Documents
===========================

Shipment Documents
----------------------
Retrieve a list of all shipment documents

**Example request**:

.. http:get:: /v1/documents/shipment/(guid: shipment_id) 


.. tabs::
    .. code-tab:: bash

        $ curl \
            -H "Content-Type: application/json" \
            -H "Authorization: Bearer <token>" \
            https://<env>.freightol.com/v1/documents/shipment/c7ef9573-59df-4da0-0983-08d95c96c463 


**Example response**:

.. sourcecode:: json

    [
        {
            "id": "74933d7c-5d07-4b94-7608-08d767961595",
            "shipmentId": "c7ef9573-59df-4da0-0983-08d95c96c463",
            "documentTemplateId": "52c1fde5-f40e-4f39-9965-80029d04c22f",
            "documentName": "Label",
            "isRequired": true,
            "validationStatus": "None",
            "observations": "Etiquetas del envio",
            "template": null,
            "templateExtension": null
        },
        {
            "id": "2c734e16-6180-4959-f585-08d95cd14e54",
            "shipmentId": "c7ef9573-59df-4da0-0983-08d95c96c463",
            "documentTemplateId": "74933d7c-5d07-4b94-7608-02d767963095",
            "documentName": "Test",
            "isRequired": false,
            "validationStatus": null,
            "observations": "Vuelve a subirlo #*Nueva Subida*",
            "template": null,
            "templateExtension": null
        },
        {
            "id": null",
            "shipmentId": "c7ef9573-59df-4da0-0983-08d95c96c463",
            "documentTemplateId": "4d6656ac-c178-474f-a54b-08d97811fda0",
            "documentName": "Tipo de documento 1",
            "isRequired": false,
            "validationStatus": null,
            "observations": "",
            "template": "JVBERi0xLjYNJeLjz9MNCjI0IDAgb2JqDTw8L0ZpbHRlci9GbGF0ZURlY29kZS9GaXJzdCA0L0xlbmd0aCAyMTYvT...",
            "templateExtension": "pdf"
        }
    ]

=====================   =========  ================================================================
Name                    Type        Description
=====================   =========  ================================================================
Id                      Guid        Shipment document ID
ShipmentId              Guid        Shipment ID
DocumentTemplateId      Guid?       DocumentTemplate ID 
DocumentName            String      Name of the document
IsRequired              String      Is required
ValidationStatus        String      Validation status
Observations            String      Observations
Template                String      Template file in base64 format
TemplateExtension       String	    Template file extension
=====================   =========  ================================================================


Download Shipment Document
--------------------------
Download a given shipment document

**Example request**:

.. http:get:: /v1/documents/shipment/(guid: shipment_id)/download


.. tabs::

    .. code-tab:: bash

        $ curl \
            -X POST \
            -H "Content-Type: application/json" \
            -H "Authorization: Bearer <token>" \
            https://<env>.freightol.com/v1/documents/shipment/c7ef9573-59df-4da0-0983-08d95c96c463/download
        
**Example response**:

.. sourcecode:: json

    {
        "id": "74933d7c-5d07-4b94-7608-08d767961595",
        "shipmentId": "c7ef9573-59df-4da0-0983-08d95c96c463",
        "documentName": "Label",
        "isRequired": true,
        "validationStatus": "None",
        "observations": "Etiquetas del envio",
        "extension": "pdf",
        "file": "JVBERi0xLjYNJeLjz9MNCjI0IDAgb2JqDTw8L0ZpbHRlci9GbGF0ZURlY29kZS9GaXJzdCA0L0xlbmd0aCAyMTYvT..."
    }
    
=====================   =========  ================================================================
Name                     Type      Description
=====================   =========  ================================================================
Id                      Guid        Shipment document ID
ShipmentId              Guid    	Shipment ID
DocumentName            String      Name of the document
IsRequired              String      True if document is required
ValidationStatus        String      Validation status
Observations            String      Comments relatives to shipment
File                    String      File content in base64 format.
Extension	  	        String	    File extension.
=====================   =========  ================================================================

Upload Shipment Document
------------------------
Upload an allow shipment document

**Example request**:

.. http:post:: /v1/documents/shipment/upload


.. tabs::

    .. code-tab:: bash

        $ curl \
            -X POST \
            -H "Content-Type: application/json" \
            -H "Authorization: Bearer <token>" \
            -d @body.json \
            https://<env>.freightol.com/v1/documents/shipment/c7ef9573-59df-4da0-0983-08d95c96c463/download 

The content of ``body.json`` is like,

.. sourcecode:: json

    {
        "shipmentId":"AB5F4325-FAB6-42BA-90C6-073FF2C1797D",
        "documentTemplateId":"74933d7c-5d07-4b94-7608-02d767963095",
        "documentName": "DocumentoPRUEBA",
        "extension": "pdf",
        "file": "JVBERi0xLjYNJeLjz9MNCjI0IDAgb2JqDTw8L0ZpbHRlci9GbGF0ZURlY29kZS9GaXJzdCA0L0xlbmd0aCAyMTYvT..." 
    }

=====================   =========  =============   ================================================================
Name                     Type      Constraint      Description
=====================   =========  =============   ================================================================
ShipmentId              Guid        Mandatory       Shipment ID
DocumentTemplateId      Guid        Mandatory       Document template ID
DocumentName            String      Mandatory       Document name
File                    String      Mandatory       File content in base64 format
Extension               String	    Mandatory       MIME type
Observations            String      Optional        Observations
=====================   =========  =============   ================================================================  
  
**Example response**:

.. sourcecode:: json

    {
        "success": true,
        "message": "Success"
    }


.. autosummary::
   :toctree: generated