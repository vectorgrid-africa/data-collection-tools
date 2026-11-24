Trap Status Update Form
=======================

**Form Code:** ``TRAP-UPD`` | **Form ID:** ``vg_trap_upd`` | **Version:** ``2026112401`` | **Component:** Adult Mosquito Sampling | **SOP Links:** :doc:`SOP 2.2 <../sops/sop_2_2>`

The Trap Status Update Form changes the status of a registered trap (active, malfunctioned or retired) and records the reason and any corrective action, without re-entering the trap's details.

How This Form Works
-------------------

* **Entity:** Updates the selected record in the ``traps`` entity list. Properties written: ``last_update_date``, ``status``, ``status_reason``.
* Select the district, then the trap from the ``traps`` entity list. The form shows the Trap ID, node and current status.
* Status values: ``active``, ``malfunctioned`` and ``retired``. A reason is always required.
* Changes overwrite the trap record. SPEC-SRT and SPEC-DIS list only ``active`` traps.

Section 1: Trap Selection
-------------------------

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

       *Hint:* Filter traps by district
   * - ``trap``
     - Select record
     - Yes
     - Select trap to update

       Pick a record from the ``traps`` entity list (filtered by district)
   * - ``node_code``
     - Calculated
     - Auto
     - Taken from the selected ``traps`` record (property ``node_code``)
   * - ``trap_id``
     - Calculated
     - Auto
     - Taken from the selected ``traps`` record (property ``trap_id``)
   * - ``previous_status``
     - Calculated
     - Auto
     - Taken from the selected ``traps`` record (property ``status``)

Section 2: Status Update
------------------------

.. list-table::
   :widths: 24 13 9 54
   :header-rows: 1

   * - Field Name
     - Type
     - Required
     - Question, Choices & Logic
   * - ``update_date``
     - Date
     - Yes
     - Date of update

       *Check:* ``value <= today()``

       *Default:* today

       *Saved to entity property* ``last_update_date``
   * - ``new_status``
     - Select one
     - Yes
     - New status

       ``active`` = Active; ``malfunctioned`` = Malfunctioned; ``retired`` = Retired

       *Saved to entity property* ``status``
   * - ``status_reason``
     - Text
     - Yes
     - Reason for status change

       *Hint:* e.g., Battery dead, Trap damaged, No longer needed

       *Saved to entity property* ``status_reason``

Section 3: Collector & Notes
----------------------------

.. list-table::
   :widths: 24 13 9 54
   :header-rows: 1

   * - Field Name
     - Type
     - Required
     - Question, Choices & Logic
   * - ``collector_id``
     - Text
     - Yes
     - Collector ID (registered staff ID)

       *Hint:* Your registered staff ID, not your name
   * - ``notes``
     - Text
     - No
     - Additional notes

       *Hint:* e.g. Battery replaced on site
