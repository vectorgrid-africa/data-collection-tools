SOP 2.1: Essential Metadata & Environmental Variables
=====================================================

This quick reference summarises the minimum metadata and environmental variables to collect during routine monthly and biannual entomological sampling, from the variable table in **VectorGrid SOP 2.1**.

Site & Location Metadata
------------------------
Record these site and location variables:

1. **Node Code**
2. **Country**
3. **Province**
4. **District**
5. **Locality**
6. **Sentinel village / biannual village**
7. **Sentinel house ID / biannual house ID**
8. **GPS coordinates of the house:** latitude, longitude and altitude (m)

**In the ODK forms:** the location is recorded once, when a household (``HH-REG``) or habitat (``HAB-REG``) is registered and for an extreme weather event (``ENV-EXT``), from location lists set for each node; the other forms pick the registered record. Country is preset in the form and Node Code is typed using your assigned code (for example ``TZ-MOR-01``).

GPS Accuracy
------------
Record GPS coordinates of each focal house in **WGS84 decimal degrees** with **±5 m accuracy** (from the :doc:`adult sampling procedure <sop_2_2>`). The GPS questions in the forms ask for coordinates within 5 m.

Sampling Event, Household & Trap Variables
------------------------------------------
* **Sampling event:** Sampling date, surveillance type (routine monthly or biannual), collection start and end time, collector or team ID.
* **Household structure** (collections in and around households): House type, changes to the house, collection location (indoor or outdoor), construction material, roof type, open eaves, livestock near the house and livestock type.
* **Monthly trap information:** Trap ID, trap type (CDC-LT, CO\ :sub:`2`-baited CDC-LT, BG-Sentinel), trap start and end time, whether the trap worked the whole night (CDC-LT and BG-Sentinel), and light status at the end time (CDC-LT).
* **Additional information:** Distance to the nearest breeding site, breeding source type, number of rooms, people sleeping in each room and in the trap room, and interventions introduced before collections (ITN, MDA-Ivermectin, LSM, IRS).

These are recorded on :doc:`../forms/hh_reg`, :doc:`../forms/hh_upd`, :doc:`../forms/trap_reg` and :doc:`../forms/spec_srt`.

**Breeding source type:** In the ODK forms, nearby aquatic habitats within 100 m are recorded on ``HH-REG`` using the standardised habitat type codes 1 to 22 (see :doc:`../codebooks`).

Weather, Temperature & Humidity
-------------------------------
* **Temperature (°C) and relative humidity (%):** Indoor and outdoor.
* **Rainfall:** Last 24 hours and last week (mm).
* **Weather summary:** Rainy, windy, cold, warm, other.
* **Wind speed:** Optional.
* **Population setting:** Urban or rural.
* **Land use near the sentinel house:** Agriculture, mining, construction, other.

Weather and microclimate are recorded on :doc:`../forms/env_obs`; population setting and land use on :doc:`../forms/hh_reg`.

Data Logger Placement
---------------------
The logger heights below come from the :doc:`adult sampling procedure <sop_2_2>`.

* **House types:** Depending on the number of loggers, make sure loggers are placed in houses of different structure types.
* **Indoor logger:** At the same height as the trap (about 1.5 m), near the bed.
* **Outdoor logger:** 1.5 m above the ground near a CDC trap, or 1 m for a BG-Sentinel. If dry ice is the CO\ :sub:`2` source, keep the logger at least 1 m away to prevent temperature interference.

Extreme Weather Events
----------------------
For each event, record the name, occurrence date, type, province, district and village, GPS coordinates, severity, and the impact on the environment and on human behaviour.

* **Event type:** Earthquake, Extreme temperature, Flood, Storm / Cyclones, Wildfire, Drought, Other.
* **Severity:** Low, Moderate, Severe, Extreme.
* **Impact on the environment:** Vegetation loss, wetland expansion, soil moisture change, others.
* **Impact on human behaviour:** People displaced, temporary shelter used, people sleeping outdoors, activities disrupted, others.

These are recorded on :doc:`../forms/env_ext`.

Biannual Human Behaviour Variables
----------------------------------
Interventions introduced between biannual collections; study volunteer code and gender (female, male, transgender, prefer not to disclose); collection start and end time; people sleeping and awake under a bed net outdoors and indoors; and people not under a bed net indoors. These are recorded on :doc:`../forms/hh_beh` (see the :doc:`human-mosquito contact sampling procedure <sop_2_2>`).

Larval Surveillance Variables
-----------------------------
Habitat ID, habitat type, habitat size (perimeter), depth, water quality, vegetation, algae, biofilm and canopy cover, predators, and counts of larvae, pupae, L3 and L4. These are recorded on :doc:`../forms/hab_reg` and :doc:`../forms/hab_srv` (see the :doc:`larval survey procedure <sop_3_1>`).
