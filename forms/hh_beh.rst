Human Behaviour Observation Form
================================

**Form Code:** ``HH-BEH`` | **Form ID:** ``vg_hh_beh`` | **Version:** ``2026112101`` | **Component:** Adult Mosquito Sampling | **SOP Links:** :doc:`SOP 2.1 <../sops/sop_2_1>`, :doc:`SOP 2.2.1 <../sops/sop_2_2>`

The Human Behaviour Observation Form records biannual human-mosquito contact sampling at a registered household: the people present and their bed net use indoors and outdoors last night, interventions introduced between rounds, the indoor and outdoor volunteer shifts (DN-Mini or HLC), and an hourly log of collection cups, mosquito counts and interruptions.

How This Form Works
-------------------

* Select the district, then an active household from the ``households`` entity list. The node and location are filled in from the household record.
* Visit ID = Household ID - survey date (``YYYYMMDD``). Each hourly entry gets a Cup ID = Household ID - location - date - hour (``HHMM``) to write on the cup.
* The shift is worked out from the hour: day 06:00 to 18:00, night 18:00 to 06:00.
* Record each exit and return during an hour (heavy rain, breaks) as an interruption in that hour.

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

       Pick a record from the ``households`` entity list (filtered by district, active records only)
   * - ``node_code``
     - Calculated
     - Auto
     - Taken from the selected ``households`` record (property ``node_code``)
   * - ``household_id``
     - Calculated
     - Auto
     - Taken from the selected ``households`` record (property ``household_id``)
   * - ``hh_village``
     - Calculated
     - Auto
     - Taken from the selected ``households`` record (property ``village``)
   * - ``hh_ward``
     - Calculated
     - Auto
     - Taken from the selected ``households`` record (property ``ward``)

Section 2: Biannual Contact Sampling Event
------------------------------------------

.. list-table::
   :widths: 24 13 9 54
   :header-rows: 1

   * - Field Name
     - Type
     - Required
     - Question, Choices & Logic
   * - ``survey_date``
     - Date
     - Yes
     - Date of Survey

       *Check:* ``value <= today()``

       *Default:* today
   * - ``collector_id``
     - Text
     - Yes
     - Collector ID (registered staff ID)

       *Hint:* Your registered staff ID, not your name
   * - ``method``
     - Select one
     - Yes
     - Method

       ``1`` = DN-Mini; ``2`` = HLC
   * - ``visit_id``
     - Calculated
     - Auto
     - Automatic Visit ID: Household ID - survey date (``YYYYMMDD``)

Section 3: Household Visit & Interventions Between Rounds
---------------------------------------------------------

.. list-table::
   :widths: 24 13 9 54
   :header-rows: 1

   * - Field Name
     - Type
     - Required
     - Question, Choices & Logic
   * - ``people_present``
     - Integer
     - Yes
     - Total people present last night

       *Check:* ``range 0 to 100``

       *Hint:* Total people present and sleeping at the household last night
   * - ``functional_nets``
     - Integer
     - Yes
     - Total functional bed nets in house

       *Check:* ``range 0 to 50``

       *Hint:* Total functional bed nets currently available and owned by household
   * - ``has_interventions``
     - Select one
     - Yes
     - Interventions between biannual rounds

       ``1`` = Yes (ITN, MDA-Ivermectin, LSM, or IRS introduced); ``0`` = None
   * - ``interventions``
     - Select multiple
     - Yes
     - Interventions introduced

       ``itn`` = ITN; ``irs`` = IRS; ``mda_ivermectin`` = MDA-Ivermectin; ``lsm`` = LSM; ``other`` = Other

       *Shown if* ``has_interventions = 1``

       *Hint:* Select all that apply
   * - ``interventions_other``
     - Text
     - Yes
     - Specify other intervention

       *Shown if* ``interventions includes other``

Section 4: Outdoor Volunteer Shifts
-----------------------------------

Repeat group: one entry per outdoor volunteer shift, added as many times as needed.

.. list-table::
   :widths: 24 13 9 54
   :header-rows: 1

   * - Field Name
     - Type
     - Required
     - Question, Choices & Logic
   * - ``out_shift_type``
     - Select one
     - Yes
     - Shift

       ``day`` = Day; ``night`` = Night
   * - ``out_volunteer_code``
     - Text
     - Yes
     - Volunteer code
   * - ``out_gender``
     - Select one
     - Yes
     - Gender

       ``1`` = Female; ``2`` = Male; ``3`` = Transgender; ``4`` = I prefer not to disclose
   * - ``out_shift_date``
     - Date
     - Yes
     - Shift start date

       *Default:* same as ``survey_date``
   * - ``out_start_time``
     - Time
     - Yes
     - Start time
   * - ``out_end_time``
     - Time
     - Yes
     - End time

Section 5: Outdoor Contact & Sleeping Patterns
----------------------------------------------

.. list-table::
   :widths: 24 13 9 54
   :header-rows: 1

   * - Field Name
     - Type
     - Required
     - Question, Choices & Logic
   * - ``out_sleeping_net``
     - Integer
     - Yes
     - People sleeping under net outdoors

       *Check:* ``range 0 to 100``

       *Hint:* Number of people sleeping under a bed net outside the house last night
   * - ``out_awake_net``
     - Integer
     - Yes
     - People awake under net outdoors

       *Check:* ``range 0 to 100``

       *Hint:* Number of people awake under a bed net outside the house last night
   * - ``out_no_net_total``
     - Integer
     - Yes
     - People sleeping outdoors without net - total

       *Check:* ``range 0 to 100``

       *Hint:* Total people (and children <5y) sleeping outdoors with NO bed net
   * - ``out_no_net_under5``
     - Integer
     - Yes
     - People sleeping outdoors without net - children under 5

       *Check:* ``range 0 to out_no_net_total``

Section 6: Indoor Volunteer Shifts
----------------------------------

Repeat group: one entry per indoor volunteer shift, added as many times as needed.

.. list-table::
   :widths: 24 13 9 54
   :header-rows: 1

   * - Field Name
     - Type
     - Required
     - Question, Choices & Logic
   * - ``in_shift_type``
     - Select one
     - Yes
     - Shift

       ``day`` = Day; ``night`` = Night
   * - ``in_volunteer_code``
     - Text
     - Yes
     - Volunteer code
   * - ``in_gender``
     - Select one
     - Yes
     - Gender

       ``1`` = Female; ``2`` = Male; ``3`` = Transgender; ``4`` = I prefer not to disclose
   * - ``in_shift_date``
     - Date
     - Yes
     - Shift start date

       *Default:* same as ``survey_date``
   * - ``in_start_time``
     - Time
     - Yes
     - Start time
   * - ``in_end_time``
     - Time
     - Yes
     - End time

Section 7: Indoor Contact & Sleeping Patterns
---------------------------------------------

.. list-table::
   :widths: 24 13 9 54
   :header-rows: 1

   * - Field Name
     - Type
     - Required
     - Question, Choices & Logic
   * - ``in_sleeping_net``
     - Integer
     - Yes
     - People sleeping under net indoors

       *Check:* ``range 0 to 100``

       *Hint:* Number of people sleeping under a bed net inside the house last night
   * - ``in_awake_net``
     - Integer
     - Yes
     - People awake under net indoors

       *Check:* ``range 0 to 100``

       *Hint:* Number of people awake under a bed net inside the house last night
   * - ``in_no_net_total``
     - Integer
     - Yes
     - People indoors without a bed net - total

       *Check:* ``range 0 to 100``

       *Hint:* Count everyone indoors without a bed net last night, awake or asleep. Include children under five in the total and record their count separately.
   * - ``in_no_net_under5``
     - Integer
     - Yes
     - People indoors without a bed net - children under 5

       *Check:* ``range 0 to in_no_net_total``

Section 8: Hourly Observations
------------------------------

Repeat group: one entry per hour and location, added as many times as needed.

.. list-table::
   :widths: 24 13 9 54
   :header-rows: 1

   * - Field Name
     - Type
     - Required
     - Question, Choices & Logic
   * - ``hour_date``
     - Date
     - Yes
     - Hour start - date

       *Default:* same as ``survey_date``
   * - ``hour_time``
     - Time
     - Yes
     - Hour start - time
   * - ``hour_location``
     - Select one
     - Yes
     - Location

       ``indoor`` = Indoor; ``outdoor`` = Outdoor
   * - ``hour_shift``
     - Calculated
     - Auto
     - ``day`` (06:00 to 17:59) or ``night``, worked out from the hour start time
   * - ``hour_volunteer``
     - Text
     - Yes
     - Volunteer code
   * - ``cup_id``
     - Calculated
     - Auto
     - Automatic Cup ID: Household ID - location - date - hour (``HHMM``). Write it on the cup
   * - ``observation``
     - Select one
     - Yes
     - Observation

       ``complete`` = Complete; ``partial`` = Partial; ``missed`` = Missed
   * - ``mosquito_count``
     - Integer
     - Yes
     - Mosquito count

       *Shown if* ``observation != missed``

       *Check:* ``value >= 0``

       *Hint:* Enter the observed count, including 0.
   * - ``missed_reason``
     - Text
     - Yes
     - Reason the hour was missed

       *Shown if* ``observation = missed``
   * - ``num_interruptions``
     - Integer
     - Yes
     - Number of interruptions in this hour

       *Shown if* ``observation != missed``

       *Check:* ``range 0 to 10``

Repeat: Interruptions
~~~~~~~~~~~~~~~~~~~~~

Repeat group: one entry per interruption, repeated ``num_interruptions`` times.

This section is shown only if ``num_interruptions > 0``.

.. list-table::
   :widths: 24 13 9 54
   :header-rows: 1

   * - Field Name
     - Type
     - Required
     - Question, Choices & Logic
   * - ``exit_time``
     - Time
     - Yes
     - Exit time
   * - ``return_time``
     - Time
     - Yes
     - Return time
   * - ``interruption_reason``
     - Text
     - Yes
     - Reason

Section 9: Signature
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
     - Field observer notes
   * - ``full_name_signature``
     - Text
     - Yes
     - Full name (as signature)

       *Hint:* Type your full name

Built-in Checks & Warnings
--------------------------

The form shows a warning when entries do not add up:

* The people counted under and without nets, indoors and outdoors, are more than the people present last night (``people_present``).
