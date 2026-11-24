SOP 2.4: Field Mosquito Processing & Handling Workflow
======================================================

This quick reference summarises specimen sorting, the downstream processing workflows, labelling and barcoding, and sample transfer from **VectorGrid SOP 2.4**.

1. Collection Days & Workflows
------------------------------
Routine monthly collections take place over three collection days, which do not need to be consecutive:

* **Days 1 and 2:** Mosquitoes follow the MIRS-to-amplicon-sequencing workflow.
* **Day 3:** Mosquitoes are processed separately, as pools, for viral pathogen screening (RT-PCR).

All specimens and pools must stay linked to their collection metadata: node, village, sampling location, indoor or outdoor collection, trap information, collection date, sex, physiological status and the lowest reliable morphological identification.

2. Sorting & Identification
---------------------------
* **Bench Hygiene:** Clean and disinfect benches with 80% ethanol. Process mosquitoes from one trap at a time.
* **Sorting:** Sort by district, village, sampling location, indoor or outdoor collection, trap or trap type, sex, physiological status and morphological identification. Identify each mosquito to the lowest reliable level with an approved key; record specimens that cannot be identified confidently as uncertain or unidentified.
* **Female Physiological Status:** Unfed (UF), Partly fed (PF), Fully fed (FD), Semi-gravid (SG) or Gravid (GV).
* **ODK recording:** Counts by species, sex and physiological status, tubes and bycatch (non-mosquito insects) are recorded on :doc:`../forms/spec_srt`, linked to the trap through the Collection ID. Females sent for fresh dissection are recorded on :doc:`../forms/spec_dis`.

3. MIRS & Amplicon Sequencing (Days 1 and 2)
--------------------------------------------
* **Killing:** Kill live mosquitoes with ethyl acetate or ethanol vapour (see the MIRS SOP).
* **Selection:** Select up to **300 individual mosquitoes per district per sampling month** (about 4 plates) for MIRS followed by amplicon sequencing. When more are available, prioritise blood-fed, unidentified or uncertain, and uncommon specimens, plus representative specimens across taxa, physiological states, villages, locations, trap types and indoor or outdoor collections.
* **MIRS Preparation:** Give each selected mosquito a unique specimen ID and store it singly in a labelled tube with fresh silica gel at 4 °C for two to three days before scanning.
* **MIRS Scanning:** Separate the head and thorax from the abdomen and scan them separately, linking each spectrum to the specimen ID with a suffix (``-HT`` head and thorax, ``-AB`` abdomen). Scan the abdomen only for blood-fed mosquitoes (blood-meal source).
* **Archive Pools:** Mosquitoes not selected are pooled by trap, house and location and stored in tubes with silica gel.
* **Amplicon Plates:** Pre-fill 96-well skirted plates with 100 µL of 95% to 100% ethanol per well. Place one mosquito (all recovered body parts) per well, filling column by column (A1 to H1, then A2 to H2), and seal each column with 8-strip caps. Update the plate map after each specimen. Plate adults separately from larvae.

4. Viral Pathogen Screening (Day 3)
-----------------------------------
* **Killing:** Immobilise mosquitoes by freezing at -20 °C for about 30 minutes or on dry ice. **Do not use ethyl acetate or ethanol vapour for virology specimens.** Keep mosquitoes cold (on ice packs) throughout sorting.
* **Pools:** 20 to 50 mosquitoes of the same taxon, trap or trap type, indoor or outdoor collection, village and district. Keep smaller pools rather than mixing categories, and record the reason. No pool may contain more than 50 mosquitoes.
* **Pool ID:** Assign before transfer, for example ``OBS01-20260911-P001`` (site code - collection date - pool number), with one pool per 1.5 mL tube (or larger tube for big pools).
* **Preservation:** RNAlater; DNA/RNA Shield or Trizol-LS are approved substitutes. Without these reagents, keep an unbroken cold chain on dry ice or in a dry shipper until the samples reach a -80 °C freezer.

5. Labelling, Barcoding & Plate Mapping
---------------------------------------
Each country and node has its own unique identifier for labelling plates:

.. code-block:: text

   [Country Code][Node Code] [Plate / Box Number]

Example:

* ``TZDS 0001``: Country: Tanzania (``TZ``), Node: Dar es Salaam (``DS``), Plate: 0001.

Plate and well tracking:

* **Plate Edges:** Label one long and one short edge with the observatory node code (for example ``OBS01``), plate number (for example ``P005``), date and barcode where available.
* **Well Register:** The specimen in each well (rows A to H, columns 1 to 12, entered as ``A1`` to ``H12``) is recorded on a data sheet that links its unique Specimen ID to its collection metadata. Pools are recorded with a unique Pool ID and the number of mosquitoes.
* **ODK recording:** :doc:`../forms/spec_srt` records each tube or well entry with its storage box or plate barcode and position, gives each tube an automatic label (Collection ID - species - sex - abdominal status - tube number), and records the specimen register or plate map ID.
* **Barcodes:** Where possible, attach a 1D/2D barcode label next to the written ID on each plate, and at trap sites.

6. Packaging, Transfer & Chain of Custody
-----------------------------------------
* **Before Transfer:** Check that every plate or tube is fully labelled and sealed. For shipping, wrap plates with parafilm and plastic wrap, place them in a labelled sealable bag and keep them upright in a cooled box.
* **Manifest and Sign-off:** Fill in a sample manifest or chain-of-custody log (plate ID, source site, trap ID, date and time, preservative). Everyone who handles the samples (field, courier, laboratory) signs and records the date and time. In the ODK forms this is :doc:`../forms/spec_hnd`.
* **Storage Conditions:** Samples in RNAlater, DNA/RNA Shield or Trizol-LS can travel at ambient temperature for weeks; ethanol samples degrade faster when warm. On receipt, check for leaks, evaporation and label legibility, and refrigerate or freeze plates (-20 °C or below) until analysis.
