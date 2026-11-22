SOP 3.1: Larval Survey and Aquatic Habitat Assessment
=====================================================

This quick reference summarises the sampling frame, dipping technique, habitat and water quality measurements, predators and specimen preservation from **VectorGrid SOP 3.1**.

Larval surveys are a supplementary activity, done during the rainy and dry seasons in the Supplementary Sites. For *Anopheles*-focused surveys the aquatic habitat is the primary sampling unit. For *Aedes*-focused surveys, the selected houses or compounds and their water-holding containers form the sampling frame. Define the sampling frame before fieldwork and use the same design in comparable survey rounds.

1. Standardised Dipping Effort & Technique
------------------------------------------
* **Sampling Device:** Standard 350 mL white dipper with handle. For very small or shallow habitats, use a turkey baster or pipette; a 10 L bucket is also available.
* **Approach:** Step lightly, face the sun so you do not cast a shadow on the water, and in strong wind dip on the windward side.
* **Dipping Technique:** Skim the dipper head (angled at 45 degrees and submerged about 3 cm) in a straight line towards the larvae.
* **Settling Interval:** Wait at least 2 minutes between dips to let larvae and pupae resurface.
* **Effort Standard:** Take a standard **10 dips** at different points along the habitat edge, if its size allows. Where 10 dips cannot be completed, record the actual number and the reason. In large habitats, spread the dips across predefined sections.
* **Zero Counts:** Record the data even when no larvae or pupae are found.
* **Rain:** Avoid dipping while it is raining (larvae dive when disturbed by raindrops) and immediately after heavy rains have flushed out habitats.
* **ODK recording:** :doc:`../forms/hab_srv` records the technique (``dipper``, ``bucket``, ``pipette``, ``whole``), the number of dips (``num_dips``) and sections sampled (``num_sections``), and asks for the reason when fewer than 10 standard dips are entered.

2. Aedes Container Sampling
---------------------------
* Inspect water-holding containers within the predefined house or compound sampling frame, indoors and outdoors. Record the number of containers inspected and the number holding water.
* Use the dipper where the container is big enough; otherwise a baster or pipette. Where the whole accessible volume can be examined, examine it all instead of taking 10 dips.
* Calculate the Container Index, House Index and Breteau Index only when the house and container denominators have been recorded.
* **ODK recording:** In :doc:`../forms/hab_srv`, choose **Container** (``sample_unit`` = ``2``) and type the Container ID and household or compound ID.

3. Instar Separation & Counts
-----------------------------
* **Early Instars (L1 and L2):** Small larvae with narrow head capsules; counted together. First instars are hard to see, so use a hand lens if needed.
* **Late Instars (L3 and L4):** Larger larvae with distinct head, thorax and abdomen. *Anopheles* larvae lie parallel to the surface without a breathing siphon; culicine larvae hang from the surface with a siphon.
* **Pupae:** Comma-shaped, non-feeding stage; counted separately.
* **ODK recording:** :doc:`../forms/hab_srv` records L1-L2, L3, L4 and pupae separately for each taxon ticked in each dip, then adds up totals and larvae per dip.

4. Habitat Characteristics
--------------------------
Identify the habitat type and record its characteristics: size (perimeter), depth, water quality, vegetation, algae, biofilm and canopy cover, and predators.

* **Habitat Type Codes:** Codes 1 to 17 match the SOP. The forms add 18 Rice field, 19 Floodplain, 20 Stream pool and 21 Spring-fed pool, and use 22 for Other (18 in the SOP) (see :doc:`../codebooks`).
* **Where Recorded:** Habitat type, origin and permanence are recorded once on :doc:`../forms/hab_reg`. Size, water, vegetation, algae, shade, surroundings and distance to nearest houses are recorded at each visit on :doc:`../forms/hab_srv`.

5. Water Quality Parameters
---------------------------
Measure water temperature, pH and salinity (or conductivity) with the field meter. The form also allows dissolved oxygen and total dissolved solids. All readings are optional in :doc:`../forms/hab_srv`.

.. list-table::
   :widths: 40 30 30
   :header-rows: 1

   * - Parameter
     - Standard Units
     - Field Name
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
     - Meter unit (typed in ``salinity_unit``)
     - ``salinity``
   * - **Dissolved Oxygen**
     - mg/L
     - ``dissolved_oxygen``
   * - **Total Dissolved Solids**
     - mg/L
     - ``tds``

6. Aquatic Predators
--------------------
Remove predators from the dipping tray as soon as possible so they do not deplete larval numbers (for example dragonfly larvae). :doc:`../forms/hab_srv` records presence and per-dip counts using these codes (see :doc:`../codebooks`):

* **Odonata:** Dragonfly (``dragonfly``) and damselfly (``damselfly``) nymphs.
* **Hemiptera:** Backswimmers (``backswimmer``), water boatmen (``water_boatman``), water scorpions (``water_scorpion``) and giant water bugs (``giant_water_bug``).
* **Coleoptera:** Predatory diving beetles (``diving_beetle``).
* **Others:** Tadpoles (``tadpole``), copepods (``copepod``) and any other predator, including small fish (``other_predator``).

7. Specimen Handling & Preservation
-----------------------------------
* **Vials:** Transfer larvae with a pipette into a labelled vial, with at least 2 mL of water per larva (for example 40 mL of water and 20 larvae in a 50 mL vial). Pour the remaining water back into the habitat.
* **Live Transport:** Keep live larvae in habitat water, cool and protected from heat (cooler box).
* **Preserved Specimens:** Kill larvae with hot water or in >70% ethanol, dry them on a paper towel, then store them in 70% ethanol. Do not let the ethanol fall below 70%.
* **Rearing:** Late (L3 and L4) instars and pupae are reared to adults, which are identified to genus and sex.

.. list-table::
   :widths: 30 35 35
   :header-rows: 1

   * - Preservation Method (``preservation``)
     - Field Protocol
     - Link
   * - ``1`` Live transport (rearing vial)
     - Vial with habitat water, kept cool
     - Reared adults are recorded on ``SPEC-SRT`` with the vial ID as the source
   * - ``2`` >70% ethanol
     - Killed, dried, stored in 70% ethanol
     - Vial ID (Country-Node-Larv-ID)
