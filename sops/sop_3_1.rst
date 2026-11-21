SOP 3.1: Larval Survey and Aquatic Habitat Assessment
=====================================================

This quick reference summarises standardised dipping effort, water quality parameters, predator presence, and specimen preservation protocols from **VectorGrid SOP Task 3.1**.

1. Standardised Dipping Effort & Technique
------------------------------------------
* **Sampling Device:** Standard 350 mL white dipper with handle. For very small or shallow habitats, a pipette or turkey baster may be used.
* **Effort Benchmark:** Dipping effort is determined by habitat size and perimeter, taken systematically around the habitat edge or accessible water surface. Record the exact number of completed dips.
* **Dipping Technique:** Skim the dipper head (angled at 45 degrees and submerged about 3 cm in the water) in a straight line towards visible larvae, paying special attention to floating vegetation, shaded emergent grass, and overhanging debris.
* **Settling Interval:** Wait at least 2 minutes between each dip to permit disturbed larvae and pupae to return to the surface film.
* **Zero Counts:** If no larvae or pupae are retrieved across completed dips, record zero counts explicitly on ``HAB-SRV``; never discard negative survey records.
* **Rain Contingency:** Avoid dipping during rainfall, as larvae dive deep when disturbed by raindrops. Avoid sampling immediately after heavy rains have flushed out habitats.

2. Instar Separation & Diagnostic Counts
----------------------------------------
* **Early Instars (L1 to L2):** Small larvae with narrow head capsules; pooled and counted together.
* **Late Instars (L3 to L4):** Fully developed larvae with distinct head, thorax, and abdominal segments; separated into *Anopheles* (horizontal surface posture without breathing siphon) and culicines (hanging posture with breathing siphon).
* **Pupae:** Comma-shaped, non-feeding stage; counted separately.

3. Water Quality Parameters
---------------------------

.. list-table::
   :widths: 40 30 30
   :header-rows: 1

   * - Parameter
     - Standard Units
     - Form Code
   * - **Water Temperature**
     - °C
     - ``temperature``
   * - **pH Level**
     - 0.0 to 14.0
     - ``ph``
   * - **Conductivity**
     - μS/cm
     - ``conductivity``
   * - **Salinity**
     - ppt / PSU (meter unit)
     - ``salinity``
   * - **Dissolved Oxygen (extended)**
     - mg/L
     - ``dissolved_oxygen``
   * - **Total Dissolved Solids (extended)**
     - mg/L
     - ``tds``

4. Aquatic Predator Presence & Counts
-------------------------------------
Field teams examine dipping trays for predators (insect larvae, tadpoles, fish) using the standardised codes in :doc:`../codebooks`:

* **Notonectids & Corixids:** Backswimmers (BS) and water boatmen (WB).
* **Odonata:** Dragonfly (DF) and damselfly (DS) nymphs.
* **Coleoptera:** Predatory diving beetles (DB).
* **Amphibians & Fish:** Tadpoles (TP) and small surface fish.

5. Specimen Preservation Guidelines
-----------------------------------

.. list-table::
   :widths: 30 35 35
   :header-rows: 1

   * - Preservation Target
     - Field Protocol
     - ID Used Later
   * - **Live Rearing**
     - Live transport (vial with habitat water)
     - Linked to ``SPEC-SRT``
   * - **Molecular / PCR**
     - >70% Ethanol
     - Linked to DNA archive
