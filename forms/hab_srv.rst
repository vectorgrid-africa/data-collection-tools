Habitat Survey & Dipping Form
=============================

**Form Code:** ``HAB-SRV`` | **Form ID:** ``vg_hab_srv`` | **Version:** ``2026112201`` | **Sampling Activity:** Larval Sampling | **SOP Links:** :doc:`SOP 3.1 <../sops/sop_3_1>`

The Habitat Survey and Dipping Form records one visit to a registered habitat or a domestic container: habitat characteristics, size, vegetation, physico-chemical readings, larvae, pupae and predators per dip, and the samples kept for the laboratory. A summary of totals is shown before signing.

How This Form Works
-------------------

* Select the district, then either an active registered habitat from the ``habitats`` entity list or a container (typed Container ID, household / compound ID and node).
* Water quality readings (pH, temperature, conductivity, salinity, TDS, dissolved oxygen) are optional.
* The standard effort is 10 dips with the dipper. If fewer are completed, the form asks for the reason.
* Counts are entered per dip for each taxon ticked (L1-L2, L3, L4, pupae) and each predator ticked. The form adds up the totals and larvae per dip.
* The vial ID (Country-Node-Larv-ID) links any adults reared from this sample to SPEC-SRT.

Section 1: Survey Information
-----------------------------

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

       *Hint:* Filter habitats by district
   * - ``collector_id``
     - Text
     - Yes
     - Field Worker Name
   * - ``survey_date``
     - Date
     - Yes
     - Survey Date

       *Check:* ``value <= today()``

       *Default:* today
   * - ``survey_time``
     - Time
     - Yes
     - Survey Time
   * - ``surveillance_type``
     - Select one
     - Yes
     - Surveillance type

       ``1`` = Routine monthly; ``2`` = Biannual
   * - ``visit_id``
     - Text
     - Yes
     - Visit ID

Section 2: Habitat Selection
----------------------------

.. list-table::
   :widths: 24 13 9 54
   :header-rows: 1

   * - Field Name
     - Type
     - Required
     - Question, Choices & Logic
   * - ``sample_unit``
     - Select one
     - Yes
     - Habitat or container?

       ``1`` = Registered habitat (HAB-REG); ``2`` = Container
   * - ``habitat``
     - Select record
     - Yes
     - Select Habitat

       Pick a record from the ``habitats`` entity list (filtered by district, active records only)

       *Shown if* ``sample_unit = 1``
   * - ``container_id``
     - Text
     - Yes
     - Container ID

       *Shown if* ``sample_unit = 2``
   * - ``compound_id``
     - Text
     - Yes
     - Household / compound ID

       *Shown if* ``sample_unit = 2``
   * - ``node_code_typed``
     - Text
     - Yes
     - Node Code

       *Shown if* ``sample_unit = 2``
   * - ``node_code``
     - Calculated
     - Auto
     - From the selected habitat, or typed for a container
   * - ``habitat_id``
     - Calculated
     - Auto
     - Habitat ID of the selected habitat, or the Container ID
   * - ``auto_village``
     - Calculated
     - Auto
     - Taken from the selected ``habitats`` record (property ``village``)
   * - ``auto_district``
     - Calculated
     - Auto
     - Taken from the selected ``habitats`` record (property ``district``)
   * - ``auto_habitat_type``
     - Calculated
     - Auto
     - Taken from the selected ``habitats`` record (property ``habitat_type_name``)
   * - ``auto_water_type``
     - Calculated
     - Auto
     - Taken from the selected ``habitats`` record (property ``water_type_name``)

Section 3: Habitat Characteristics
----------------------------------

.. list-table::
   :widths: 24 13 9 54
   :header-rows: 1

   * - Field Name
     - Type
     - Required
     - Question, Choices & Logic
   * - ``water_colour``
     - Select one
     - Yes
     - Water colour

       ``1`` = Clear; ``2`` = Coloured / Turbid; ``3`` = Polluted; ``4`` = Other
   * - ``water_colour_other``
     - Text
     - Yes
     - Specify other water colour

       *Shown if* ``water_colour = 4``
   * - ``water_source``
     - Select one
     - Yes
     - Water source

       ``1`` = Rainwater; ``2`` = Ground, spring or stream water; ``3`` = Human supply (tap, leak, irrigation)
   * - ``algal_quantity``
     - Select one
     - Yes
     - Algal quantity

       ``0`` = None; ``1`` = Scarce; ``2`` = Moderate; ``3`` = Abundant
   * - ``algae_type``
     - Select multiple
     - Yes
     - Algae type

       ``0`` = None; ``1`` = Filamentous; ``2`` = Green; ``3`` = Blue-green; ``4`` = Brown; ``5`` = Other (specify); ``6`` = Unidentifiable

       *Shown if* ``algal_quantity != 0``

       *Check:* ``0 cannot be combined with other options``

       *Hint:* Select all that apply
   * - ``algae_type_other``
     - Text
     - Yes
     - Specify other algae type

       *Shown if* ``algae_type includes 5``
   * - ``algae_cover``
     - Decimal
     - Yes
     - Algae cover (%)

       *Shown if* ``algal_quantity != 0``

       *Check:* ``range 0 to 100``

       *Hint:* Visual estimate of water surface covered by algae
   * - ``water_movement``
     - Select one
     - Yes
     - Water movement

       ``1`` = Stagnant; ``2`` = Slow; ``3`` = Fast
   * - ``shade``
     - Select one
     - Yes
     - Shade over habitat

       ``0`` = None; ``1`` = Partial; ``2`` = Heavy (Fully shaded)
   * - ``canopy_cover``
     - Decimal
     - Yes
     - Canopy cover (%)

       *Shown if* ``shade != 0``

       *Check:* ``range 0 to 100``

       *Hint:* Estimated percentage of the habitat under canopy
   * - ``biofilm_cover``
     - Decimal
     - Yes
     - Biofilm cover (%)

       *Check:* ``range 0 to 100``

       *Hint:* Visual estimate of water surface covered by biofilm. Enter 0 if none.

Section 4: Habitat Size
-----------------------

.. list-table::
   :widths: 24 13 9 54
   :header-rows: 1

   * - Field Name
     - Type
     - Required
     - Question, Choices & Logic
   * - ``habitat_length``
     - Decimal
     - Yes
     - Length (m)

       *Check:* ``value > 0``
   * - ``habitat_width``
     - Decimal
     - Yes
     - Width (m)

       *Check:* ``value > 0``
   * - ``habitat_perimeter``
     - Decimal
     - Yes
     - Perimeter (m)

       *Check:* ``value > 0``

       *Hint:* Distance around the water's edge
   * - ``water_depth``
     - Decimal
     - Yes
     - Water depth (cm)

       *Check:* ``value >= 0``
   * - ``total_surface_area``
     - Decimal
     - Yes
     - Habitat total surface area (m²)

       *Check:* ``value > 0``

       *Hint:* The form shows length x width as a suggestion. Correct it if the habitat is irregular.

Section 5: Vegetation
---------------------

.. list-table::
   :widths: 24 13 9 54
   :header-rows: 1

   * - Field Name
     - Type
     - Required
     - Question, Choices & Logic
   * - ``vegetation_type``
     - Select multiple
     - Yes
     - Vegetation type

       ``0`` = None; ``1`` = Submerged; ``2`` = Floating; ``3`` = Emergent; ``4`` = Other

       *Check:* ``0 cannot be combined with other options``

       *Hint:* Select all that apply
   * - ``vegetation_type_other``
     - Text
     - Yes
     - Specify other vegetation type

       *Shown if* ``vegetation_type includes 4``
   * - ``vegetation_quantity``
     - Select one
     - Yes
     - Vegetation quantity

       ``0`` = None; ``1`` = Scarce (<25%); ``2`` = Moderate (25-50%); ``3`` = Abundant (>50%)

       *Shown if* ``vegetation_type excludes 0``
   * - ``vegetation_cover``
     - Decimal
     - Yes
     - Vegetation cover (%)

       *Shown if* ``vegetation_type excludes 0``

       *Check:* ``range 0 to 100``

       *Hint:* Visual estimate of water surface occupied by vegetation

Section 6: Water Type, Season & Surroundings
--------------------------------------------

.. list-table::
   :widths: 24 13 9 54
   :header-rows: 1

   * - Field Name
     - Type
     - Required
     - Question, Choices & Logic
   * - ``water_type``
     - Select one
     - Yes
     - Water type

       ``1`` = Temporary; ``2`` = Semi-permanent; ``3`` = Permanent
   * - ``season``
     - Select one
     - Yes
     - Season

       ``1`` = Dry; ``2`` = Rainy; ``3`` = Other
   * - ``season_other``
     - Text
     - Yes
     - Specify other season

       *Shown if* ``season = 3``
   * - ``environment_around``
     - Select multiple
     - Yes
     - Environment around habitat

       ``1`` = Shrub/Bush; ``2`` = Grassland; ``3`` = Swamp; ``4`` = Cultivated field; ``5`` = Residential; ``6`` = Cattle grazing; ``7`` = Forest; ``8`` = Urban; ``9`` = Other (specify)

       *Hint:* Select all that apply
   * - ``environment_other``
     - Text
     - Yes
     - Specify other environment

       *Shown if* ``environment_around includes 9``
   * - ``distance_homes``
     - Decimal
     - Yes
     - Distance from nearest homes (m)

       *Check:* ``value >= 0``
   * - ``notes``
     - Text
     - No
     - Observer Comments

       *Hint:* Any environmental changes observed

Section 7: Physio-Chemical Parameters
-------------------------------------

.. list-table::
   :widths: 24 13 9 54
   :header-rows: 1

   * - Field Name
     - Type
     - Required
     - Question, Choices & Logic
   * - ``ph``
     - Decimal
     - No
     - pH

       *Check:* ``range 0 to 14``
   * - ``temperature``
     - Decimal
     - No
     - Temperature (°C)

       *Check:* ``range 0 to 50``
   * - ``conductivity``
     - Decimal
     - No
     - Electrical Conductivity (μS/cm)

       *Check:* ``value >= 0``
   * - ``salinity``
     - Decimal
     - No
     - Salinity (value)

       *Check:* ``value >= 0``
   * - ``salinity_unit``
     - Text
     - Conditional
     - Salinity unit

       *Shown if* ``salinity is answered``

       *Required if* ``salinity is answered``
   * - ``tds``
     - Decimal
     - No
     - Total Dissolved Solids (mg/L)

       *Check:* ``value >= 0``
   * - ``dissolved_oxygen``
     - Decimal
     - No
     - Dissolved Oxygen (mg/L)

       *Check:* ``range 0 to 30``

Section 8: Larval & Predator Sampling
-------------------------------------

.. list-table::
   :widths: 24 13 9 54
   :header-rows: 1

   * - Field Name
     - Type
     - Required
     - Question, Choices & Logic
   * - ``larvae_present``
     - Select one
     - Yes
     - Larvae present?

       ``1`` = Yes; ``0`` = No
   * - ``pupae_present``
     - Select one
     - Yes
     - Pupae present?

       ``1`` = Yes; ``0`` = No
   * - ``predators_present``
     - Select one
     - Yes
     - Predators present?

       ``1`` = Yes; ``0`` = No
   * - ``needs_sampling``
     - Calculated
     - Auto
     - ``1`` when larvae, pupae or predators are present, otherwise ``0``
   * - ``taxa_found``
     - Select multiple
     - Yes
     - Mosquito taxa found

       ``gam`` = An. gambiae; ``fun`` = An. funestus; ``oan`` = Other Anopheline; ``cul`` = Culex; ``aed`` = Aedes; ``man`` = Mansonia; ``oth`` = Other taxon

       *Shown if* ``((larvae_present = 1 or pupae_present = 1))``

       *Hint:* Select all that apply
   * - ``other_taxon_name``
     - Text
     - Yes
     - Specify other taxon

       *Shown if* ``((larvae_present = 1 or pupae_present = 1) and taxa_found includes oth)``
   * - ``predators_found``
     - Select multiple
     - Yes
     - Predators found

       ``dragonfly`` = Dragonflies; ``damselfly`` = Damselflies; ``diving_beetle`` = Diving beetles; ``backswimmer`` = Backswimmers; ``water_boatman`` = Water boatman; ``water_scorpion`` = Water scorpion; ``giant_water_bug`` = Giant water bugs; ``tadpole`` = Tadpoles; ``copepod`` = Copepods; ``other_predator`` = Other predators

       *Shown if* ``predators_present = 1``

       *Hint:* Select all that apply
   * - ``sampling_technique``
     - Select one
     - Yes
     - Sampling technique

       ``dipper`` = Standard Dipper (350 mL); ``bucket`` = 10L Bucket; ``pipette`` = Baster / pipette; ``whole`` = Whole accessible volume

       *Shown if* ``needs_sampling = 1``

       *Hint:* Select the sampling method used
   * - ``num_dips``
     - Integer
     - Yes
     - Number of dips / buckets / samples completed

       *Shown if* ``needs_sampling = 1``

       *Check:* ``range 1 to 100``
   * - ``num_sections``
     - Integer
     - Yes
     - Number of habitat sections sampled

       *Shown if* ``needs_sampling = 1``

       *Check:* ``value >= 1``
   * - ``fewer_dips_reason``
     - Text
     - Yes
     - Reason for fewer dips

       *Shown if* ``needs_sampling = 1 and sampling_technique = dipper and num_dips < 10``

       *Hint:* Standard dipping: if fewer than 10 were completed, record why.
   * - ``total_larvae``
     - Calculated
     - Auto
     - All larvae (L1 to L4, all taxa) over all dips
   * - ``total_pupae``
     - Calculated
     - Auto
     - All pupae (all taxa) over all dips
   * - ``larvae_per_dip``
     - Calculated
     - Auto
     - ``total_larvae`` / ``num_dips``, two decimals

Repeat: Dip Counts
~~~~~~~~~~~~~~~~~~

Repeat group: one entry per dip, bucket or sample, repeated ``num_dips`` times.

This section is shown only if ``needs_sampling = 1``.

Counts are asked only for the taxa ticked in ``taxa_found`` and the predators ticked in ``predators_found``. A blank count is stored as 0.

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Field Names
     - Meaning
   * - ``<taxon>_l12_input``, ``<taxon>_l3_input``, ``<taxon>_l4_input``, ``<taxon>_pupae_input``
     - Integer counts of early instars (L1-L2), L3, L4 and pupae in this dip. ``<taxon>`` is ``gam``, ``fun``, ``oan``, ``cul``, ``aed``, ``man`` or ``oth``. Shown only if ``taxa_found`` includes that taxon.
   * - ``<predator>_dip_input``
     - Integer count of that predator in this dip. ``<predator>`` is ``dragonfly``, ``damselfly``, ``diving_beetle``, ``backswimmer``, ``water_boatman``, ``water_scorpion``, ``giant_water_bug``, ``tadpole``, ``copepod`` or ``other_predator``. Shown only if ``predators_found`` includes that predator.
   * - ``<taxon>_total``, ``<predator>_total``
     - Calculated: the sum of that count over all dips.

Section 9: Specimen Preservation & Field Archiving
--------------------------------------------------

.. list-table::
   :widths: 24 13 9 54
   :header-rows: 1

   * - Field Name
     - Type
     - Required
     - Question, Choices & Logic
   * - ``sample_collected``
     - Select one
     - Yes
     - Sample collected for lab analysis

       ``1`` = Yes; ``0`` = No
   * - ``no_sample_reason``
     - Text
     - Yes
     - Reason none retained

       *Shown if* ``(sample_collected = 0 and (larvae_present = 1 or pupae_present = 1))``

       *Hint:* Immatures were found but none were retained.
   * - ``preservation``
     - Select one
     - Yes
     - Preservation method applied

       ``1`` = Live transport (rearing vial); ``2`` = >70% Ethanol

       *Shown if* ``sample_collected = 1``
   * - ``vial_id``
     - Text
     - Yes
     - Sample tube / vial ID

       *Shown if* ``sample_collected = 1``

       *Hint:* Country-Node-Larv-ID. Link any reared adults to this vial on SPEC-SRT.
   * - ``photo_taken``
     - Select one
     - Yes
     - Habitat photograph taken

       ``1`` = Yes; ``0`` = No
   * - ``photo_file_name``
     - Text
     - Yes
     - File name

       *Shown if* ``photo_taken = 1``

       *Hint:* Format HabitatID_YYYYMMDD. The form shows the suggested name for this habitat and date.

Section 10: Survey Summary
--------------------------

.. list-table::
   :widths: 24 13 9 54
   :header-rows: 1

   * - Field Name
     - Type
     - Required
     - Question, Choices & Logic
   * - ``full_name_signature``
     - Text
     - Yes
     - Full name (as signature)
