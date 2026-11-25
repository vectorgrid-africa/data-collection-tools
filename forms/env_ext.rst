Extreme Weather Event Form
==========================

**Form Code:** ``ENV-EXT`` | **Form ID:** ``vg_env_ext`` | **Version:** ``2026112101`` | **Component:** Adult Mosquito Sampling | **SOP Links:** :doc:`SOP 2.1 <../sops/sop_2_1>`

The Extreme Weather Event Form is completed when an extreme weather event affects a node. It records where and when the event happened, its type and severity, its impact on the environment and on people, and its effect on trapping.

How This Form Works
-------------------

* The event location is asked in full, with a GPS point. Country is preset in the form.
* Event code = ``EVT`` - node - event start date - event type. It is the same for every assessment of one event, so repeat assessments can be linked.
* Event types: Earthquake, Extreme temperature, Flood, Storm / Cyclones, Wildfire, Drought, Other. Severity: Low, Moderate, Severe, Extreme.

Section 1: Location
-------------------

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
   * - ``country``
     - Calculated
     - Auto
     - Preset in the form to the node's country
   * - ``district``
     - Select one
     - Yes
     - District

       District list (set for each node)
   * - ``ward``
     - Select one
     - Yes
     - Ward

       Ward list (set for each node)
   * - ``event_village``
     - Select one
     - Yes
     - Event Village

       Village list (set for each node)
   * - ``event_gps``
     - GPS point
     - Yes
     - GPS coordinates

Section 2: Extreme Event Context & Recorder
-------------------------------------------

.. list-table::
   :widths: 24 13 9 54
   :header-rows: 1

   * - Field Name
     - Type
     - Required
     - Question, Choices & Logic
   * - ``assessment_date``
     - Date
     - Yes
     - Date of Event Assessment

       *Check:* ``value <= today()``

       *Default:* today
   * - ``collector_id``
     - Text
     - Yes
     - Observer ID (registered staff ID)

       *Hint:* Your registered staff ID, not your name
   * - ``assessment_timing``
     - Select one
     - Yes
     - Assessment Timing

       ``1`` = Immediate (within 48 hours); ``2`` = Post-Event

Section 3: Event Type & Severity
--------------------------------

.. list-table::
   :widths: 24 13 9 54
   :header-rows: 1

   * - Field Name
     - Type
     - Required
     - Question, Choices & Logic
   * - ``event_name``
     - Text
     - Yes
     - Extreme event official name

       *Hint:* Common or administrative name of the extreme weather event
   * - ``event_start_date``
     - Date
     - Yes
     - Event start date

       *Check:* ``value <= assessment_date``

       *Hint:* Enter the date the event began.
   * - ``event_type``
     - Select one
     - Yes
     - Extreme event type

       ``1`` = Earthquake; ``2`` = Extreme temperature; ``3`` = Flood; ``4`` = Storm / Cyclones; ``5`` = Wildfire; ``6`` = Drought; ``7`` = Other (specify)
   * - ``event_type_other``
     - Text
     - Yes
     - Specify other event type

       *Shown if* ``event_type = 7``
   * - ``event_severity``
     - Select one
     - Yes
     - Event severity scale

       ``1`` = Low; ``2`` = Moderate; ``3`` = Severe; ``4`` = Extreme
   * - ``event_code``
     - Calculated
     - Auto
     - Automatic event code: ``EVT`` - node - event start date (``YYYYMMDD``) - event type, e.g. ``EVT-<node>-20261120-Flood``. The same for every assessment of one event

Section 4: Impact on the Natural & Aquatic Environment
------------------------------------------------------

.. list-table::
   :widths: 24 13 9 54
   :header-rows: 1

   * - Field Name
     - Type
     - Required
     - Question, Choices & Logic
   * - ``vegetation_loss``
     - Select one
     - Yes
     - Vegetation loss / canopy damage

       ``1`` = Yes (significant forest / shrub / crop canopy destroyed); ``0`` = None
   * - ``wetland_expansion``
     - Select one
     - Yes
     - Wetland expansion / flooding

       ``1`` = Yes (extensive floodplains, ponds, or standing pools created); ``0`` = None
   * - ``soil_moisture``
     - Select one
     - Yes
     - Soil moisture change / drying

       ``1`` = Extreme saturation / mud; ``2`` = Extreme drought / cracked soil; ``0`` = Normal
   * - ``other_env_impact``
     - Select one
     - Yes
     - Other environmental disruption

       ``1`` = Yes; ``0`` = None
   * - ``other_env_impact_desc``
     - Text
     - Yes
     - Describe the impact

       *Shown if* ``other_env_impact = 1``

Section 5: Impact on Human Behaviour & Displacement
---------------------------------------------------

.. list-table::
   :widths: 24 13 9 54
   :header-rows: 1

   * - Field Name
     - Type
     - Required
     - Question, Choices & Logic
   * - ``displacement``
     - Select one
     - Yes
     - Population displacement

       ``1`` = Yes (residents displaced / evacuated from homes); ``0`` = None displaced
   * - ``displaced_count``
     - Integer
     - Yes
     - Number of people displaced

       *Shown if* ``displacement = 1``

       *Check:* ``value >= 1``
   * - ``temporary_shelter``
     - Select one
     - Yes
     - Temporary shelter use

       ``1`` = Yes (displaced camps, school halls, or communal tents occupied); ``0`` = None
   * - ``sleeping_outdoors``
     - Select one
     - Yes
     - People sleeping outdoors

       ``1`` = Yes (people slept outdoors because of the event); ``0`` = No
   * - ``livelihood_disrupted``
     - Select one
     - Yes
     - Livelihood & daily activities disrupted

       ``1`` = Yes (farming, school, markets, or cooking disrupted); ``0`` = Normal routines
   * - ``other_human_impact``
     - Select one
     - Yes
     - Other human behaviour impacts

       ``1`` = Yes; ``0`` = None
   * - ``other_human_impact_desc``
     - Text
     - Yes
     - Describe the impact

       *Shown if* ``other_human_impact = 1``

Section 6: Surveillance Continuity & Incident Log
-------------------------------------------------

.. list-table::
   :widths: 24 13 9 54
   :header-rows: 1

   * - Field Name
     - Type
     - Required
     - Question, Choices & Logic
   * - ``trapping_continuity``
     - Select one
     - Yes
     - Entomological trapping continuity

       ``1`` = Trapping continuing normally; ``2`` = Partial operation; ``3`` = Full pause
   * - ``traps_affected``
     - Integer
     - Yes
     - Sentinel trap stations affected

       *Check:* ``value >= 0``

       *Hint:* Number of sentinel trap stations submerged, damaged, or inaccessible.

Section 7: Signature
--------------------

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
     - Observer incident remarks
   * - ``full_name_signature``
     - Text
     - Yes
     - Full name (as signature)

       *Hint:* Type your full name
