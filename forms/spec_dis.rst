Mosquito Dissection & Parity Form
==================================

**Form Code:** ``SPEC-DIS`` | **Study Component:** Adult Vector Surveillance

The Mosquito Dissection & Parity Form records individual female *Anopheles* dissections for ovarian tracheole coiling (parity), Christophers egg stage, insemination, max dilatations, wing length, and storage well mapping.

Section 1: Dissection Bench & Source Links
------------------------------------------

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
     - Observatory Node Code
   * - ``village_id``
     - Text
     - Yes
     - Village Identifier
   * - ``household_id``
     - Text
     - Optional
     - Source Household ID
   * - ``trap_id``
     - Text
     - Optional
     - Source Trap ID
   * - ``collection_record_id``
     - Text
     - Yes
     - Linked from Collection & Sorting form
   * - ``dissection_date``
     - Date
     - Yes
     - Date of bench dissection
   * - ``dissector_id``
     - Text
     - Yes
     - Technician / Dissector ID
   * - ``dissection_start_time``
     - Time
     - Yes
     - Dissection start time

Section 2: Specimen Dissections
-------------------------------
Record for each dissected female specimen:

.. list-table::
   :widths: 20 15 15 15 15 20
   :header-rows: 1

   * - Specimen ID
     - Species
     - Blood
     - Insem.
     - Parity
     - Plate Well
   * - Unique Code
     - 1=gam, 2=fun, 3=oth
     - 1=Unfed, 2=Fresh, 3=Brown
     - 1=Pos, 0=Neg
     - 1=Parous, 2=Nulliparous
     - Box / Well ID

Section 3: Diagnostic Parameter Codes
-------------------------------------
- **Species:** 1=*An. gambiae s.l.*, 2=*An. funestus group*, 3=*Other Anopheline*.
- **Midgut Blood Content:** 1=No blood (unfed), 2=Fresh blood, 3=Brown / digested blood.
- **Spermatheca Insemination:** 1=Positive (sperm present), 0=Negative (empty).
- **Ovarian Parity Status:** 1=Parous (uncoiled tracheoles), 2=Nulliparous (tightly coiled skeins).
- **Egg Stage:** Stages I, IIe, II, III, IV, V (Christophers staging).
- **Sac Stage:** Stages 0 to 7.
- **Max Dilatations:** Count (0 to 5).
- **Wing Length:** Measured length in millimeters.
- **Specimen Condition:** 1=Fresh (dissected immediately), 2=Dry (rehydrated).

Section 4: Dissection Summary & Totals
--------------------------------------
- Total Dissected (count)
- Total Parous (count)
- Total Nulliparous (count)
- Parity Rate (% = Total Parous / Total Dissected × 100)
