Trap Registration Form
======================

**Form Code:** ``TRAP-REG`` | **Study Component:** Adult Vector Collection & Lab Sorting

The Trap Registration Form registers fixed and mobile trap deployments, recording trapping methods, bait types, and microhabitat placement references.

Section 1: Node & Location Metadata
-----------------------------------

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
   * - ``country``
     - Text
     - Yes
     - Country of surveillance
   * - ``province``
     - Text
     - No
     - Province or Region
   * - ``district``
     - Text
     - No
     - District
   * - ``locality``
     - Text
     - No
     - Locality
   * - ``village_name``
     - Text
     - Yes
     - Village Name
   * - ``village_id``
     - Text
     - Yes
     - Standard Village ID
   * - ``registration_date``
     - Date
     - Yes
     - Registration Date
   * - ``collector_id``
     - Text
     - Yes
     - Registrar or Team ID

Section 2: Trap Deployment Ledger
---------------------------------

Repeat group recorded for each registered trap deployment:

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - Field
     - Label
     - Type
     - Valid Codes
     - Notes
   * - ``trap_id``
     - Trap Identifier
     - Text
     - ``Node-Village-T01``
     - Primary key for trap
   * - ``trap_method``
     - Trapping Method
     - Select One
     - 1 to 6
     - 1=DN, 2=CDC, 3=RB, 4=PKP, 5=BGS, 6=Other
   * - ``co2_bait``
     - CO₂ Bait Used
     - Select One
     - 1=Yes, 0=No
     - For CDC light traps
   * - ``trap_location``
     - Placement
     - Select One
     - 1=Indoor, 2=Outdoor
     - Broad location category
   * - ``outdoor_context``
     - Outdoor Context
     - Select One
     - 1=Within 10m, 2=Other
     - Required if outdoor
   * - ``placement_ref``
     - Household / Site Ref
     - Text
     - Household ID or GPS
     - Links trap to house
   * - ``hardware_serial``
     - Serial / Barcode
     - Text
     - Device serial
     - Hardware tracking
   * - ``placement_notes``
     - Microhabitat Notes
     - Text
     - Descriptive text
     - Vegetation or shade notes
