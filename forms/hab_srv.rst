Habitat Survey & Dipping Form
=============================

**Form Code:** ``HAB-SRV`` | **Study Component:** Larval & Aquatic Habitat Ecology | **SOP Links:** SOP 3.1

The Habitat Survey & Dipping Form documents periodic aquatic habitat visits, recording physicochemical water quality, dipping sampling effort (10 dips), taxon-specific instar and pupae counts, predator guild tallies, and voucher tube preservation.

Section 1: Node & Survey Visit Metadata
---------------------------------------

.. list-table::
   :widths: 25 20 20 35
   :header-rows: 1

   * - Field Name
     - Type
     - Required
     - Description / Source
   * - ``node_code``
     - Text
     - Yes
     - Study Node Code
   * - ``village_id``
     - Text
     - Yes
     - Village Identifier
   * - ``habitat_id``
     - Text
     - Yes
     - From Habitat Registration or container ID
   * - ``visit_id``
     - Text
     - Yes
     - Unique Survey Visit ID
   * - ``survey_time``
     - Time
     - Yes
     - Dipping visit time
   * - ``survey_date``
     - Date
     - Yes
     - Date of visit
   * - ``surveillance_round``
     - Select One
     - Yes
     - 1=Routine, 2=Biannual
   * - ``collector_id``
     - Text
     - Yes
     - Surveyor or Team ID
   * - ``season``
     - Select One
     - Yes
     - 1=Dry, 2=Rainy, 3=Other
   * - ``container_household_id``
     - Text
     - Optional
     - For domestic containers: Compound or House ID

Section 2: Water Physico-Chemical Parameters (SOP 3.1 Table 6)
--------------------------------------------------------------
* **Q01:** Water Temperature (°C).
* **Q02:** pH Level (0.0 to 14.0).
* **Q03:** Electrical Conductivity (μS/cm).
* **Q04:** Salinity reading and meter unit.
* **Q05:** Total Dissolved Solids (TDS mg/L).
* **Q06:** Dissolved Oxygen (DO mg/L).
* **Q07:** Water Movement (1=Stagnant, 2=Slow, 3=Fast).
* **Q08:** Water Colour (1=Clear, 2=Turbid, 3=Polluted, 4=Other).
* **Q09:** Water Source Origin (1=Rainwater, 2=Ground, spring, or stream, 3=Human supply or tap).

Section 3: Habitat Morphometry & Vegetation
-------------------------------------------
* **Q10 to Q13:** Length, Width, Perimeter, Surface Area, and Column Depth this visit.
* **Q14 to Q18:** Shade level, Vegetation type and quantity, Algae type and quantity.
* **Q19 and Q20:** Percent cover (Vegetation, Algae, Canopy, Biofilm) and Environment type.

Section 4: Sampling Effort & Completed Dips
-------------------------------------------
* **Q21 and Q22:** Immatures observed (Larvae 1/0, Pupae 1/0) and Predators observed (1/0).
* **Q23:** Technique (1=Dipper 350mL, 2=Bucket 10L, 3=Pipette, 4=Whole volume).
* **Q24:** Actual completed dips (standard = 10) and habitat sections sampled.
* **Q24a:** Reason if fewer than 10 dips were completed.

Section 5: Completed Samples & Taxon Counts
-------------------------------------------
Repeat group recorded for each completed dip, bucket, or container examination:

* Sample Number (sequential counter)
* Taxon Code (1=*An. gambiae complex*, 2=*An. funestus*, 3=*Other Anopheline*, 4=*Culex*, 5=*Aedes*, 6=*Mansonia*, 7=*Other*)
* Immature Counts: L1-L2, L3, L4, Pupae, Total Larvae (calculated)
* Aquatic Predators: Predator Code (1 to 10) and count per sample

Section 6: Aquatic Predator Reconciliation Totals
-------------------------------------------------
Sum of all predators observed across completed dips:

1. Dragonfly (DF) | 2. Damselfly (DS) | 3. Diving Beetle (DB) | 4. Backswimmer (BS) | 5. Water Boatman (WB)
6. Water Scorpion (WS) | 7. Giant Water Bug (GB) | 8. Tadpole (TP) | 9. Copepod (CP) | 10. Other Predators (OT)

Section 7: Specimen Preservation & Field Archiving (SOP 3.1 Table 13)
---------------------------------------------------------------------
* **Q25:** Sample collected for lab analysis (1=Yes, 0=No with reason).
* **Q26:** Preservation method applied (1=Live transport for rearing, 2=>70% Ethanol).
* **Q27:** Sample Tube / Voucher Vial ID (Format: ``Country-Node-Larv-ID``; links reared adults to collection form).
* **Q28:** Habitat photograph taken (1=Yes, 0=No) and file name (``HabitatID_YYYYMMDD``).
