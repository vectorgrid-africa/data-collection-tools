Household Status Update Form
============================

**Form Code:** ``HH-UPD`` | **Form ID:** ``vg_hh_upd`` | **Version:** ``2026112201`` | **Sampling Activity:** Site & Household Selection | **SOP Links:** :doc:`SOP 1.1 <../sops/sop_1_1>`, :doc:`SOP 2.1 <../sops/sop_2_1>`

The Household Status Update Form records changes to a registered household at later sampling rounds. Part A records the new status and, for active households, who slept in the house last night. Part B lets the field worker pick only the sections that changed (location, household head, members, house structure, windows and doors, bed nets, other features, nearby aquatic habitat, sleep behaviour, room details). Only the selected sections are shown.

How This Form Works
-------------------

* **Entity:** Updates the selected record in the ``households`` entity list. Properties written: ``last_update_date``, ``status``, ``status_reason``, ``district``, ``ward``, ``village``, ``subvillage``, ``geometry``, ``household_head``, ``total_occupants``.
* Select the district, then the household from the ``households`` entity list. The form shows the Household ID, node and current status.
* Status values: ``active``, ``withdrew``, ``refused``, ``relocated`` and ``inactive``. A reason is required for any status other than ``active``. The last-night counts and Part B are shown only for active households.
* Sections that are not selected leave the existing household entity record unchanged, while selected sections overwrite the existing data upon submission.

Section 1: Household Selection
------------------------------

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

       *Hint:* Filter households by district
   * - ``household``
     - Select record
     - Yes
     - Select household

       Pick a record from the ``households`` entity list (filtered by district)

       *Hint:* Select the household to update
   * - ``node_code``
     - Calculated
     - Auto
     - Taken from the selected ``households`` record (property ``node_code``)
   * - ``household_id``
     - Calculated
     - Auto
     - Taken from the selected ``households`` record (property ``household_id``)
   * - ``previous_status``
     - Calculated
     - Auto
     - Taken from the selected ``households`` record (property ``status``)

Section 2: Status Update
------------------------

.. list-table::
   :widths: 24 13 9 54
   :header-rows: 1

   * - Field Name
     - Type
     - Required
     - Question, Choices & Logic
   * - ``update_date``
     - Date
     - Yes
     - Date of update

       *Check:* ``value <= today()``

       *Default:* today

       *Saved to entity property* ``last_update_date``
   * - ``surveillance_type``
     - Select one
     - Yes
     - Surveillance type

       ``1`` = Routine monthly; ``2`` = Biannual
   * - ``collector_id``
     - Text
     - Yes
     - Updated by
   * - ``new_status``
     - Select one
     - Yes
     - New status

       ``active`` = Active; ``withdrew`` = Dropped / Withdrawn; ``refused`` = Refused to continue; ``relocated`` = Relocated / Moved; ``inactive`` = Temporarily inactive

       *Saved to entity property* ``status``
   * - ``status_reason``
     - Text
     - Yes
     - Reason for status change

       *Shown if* ``new_status != active``

       *Hint:* Required if not active

       *Saved to entity property* ``status_reason``

Section 3: Occupants Sleeping Last Night
----------------------------------------

This section is shown only if ``new_status = active``.

.. list-table::
   :widths: 24 13 9 54
   :header-rows: 1

   * - Field Name
     - Type
     - Required
     - Question, Choices & Logic
   * - ``slept_total``
     - Integer
     - Yes
     - Total occupants sleeping last night

       *Check:* ``range 0 to 50``
   * - ``slept_males``
     - Integer
     - Yes
     - Males

       *Check:* ``value >= 0``
   * - ``slept_females``
     - Integer
     - Yes
     - Females

       *Check:* ``value >= 0 and slept_males + value = slept_total``

Section 4: Sections to Update (Part B)
--------------------------------------

.. list-table::
   :widths: 24 13 9 54
   :header-rows: 1

   * - Field Name
     - Type
     - Required
     - Question, Choices & Logic
   * - ``update_sections``
     - Select multiple
     - No
     - Select sections to update:

       ``location`` = Location; ``head`` = Household Head; ``members`` = Household Members; ``structure`` = House Structure; ``openings`` = Windows & Doors; ``bed_nets`` = Bed Nets; ``features`` = Other Features; ``aquatic`` = Nearby Aquatic Habitat; ``sleep`` = Sleep Behaviour; ``rooms`` = Room Details

       *Shown if* ``new_status = active``

       *Hint:* Check all that apply

Section 5: Location Information
-------------------------------

This section is shown only if ``update_sections includes location``.

.. list-table::
   :widths: 24 13 9 54
   :header-rows: 1

   * - Field Name
     - Type
     - Required
     - Question, Choices & Logic
   * - ``upd_district``
     - Select one
     - Yes
     - District

       District list (set for each node)

       *Saved to entity property* ``district``
   * - ``upd_ward``
     - Select one
     - Yes
     - Ward

       Ward list (set for each node)

       *Saved to entity property* ``ward``
   * - ``upd_village``
     - Select one
     - Yes
     - Village

       Village list (set for each node)

       *Saved to entity property* ``village``
   * - ``upd_subvillage``
     - Text
     - No
     - Subvillage

       *Saved to entity property* ``subvillage``
   * - ``upd_gps_location``
     - GPS point
     - Yes
     - GPS Location

       *Hint:* Capture household coordinates (within 5 m)

       *Saved to entity property* ``geometry``

Section 6: Household Head
-------------------------

This section is shown only if ``update_sections includes head``.

.. list-table::
   :widths: 24 13 9 54
   :header-rows: 1

   * - Field Name
     - Type
     - Required
     - Question, Choices & Logic
   * - ``household_head``
     - Text
     - Yes
     - Household head name

       *Saved to entity property* ``household_head``

Section 7: Household Members
----------------------------

This section is shown only if ``update_sections includes members``.

.. list-table::
   :widths: 24 13 9 54
   :header-rows: 1

   * - Field Name
     - Type
     - Required
     - Question, Choices & Logic
   * - ``hh_occupants``
     - Integer
     - Yes
     - Total occupants

       *Check:* ``range 1 to 50``

       *Saved to entity property* ``total_occupants``
   * - ``hh_m_under5``
     - Integer
     - No
     - Males under 5 years

       *Check:* ``value >= 0``
   * - ``hh_m_5_15``
     - Integer
     - No
     - Males 5-15 years

       *Check:* ``value >= 0``
   * - ``hh_m_over15``
     - Integer
     - No
     - Males above 15 years

       *Check:* ``value >= 0``
   * - ``hh_f_under5``
     - Integer
     - No
     - Females under 5 years

       *Check:* ``value >= 0``
   * - ``hh_f_5_15``
     - Integer
     - No
     - Females 5-15 years

       *Check:* ``value >= 0``
   * - ``hh_f_over15``
     - Integer
     - No
     - Females above 15 years

       *Check:* ``value >= 0``

Section 8: House Structure
--------------------------

This section is shown only if ``update_sections includes structure``.

.. list-table::
   :widths: 24 13 9 54
   :header-rows: 1

   * - Field Name
     - Type
     - Required
     - Question, Choices & Logic
   * - ``house_type``
     - Select one
     - Yes
     - House type

       ``1`` = Traditional; ``2`` = Modern; ``99`` = Other
   * - ``house_type_other``
     - Text
     - Yes
     - Specify other house type

       *Shown if* ``house_type = 99``
   * - ``total_rooms``
     - Integer
     - Yes
     - Total rooms in house

       *Check:* ``range 1 to 50``

       *Hint:* Count all rooms, including sleeping rooms
   * - ``eave_type``
     - Select one
     - Yes
     - Eave status

       ``1`` = Open; ``2`` = Partly screened/blocked; ``3`` = Fully screened; ``4`` = Fully blocked; ``99`` = Other
   * - ``eave_type_other``
     - Text
     - Yes
     - Specify other eave type

       *Shown if* ``eave_type = 99``
   * - ``roof_type``
     - Select one
     - Yes
     - Roof material

       ``1`` = Grass / Thatch; ``2`` = Metal / Iron sheets; ``3`` = Tiles; ``4`` = Concrete slab; ``99`` = Other
   * - ``roof_type_other``
     - Text
     - Yes
     - Specify other roof type

       *Shown if* ``roof_type = 99``
   * - ``has_ceiling``
     - Select one
     - Yes
     - Does house have ceiling?

       ``1`` = Yes; ``0`` = No
   * - ``wall_material``
     - Select one
     - Yes
     - Wall material

       ``1`` = Mud; ``2`` = Brick; ``3`` = Cement blocks; ``4`` = Thatch; ``99`` = Other
   * - ``wall_material_other``
     - Text
     - Yes
     - Specify other wall material

       *Shown if* ``wall_material = 99``
   * - ``wall_interior``
     - Select one
     - Yes
     - Interior wall surface

       ``1`` = Not plastered; ``2`` = Plastered with cement; ``3`` = Plastered with mud
   * - ``floor_type``
     - Select one
     - Yes
     - Floor type

       ``1`` = Earth / Mud; ``2`` = Cement; ``3`` = Tiles; ``99`` = Other
   * - ``floor_type_other``
     - Text
     - Yes
     - Specify other floor type

       *Shown if* ``floor_type = 99``

Section 9: Windows & Doors
--------------------------

This section is shown only if ``update_sections includes openings``.

.. list-table::
   :widths: 24 13 9 54
   :header-rows: 1

   * - Field Name
     - Type
     - Required
     - Question, Choices & Logic
   * - ``num_windows``
     - Integer
     - Yes
     - Total number of windows

       *Check:* ``range 0 to 50``
   * - ``window_status``
     - Select one
     - Yes
     - Window status

       ``1`` = Open (no screening); ``2`` = Screened; ``3`` = Blocked / Closed

       *Shown if* ``num_windows > 0``
   * - ``num_doors``
     - Integer
     - Yes
     - Number of entry doors

       *Check:* ``range 0 to 20``
   * - ``door_status``
     - Select one
     - Yes
     - Door status

       ``1`` = Open (no door); ``2`` = Door with gaps; ``3`` = Tightly fitted

Section 10: Bed Nets
--------------------

This section is shown only if ``update_sections includes bed_nets``.

.. list-table::
   :widths: 24 13 9 54
   :header-rows: 1

   * - Field Name
     - Type
     - Required
     - Question, Choices & Logic
   * - ``bed_nets``
     - Integer
     - Yes
     - How many bed nets are used in the house?

       *Check:* ``range 0 to 50``
   * - ``num_treated_nets``
     - Integer
     - Yes
     - How many are treated bed nets?

       *Shown if* ``bed_nets > 0``

       *Check:* ``value >= 0``

       *Hint:* ITN / LLIN
   * - ``num_untreated_nets``
     - Integer
     - Yes
     - How many are untreated bed nets?

       *Shown if* ``bed_nets > 0``

       *Check:* ``value >= 0``
   * - ``num_unidentified_nets``
     - Integer
     - Yes
     - How many are unidentified bed nets?

       *Shown if* ``bed_nets > 0``

       *Check:* ``num_treated_nets + num_untreated_nets + value = bed_nets``

Section 11: Other Features
--------------------------

This section is shown only if ``update_sections includes features``.

.. list-table::
   :widths: 24 13 9 54
   :header-rows: 1

   * - Field Name
     - Type
     - Required
     - Question, Choices & Logic
   * - ``latrine_inside``
     - Select one
     - Yes
     - Is latrine inside house?

       ``1`` = Yes; ``0`` = No
   * - ``latrine_distance``
     - Decimal
     - Yes
     - Distance to latrine (metres)

       *Shown if* ``latrine_inside = 0``

       *Check:* ``value >= 0``
   * - ``has_animal_shed``
     - Select one
     - Yes
     - Is there an animal shed?

       ``1`` = Yes; ``0`` = No
   * - ``animal_shed_distance``
     - Decimal
     - Yes
     - Distance to animal shed (m)

       *Shown if* ``has_animal_shed = 1``

       *Check:* ``value >= 0``
   * - ``chicken_inside``
     - Select one
     - Yes
     - Chickens kept inside at night?

       ``1`` = Yes; ``0`` = No
   * - ``livestock_near``
     - Select one
     - Yes
     - Livestock kept near the house?

       ``1`` = Yes; ``0`` = No
   * - ``livestock_types``
     - Select multiple
     - Yes
     - Livestock types

       ``cattle`` = Cattle; ``goats`` = Goats; ``chickens`` = Chickens; ``pigs`` = Pigs; ``other`` = Other

       *Shown if* ``livestock_near = 1``

       *Hint:* Select all that apply
   * - ``livestock_other``
     - Text
     - Yes
     - Specify other livestock

       *Shown if* ``livestock_types includes other``
   * - ``has_interventions``
     - Select one
     - Yes
     - Other mosquito interventions?

       ``1`` = Yes; ``0`` = No
   * - ``interventions``
     - Select multiple
     - Yes
     - Interventions

       ``itn`` = ITN; ``irs`` = IRS; ``mda_ivermectin`` = MDA-Ivermectin; ``lsm`` = LSM; ``other`` = Other

       *Shown if* ``has_interventions = 1``

       *Hint:* Select all that apply
   * - ``interventions_other``
     - Text
     - Yes
     - Specify other intervention

       *Shown if* ``interventions includes other``
   * - ``land_use``
     - Select one
     - Yes
     - Land use activity near house

       ``1`` = Agriculture; ``2`` = Mining; ``3`` = Construction; ``99`` = Other
   * - ``land_use_other``
     - Text
     - Yes
     - Specify other land use

       *Shown if* ``land_use = 99``

Section 12: Aquatic Habitat Nearby
----------------------------------

This section is shown only if ``update_sections includes aquatic``.

.. list-table::
   :widths: 24 13 9 54
   :header-rows: 1

   * - Field Name
     - Type
     - Required
     - Question, Choices & Logic
   * - ``has_aquatic_habitat``
     - Select one
     - Yes
     - Mosquito aquatic habitat within 100m?

       ``1`` = Yes; ``0`` = No
   * - ``aquatic_habitat_type``
     - Select multiple
     - Yes
     - Type of aquatic habitat

       22 options, see :doc:`../codebooks`

       *Shown if* ``has_aquatic_habitat = 1``

       *Hint:* Select all that apply
   * - ``aquatic_habitat_other``
     - Text
     - Yes
     - Specify other habitat type

       *Shown if* ``aquatic_habitat_type includes 22``
   * - ``aquatic_habitat_distance``
     - Decimal
     - Yes
     - Distance to nearest habitat (m)

       *Shown if* ``has_aquatic_habitat = 1``

       *Check:* ``range 0 to 100``

Section 13: Sleep Behaviour
---------------------------

This section is shown only if ``update_sections includes sleep``.

.. list-table::
   :widths: 24 13 9 54
   :header-rows: 1

   * - Field Name
     - Type
     - Required
     - Question, Choices & Logic
   * - ``sleep_time``
     - Time
     - Yes
     - At what time do you usually sleep?
   * - ``wake_time``
     - Time
     - Yes
     - At what time do you usually wake up?

Section 14: Sleeping Rooms
--------------------------

.. list-table::
   :widths: 24 13 9 54
   :header-rows: 1

   * - Field Name
     - Type
     - Required
     - Question, Choices & Logic
   * - ``num_rooms``
     - Integer
     - Yes
     - Number of sleeping rooms

       *Shown if* ``update_sections includes rooms``

       *Check:* ``range 1 to 30``

Section 15: Room Details
------------------------

Repeat group: one entry per sleeping room, repeated ``num_rooms`` times.

This section is shown only if ``update_sections includes rooms and num_rooms is answered``.

.. list-table::
   :widths: 24 13 9 54
   :header-rows: 1

   * - Field Name
     - Type
     - Required
     - Question, Choices & Logic
   * - ``room_code``
     - Text
     - Yes
     - Room code/name

       *Hint:* e.g., Room 1, Bedroom
   * - ``trap_room``
     - Select one
     - Yes
     - Is the trap placed in this room?

       ``1`` = Yes; ``0`` = No
   * - ``room_m_under5``
     - Integer
     - No
     - Males under 5 years

       *Check:* ``range 0 to 30``
   * - ``room_m_5_15``
     - Integer
     - No
     - Males 5-15 years

       *Check:* ``range 0 to 30``
   * - ``room_m_over15``
     - Integer
     - No
     - Males above 15 years

       *Check:* ``range 0 to 30``
   * - ``room_f_under5``
     - Integer
     - No
     - Females under 5 years

       *Check:* ``range 0 to 30``
   * - ``room_f_5_15``
     - Integer
     - No
     - Females 5-15 years

       *Check:* ``range 0 to 30``
   * - ``room_f_over15``
     - Integer
     - No
     - Females above 15 years

       *Check:* ``range 0 to 30``
   * - ``room_total``
     - Calculated
     - Auto
     - Calculated automatically (see the XLSForm)

Section 16: Signature
---------------------

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
     - General notes

Built-in Checks & Warnings
--------------------------

The form shows a warning when entries do not add up:

* The age and sex counts do not add up to the total occupants (``hh_occupants``).
* More than one room is marked as the trap room (``trap_room``).
