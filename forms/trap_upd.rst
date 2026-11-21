Trap Status Update Form
=======================

**Form Code:** ``TRAP-UPD`` | **Study Component:** Adult Vector Surveillance | **SOP Links:** SOP 2.2

The Trap Status Update Form records operational status updates for registered surveillance traps. Field technicians use this form to record operational changes (active, malfunctioned, retired) and document maintenance actions without needing to re-record fixed GPS locations or trap specifications.

Section 1: Trap Location & Update Information
---------------------------------------------

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
   * - ``village_id``
     - Text
     - Yes
     - Sentinel Village Identifier
   * - ``update_date``
     - Date
     - Yes
     - Date of update
   * - ``collector_id``
     - Text
     - Yes
     - Collector / Team ID

Section 2: Trap Status Updates
------------------------------

A dynamic repeating group recording status updates for one or more traps:

.. list-table::
   :widths: 25 20 20 35
   :header-rows: 1

   * - Field Name
     - Type
     - Required
     - Description / Choice List
   * - ``trap_id``
     - Text
     - Yes
     - Trap Identifier (links to ``TRAP-REG``)
   * - ``new_status``
     - Select One
     - Yes
     - 1=Active, 2=Malfunctioned, 3=Retired
   * - ``status_change_reason``
     - Text
     - Yes
     - Reason for status change (battery failure, fan motor burnt, torn collection net, stolen, retired)
   * - ``additional_notes``
     - Text
     - No
     - Corrective action taken (battery replaced, spare parts fitted, redeployed)

Section 3: Field Verification
-----------------------------

- **Technician Name:** Full name or digital signature of the responsible technician.
- **Submission Timestamp:** Automated system time of status update record.
