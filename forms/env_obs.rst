Environmental Observation Form
==============================

**Form Code:** ``ENV-OBS`` | **Study Component:** Adult Vector Surveillance | **SOP Links:** SOP 2.1

The Environmental Observation Form captures meteorological conditions, indoor and outdoor microclimate parameters, and electronic data logger records on adult mosquito trapping nights. It links directly to ``HH-REG`` and ``SPEC-SRT`` using the Household ID and collection date.

Section 1: Node & Sampling Event
--------------------------------

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
   * - ``collection_date``
     - Date
     - Yes
     - Night of mosquito collection
   * - ``collector_id``
     - Text
     - Yes
     - Field technician or team identifier
   * - ``measurement_method``
     - Select One
     - Yes
     - 1=Automated Data Logger, 2=Manual Handheld Meter

Section 2: Weather Observations
-------------------------------

.. list-table::
   :widths: 25 20 20 35
   :header-rows: 1

   * - Field Name
     - Type
     - Required
     - Description / Choice List
   * - ``weather_start``
     - Select Multiple
     - Yes
     - Weather at trap start: Rainy, Windy, Cold, Warm, Calm and dry, Other
   * - ``weather_end``
     - Select Multiple
     - Yes
     - Weather at trap end: Rainy, Windy, Cold, Warm, Calm and dry, Other
   * - ``rainfall_24h``
     - Decimal
     - No
     - Measured rainfall in preceding 24 hours (mm)
   * - ``rainfall_week``
     - Decimal
     - No
     - Cumulative rainfall over past week (mm)
   * - ``wind_speed``
     - Decimal
     - No
     - Measured wind velocity in meters per second (m/s)

Section 3: Microclimate Measurements
------------------------------------

Recorded when using a handheld meter, or as a manual backup if electronic loggers fail:

.. list-table::
   :widths: 30 18 18 18 18
   :header-rows: 1

   * - Parameter
     - At Trap Start
     - Overnight Min
     - Overnight Max
     - At Trap End
   * - Outdoor Temperature (°C)
     - ``temp_out_start``
     - ``temp_out_min``
     - ``temp_out_max``
     - ``temp_out_end``
   * - Indoor Temperature (°C)
     - ``temp_in_start``
     - ``temp_in_min``
     - ``temp_in_max``
     - ``temp_in_end``
   * - Outdoor Relative Humidity (%)
     - ``rh_out_start``
     - ``rh_out_min``
     - ``rh_out_max``
     - ``rh_out_end``
   * - Indoor Relative Humidity (%)
     - ``rh_in_start``
     - ``rh_in_min``
     - ``rh_in_max``
     - ``rh_in_end``

Section 4: Automated Data Loggers
---------------------------------

- **Indoor Logger Serial Number:** Serial or barcode of indoor temperature and RH sensor.
- **Outdoor Logger Serial Number:** Serial or barcode of peridomestic sensor.
- **Data Offload Status:** 1=Downloaded successfully, 2=Logger missing or damaged, 3=Battery dead.
- **Observer Notes:** Narrative comments on microclimate anomalies or sensor placement.
