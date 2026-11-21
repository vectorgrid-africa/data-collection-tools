Aquatic Habitat Registration Form
=================================

**Form Code:** ``HAB-REG`` | **Study Component:** Larval & Aquatic Habitat Ecology | **SOP Links:** SOP 3.1

The Aquatic Habitat Registration Form establishes the permanent GPS location, permanence, physical dimensions, vegetation cover, and predator observations for an aquatic breeding site.

Section 1: Node & Habitat Metadata
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
     - Observatory Node Code
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
     - Village or Locality
   * - ``village_id``
     - Text
     - Yes
     - Village ID
   * - ``gps_location``
     - Geopoint
     - Yes
     - Lat, Lon, Alt, Accuracy (±5 m)
   * - ``registration_date``
     - Date
     - Yes
     - Date of registration
   * - ``registration_time``
     - Time
     - Yes
     - Time of registration
   * - ``collector_id``
     - Text
     - Yes
     - Collector / Team ID
   * - ``habitat_id``
     - Text
     - Yes
     - Unique ID (``HAB-__________``)

Section 2: Classification & Physical Dimensions
-----------------------------------------------
* **Q01:** Natural or Artificial (1=Natural, 2=Artificial).
* **Q02:** Habitat Permanence (1=Temporary, 2=Semi-permanent, 3=Permanent).
* **Q03:** Habitat Type (Codes 1 to 22: Swamp, puddle, pool, tyre, borrow pit, etc.).
* **Q04:** Surface Length and Width in metres.
* **Q05:** Habitat Perimeter in metres.
* **Q06:** Surface Area (m² = Length × Width approximation).
* **Q07:** Average Water Column Depth in centimeters.
* **Q08:** Water Movement (1=Stagnant, 2=Slow, 3=Fast).
* **Q09:** Water Colour (1=Clear, 2=Turbid (cloudy) or Coloured, 3=Polluted, 4=Other).

Section 3: Vegetation, Algae & Environment
------------------------------------------
* **Q10:** Vegetation Type (0=None, 1=Submerged, 2=Floating, 3=Emergent, 4=Other).
* **Q11:** Vegetation Quantity (0=None, 1=Scarce <25%, 2=Moderate 25% to 50%, 3=Abundant >50%).
* **Q12:** Estimated Vegetation Cover (0% to 100%).
* **Q13:** Algae Quantity (0=None, 1=Scarce, 2=Moderate, 3=Abundant).
* **Q14:** Algae Type (0=None, 1=Filamentous, 2=Green, 3=Blue-green, 4=Brown, 5=Other, 6=Unidentifiable).
* **Q15:** Shade over habitat (0=None, 1=Partial, 2=Heavy or Fully shaded).
* **Q16:** Surface biofilm or sheen present (1=Yes, 0=No).
* **Q17:** Estimated separate cover percentages for Algae, Canopy, and Biofilm.
* **Q18:** Environment around habitat (Shrub, Grassland, Swamp, Field, Residential, Forest, Urban, etc.).
* **Q19:** Linear distance from habitat to nearest homes in metres.
* **Q20:** Aquatic Predators present (1/0) and Mosquito Larvae or Pupae present (1/0).

Habitat Status Update
---------------------

For subsequent surveillance rounds, aquatic habitat status changes (seasonal drying, drainage, destruction) are logged using the update form:

.. toctree::
   :maxdepth: 2

   hab_upd
