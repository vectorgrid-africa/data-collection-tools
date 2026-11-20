Household Registration Form
===========================

**Form Code:** ``HH-REG`` | **Study Component:** Household Surveillance

The Household Registration Form captures administrative geography, GPS geolocation, household cohort demographics, house construction characteristics, vector control interventions, domestic animal proximity, and a room-by-room census.

Section 1: Administrative Geography & Event
-------------------------------------------

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
   * - ``country``
     - Text
     - Yes
     - Country of surveillance
   * - ``province``
     - Text
     - Yes
     - Province or Region
   * - ``district``
     - Text
     - Yes
     - District
   * - ``locality``
     - Text
     - Yes
     - Ward or Locality
   * - ``village_name``
     - Text
     - Yes
     - Village or Community Name
   * - ``village_id``
     - Text
     - Yes
     - Standard Village Identifier
   * - ``gps_location``
     - Geopoint
     - Yes
     - Latitude, Longitude, Altitude, Accuracy (±5 m)
   * - ``registration_date``
     - Date
     - Yes
     - Date of baseline census
   * - ``household_type``
     - Select One
     - Yes
     - 1=Monthly sentinel, 2=Biannual supplementary
   * - ``collector_id``
     - Text
     - Yes
     - Enumerator or Team ID
   * - ``household_id``
     - Text
     - Yes
     - Unique Household ID (for example, ``VG01-001``)
   * - ``population_setting``
     - Select One
     - Yes
     - 1=Urban, 2=Rural

Section 2: Occupant Demographics
--------------------------------
Summary table of occupants aggregated across all sleeping rooms:

* **Males:** under 5 years, 5 to 15 years, over 15 years
* **Females:** under 5 years, 5 to 15 years, over 15 years

Section 3: House Structure & Architecture
-----------------------------------------

.. list-table::
   :widths: 10 25 35 30
   :header-rows: 1

   * - Code
     - Variable Name
     - Question Label
     - Valid Choices / Logic
   * - Q01
     - ``sleeping_rooms``
     - Sleeping Rooms in House
     - Integer (≥ 1)
   * - Q02
     - ``total_rooms``
     - Total Rooms in House
     - Integer (≥ sleeping rooms)
   * - Q03
     - ``house_type``
     - House Construction Type
     - 1=Traditional, 2=Modern, 99=Other
   * - Q04
     - ``sleep_wake_schedule``
     - Usual Sleep & Wake Times
     - 24h Sleep Time and Wake Time
   * - Q05
     - ``eave_status``
     - Eave Status
     - 1=Open, 2=Partly screened, 3=Fully screened, 4=Fully blocked
   * - Q06
     - ``roof_material``
     - Roof Material
     - 1=Thatch, 2=Metal sheets, 3=Tiles, 4=Concrete, 99=Other
   * - Q07
     - ``has_ceiling``
     - Ceiling Beneath Roof
     - 1=Yes, 0=No
   * - Q08
     - ``exterior_wall_material``
     - Exterior Wall Material
     - 1=Mud, 2=Brick, 3=Cement blocks, 4=Thatch, 99=Other
   * - Q09
     - ``interior_wall_surface``
     - Interior Wall Surface
     - 1=Not plastered, 2=Cement plaster, 3=Mud plaster
   * - Q10
     - ``floor_material``
     - Floor Material
     - 1=Earth or Mud, 2=Cement, 3=Tiles, 99=Other
   * - Q11
     - ``window_count``
     - Total Windows
     - Integer count
   * - Q12
     - ``window_status``
     - Window Screening
     - 1=Open, 2=Screened, 3=Closed (if windows > 0)
   * - Q13
     - ``entry_door_count``
     - Entry Doors Count
     - Integer count
   * - Q14
     - ``door_status``
     - Door Fit & Gaps
     - 1=Open, 2=Gaps, 3=Tight fit (if doors > 0)

Section 4: Bed Nets & Interventions
-----------------------------------
* **Q15:** Total Bed Nets Owned (Calculated: treated + untreated + unidentified).
* **Q16 to Q18:** Counts of Treated (ITN/LLIN), Untreated, and Unidentified nets.
* **Q19 and Q20:** Other Mosquito Control Interventions (IRS, MDA-Ivermectin, LSM, Other).

Section 5: Sanitation & Livestock Proximity
-------------------------------------------
* **Q21 and Q22:** Latrine inside house (1=Yes, 0=No) and linear distance in meters.
* **Q23 and Q24:** Animal shed present (1=Yes, 0=No) and linear distance in meters.
* **Q25:** Chickens kept inside house at night (1=Yes, 0=No).
* **Q26 and Q26a:** Livestock near house (Cattle, Goats, Chickens, Pigs, Other).

Section 6: Breeding Sites & Land Use
------------------------------------
* **Q27 to Q29:** Mosquito aquatic habitat ≤100 m, Habitat Typology (1 to 22), and Distance in meters.
* **Q30:** Land use activity around house (1=Agriculture, 2=Mining, 3=Construction, 4=Other).

Section 7: Room-by-Room Census
------------------------------
Repeat group recorded for each sleeping room in the house:

* ``room_id`` (for example, R01, R02)
* ``is_trap_room`` (1=Yes, 0=No)
* Demographics: Males under 5, 5 to 15, over 15; Females under 5, 5 to 15, over 15.

Household Status Update
-----------------------

For subsequent surveillance rounds, enrolled households are tracked using the update form rather than repeated baseline registration:

.. toctree::
   :maxdepth: 2

   hh_upd
