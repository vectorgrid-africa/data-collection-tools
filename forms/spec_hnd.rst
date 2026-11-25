Sample Handover & Custody Form
==============================

**Form Code:** ``SPEC-HND`` | **Form ID:** ``vg_spec_hnd`` | **Version:** ``2026112101`` | **Component:** Adult Mosquito Sampling and Larval Sampling | **SOP Links:** :doc:`SOP 2.4 <../sops/sop_2_4>`

The Sample Handover and Custody Form documents one shipping container sent from a field node to a laboratory: routing and dispatch, cold-chain checks, a manifest of the plates, boxes or batches inside, and the three chain-of-custody sign-offs (field team, courier and receiving laboratory).

How This Form Works
-------------------

* Dispatch fields are required. Receipt fields (receipt temperature, breach indicator, physical integrity, intake status, courier and laboratory sign-offs) are optional and are completed at the laboratory by editing the submission in ODK Central.
* Each manifest row links to a SPEC-SRT Collection ID or a HAB-SRV vial ID. Site, trap and collection date come from that record.
* The manifest's sampling method uses numeric codes (``1`` Double net to ``7`` Larval), not the letter codes used in TRAP-REG.
* When using approved substitutes like DNA/RNA Shield or Trizol-LS, choose ``99`` (Other) and type the reagent name in ``medium_other``.

Section 1: Shipment Details
---------------------------

.. list-table::
   :widths: 24 13 9 54
   :header-rows: 1

   * - Field Name
     - Type
     - Required
     - Question, Choices & Logic
   * - ``node_code``
     - Text
     - Yes
     - Originating Node Code
   * - ``country``
     - Calculated
     - Auto
     - Preset in the form to the node's country
   * - ``destination_lab``
     - Text
     - Yes
     - Destination Laboratory
   * - ``waybill_id``
     - Text
     - Yes
     - Courier / Transport Waybill ID

Section 2: Shipment Batch & Dispatch Event
------------------------------------------

.. list-table::
   :widths: 24 13 9 54
   :header-rows: 1

   * - Field Name
     - Type
     - Required
     - Question, Choices & Logic
   * - ``dispatch_date``
     - Date
     - Yes
     - Dispatch Date

       *Check:* ``value <= today()``

       *Default:* today
   * - ``dispatch_time``
     - Time
     - Yes
     - Dispatch Time
   * - ``officer_id``
     - Text
     - Yes
     - Dispatcher ID (registered staff ID)

       *Hint:* Your registered staff ID, not your name
   * - ``container_id``
     - Text
     - Yes
     - Shipping Container ID

Section 3: Cold Chain Checks & Temperature
------------------------------------------

.. list-table::
   :widths: 24 13 9 54
   :header-rows: 1

   * - Field Name
     - Type
     - Required
     - Question, Choices & Logic
   * - ``dispatch_temp``
     - Decimal
     - Yes
     - Dispatch temperature (field origin, °C)

       *Check:* ``range -100 to 50``

       *Hint:* Record cooler temperature at departure
   * - ``dispatch_initials``
     - Text
     - Yes
     - Initials
   * - ``receipt_temp``
     - Decimal
     - No
     - Lab receipt temperature (intake, °C)

       *Check:* ``range -100 to 50``

       *Hint:* Completed at the laboratory. Record the reading on arrival and assess it against the approved requirements for this shipment.
   * - ``receipt_initials``
     - Text
     - Conditional
     - Initials

       *Required if* ``receipt_temp is answered``
   * - ``cold_chain_breach``
     - Select one
     - No
     - Cold chain breach / thaw indicator

       ``1`` = No breach (intact); ``2`` = Breach / spike

       *Hint:* Completed at the laboratory. Flag if ice packs completely melted or indicator spiked
   * - ``logger_deployed``
     - Select one
     - Yes
     - Electronic logger deployed?

       ``1`` = Yes; ``0`` = No

       *Hint:* Verify continuous USB/BLE datalogger enclosed in shipper
   * - ``logger_id``
     - Text
     - Yes
     - Logger ID

       *Shown if* ``logger_deployed = 1``

Section 4: Manifest Rows
------------------------

.. list-table::
   :widths: 24 13 9 54
   :header-rows: 1

   * - Field Name
     - Type
     - Required
     - Question, Choices & Logic
   * - ``num_rows``
     - Integer
     - Yes
     - Number of manifest rows in this container

       *Check:* ``range 1 to 20``

Section 5: Specimen Manifest
----------------------------

Repeat group: one entry per manifest row, repeated ``num_rows`` times.

.. list-table::
   :widths: 24 13 9 54
   :header-rows: 1

   * - Field Name
     - Type
     - Required
     - Question, Choices & Logic
   * - ``batch_id``
     - Text
     - Yes
     - Plate / box barcode or batch ID
   * - ``record_id``
     - Text
     - Yes
     - Collection record ID (SPEC-SRT) or larval vial ID (HAB-SRV)

       *Hint:* SPEC-SRT: Trap ID-YYYYMMDD (a BG bag adds -D or -N), e.g. HH001-CDC-IN-20261120. HAB-SRV: the vial ID.
   * - ``sampling_method``
     - Select one
     - Yes
     - Sampling method

       ``1`` = Double net; ``2`` = CDC; ``3`` = Resting bucket; ``4`` = Prokopack; ``5`` = BG Sentinel; ``6`` = Other (write in); ``7`` = Larval
   * - ``sampling_method_other``
     - Text
     - Yes
     - Specify other sampling method

       *Shown if* ``sampling_method = 6``
   * - ``specimen_category``
     - Select one
     - Yes
     - Specimen category

       ``1`` = Anopheles female; ``2`` = Anopheles male; ``3`` = Culicine; ``4`` = Larval; ``5`` = Parts; ``99`` = Other taxa or category (write in)
   * - ``specimen_category_other``
     - Text
     - Yes
     - Specify other taxa or category

       *Shown if* ``specimen_category = 99``
   * - ``container_qty``
     - Text
     - Yes
     - Container and quantity

       *Hint:* e.g. 1 plate
   * - ``medium``
     - Select one
     - Yes
     - Medium at dispatch

       ``1`` = Ethanol; ``2`` = RNAlater; ``3`` = Silica; ``0`` = None; ``99`` = Other (write in)
   * - ``medium_other``
     - Text
     - Yes
     - Specify other medium

       *Shown if* ``medium = 99``
   * - ``storage_condition``
     - Text
     - Yes
     - Storage condition

       *Hint:* e.g. Chilled. Record frozen here.
   * - ``integrity``
     - Select one
     - No
     - Physical integrity

       ``1`` = Intact; ``2`` = Leak / damage

       *Hint:* Completed at the laboratory
   * - ``intake``
     - Select one
     - No
     - Lab intake status

       ``1`` = Accepted; ``2`` = Hold / reject

       *Hint:* Completed at the laboratory
   * - ``exception_reason``
     - Text
     - Conditional
     - Exception or intake reason

       *Hint:* Describe any leak / damage, or the reason for hold or rejection.

       *Required if* ``integrity = 2 or intake = 2``

Section 6: Shipment Totals
--------------------------

.. list-table::
   :widths: 24 13 9 54
   :header-rows: 1

   * - Field Name
     - Type
     - Required
     - Question, Choices & Logic
   * - ``total_containers``
     - Integer
     - Yes
     - Total containers in this shipment

       *Check:* ``value >= 1``

Section 7: Review Before Submitting
-----------------------------------

.. list-table::
   :widths: 24 13 9 54
   :header-rows: 1

   * - Field Name
     - Type
     - Required
     - Question, Choices & Logic
   * - ``summary_confirmed``
     - Select one
     - Yes
     - I have reviewed this summary and the data are correct

       ``1`` = Yes; ``0`` = No

       *Check:* ``value = 1``

       *Hint:* If anything is wrong, go back and correct it first

Section 8: Sign-off: Field Team
-------------------------------

.. list-table::
   :widths: 24 13 9 54
   :header-rows: 1

   * - Field Name
     - Type
     - Required
     - Question, Choices & Logic
   * - ``stage1_name``
     - Text
     - Yes
     - Full name & organisation
   * - ``stage1_signature``
     - Signature
     - Yes
     - Signature / seal
   * - ``stage1_datetime``
     - Date and time
     - Yes
     - Date & time

Section 9: Sign-off: Courier
----------------------------

.. list-table::
   :widths: 24 13 9 54
   :header-rows: 1

   * - Field Name
     - Type
     - Required
     - Question, Choices & Logic
   * - ``stage2_name``
     - Text
     - No
     - Full name & organisation
   * - ``stage2_signature``
     - Signature
     - No
     - Signature / seal
   * - ``stage2_datetime``
     - Date and time
     - No
     - Date & time

Section 10: Sign-off: Receiving Laboratory
------------------------------------------

.. list-table::
   :widths: 24 13 9 54
   :header-rows: 1

   * - Field Name
     - Type
     - Required
     - Question, Choices & Logic
   * - ``stage3_name``
     - Text
     - No
     - Full name & organisation
   * - ``stage3_signature``
     - Signature
     - No
     - Signature / seal
   * - ``stage3_datetime``
     - Date and time
     - No
     - Date & time
