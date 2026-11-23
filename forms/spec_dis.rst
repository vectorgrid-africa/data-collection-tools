Mosquito Dissection & Parity Form
=================================

**Form Code:** ``SPEC-DIS`` | **Form ID:** ``vg_spec_dis`` | **Version:** ``2026112201`` | **Component:** Adult Mosquito Sampling | **SOP Links:** SOP 1.1.1, :doc:`SOP 2.4 <../sops/sop_2_4>`

The Mosquito Dissection and Parity Form records fresh dissections of female *Anopheles* from one collection. For each specimen it records midgut content, spermatheca (insemination), parity, Christophers egg stage, sac stage, maximum dilatations, wing length and condition, and it calculates the parity rate.

How This Form Works
-------------------

* Pick the source the same way as SPEC-SRT (district, household, active trap), or type the source vial ID for adults reared from larvae. With the collection date, the form rebuilds the same Collection ID as SPEC-SRT, so the ID is not typed.
* Specimen ID = Collection ID - species - specimen number. Parity rate = parous / (parous + nulliparous) x 100.
* Egg stage, sac stage, dilatations and wing length are required for each dissected specimen.

Section 1: Session Information
------------------------------

.. list-table::
   :widths: 24 13 9 54
   :header-rows: 1

   * - Field Name
     - Type
     - Required
     - Question, Choices & Logic
   * - ``dissection_date``
     - Date
     - Yes
     - Dissection date

       *Check:* ``value <= today()``

       *Default:* today
   * - ``start_time``
     - Time
     - Yes
     - Dissection start time
   * - ``technician``
     - Text
     - Yes
     - Technician

Section 2: Sample Selection
---------------------------

.. list-table::
   :widths: 24 13 9 54
   :header-rows: 1

   * - Field Name
     - Type
     - Required
     - Question, Choices & Logic
   * - ``from_trap``
     - Select one
     - Yes
     - Are the specimens from a trap catch?

       ``1`` = Yes; ``0`` = No
   * - ``district``
     - Select one
     - Yes
     - Select district

       District list (set for each node)

       *Shown if* ``from_trap = 1``

       *Hint:* Filter households and traps by district
   * - ``at_household``
     - Select one
     - Yes
     - Is the trap at a household?

       ``1`` = Yes; ``0`` = No

       *Shown if* ``from_trap = 1``

       *Hint:* No = outdoor site with no household

Section 3: Household Selection
------------------------------

This section is shown only if ``from_trap = 1 and at_household = 1``.

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

Section 4: Trap Selection
-------------------------

This section is shown only if ``from_trap = 1``.

.. list-table::
   :widths: 24 13 9 54
   :header-rows: 1

   * - Field Name
     - Type
     - Required
     - Question, Choices & Logic
   * - ``trap``
     - Select record
     - Yes
     - Select trap

       Pick a record from the ``traps`` entity list (active traps at the selected household, or outdoor-site traps in the district)
   * - ``trap_id``
     - Calculated
     - Auto
     - Taken from the selected ``traps`` record (property ``trap_id``)
   * - ``node_code``
     - Calculated
     - Auto
     - Taken from the selected ``traps`` record (property ``node_code``)

Section 5: Specimen Source
--------------------------

This section is shown only if ``from_trap = 0``.

.. list-table::
   :widths: 24 13 9 54
   :header-rows: 1

   * - Field Name
     - Type
     - Required
     - Question, Choices & Logic
   * - ``source_vial``
     - Text
     - Yes
     - Source vial / habitat ID

       *Hint:* Larval vial ID, as on SPEC-SRT
   * - ``source_household_site``
     - Text
     - Yes
     - Source household / site ID
   * - ``node_code_typed``
     - Text
     - Yes
     - Node Code

Section 6: Collection Date & Species
------------------------------------

.. list-table::
   :widths: 24 13 9 54
   :header-rows: 1

   * - Field Name
     - Type
     - Required
     - Question, Choices & Logic
   * - ``collection_date``
     - Date
     - Yes
     - Collection date

       *Check:* ``value <= dissection_date``

       *Hint:* When was the sample collected?
   * - ``collection_record_id``
     - Calculated
     - Auto
     - Automatic Collection ID: Trap ID (or source vial ID) - collection date. It matches the Collection ID on SPEC-SRT
   * - ``num_species``
     - Integer
     - Yes
     - How many species to dissect?

       *Check:* ``range 1 to 10``

       *Hint:* Enter the number of different species

Section 7: Species Dissection
-----------------------------

Repeat group: one entry per species dissected, repeated ``num_species`` times.

.. list-table::
   :widths: 24 13 9 54
   :header-rows: 1

   * - Field Name
     - Type
     - Required
     - Question, Choices & Logic
   * - ``species``
     - Select one
     - Yes
     - Select species

       Species list set for each node (see :doc:`../codebooks`)
   * - ``species_other``
     - Text
     - Yes
     - Specify other species

       *Shown if* ``species = other``
   * - ``num_specimens``
     - Integer
     - Yes
     - Number of specimens to dissect

       *Check:* ``range 1 to 100``

Repeat: Specimen Dissection
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Repeat group: one entry per specimen, repeated ``num_specimens`` times.

.. list-table::
   :widths: 24 13 9 54
   :header-rows: 1

   * - Field Name
     - Type
     - Required
     - Question, Choices & Logic
   * - ``specimen_id``
     - Calculated
     - Auto
     - Automatic Specimen ID: Collection ID - species - specimen number
   * - ``midgut``
     - Select one
     - Yes
     - Midgut content

       ``nb`` = No blood; ``fb`` = Fresh blood; ``bb`` = Brown blood
   * - ``spermatheca``
     - Select one
     - Yes
     - Spermatheca

       ``positive`` = Positive (sperm present); ``negative`` = Negative (no sperm)
   * - ``parity``
     - Select one
     - Yes
     - Parity status

       ``parous`` = Parous; ``nulliparous`` = Nulliparous
   * - ``egg_stage``
     - Select one
     - Yes
     - Egg stage (Christophers)

       ``stage1`` = I; ``stage2e`` = IIe; ``stage2`` = II; ``stage3`` = III; ``stage4`` = IV; ``stage5`` = V
   * - ``sac_stage``
     - Integer
     - Yes
     - Sac stage (0-7)

       *Check:* ``range 0 to 7``
   * - ``max_dilatation``
     - Integer
     - Yes
     - Max dilatation count (0-5)

       *Check:* ``range 0 to 5``
   * - ``wing_length``
     - Decimal
     - Yes
     - Wing length (mm)

       *Check:* ``value > 0 and value < 10``
   * - ``condition``
     - Select one
     - Yes
     - Specimen condition

       ``fresh`` = Fresh; ``dry`` = Dry
   * - ``sample_tube``
     - Text
     - No
     - Sample tube / plate well

       *Hint:* Barcode / Well ID
   * - ``specimen_notes``
     - Text
     - No
     - Notes

Section 8: Summary & Sign-off
-----------------------------

.. list-table::
   :widths: 24 13 9 54
   :header-rows: 1

   * - Field Name
     - Type
     - Required
     - Question, Choices & Logic
   * - ``total_dissected``
     - Calculated
     - Auto
     - Number of specimens dissected
   * - ``total_parous``
     - Calculated
     - Auto
     - Number of specimens with ``parity`` = ``parous``
   * - ``total_nulliparous``
     - Calculated
     - Auto
     - Number of specimens with ``parity`` = ``nulliparous``
   * - ``parity_rate``
     - Calculated
     - Auto
     - Parity rate (%) = parous / (parous + nulliparous) x 100, one decimal
   * - ``full_name_signature``
     - Text
     - Yes
     - Dissected by (full name)

       *Hint:* Enter your full name
   * - ``notes``
     - Text
     - No
     - Session notes
   * - ``dissection_id``
     - Calculated
     - Auto
     - Collection ID followed by ``-DISS``
