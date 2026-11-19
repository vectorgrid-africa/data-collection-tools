Extreme Weather Event Form
==========================

**Form Code:** ``ENV-EXT`` | **Study Component:** Adult Vector Collection & Lab Sorting | **SOP Links:** SOP 2.1

The Extreme Weather Event Form is an event-triggered surveillance tool for documenting climate shocks (such as floods, cyclones, severe droughts, and heatwaves). It systematically records event severity, ecological and habitat alterations, community displacement, and disruptions to entomological surveillance networks.

Section 1: Node & Event Characterization
----------------------------------------

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
     - Sentinel Village Identifier
   * - ``event_id``
     - Text
     - Yes
     - Unique Extreme Event Identifier
   * - ``event_date``
     - Date
     - Yes
     - Date of event onset or recording
   * - ``collector_id``
     - Text
     - Yes
     - Field observer or team identifier

Section 2: Event Typology & Severity
------------------------------------

.. list-table::
   :widths: 25 20 20 35
   :header-rows: 1

   * - Field Name
     - Type
     - Required
     - Description / Choice List
   * - ``event_type``
     - Select One
     - Yes
     - 1=Flood, 2=Tropical Cyclone or Severe Storm, 3=Prolonged Drought, 4=Heatwave, 5=Cold Snap, 99=Other
   * - ``event_severity``
     - Select One
     - Yes
     - 1=Minor, 2=Moderate, 3=Severe, 4=Catastrophic
   * - ``event_duration_days``
     - Integer
     - Yes
     - Duration of extreme conditions in days
   * - ``warning_system_active``
     - Select One
     - Yes
     - Community early warning alert received (1=Yes, 0=No)

Section 3: Environmental & Aquatic Habitat Impacts
--------------------------------------------------

.. list-table::
   :widths: 25 20 20 35
   :header-rows: 1

   * - Field Name
     - Type
     - Required
     - Description / Choice List
   * - ``vegetation_loss``
     - Select One
     - Yes
     - Canopy or vegetation destroyed (1=Yes, 0=None)
   * - ``wetland_expansion``
     - Select One
     - Yes
     - Extensive new floodplains or standing water created (1=Yes, 0=None)
   * - ``soil_moisture_change``
     - Select One
     - Yes
     - 1=Extreme saturation or mud, 2=Extreme drought or cracked soil, 0=Normal
   * - ``other_environmental_disruption``
     - Text
     - No
     - Description of other ecological disturbances

Section 4: Human Behaviour & Household Displacement
---------------------------------------------------

.. list-table::
   :widths: 25 20 20 35
   :header-rows: 1

   * - Field Name
     - Type
     - Required
     - Description / Choice List
   * - ``population_displacement``
     - Select One
     - Yes
     - Residents displaced from dwellings (1=Yes, 0=None)
   * - ``displaced_persons_count``
     - Integer
     - No
     - Estimated count of displaced individuals
   * - ``temporary_shelter``
     - Select One
     - Yes
     - Communal camps or emergency shelters in use (1=Yes, 0=None)
   * - ``people_sleeping_outdoors``
     - Select One
     - Yes
     - Increased outdoor sleeping due to heat or house collapse (1=Yes, 0=None)
   * - ``livelihood_disrupted``
     - Select One
     - Yes
     - Farming, market, or schooling routines disrupted (1=Yes, 0=None)

Section 5: Surveillance Continuity & Trap Impact
------------------------------------------------

.. list-table::
   :widths: 25 20 20 35
   :header-rows: 1

   * - Field Name
     - Type
     - Required
     - Description / Choice List
   * - ``trapping_continuity``
     - Select One
     - Yes
     - 1=Trapping continuing normally, 2=Partial operation, 3=Full surveillance pause
   * - ``traps_affected_count``
     - Integer
     - Yes
     - Count of sentinel trap stations submerged, damaged, or unreachable
   * - ``continuity_remarks``
     - Text
     - No
     - Corrective measures and observatory recovery timeline
