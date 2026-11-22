Mosquito Collection & Sorting Form
==================================

**Form Code:** ``SPEC-SRT`` | **Form ID:** ``vg_spec_srt`` | **Version:** ``2026112201`` | **Sampling Activity:** Adult Mosquito Sampling | **SOP Links:** :doc:`SOP 2.2 <../sops/sop_2_2>`, :doc:`SOP 2.4 <../sops/sop_2_4>`

The Mosquito Collection and Sorting Form records one trap collection (or one batch of adults reared from larvae): collection timing and validity, then counts by species, sex and physiological status, how the mosquitoes were packed into tubes, bycatch, and how many *Anopheles* went to fresh dissection. A review screen summarises the record before it is signed.

How This Form Works
-------------------

* Part A: for a trap catch, select the district, say whether the trap is at a household, pick the household, then pick the active trap. The trap's method decides which CDC and BG-Sentinel questions are asked. For adults reared from larvae, type the source vial ID from ``HAB-SRV``.
* Collection ID = Trap ID (or source vial ID) - collection date, for example ``HH001-CDC-IN-20261120``. SPEC-DIS and SPEC-HND link to the collection through this ID. ENV-OBS links by Household ID and collection date.
* Part B is shown only when mosquitoes were caught. *Anopheles* females are counted by physiological status (UF, PF, FD, SG, GV) plus total males. Culicines are counted by sex only.
* Each tube gets an automatic label: Collection ID - species - sex - abdominal status (females only) - tube number. Storage box and plate barcodes use the country code, node code and plate or box number (for example ``TZDS 0001``).
* For 24-hour BG-Sentinel collections, the morning (night catch) and evening (day catch) bags are entered as separate records using the standard Collection ID pattern and their respective start and end times.

Section 1: Form Information
---------------------------

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

       *Check:* ``value <= today()``

       *Default:* today
   * - ``surveillance_type``
     - Select one
     - Yes
     - Surveillance type

       ``1`` = Routine monthly; ``2`` = Biannual
   * - ``collector_id``
     - Text
     - Yes
     - Collector name / ID
   * - ``origin``
     - Select one
     - Yes
     - Origin

       ``1`` = Trap catch; ``2`` = Adult reared from larvae
   * - ``source_vial``
     - Text
     - Yes
     - Source vial / habitat ID

       *Shown if* ``origin = 2``

       *Hint:* Larval vial ID from HAB-SRV
   * - ``household_site``
     - Text
     - No
     - Household / site ID

       *Shown if* ``origin = 2``

       *Hint:* Where the larvae were collected

Section 2: Household Selection
------------------------------

This section is shown only if ``origin = 1 and at_household = 1``.

.. list-table::
   :widths: 24 13 9 54
   :header-rows: 1

   * - Field Name
     - Type
     - Required
     - Question, Choices & Logic
   * - ``district``
     - Select one
     - Yes
     - Select district

       District list (set for each node)

       *Shown if* ``origin = 1``

       *Hint:* Filter households and traps by district
   * - ``at_household``
     - Select one
     - Yes
     - Is the trap at a household?

       ``1`` = Yes; ``0`` = No

       *Shown if* ``origin = 1``

       *Hint:* No = outdoor site with no household
   * - ``household``
     - Select record
     - Yes
     - Select household

       Pick a record from the ``households`` entity list (filtered by district)

       *Hint:* The household where the trap is placed

Section 3: Trap Selection
-------------------------

This section is shown only if ``origin = 1``.

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

       *Hint:* Select the trap being collected
   * - ``trap_id``
     - Calculated
     - Auto
     - Taken from the selected ``traps`` record (property ``trap_id``)
   * - ``trap_method``
     - Calculated
     - Auto
     - Taken from the selected ``traps`` record (property ``method``)
   * - ``node_code``
     - Calculated
     - Auto
     - Taken from the selected ``traps`` record (property ``node_code``)
   * - ``site_id``
     - Calculated
     - Auto
     - Taken from the selected ``traps`` record (property ``site_id``)

Section 4: Timing
-----------------

This section is shown only if ``origin = 1``.

.. list-table::
   :widths: 24 13 9 54
   :header-rows: 1

   * - Field Name
     - Type
     - Required
     - Question, Choices & Logic
   * - ``start_time``
     - Date and time
     - Yes
     - Start (date and time)
   * - ``end_time``
     - Date and time
     - Yes
     - End (date and time)

       *Check:* ``value > start_time``
   * - ``whole_period``
     - Select one
     - Yes
     - Did the trap operate for the whole period?

       ``1`` = Yes; ``0`` = No

       *Shown if* ``(trap_method = CDC or trap_method = BGS)``
   * - ``light_at_retrieval``
     - Select one
     - Yes
     - Light at retrieval

       ``1`` = On; ``0`` = Off

       *Shown if* ``trap_method = CDC``

Section 5: Collection Outcome
-----------------------------

.. list-table::
   :widths: 24 13 9 54
   :header-rows: 1

   * - Field Name
     - Type
     - Required
     - Question, Choices & Logic
   * - ``valid_catch``
     - Select one
     - Yes
     - Was collection valid?

       ``1`` = Yes; ``0`` = No
   * - ``invalid_reason``
     - Text
     - Yes
     - Reason if invalid

       *Shown if* ``valid_catch = 0``
   * - ``mosquitoes_caught``
     - Select one
     - Yes
     - Were mosquitoes caught?

       ``1`` = Yes; ``0`` = No

       *Shown if* ``valid_catch = 1``

Section 6: Collection ID & Sorting Date
---------------------------------------

.. list-table::
   :widths: 24 13 9 54
   :header-rows: 1

   * - Field Name
     - Type
     - Required
     - Question, Choices & Logic
   * - ``collection_id``
     - Calculated
     - Auto
     - Automatic Collection ID: Trap ID (or source vial ID) - collection date (``YYYYMMDD``), e.g. ``HH001-CDC-IN-20261120``
   * - ``sorting_date``
     - Date
     - Yes
     - Sorting date

       *Shown if* ``mosquitoes_caught = 1``

       *Check:* ``range collection_date to today()``

       *Default:* today

Section 7: *Anopheles* Species
------------------------------

Repeat group: one entry per Anopheles species found, added as many times as needed.

This section is shown only if ``mosquitoes_caught = 1``.

.. list-table::
   :widths: 24 13 9 54
   :header-rows: 1

   * - Field Name
     - Type
     - Required
     - Question, Choices & Logic
   * - ``an_species``
     - Select one
     - Yes
     - Anopheles specie

       Species list set for each node (see :doc:`../codebooks`)
   * - ``an_species_other``
     - Text
     - Yes
     - Specify other species

       *Shown if* ``an_species = other``
   * - ``an_female_unfed``
     - Integer
     - No
     - Females - Unfed (UF)

       *Check:* ``value >= 0``
   * - ``an_female_partly_fed``
     - Integer
     - No
     - Females - Partly fed (PF)

       *Check:* ``value >= 0``
   * - ``an_female_fed``
     - Integer
     - No
     - Females - Fully fed (FD)

       *Check:* ``value >= 0``
   * - ``an_female_semigravid``
     - Integer
     - No
     - Females - Semi-gravid (SG)

       *Check:* ``value >= 0``
   * - ``an_female_gravid``
     - Integer
     - No
     - Females - Gravid (GV)

       *Check:* ``value >= 0``
   * - ``an_male_total``
     - Integer
     - No
     - Males - Total

       *Check:* ``value >= 0``
   * - ``an_total``
     - Calculated
     - Auto
     - Males + females counted for this species
   * - ``an_num_batches``
     - Integer
     - Yes
     - Number of tubes

       *Shown if* ``an_total > 0``

       *Check:* ``range 0 to 100``
   * - ``an_discarded``
     - Integer
     - No
     - Number discarded

       *Shown if* ``an_total > 0``

       *Check:* ``value >= 0``

Repeat: Tube Details
~~~~~~~~~~~~~~~~~~~~

Repeat group: one entry per tube, repeated ``an_num_batches`` times.

This section is shown only if ``an_total > 0 and an_num_batches > 0``.

.. list-table::
   :widths: 24 13 9 54
   :header-rows: 1

   * - Field Name
     - Type
     - Required
     - Question, Choices & Logic
   * - ``an_sex``
     - Select one
     - Yes
     - Sex

       ``M`` = Male; ``F`` = Female
   * - ``an_abd``
     - Select one
     - Yes
     - Abdominal status

       ``UF`` = Unfed; ``PF`` = Partly fed; ``FD`` = Fully fed; ``SG`` = Semi-gravid; ``GV`` = Gravid

       *Shown if* ``an_sex = F``
   * - ``an_tube_label``
     - Calculated
     - Auto
     - Automatic tube label: Collection ID - species - sex - abdominal status (females) - tube number
   * - ``an_batch_count``
     - Integer
     - Yes
     - Mosquitoes in tube

       *Check:* ``value >= 1``
   * - ``an_sample_type``
     - Select one
     - Yes
     - Sample type

       ``pool`` = Pool (multiple); ``individual`` = Individual
   * - ``an_storage_box``
     - Text
     - Yes
     - Storage box / plate barcode

       *Hint:* Country + Node + Plate/Box number (SOP 2.4, e.g. TZDS 0001)
   * - ``an_box_position``
     - Text
     - Yes
     - Box / plate position

       *Hint:* e.g. 12 or A1
   * - ``an_batch_notes``
     - Text
     - No
     - Notes (optional)

Section 8: Culicine Species
---------------------------

Repeat group: one entry per Culicine species found, added as many times as needed.

This section is shown only if ``mosquitoes_caught = 1``.

.. list-table::
   :widths: 24 13 9 54
   :header-rows: 1

   * - Field Name
     - Type
     - Required
     - Question, Choices & Logic
   * - ``cul_species``
     - Select one
     - Yes
     - Culicine specie

       Species list set for each node (see :doc:`../codebooks`)
   * - ``cul_species_other``
     - Text
     - Yes
     - Specify other species

       *Shown if* ``cul_species = other``
   * - ``cul_male_total``
     - Integer
     - No
     - Males - Total

       *Check:* ``value >= 0``
   * - ``cul_female_total``
     - Integer
     - No
     - Females - Total

       *Check:* ``value >= 0``
   * - ``cul_total``
     - Calculated
     - Auto
     - Males + females counted for this species
   * - ``cul_num_batches``
     - Integer
     - Yes
     - Number of tubes

       *Shown if* ``cul_total > 0``

       *Check:* ``range 0 to 100``
   * - ``cul_discarded``
     - Integer
     - No
     - Number discarded

       *Shown if* ``cul_total > 0``

       *Check:* ``value >= 0``

Repeat: Tube Details
~~~~~~~~~~~~~~~~~~~~

Repeat group: one entry per tube, repeated ``cul_num_batches`` times.

This section is shown only if ``cul_total > 0 and cul_num_batches > 0``.

.. list-table::
   :widths: 24 13 9 54
   :header-rows: 1

   * - Field Name
     - Type
     - Required
     - Question, Choices & Logic
   * - ``cul_sex``
     - Select one
     - Yes
     - Sex

       ``M`` = Male; ``F`` = Female
   * - ``cul_abd``
     - Select one
     - Yes
     - Abdominal status

       ``UF`` = Unfed; ``PF`` = Partly fed; ``FD`` = Fully fed; ``SG`` = Semi-gravid; ``GV`` = Gravid

       *Shown if* ``cul_sex = F``
   * - ``cul_tube_label``
     - Calculated
     - Auto
     - Automatic tube label: Collection ID - species - sex - abdominal status (females) - tube number
   * - ``cul_batch_count``
     - Integer
     - Yes
     - Mosquitoes in tube

       *Check:* ``value >= 1``
   * - ``cul_sample_type``
     - Select one
     - Yes
     - Sample type

       ``pool`` = Pool (multiple); ``individual`` = Individual
   * - ``cul_storage_box``
     - Text
     - Yes
     - Storage box / plate barcode

       *Hint:* Country + Node + Plate/Box number (SOP 2.4, e.g. TZDS 0001)
   * - ``cul_box_position``
     - Text
     - Yes
     - Box / plate position

       *Hint:* e.g. 12 or A1
   * - ``cul_batch_notes``
     - Text
     - No
     - Notes (optional)

Section 9: Bycatch
------------------

This section is shown only if ``mosquitoes_caught = 1``.

.. list-table::
   :widths: 24 13 9 54
   :header-rows: 1

   * - Field Name
     - Type
     - Required
     - Question, Choices & Logic
   * - ``bycatch_count``
     - Integer
     - No
     - Number of bycatch

       *Check:* ``value >= 0``

Section 10: Dissection & Specimen Register
------------------------------------------

.. list-table::
   :widths: 24 13 9 54
   :header-rows: 1

   * - Field Name
     - Type
     - Required
     - Question, Choices & Logic
   * - ``summary_an_total``
     - Calculated
     - Auto
     - All *Anopheles* counted (all species)
   * - ``sum_an_female``
     - Calculated
     - Auto
     - All female *Anopheles* counted
   * - ``for_dissection``
     - Select one
     - Yes
     - Anopheles for fresh dissection (SPEC-DIS)?

       ``1`` = Yes; ``0`` = No

       *Shown if* ``summary_an_total > 0``
   * - ``dissection_qty``
     - Integer
     - Yes
     - Number transferred to SPEC-DIS

       *Shown if* ``for_dissection = 1``

       *Check:* ``range 1 to sum_an_female``
   * - ``sum_tubes``
     - Calculated
     - Auto
     - Number of tubes recorded (all species)
   * - ``register_id``
     - Text
     - Yes
     - Specimen register / plate map ID

       *Shown if* ``sum_tubes > 0``

       *Hint:* Record listing the specimen or pool IDs, positions and storage medium
   * - ``notes``
     - Text
     - No
     - General notes

Section 11: Review Before Submitting
------------------------------------

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
   * - ``full_name_signature``
     - Text
     - Yes
     - Full name (as signature)

       *Hint:* Type your full name

Built-in Checks & Warnings
--------------------------

The form shows a warning when entries do not add up:

* For an *Anopheles* species, the number counted (``an_total``) is not equal to the mosquitoes put in tubes plus the number discarded (``an_discarded``).
* For a Culicine species, the number counted (``cul_total``) is not equal to the mosquitoes put in tubes plus the number discarded (``cul_discarded``).
* On the review screen: one or more species entries have that mismatch.
* On the review screen: mosquitoes were reported caught but no counts were entered.
