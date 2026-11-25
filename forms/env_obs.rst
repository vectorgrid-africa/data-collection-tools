Environmental Observation Form
==============================

**Form Code:** ``ENV-OBS`` | **Form ID:** ``vg_env_obs`` | **Version:** ``2026112101`` | **Component:** Adult Mosquito Sampling | **SOP Links:** :doc:`SOP 2.1 <../sops/sop_2_1>`, :doc:`SOP 2.2 <../sops/sop_2_2>`

The Environmental Observation Form records the weather, temperature and humidity on an adult trapping night at a registered household: weather at trap start and end, rainfall, wind speed, the temperature and humidity data loggers used, and manual readings when a handheld meter is used or a logger fails.

How This Form Works
-------------------

* Select the district, then an active household from the ``households`` entity list. The record links to SPEC-SRT by Household ID and collection date.
* With automated loggers (``method`` = 1) there is one entry per logger (default 2). The manual temperature and humidity section is shown for a manual meter, where it is required, or when any logger download fails, where readings are optional.
* Place indoor loggers at trap height (about 1.5 m) near the bed, and outdoor loggers 1.5 m above the ground (1 m for BG-Sentinel), at least 1 m from dry ice.

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

Section 2: Sampling Event
-------------------------

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
     - Collection Date

       *Check:* ``value <= today()``

       *Default:* today

       *Hint:* Same date as the SPEC-SRT record
   * - ``collector_id``
     - Text
     - Yes
     - Collector ID (registered staff ID)

       *Hint:* Your registered staff ID, not your name
   * - ``method``
     - Select one
     - Yes
     - Measurement Method

       ``1`` = Automated logger; ``2`` = Manual meter

Section 3: Weather Observations
-------------------------------

.. list-table::
   :widths: 24 13 9 54
   :header-rows: 1

   * - Field Name
     - Type
     - Required
     - Question, Choices & Logic
   * - ``weather_start``
     - Select multiple
     - Yes
     - Weather at trap start

       ``rainy`` = Rainy; ``windy`` = Windy; ``cold`` = Cold; ``warm`` = Warm; ``none`` = None of these (calm, dry); ``other`` = Other

       *Check:* ``none cannot be combined with other options``

       *Hint:* Tick all that apply
   * - ``weather_start_other``
     - Text
     - Yes
     - Specify other weather

       *Shown if* ``weather_start includes other``
   * - ``weather_end``
     - Select multiple
     - Yes
     - Weather at trap end

       ``rainy`` = Rainy; ``windy`` = Windy; ``cold`` = Cold; ``warm`` = Warm; ``none`` = None of these (calm, dry); ``other`` = Other

       *Check:* ``none cannot be combined with other options``

       *Hint:* Tick all that apply
   * - ``weather_end_other``
     - Text
     - Yes
     - Specify other weather

       *Shown if* ``weather_end includes other``
   * - ``rainfall_24h``
     - Decimal
     - Yes
     - Rainfall - last 24 hours (mm)

       *Check:* ``range 0 to 500``
   * - ``rainfall_week``
     - Decimal
     - Yes
     - Rainfall - last week (mm)

       *Check:* ``range rainfall_24h to 2000``
   * - ``wind_speed``
     - Decimal
     - No
     - Wind speed (optional, m/s)

       *Check:* ``range 0 to 60``

       *Hint:* Instantaneous measured wind velocity in metres per second

Section 4: Data Loggers
-----------------------

.. list-table::
   :widths: 24 13 9 54
   :header-rows: 1

   * - Field Name
     - Type
     - Required
     - Question, Choices & Logic
   * - ``num_loggers``
     - Integer
     - Yes
     - Number of data loggers

       *Shown if* ``method = 1``

       *Check:* ``range 1 to 4``

Section 5: Temperature & Humidity Data Loggers
----------------------------------------------

Repeat group: one entry per data logger, repeated ``num_loggers`` times.

This section is shown only if ``method = 1``.

.. list-table::
   :widths: 24 13 9 54
   :header-rows: 1

   * - Field Name
     - Type
     - Required
     - Question, Choices & Logic
   * - ``logger_serial``
     - Text
     - Yes
     - Barcode / serial no.
   * - ``logger_placement``
     - Select one
     - Yes
     - Placement

       ``1`` = Indoor; ``2`` = Outdoor
   * - ``logger_height``
     - Decimal
     - Yes
     - Height (m)

       *Check:* ``range 0 to 10``
   * - ``logger_start``
     - Time
     - Yes
     - Start time
   * - ``logger_stop``
     - Time
     - Yes
     - Stop time
   * - ``logger_download``
     - Select one
     - Yes
     - Download status

       ``1`` = Pass; ``0`` = Fail

Section 6: Indoor & Outdoor Temperature & Humidity
--------------------------------------------------

This section is shown only if ``method = 2 or loggers_failed > 0``.

.. list-table::
   :widths: 24 13 9 54
   :header-rows: 1

   * - Field Name
     - Type
     - Required
     - Question, Choices & Logic
   * - ``loggers_failed``
     - Calculated
     - Auto
     - Number of loggers with download status Fail
   * - ``t_out_start``
     - Decimal
     - Conditional
     - At trap start

       *Check:* ``range -10 to 60``

       *Required if* ``method = 2`` (manual meter)
   * - ``t_out_min``
     - Decimal
     - Conditional
     - Overnight min (low)

       *Check:* ``range -10 to 60``

       *Required if* ``method = 2`` (manual meter)
   * - ``t_out_max``
     - Decimal
     - Conditional
     - Overnight max (high)

       *Check:* ``value >= -10 and value <= 60 and value >= t_out_min``

       *Required if* ``method = 2`` (manual meter)
   * - ``t_out_end``
     - Decimal
     - Conditional
     - At trap end

       *Check:* ``range -10 to 60``

       *Required if* ``method = 2`` (manual meter)
   * - ``t_in_start``
     - Decimal
     - Conditional
     - At trap start

       *Check:* ``range -10 to 60``

       *Required if* ``method = 2`` (manual meter)
   * - ``t_in_min``
     - Decimal
     - Conditional
     - Overnight min (low)

       *Check:* ``range -10 to 60``

       *Required if* ``method = 2`` (manual meter)
   * - ``t_in_max``
     - Decimal
     - Conditional
     - Overnight max (high)

       *Check:* ``value >= -10 and value <= 60 and value >= t_in_min``

       *Required if* ``method = 2`` (manual meter)
   * - ``t_in_end``
     - Decimal
     - Conditional
     - At trap end

       *Check:* ``range -10 to 60``

       *Required if* ``method = 2`` (manual meter)
   * - ``rh_out_start``
     - Decimal
     - Conditional
     - At trap start

       *Check:* ``range 0 to 100``

       *Required if* ``method = 2`` (manual meter)
   * - ``rh_out_min``
     - Decimal
     - Conditional
     - Overnight min (low)

       *Check:* ``range 0 to 100``

       *Required if* ``method = 2`` (manual meter)
   * - ``rh_out_max``
     - Decimal
     - Conditional
     - Overnight max (high)

       *Check:* ``value >= 0 and value <= 100 and value >= rh_out_min``

       *Required if* ``method = 2`` (manual meter)
   * - ``rh_out_end``
     - Decimal
     - Conditional
     - At trap end

       *Check:* ``range 0 to 100``

       *Required if* ``method = 2`` (manual meter)
   * - ``rh_in_start``
     - Decimal
     - Conditional
     - At trap start

       *Check:* ``range 0 to 100``

       *Required if* ``method = 2`` (manual meter)
   * - ``rh_in_min``
     - Decimal
     - Conditional
     - Overnight min (low)

       *Check:* ``range 0 to 100``

       *Required if* ``method = 2`` (manual meter)
   * - ``rh_in_max``
     - Decimal
     - Conditional
     - Overnight max (high)

       *Check:* ``value >= 0 and value <= 100 and value >= rh_in_min``

       *Required if* ``method = 2`` (manual meter)
   * - ``rh_in_end``
     - Decimal
     - Conditional
     - At trap end

       *Check:* ``range 0 to 100``

       *Required if* ``method = 2`` (manual meter)

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
     - Additional environmental notes

       *Hint:* Field observations (e.g. sudden weather change, spraying or smoke)
   * - ``full_name_signature``
     - Text
     - Yes
     - Full name (as signature)

       *Hint:* Type your full name
