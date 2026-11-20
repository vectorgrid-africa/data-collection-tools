Human Behaviour Observation Form
================================

**Form Code:** ``HH-BEH`` | **Study Component:** Household Surveillance | **SOP Links:** SOP 2.1, SOP 2.2.1

The Human Behaviour Observation Form standardizes direct human-mosquito contact surveillance. It records biannual human sleeping patterns, indoor and outdoor exposure, net utilization across age groups, volunteer collection shifts (DN-Mini or HLC), and hourly mosquito biting catches.

Section 1: Node & Contact Sampling
----------------------------------

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
   * - ``household_id``
     - Text
     - Yes
     - Household ID (links to ``HH-REG``)
   * - ``visit_id``
     - Text
     - Yes
     - Unique Contact Sampling Visit Identifier
   * - ``survey_date``
     - Date
     - Yes
     - Date of survey
   * - ``collector_id``
     - Text
     - Yes
     - Field observer or team identifier
   * - ``sampling_method``
     - Select One
     - Yes
     - 1=DN-Mini, 2=HLC (Human Landing Catch)

Section 2: Household Visit & Interventions Between Rounds
---------------------------------------------------------

.. list-table::
   :widths: 25 20 20 35
   :header-rows: 1

   * - Field Name
     - Type
     - Required
     - Description / Choice List
   * - ``total_people_present``
     - Integer
     - Yes
     - Total people present and sleeping at the household last night
   * - ``functional_nets_count``
     - Integer
     - Yes
     - Total functional bed nets currently owned by household
   * - ``interventions_between_rounds``
     - Select One
     - Yes
     - 1=Yes (ITN, MDA-Ivermectin, LSM, IRS introduced), 0=None

Section 3: Outdoor Contact & Sleeping Patterns
----------------------------------------------

.. list-table::
   :widths: 25 20 20 35
   :header-rows: 1

   * - Field Name
     - Type
     - Required
     - Description / Choice List
   * - ``outdoor_shift``
     - Select One
     - Yes
     - Day, Night
   * - ``outdoor_volunteer_code``
     - Text
     - Yes
     - Assigned outdoor volunteer identifier
   * - ``outdoor_volunteer_gender``
     - Select One
     - Yes
     - 1=Female, 2=Male, 3=Transgender, 4=Prefer not to disclose
   * - ``outdoor_shift_start``
     - Time
     - Yes
     - Shift start time
   * - ``outdoor_shift_end``
     - Time
     - Yes
     - Shift end time
   * - ``outdoor_sleeping_under_net``
     - Integer
     - Yes
     - People sleeping under a bed net outside last night
   * - ``outdoor_awake_under_net``
     - Integer
     - Yes
     - People awake under a bed net outside last night
   * - ``outdoor_sleeping_no_net_total``
     - Integer
     - Yes
     - Total people sleeping outdoors without a net
   * - ``outdoor_sleeping_no_net_u5``
     - Integer
     - Yes
     - Children under 5 years sleeping outdoors without a net

Section 4: Indoor Contact & Sleeping Patterns
---------------------------------------------

.. list-table::
   :widths: 25 20 20 35
   :header-rows: 1

   * - Field Name
     - Type
     - Required
     - Description / Choice List
   * - ``indoor_shift``
     - Select One
     - Yes
     - Day, Night
   * - ``indoor_volunteer_code``
     - Text
     - Yes
     - Assigned indoor volunteer identifier
   * - ``indoor_volunteer_gender``
     - Select One
     - Yes
     - 1=Female, 2=Male, 3=Transgender, 4=Prefer not to disclose
   * - ``indoor_shift_start``
     - Time
     - Yes
     - Shift start time
   * - ``indoor_shift_end``
     - Time
     - Yes
     - Shift end time
   * - ``indoor_sleeping_under_net``
     - Integer
     - Yes
     - People sleeping under a bed net indoors last night
   * - ``indoor_awake_under_net``
     - Integer
     - Yes
     - People awake under a bed net indoors last night
   * - ``indoor_no_net_total``
     - Integer
     - Yes
     - Total people indoors without a bed net (awake or asleep)
   * - ``indoor_no_net_u5``
     - Integer
     - Yes
     - Children under 5 years indoors without a net

Section 5: Hourly Observation Roster
------------------------------------

A dynamic repeating group recording each collection hour (Day shift 06:00 to 18:00, Night shift 18:00 to 06:00):

- **Hour Start Time:** Sampling hour start timestamp.
- **Location:** Indoor or Outdoor.
- **Shift:** Day or Night.
- **Volunteer Code:** Assigned volunteer identifier.
- **Cup ID:** Pre-labeled collection cup barcode or ID.
- **Observation Status:** Complete, Partial, or Missed.
- **Mosquito Count:** Observed mosquito count (including zero).
- **Interruption Log:** Recorded exit time, return time, and interruption reason.
