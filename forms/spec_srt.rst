Mosquito Collection & Sorting Form
===================================

**Form Code:** ``SPEC-SRT`` | **Study Component:** Adult Vector Collection & Lab Sorting | **SOP Links:** SOP 2.2, SOP 2.4

The Mosquito Collection and Sorting Form records trap retrieval timing, collection validity, morphological sorting counts across female abdominal stages and males, tube packaging, and biobank storage plate barcodes.

Section 1: Node & Retrieval Metadata
------------------------------------

.. list-table::
   :widths: 25 20 20 35
   :header-rows: 1

   * - Field Name
     - Type
     - Required
     - Description / Choice List
   * - ``node_code``
     - Text
     - Yes
     - Study Node Code
   * - ``village_id``
     - Text
     - Yes
     - Village Identifier
   * - ``trap_id``
     - Text
     - Optional
     - Trap ID from Trap Registration
   * - ``household_id``
     - Text
     - Optional
     - Household ID fallback if no trap ID
   * - ``deployment_id``
     - Text
     - Yes
     - Shared across BG Day/Night portions
   * - ``collection_date``
     - Date
     - Yes
     - Retrieval Date
   * - ``surveillance_round``
     - Select One
     - Yes
     - 1=Routine, 2=Biannual
   * - ``collector_id``
     - Text
     - Yes
     - Collector / Team ID
   * - ``collection_origin``
     - Select One
     - Yes
     - 1=Trap catch, 2=Adult reared from larvae
   * - ``source_vial_id``
     - Text
     - Conditional
     - Habitat vial ID if reared from larvae

Section 2: Collection Timing & Validity
---------------------------------------
- **Q01:** Actual trap operation start/end interval (24h dates and times).
- **Q02:** BG Portion (Day / Night).
- **Q03:** Did trap operate for the whole period? (1=Yes, 0=No).
- **Q04:** CDC Light status at retrieval (1=On, 0=Off).
- **Q05:** Collection Record ID (Unique identifier carried forward to the dissection form).
- **Q06:** Validity (1=Valid collection catch, 0=Invalid with reason).
- **Q07:** Mosquitoes Caught (1=Yes, 0=Zero catch) and Sorting Date.

Section 3: Morphological Identification & Physiological Matrix
--------------------------------------------------------------

.. list-table::
   :widths: 22 8 8 8 9 8 9 9 9 10 10
   :header-rows: 1

   * - Taxon
     - UF
     - PF
     - FD
     - Semi-gravid
     - GV
     - Total Females
     - Total Males
     - Total Caught
     - Tubes Packed
     - Discarded
   * - *Anopheles gambiae s.l.*
     - Count
     - Count
     - Count
     - Count
     - Count
     - Calc.
     - Count
     - Calc.
     - Count
     - Count
   * - *Anopheles funestus group*
     - Count
     - Count
     - Count
     - Count
     - Count
     - Calc.
     - Count
     - Calc.
     - Count
     - Count
   * - *Other Anopheline*
     - Count
     - Count
     - Count
     - Count
     - Count
     - Calc.
     - Count
     - Calc.
     - Count
     - Count
   * - *Culicines*
     - Count
     - Count
     - Count
     - Count
     - Count
     - Calc.
     - Count
     - Calc.
     - Count
     - Count

Section 4: Packaging, Dissection & Storage (SOP 2.4)
----------------------------------------------------
- **Q08:** Non-mosquito bycatch count (moths, beetles discarded).
- **Q09:** Anopheles fresh dissection (1=Yes transferred for dissection, 0=No).
- **Q10:** Packing type (1=Pool, 2=Individual).
- **Q11:** Storage Box / Plate Barcode (for example, ``TZ01 0001``).
- **Q12:** Well / position allocation (From: well to To: well).
- **Q13:** Specimen register or plate map ID.
