Household Registration Form
===========================

**Form Code:** ``HH-REG`` | **Form ID:** ``vg_hh_reg`` | **Version:** ``2026112401`` | **Component:** Site & Household Selection | **SOP Links:** :doc:`SOP 1.1 <../sops/sop_1_1>`, :doc:`SOP 2.1 <../sops/sop_2_1>`

The Household Registration Form registers a selected household once, at baseline. It records the household's location and GPS point, the people who sleep in the house by age group and sex, house structure, windows and doors, bed nets, other features, nearby aquatic habitats, usual sleep and wake times, and the number of people sleeping in each room.

How This Form Works
-------------------

* **Entity:** Creates a new record in the ``households`` entity list. Properties written: ``node_code``, ``country``, ``household_id``, ``household_head``, ``household_type``, ``population_setting``, ``registration_date``, ``district``, ``ward``, ``village``, ``subvillage``, ``geometry``, ``total_occupants``, ``status``.
* The full location and GPS point are asked only on this form. Later forms ask for the district and then pick the household.
* Household ID is typed (no format check). Country is preset in the form.
* Entity label shown on other forms: the Household ID with its location.
* For later rounds, update the household with :doc:`hh_upd` instead of registering it again.

Section 1: Basic Information
----------------------------

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
     - Node Code

       *Saved to entity property* ``node_code``
   * - ``country``
     - Calculated
     - Auto
     - Preset in the form to the node's country

       *Saved to entity property* ``country``
   * - ``household_id``
     - Text
     - Yes
     - Household ID

       *Saved to entity property* ``household_id``
   * - ``household_head``
     - Text
     - Yes
     - Household head name

       *Saved to entity property* ``household_head``
   * - ``household_type``
     - Select one
     - Yes
     - Household type

       ``1`` = Monthly sentinel; ``2`` = Biannual supplementary

       *Saved to entity property* ``household_type``
   * - ``population_setting``
     - Select one
     - Yes
     - Population setting

       ``1`` = Urban; ``2`` = Rural

       *Saved to entity property* ``population_setting``
   * - ``registration_date``
     - Date
     - Yes
     - Date registered

       *Check:* ``value <= today()``

       *Default:* today

       *Saved to entity property* ``registration_date``
   * - ``collector_id``
     - Text
     - Yes
     - Collector ID (registered staff ID)

       *Hint:* Your registered staff ID, not your name

Section 2: Location
-------------------

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
     - District

       District list (set for each node)

       *Saved to entity property* ``district``
   * - ``ward``
     - Select one
     - Yes
     - Ward

       Ward list (set for each node)

       *Saved to entity property* ``ward``
   * - ``village``
     - Select one
     - Yes
     - Village

       Village list (set for each node)

       *Saved to entity property* ``village``
   * - ``subvillage``
     - Text
     - No
     - Subvillage

       *Saved to entity property* ``subvillage``
   * - ``gps_location``
     - GPS point
     - Yes
     - GPS Location

       *Hint:* Capture household coordinates (within 5 m)

       *Saved to entity property* ``geometry``

Section 3: Household Members
----------------------------

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

Section 4: House Structure
--------------------------

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

Section 5: Windows & Doors
--------------------------

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

Section 6: Bed Nets
-------------------

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

Section 7: Other Features
-------------------------

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

Section 8: Aquatic Habitat Nearby
---------------------------------

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

Section 9: Sleep Behaviour
--------------------------

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

Section 10: Sleeping Rooms
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

       *Check:* ``range 1 to 30``

Section 11: Room Details
------------------------

Repeat group: one entry per sleeping room, repeated ``num_rooms`` times.

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

Section 12: Signature
---------------------

.. list-table::
   :widths: 24 13 9 54
   :header-rows: 1

   * - Field Name
     - Type
     - Required
     - Question, Choices & Logic
   * - ``notes``
     - Text
     - No
     - Additional comments
   * - ``full_name_signature``
     - Text
     - Yes
     - Full name (as signature)

       *Hint:* Type your full name

Section 13: System Fields
-------------------------

.. list-table::
   :widths: 24 13 9 54
   :header-rows: 1

   * - Field Name
     - Type
     - Required
     - Question, Choices & Logic
   * - ``status``
     - Calculated
     - Auto
     - Fixed value: ``active``

       *Saved to entity property* ``status``

Built-in Checks & Warnings
--------------------------

The form shows a warning when entries do not add up:

* The age and sex counts do not add up to the total occupants (``hh_occupants``).
* More than one room is marked as the trap room (``trap_room``).
* The sleepers entered in the rooms do not add up to the total occupants (``hh_occupants``).

Household Status Update
-----------------------

For later sampling rounds, registered households are updated with the status update form instead of a new registration:

.. toctree::
   :maxdepth: 2

   hh_upd
