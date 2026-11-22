SOP 1.1: Site & Household Selection
===================================

This quick reference summarises site selection, household selection and household replacement from **VectorGrid SOP 1.1** (Site and Household Selection for Core and Supplementary Sampling).

Node Structure & Site Rotation (Figure 1 and Table 1)
-----------------------------------------------------
For each observatory node, ten sites at village or neighbourhood level are selected: one Monthly Sentinel Site (M1) and nine Supplementary Sites (S1 to S9).

* **Monthly Sentinel Site:** The core longitudinal strand, with routine entomological sampling every month, all year.
* **Supplementary Sites:** Sampled biannually, in the dry and wet seasons, during community engagement "Mosquito weeks". Where a location has no clear wet and dry season, choose the two time points with the strongest seasonal contrast.
* **Rotation:** Each year the Monthly Sentinel Site and at least four Supplementary Sites are sampled (for example M1 with S1 to S4 in year 1, and M1 with S5 to S8 in year 2).

Site Selection Criteria (Table 2)
---------------------------------
* **Logistics & Feasibility:** Year-round access and at least 10 households per village for the Monthly Sentinel Site; wet and dry season access and country-wide geographic representation for Supplementary Sites.
* **Minimum Distance Between Sites:** At least 2 km between sites (the maximum lifetime dispersal of *Anopheles*, *Aedes* and *Culex*), ideally about 5 km. There is no maximum distance, as long as all sites are within the same administrative unit.
* **Ecological & Environmental Diversity:** Sentinel sites represent the environmental profile of the bioregion (climate, land use, population). Supplementary sites add variation in environmental and socioeconomic characteristics where possible.
* **Human & Zoonotic (One Health) Disease Risk:** Plausible local exposure or transmission risk for the main vector-borne diseases of concern. Where relevant, supplementary sites cover a range of human and zoonotic diseases, including proximity to wildlife reservoirs.
* **Security & Community Acceptability:** A strong basis for community engagement and long-term acceptability, in areas with no history of security risks.

Household Selection (Table 3)
-----------------------------
The criteria are not in order of importance. Teams decide using local knowledge, balancing study design with feasibility; the safety of field staff is a non-negotiable priority.

1. **Random Selection (Preferred):**
   Use a random number generator to pick households from a census list, with extra reserve households in case some are unsuitable. Approach households, check eligibility and seek consent until **10 households** are confirmed. If no census list exists, use the village boundary shapefile to generate random GPS points in QGIS (for example 20 points at least 100 m apart), approach the nearest house to each point, and continue until 10 households are confirmed.

2. **Haphazard Selection (Secondary):**
   Used when random selection is not practical.

3. **Logistics & Feasibility:**
   Selected households must be accessible in both wet and dry seasons.

4. **Minimum Distance Between Households:**
   Houses (and sampling points) at least 100 m apart, to limit trap interference.

5. **Human Occupancy:**
   Only households where people sleep.

6. **Household Structure:**
   Houses built with the predominant materials at the site, with proportional variation in structure types where appropriate.

7. **Security:**
   Follow local guidance at site level to avoid security risks (for example dangerous animals, buildings or environments) and to ensure community acceptance.

Household Replacement
---------------------
A household that refuses, withdraws or is no longer appropriate to work in is replaced with an eligible alternative that meets the criteria above, such as one of the reserve households.

How this is recorded in the ODK forms:

* Record the change on :doc:`../forms/hh_upd` with the new status ``withdrew``, ``refused``, ``relocated`` or ``inactive``, and the reason.
* Register the replacement household on :doc:`../forms/hh_reg` with its own unique Household ID; do not reuse the ID of a household that has left the study.
* ``HH-REG`` records the household type: ``1`` = Monthly sentinel, ``2`` = Biannual supplementary.
