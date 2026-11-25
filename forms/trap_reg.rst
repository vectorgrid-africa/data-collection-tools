Trap Registration Form
======================

**Form Code:** ``TRAP-REG`` | **Form ID:** ``vg_trap_reg`` | **Version:** ``2026112101`` | **Component:** Adult Mosquito Sampling | **SOP Links:** :doc:`SOP 2.2 <../sops/sop_2_2>`, :doc:`SOP 2.3 <../sops/sop_2_2>`

The Trap Registration Form registers one trap per submission: the collection method, CO\ :sub:`2` bait (CDC light traps only), indoor or outdoor placement, and the household or outdoor site where the trap is placed.

How This Form Works
-------------------

* **Entity:** Creates a new record in the ``traps`` entity list. Properties written: ``registration_date``, ``node_code``, ``district``, ``method``, ``co2_bait``, ``indoor_outdoor``, ``outdoor_context``, ``household_id``, ``site_id``, ``geometry``, ``trap_id``, ``status``.
* Indoor traps, and outdoor traps within 10 m of a house, are linked to a household picked from the ``households`` entity list. Traps at another outdoor site get a typed Site ID and a GPS point.
* Trap ID is made automatically: household ID (or site ID) - method - ``IN`` / ``OUT``, for example ``HH001-CDC-IN``.
* Method codes: ``DN`` Double Net, ``CDC`` CDC Light Trap, ``RB`` Resting Bucket, ``PKP`` Prokopack Aspirator, ``BGS`` BG Sentinel, ``other``.
* The household link saved on the trap (``household_id``) is the household record's entity ID, not the typed Household ID.

Section 1: Basic Information
----------------------------

.. list-table::
   :widths: 24 13 9 54
   :header-rows: 1

   * - Field Name
     - Type
     - Required
     - Question, Choices & Logic
   * - ``registration_date``
     - Date
     - Yes
     - Registration date

       *Check:* ``value <= today()``

       *Default:* today

       *Saved to entity property* ``registration_date``
   * - ``collector_id``
     - Text
     - Yes
     - Collector ID (registered staff ID)

       *Hint:* Your registered staff ID, not your name
   * - ``node_code``
     - Text
     - Yes
     - Node Code

       *Saved to entity property* ``node_code``
   * - ``district``
     - Select one
     - Yes
     - Select district

       District list (set for each node)

       *Hint:* Filter households by district

       *Saved to entity property* ``district``

Section 2: Trap Details
-----------------------

.. list-table::
   :widths: 24 13 9 54
   :header-rows: 1

   * - Field Name
     - Type
     - Required
     - Question, Choices & Logic
   * - ``method``
     - Select one
     - Yes
     - Collection method

       ``DN`` = Double Net; ``CDC`` = CDC Light Trap; ``RB`` = Resting Bucket; ``PKP`` = Prokopack Aspirator; ``BGS`` = BG Sentinel; ``other`` = Other

       *Saved to entity property* ``method``
   * - ``method_other``
     - Text
     - Yes
     - Specify other method

       *Shown if* ``method = other``
   * - ``co2_bait``
     - Select one
     - Yes
     - CO2 bait used?

       ``1`` = Yes; ``0`` = No

       *Shown if* ``method = CDC``

       *Hint:* CDC light trap only

       *Saved to entity property* ``co2_bait``
   * - ``indoor_outdoor``
     - Select one
     - Yes
     - Indoor or Outdoor?

       ``IN`` = Indoor; ``OUT`` = Outdoor

       *Saved to entity property* ``indoor_outdoor``
   * - ``outdoor_context``
     - Select one
     - Yes
     - Outdoor placement

       ``1`` = Within 10 m of the house (peridomestic); ``2`` = Other outdoor site

       *Shown if* ``indoor_outdoor = OUT``

       *Saved to entity property* ``outdoor_context``

Section 3: Household Selection
------------------------------

This section is shown only if ``indoor_outdoor = IN or outdoor_context = 1``.

.. list-table::
   :widths: 24 13 9 54
   :header-rows: 1

   * - Field Name
     - Type
     - Required
     - Question, Choices & Logic
   * - ``household``
     - Select record
     - Yes
     - Select household

       Pick a record from the ``households`` entity list (filtered by district)

       *Hint:* The household where the trap is placed

       *Saved to entity property* ``household_id``

Section 4: Collection Site
--------------------------

This section is shown only if ``indoor_outdoor = OUT and outdoor_context = 2``.

.. list-table::
   :widths: 24 13 9 54
   :header-rows: 1

   * - Field Name
     - Type
     - Required
     - Question, Choices & Logic
   * - ``site_id``
     - Text
     - Yes
     - Site ID

       *Saved to entity property* ``site_id``
   * - ``site_gps``
     - GPS point
     - Yes
     - GPS Location

       *Hint:* Capture site coordinates (within 5 m)

       *Saved to entity property* ``geometry``

Section 5: Placement
--------------------

.. list-table::
   :widths: 24 13 9 54
   :header-rows: 1

   * - Field Name
     - Type
     - Required
     - Question, Choices & Logic
   * - ``hardware_serial``
     - Text
     - No
     - Serial / barcode
   * - ``placement_notes``
     - Text
     - No
     - Placement notes

Section 6: Trap ID
------------------

.. list-table::
   :widths: 24 13 9 54
   :header-rows: 1

   * - Field Name
     - Type
     - Required
     - Question, Choices & Logic
   * - ``trap_id``
     - Calculated
     - Auto
     - Automatic Trap ID: household ID (or site ID) - method - ``IN``/``OUT``, e.g. ``HH001-CDC-IN``

       *Saved to entity property* ``trap_id``
   * - ``status``
     - Calculated
     - Auto
     - Fixed value: ``active``

       *Saved to entity property* ``status``

Section 7: Signature
--------------------

.. list-table::
   :widths: 24 13 9 54
   :header-rows: 1

   * - Field Name
     - Type
     - Required
     - Question, Choices & Logic
   * - ``full_name_signature``
     - Text
     - Yes
     - Full name (as signature)

       *Hint:* Type your full name
   * - ``notes``
     - Text
     - No
     - Additional notes

Trap Status Update
------------------

For later operational rounds, trap status changes (maintenance, malfunction, retirement) are recorded with the update form:

.. toctree::
   :maxdepth: 2

   trap_upd
