Codebooks
=========

Answer codes used by the VectorGrid ODK forms (versions as listed on :doc:`downloads`). The **Code** column is the value stored in the submitted data; the label is what the field worker sees. Every list on this page is taken directly from the downloadable XLSForms. Lists with up to 12 options are also shown in the field tables on each form's page; the habitat types are shown only here, and the species lists are set for each node.

Shared Lists
------------

Yes / No
~~~~~~~~

List ``yes_no``, used in ``HAB-SRV``, ``HH-BEH``, ``HH-REG``, ``HH-UPD``, ``SPEC-DIS``, ``SPEC-HND``, ``SPEC-SRT``, ``TRAP-REG``.

.. list-table::
   :widths: 18 82
   :header-rows: 1

   * - Code
     - Label
   * - ``1``
     - Yes
   * - ``0``
     - No

Surveillance Type
~~~~~~~~~~~~~~~~~

List ``surveillance_type``, used in ``HAB-SRV``, ``HH-UPD``, ``SPEC-SRT``.

.. list-table::
   :widths: 18 82
   :header-rows: 1

   * - Code
     - Label
   * - ``1``
     - Routine monthly
   * - ``2``
     - Biannual

Household Type
~~~~~~~~~~~~~~

List ``household_type``, used in ``HH-REG``.

.. list-table::
   :widths: 18 82
   :header-rows: 1

   * - Code
     - Label
   * - ``1``
     - Monthly sentinel
   * - ``2``
     - Biannual supplementary

Population Setting
~~~~~~~~~~~~~~~~~~

List ``population_setting``, used in ``HH-REG``.

.. list-table::
   :widths: 18 82
   :header-rows: 1

   * - Code
     - Label
   * - ``1``
     - Urban
   * - ``2``
     - Rural

Mosquito Control Interventions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

List ``interventions``, used in ``HH-BEH``, ``HH-REG``, ``HH-UPD``.

.. list-table::
   :widths: 18 82
   :header-rows: 1

   * - Code
     - Label
   * - ``itn``
     - ITN
   * - ``irs``
     - IRS
   * - ``mda_ivermectin``
     - MDA-Ivermectin
   * - ``lsm``
     - LSM
   * - ``other``
     - Other

Livestock Types
~~~~~~~~~~~~~~~

List ``livestock``, used in ``HH-REG``, ``HH-UPD``.

.. list-table::
   :widths: 18 82
   :header-rows: 1

   * - Code
     - Label
   * - ``cattle``
     - Cattle
   * - ``goats``
     - Goats
   * - ``chickens``
     - Chickens
   * - ``pigs``
     - Pigs
   * - ``other``
     - Other

Location Lists
~~~~~~~~~~~~~~

Lists ``district``, ``ward`` and ``village`` are set for each node. The example forms come with demonstration lists for testing; replace them with your node's site list before field use. ``country`` is preset in each form.

Record Status Codes
-------------------

The update forms write these values to the ``status`` property of the entity record. HH-BEH and ENV-OBS list only ``active`` households, SPEC-SRT and SPEC-DIS list only ``active`` traps, and HAB-SRV lists only ``active`` habitats. TRAP-REG, SPEC-SRT and SPEC-DIS list all households in the selected district, and the update forms list all records so a status can be changed back.

Household Status (HH-UPD)
~~~~~~~~~~~~~~~~~~~~~~~~~

List ``household_status``, used in ``HH-UPD``.

.. list-table::
   :widths: 18 82
   :header-rows: 1

   * - Code
     - Label
   * - ``active``
     - Active
   * - ``withdrew``
     - Dropped / Withdrawn
   * - ``refused``
     - Refused to continue
   * - ``relocated``
     - Relocated / Moved
   * - ``inactive``
     - Temporarily inactive

Trap Status (TRAP-UPD)
~~~~~~~~~~~~~~~~~~~~~~

List ``trap_status``, used in ``TRAP-UPD``.

.. list-table::
   :widths: 18 82
   :header-rows: 1

   * - Code
     - Label
   * - ``active``
     - Active
   * - ``malfunctioned``
     - Malfunctioned
   * - ``retired``
     - Retired

Habitat Status (HAB-UPD)
~~~~~~~~~~~~~~~~~~~~~~~~

List ``status_list``, used in ``HAB-UPD``.

.. list-table::
   :widths: 18 82
   :header-rows: 1

   * - Code
     - Label
   * - ``active``
     - Active
   * - ``inactive``
     - Inactive (temporarily dry)
   * - ``destroyed``
     - Destroyed / Removed
   * - ``seasonal_dry``
     - Seasonal Dry
   * - ``flooded``
     - Flooded / Inaccessible

Habitat Status Change Reason (HAB-UPD)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

List ``reason_list``, used in ``HAB-UPD``.

.. list-table::
   :widths: 18 82
   :header-rows: 1

   * - Code
     - Label
   * - ``natural_drying``
     - Natural drying
   * - ``drainage``
     - Drainage / Filled
   * - ``construction``
     - Construction / Development
   * - ``agriculture``
     - Agricultural activity
   * - ``flooding``
     - Flooding
   * - ``other``
     - Other

Adult Mosquito Collection Codes
-------------------------------

Trap Collection Method (TRAP-REG)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

List ``collection_method``, used in ``TRAP-REG``.

CO\ :sub:`2` bait (``co2_bait``) is asked only for ``CDC``. Methods not in this list, such as the Muirhead-Thomson pit trap, can be recorded as ``other`` with the method typed in ``method_other``.

.. list-table::
   :widths: 18 82
   :header-rows: 1

   * - Code
     - Label
   * - ``DN``
     - Double Net
   * - ``CDC``
     - CDC Light Trap
   * - ``RB``
     - Resting Bucket
   * - ``PKP``
     - Prokopack Aspirator
   * - ``BGS``
     - BG Sentinel
   * - ``other``
     - Other

Trap Placement (TRAP-REG)
~~~~~~~~~~~~~~~~~~~~~~~~~

List ``location_type``, used in ``TRAP-REG``.

.. list-table::
   :widths: 18 82
   :header-rows: 1

   * - Code
     - Label
   * - ``IN``
     - Indoor
   * - ``OUT``
     - Outdoor

Outdoor Placement (TRAP-REG)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

List ``outdoor_context``, used in ``TRAP-REG``.

.. list-table::
   :widths: 18 82
   :header-rows: 1

   * - Code
     - Label
   * - ``1``
     - Within 10 m of the house (peridomestic)
   * - ``2``
     - Other outdoor site

Human-Mosquito Contact Method (HH-BEH)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

List ``beh_method``, used in ``HH-BEH``.

.. list-table::
   :widths: 18 82
   :header-rows: 1

   * - Code
     - Label
   * - ``1``
     - DN-Mini
   * - ``2``
     - HLC

Sampling Method in the Shipment Manifest (SPEC-HND)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

List ``sampling_method``, used in ``SPEC-HND``.

This list uses numbers, while TRAP-REG uses letter codes for the same trap types.

.. list-table::
   :widths: 18 82
   :header-rows: 1

   * - Code
     - Label
   * - ``1``
     - Double net
   * - ``2``
     - CDC
   * - ``3``
     - Resting bucket
   * - ``4``
     - Prokopack
   * - ``5``
     - BG Sentinel
   * - ``6``
     - Other (write in)
   * - ``7``
     - Larval

Collection Origin (SPEC-SRT)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

List ``origin``, used in ``SPEC-SRT``.

.. list-table::
   :widths: 18 82
   :header-rows: 1

   * - Code
     - Label
   * - ``1``
     - Trap catch
   * - ``2``
     - Adult reared from larvae

Abdominal Physiological Status (SPEC-SRT)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

List ``abd_status``, used in ``SPEC-SRT``.

Females are counted in ``an_female_unfed``, ``an_female_partly_fed``, ``an_female_fed``, ``an_female_semigravid`` and ``an_female_gravid``; the same codes label female tubes (``an_abd``, ``cul_abd``). The form splits the fed category of SOP 1.1.1 into partly fed (``PF``) and fully fed (``FD``); adults reared from larvae are recorded with ``origin`` = ``2`` instead of a status.

.. list-table::
   :widths: 14 22 64
   :header-rows: 1

   * - Code
     - Label
     - Description
   * - ``UF``
     - Unfed
     - Abdomen flat, no blood visible.
   * - ``PF``
     - Partly fed
     - Abdomen partly filled with blood.
   * - ``FD``
     - Fully fed
     - Abdomen distended; bright to dark red blood fills most of the abdomen.
   * - ``SG``
     - Semi-gravid
     - Abdomen partly white with developing eggs and some digested blood remaining.
   * - ``GV``
     - Gravid
     - Abdomen white with eggs visible; blood fully digested.

Tube Sex (SPEC-SRT)
~~~~~~~~~~~~~~~~~~~

List ``tube_sex``, used in ``SPEC-SRT``.

.. list-table::
   :widths: 18 82
   :header-rows: 1

   * - Code
     - Label
   * - ``M``
     - Male
   * - ``F``
     - Female

Tube Sample Type (SPEC-SRT)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

List ``sample_type``, used in ``SPEC-SRT``. The paper layout codes them ``1`` = Individual, ``2`` = Pool.

.. list-table::
   :widths: 18 82
   :header-rows: 1

   * - Code
     - Label
   * - ``individual``
     - Individual
   * - ``pool``
     - Pool (multiple)

Mosquito Species (SPEC-SRT, SPEC-DIS)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Lists ``anopheles_species`` (``SPEC-SRT``, ``SPEC-DIS``) and ``culicine_species`` (``SPEC-SRT``).

Mosquitoes are identified to the lowest reliable taxonomic level (species complex where possible) with an approved morphological key; uncertain specimens are recorded as uncertain or unidentified. Genera recorded: *Anopheles*, *Culex*, *Aedes*, *Mansonia*, *Coquillettidia*, *Uranotaenia* and others (SOP 1.1.1). In the example forms, species codes combine the genus and species, for example ``an_funestus``, ``cx_pipiens`` and ``ae_aegypti``, and ``other`` lets the field worker type a name. Each node uses the species list for its own area.

Dissection Codes (SPEC-DIS)
---------------------------

Midgut Content
~~~~~~~~~~~~~~

List ``midgut_status``, used in ``SPEC-DIS``.

.. list-table::
   :widths: 14 22 64
   :header-rows: 1

   * - Code
     - Label
     - Description
   * - ``nb``
     - No blood
     - No blood visible in the midgut.
   * - ``fb``
     - Fresh blood
     - Fresh red blood present.
   * - ``bb``
     - Brown blood
     - Brown or darkened (digested) blood present.

Spermatheca (Insemination)
~~~~~~~~~~~~~~~~~~~~~~~~~~

List ``spermatheca_status``, used in ``SPEC-DIS``.

.. list-table::
   :widths: 18 82
   :header-rows: 1

   * - Code
     - Label
   * - ``positive``
     - Positive (sperm present)
   * - ``negative``
     - Negative (no sperm)

Parity (Detinova)
~~~~~~~~~~~~~~~~~

List ``parity_status``, used in ``SPEC-DIS``.

.. list-table::
   :widths: 14 22 64
   :header-rows: 1

   * - Code
     - Label
     - Description
   * - ``parous``
     - Parous
     - Ovarian tracheole skeins uncoiled and stretched out: the female has laid at least one batch of eggs.
   * - ``nulliparous``
     - Nulliparous
     - Ovarian tracheoles tightly coiled into skeins: the female has never laid eggs.

Egg Development Stage (Christophers)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

List ``egg_stage``, used in ``SPEC-DIS``.

.. list-table::
   :widths: 14 22 64
   :header-rows: 1

   * - Code
     - Label
     - Description
   * - ``stage1``
     - I
     - Small round follicles, transparent, no yolk granules.
   * - ``stage2e``
     - IIe
     - Early stage II: fine yolk granules appearing around the nucleus.
   * - ``stage2``
     - II
     - Oval follicles; yolk fills up to half of the follicle.
   * - ``stage3``
     - III
     - Elongated follicles; yolk fills more than half to three-quarters of the follicle.
   * - ``stage4``
     - IV
     - Cylindrical follicles; yolk fills almost the whole follicle.
   * - ``stage5``
     - V
     - Mature eggs with floats, ready to be laid.

Specimen Condition
~~~~~~~~~~~~~~~~~~

List ``specimen_condition``, used in ``SPEC-DIS``.

.. list-table::
   :widths: 18 82
   :header-rows: 1

   * - Code
     - Label
   * - ``fresh``
     - Fresh
   * - ``dry``
     - Dry

Sac stage (``sac_stage``, 0 to 7), maximum dilatations (``max_dilatation``, 0 to 5) and wing length (``wing_length``, mm) are entered as numbers.

Sample Handover Codes (SPEC-HND)
--------------------------------

Preservation Medium at Dispatch
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

List ``medium``, used in ``SPEC-HND``.

Frozen storage is recorded in the free-text storage condition, not as a medium. DNA/RNA Shield and Trizol-LS, the approved substitutes for RNAlater, are recorded as ``99`` (Other).

.. list-table::
   :widths: 18 82
   :header-rows: 1

   * - Code
     - Label
   * - ``1``
     - Ethanol
   * - ``2``
     - RNAlater
   * - ``3``
     - Silica
   * - ``0``
     - None
   * - ``99``
     - Other (write in)

Specimen Category
~~~~~~~~~~~~~~~~~

List ``specimen_category``, used in ``SPEC-HND``.

.. list-table::
   :widths: 18 82
   :header-rows: 1

   * - Code
     - Label
   * - ``1``
     - Anopheles female
   * - ``2``
     - Anopheles male
   * - ``3``
     - Culicine
   * - ``4``
     - Larval
   * - ``5``
     - Parts
   * - ``99``
     - Other taxa or category (write in)

Cold Chain Breach Indicator
~~~~~~~~~~~~~~~~~~~~~~~~~~~

List ``cold_chain``, used in ``SPEC-HND``.

.. list-table::
   :widths: 18 82
   :header-rows: 1

   * - Code
     - Label
   * - ``1``
     - No breach (intact)
   * - ``2``
     - Breach / spike

Physical Integrity
~~~~~~~~~~~~~~~~~~

List ``integrity``, used in ``SPEC-HND``.

.. list-table::
   :widths: 18 82
   :header-rows: 1

   * - Code
     - Label
   * - ``1``
     - Intact
   * - ``2``
     - Leak / damage

Laboratory Intake Status
~~~~~~~~~~~~~~~~~~~~~~~~

List ``intake``, used in ``SPEC-HND``.

.. list-table::
   :widths: 18 82
   :header-rows: 1

   * - Code
     - Label
   * - ``1``
     - Accepted
   * - ``2``
     - Hold / reject

Environmental Codes
-------------------

Weather at Trap Start and End (ENV-OBS)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

List ``weather``, used in ``ENV-OBS``.

``none`` cannot be combined with other options.

.. list-table::
   :widths: 18 82
   :header-rows: 1

   * - Code
     - Label
   * - ``rainy``
     - Rainy
   * - ``windy``
     - Windy
   * - ``cold``
     - Cold
   * - ``warm``
     - Warm
   * - ``none``
     - None of these (calm, dry)
   * - ``other``
     - Other

Measurement Method (ENV-OBS)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

List ``measurement_method``, used in ``ENV-OBS``.

.. list-table::
   :widths: 18 82
   :header-rows: 1

   * - Code
     - Label
   * - ``1``
     - Automated logger
   * - ``2``
     - Manual meter

Data Logger Placement (ENV-OBS)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

List ``logger_placement``, used in ``ENV-OBS``.

.. list-table::
   :widths: 18 82
   :header-rows: 1

   * - Code
     - Label
   * - ``1``
     - Indoor
   * - ``2``
     - Outdoor

Data Logger Download Status (ENV-OBS)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

List ``download_status``, used in ``ENV-OBS``.

.. list-table::
   :widths: 18 82
   :header-rows: 1

   * - Code
     - Label
   * - ``1``
     - Pass
   * - ``0``
     - Fail

Extreme Weather Event Type (ENV-EXT)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

List ``event_type``, used in ``ENV-EXT``.

The event types match the SOP 2.1 variable table.

.. list-table::
   :widths: 18 82
   :header-rows: 1

   * - Code
     - Label
   * - ``1``
     - Earthquake
   * - ``2``
     - Extreme temperature
   * - ``3``
     - Flood
   * - ``4``
     - Storm / Cyclones
   * - ``5``
     - Wildfire
   * - ``6``
     - Drought
   * - ``7``
     - Other (specify)

Extreme Event Severity (ENV-EXT)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

List ``severity``, used in ``ENV-EXT``.

.. list-table::
   :widths: 18 82
   :header-rows: 1

   * - Code
     - Label
   * - ``1``
     - Low
   * - ``2``
     - Moderate
   * - ``3``
     - Severe
   * - ``4``
     - Extreme

Assessment Timing (ENV-EXT)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

List ``assessment_timing``, used in ``ENV-EXT``.

.. list-table::
   :widths: 18 82
   :header-rows: 1

   * - Code
     - Label
   * - ``1``
     - Immediate (within 48 hours)
   * - ``2``
     - Post-Event

Trapping Continuity (ENV-EXT)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

List ``trapping_continuity``, used in ``ENV-EXT``.

.. list-table::
   :widths: 18 82
   :header-rows: 1

   * - Code
     - Label
   * - ``1``
     - Trapping continuing normally
   * - ``2``
     - Partial operation
   * - ``3``
     - Full pause

Aquatic Habitat & Larval Codes
------------------------------

Habitat Type
~~~~~~~~~~~~

List ``habitat_type``, used in ``HAB-REG``, ``HH-REG``, ``HH-UPD``.

Codes 1 to 17 match SOP 3.1. The forms add 18 Rice field, 19 Floodplain, 20 Stream pool and 21 Spring-fed pool, and use 22 for Other (18 in SOP 3.1).

.. list-table::
   :widths: 18 82
   :header-rows: 1

   * - Code
     - Label
   * - ``1``
     - Swamp/Marsh
   * - ``2``
     - Cultivated swamp
   * - ``3``
     - River fringe
   * - ``4``
     - Puddle
   * - ``5``
     - Pool
   * - ``6``
     - Borrow pit
   * - ``7``
     - Drain/Ditch
   * - ``8``
     - Cemented pit
   * - ``9``
     - Mining pit
   * - ``10``
     - Movable container
   * - ``11``
     - Fixed water tank
   * - ``12``
     - Old tyre
   * - ``13``
     - Seasonal river pan
   * - ``14``
     - Flower pot
   * - ``15``
     - Tree hole
   * - ``16``
     - Gutter
   * - ``17``
     - Pond
   * - ``18``
     - Rice field
   * - ``19``
     - Floodplain
   * - ``20``
     - Stream pool
   * - ``21``
     - Spring-fed pool
   * - ``22``
     - Other (specify)

Natural or Artificial (HAB-REG)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

List ``natural_artificial``, used in ``HAB-REG``.

.. list-table::
   :widths: 18 82
   :header-rows: 1

   * - Code
     - Label
   * - ``1``
     - Natural
   * - ``2``
     - Artificial

Water Type / Permanence
~~~~~~~~~~~~~~~~~~~~~~~

List ``permanence``, used in ``HAB-REG``, ``HAB-SRV``.

.. list-table::
   :widths: 18 82
   :header-rows: 1

   * - Code
     - Label
   * - ``1``
     - Temporary
   * - ``2``
     - Semi-permanent
   * - ``3``
     - Permanent

Water Colour (HAB-SRV)
~~~~~~~~~~~~~~~~~~~~~~

List ``water_colour``, used in ``HAB-SRV``.

.. list-table::
   :widths: 18 82
   :header-rows: 1

   * - Code
     - Label
   * - ``1``
     - Clear
   * - ``2``
     - Coloured / Turbid
   * - ``3``
     - Polluted
   * - ``4``
     - Other

Water Source (HAB-SRV)
~~~~~~~~~~~~~~~~~~~~~~

List ``water_source``, used in ``HAB-SRV``.

.. list-table::
   :widths: 18 82
   :header-rows: 1

   * - Code
     - Label
   * - ``1``
     - Rainwater
   * - ``2``
     - Ground, spring or stream water
   * - ``3``
     - Human supply (tap, leak, irrigation)

Water Movement (HAB-SRV)
~~~~~~~~~~~~~~~~~~~~~~~~

List ``water_movement``, used in ``HAB-SRV``.

.. list-table::
   :widths: 18 82
   :header-rows: 1

   * - Code
     - Label
   * - ``1``
     - Stagnant
   * - ``2``
     - Slow
   * - ``3``
     - Fast

Shade over Habitat (HAB-SRV)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

List ``shade``, used in ``HAB-SRV``.

.. list-table::
   :widths: 18 82
   :header-rows: 1

   * - Code
     - Label
   * - ``0``
     - None
   * - ``1``
     - Partial
   * - ``2``
     - Heavy (Fully shaded)

Vegetation Type (HAB-SRV)
~~~~~~~~~~~~~~~~~~~~~~~~~

List ``vegetation_type``, used in ``HAB-SRV``.

.. list-table::
   :widths: 18 82
   :header-rows: 1

   * - Code
     - Label
   * - ``0``
     - None
   * - ``1``
     - Submerged
   * - ``2``
     - Floating
   * - ``3``
     - Emergent
   * - ``4``
     - Other

Vegetation Quantity (HAB-SRV)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

List ``vegetation_qty``, used in ``HAB-SRV``.

.. list-table::
   :widths: 18 82
   :header-rows: 1

   * - Code
     - Label
   * - ``0``
     - None
   * - ``1``
     - Scarce (<25%)
   * - ``2``
     - Moderate (25-50%)
   * - ``3``
     - Abundant (>50%)

Algal Quantity (HAB-SRV)
~~~~~~~~~~~~~~~~~~~~~~~~

List ``algae_qty``, used in ``HAB-SRV``.

.. list-table::
   :widths: 18 82
   :header-rows: 1

   * - Code
     - Label
   * - ``0``
     - None
   * - ``1``
     - Scarce
   * - ``2``
     - Moderate
   * - ``3``
     - Abundant

Algae Type (HAB-SRV)
~~~~~~~~~~~~~~~~~~~~

List ``algae``, used in ``HAB-SRV``.

.. list-table::
   :widths: 18 82
   :header-rows: 1

   * - Code
     - Label
   * - ``0``
     - None
   * - ``1``
     - Filamentous
   * - ``2``
     - Green
   * - ``3``
     - Blue-green
   * - ``4``
     - Brown
   * - ``5``
     - Other (specify)
   * - ``6``
     - Unidentifiable

Environment around Habitat (HAB-SRV)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

List ``environment``, used in ``HAB-SRV``.

.. list-table::
   :widths: 18 82
   :header-rows: 1

   * - Code
     - Label
   * - ``1``
     - Shrub/Bush
   * - ``2``
     - Grassland
   * - ``3``
     - Swamp
   * - ``4``
     - Cultivated field
   * - ``5``
     - Residential
   * - ``6``
     - Cattle grazing
   * - ``7``
     - Forest
   * - ``8``
     - Urban
   * - ``9``
     - Other (specify)

Season (HAB-SRV)
~~~~~~~~~~~~~~~~

List ``season``, used in ``HAB-SRV``.

.. list-table::
   :widths: 18 82
   :header-rows: 1

   * - Code
     - Label
   * - ``1``
     - Dry
   * - ``2``
     - Rainy
   * - ``3``
     - Other

Habitat or Container (HAB-SRV)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

List ``sample_unit``, used in ``HAB-SRV``.

.. list-table::
   :widths: 18 82
   :header-rows: 1

   * - Code
     - Label
   * - ``1``
     - Registered habitat (HAB-REG)
   * - ``2``
     - Container

Sampling Technique (HAB-SRV)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

List ``sampling_technique``, used in ``HAB-SRV``.

.. list-table::
   :widths: 18 82
   :header-rows: 1

   * - Code
     - Label
   * - ``dipper``
     - Standard Dipper (350 mL)
   * - ``bucket``
     - 10L Bucket
   * - ``pipette``
     - Baster / pipette
   * - ``whole``
     - Whole accessible volume

Larval Taxa (HAB-SRV)
~~~~~~~~~~~~~~~~~~~~~

List ``larval_taxa``, used in ``HAB-SRV``.

Each code is also the prefix of that taxon's per-dip count fields, for example ``gam_l12_input`` and ``gam_total``.

.. list-table::
   :widths: 18 82
   :header-rows: 1

   * - Code
     - Label
   * - ``gam``
     - An. gambiae
   * - ``fun``
     - An. funestus
   * - ``oan``
     - Other Anopheline
   * - ``cul``
     - Culex
   * - ``aed``
     - Aedes
   * - ``man``
     - Mansonia
   * - ``oth``
     - Other taxon

Aquatic Predators (HAB-SRV)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

List ``predator_list``, used in ``HAB-SRV``.

Each code is also the prefix of that predator's per-dip count field, for example ``dragonfly_dip_input`` and ``dragonfly_total``.

.. list-table::
   :widths: 14 22 64
   :header-rows: 1

   * - Code
     - Label
     - Description
   * - ``dragonfly``
     - Dragonflies
     - Dragonfly nymphs (Odonata: Anisoptera).
   * - ``damselfly``
     - Damselflies
     - Damselfly nymphs (Odonata: Zygoptera).
   * - ``diving_beetle``
     - Diving beetles
     - Predatory diving beetles (Dytiscidae).
   * - ``backswimmer``
     - Backswimmers
     - Backswimmers (Notonectidae).
   * - ``water_boatman``
     - Water boatman
     - Water boatmen (Corixidae).
   * - ``water_scorpion``
     - Water scorpion
     - Water scorpions (Nepidae).
   * - ``giant_water_bug``
     - Giant water bugs
     - Giant water bugs (Belostomatidae).
   * - ``tadpole``
     - Tadpoles
     - Tadpoles (anuran larvae).
   * - ``copepod``
     - Copepods
     - Copepods.
   * - ``other_predator``
     - Other predators
     - Any other aquatic predator, including small fish.

Larval Preservation Method (HAB-SRV)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

List ``preservation``, used in ``HAB-SRV``.

.. list-table::
   :widths: 18 82
   :header-rows: 1

   * - Code
     - Label
   * - ``1``
     - Live transport (rearing vial)
   * - ``2``
     - >70% Ethanol
