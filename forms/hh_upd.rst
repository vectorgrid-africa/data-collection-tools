Household Status Update Form
============================

**Form Code:** ``HH-UPD`` | **Study Component:** Household Surveillance | **SOP Links:** SOP 1.1, SOP 2.1

The Household Status Update Form records longitudinal changes to enrolled households across surveillance rounds. It audits household cohort operational status, structural dwelling modifications, occupant census changes, net acquisitions, vector control interventions, and domestic livestock alterations without re-recording fixed baseline geography.

Section 1: Node & Household Identification
------------------------------------------

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
     - Study Node Code
   * - ``village_id``
     - Text
     - Yes
     - Sentinel Village Identifier
   * - ``household_id``
     - Text
     - Yes
     - Household ID (links to ``HH-REG``)
   * - ``update_date``
     - Date
     - Yes
     - Date of status update visit
   * - ``surveillance_round``
     - Select One
     - Yes
     - 1=Routine, 2=Biannual
   * - ``collector_id``
     - Text
     - Yes
     - Field enumerator or team identifier

Section 2: Household Operational Status
---------------------------------------

.. list-table::
   :widths: 25 20 20 35
   :header-rows: 1

   * - Field Name
     - Type
     - Required
     - Description / Choice List
   * - ``hh_operational_status``
     - Select One
     - Yes
     - 1=Active, 2=Withdrew or refused, 3=Relocated or moved, 5=Temporarily inactive
   * - ``status_change_reason``
     - Text
     - No
     - Reason if withdrew, relocated, or inactive
   * - ``structural_changes``
     - Select One
     - Yes
     - Structural changes made to dwelling (1=Yes, 0=No changes)

Section 3: House Modifications Since Last Visit
-----------------------------------------------

.. list-table::
   :widths: 25 20 20 35
   :header-rows: 1

   * - Field Name
     - Type
     - Required
     - Description / Choice List
   * - ``house_type_updated``
     - Select One
     - Yes
     - 0=Unchanged, 1=Traditional, 2=Modern, 99=Other (specify)
   * - ``wall_material_altered``
     - Select One
     - Yes
     - Altered: 1=Yes, 0=No (If yes: 1=Mud, 2=Brick, 3=Cement blocks, 4=Thatch, 99=Other)
   * - ``roof_structure_altered``
     - Select One
     - Yes
     - Replaced: 1=Yes, 0=No (If yes: 1=Thatch, 2=Metal, 3=Tiles, 4=Concrete slab, 99=Other)
   * - ``eave_status_altered``
     - Select One
     - Yes
     - 0=No change, 1=Open, 2=Partly screened/blocked, 3=Fully screened, 4=Fully blocked, 99=Other
   * - ``ceiling_status_altered``
     - Select One
     - Yes
     - 1=Newly installed, 2=Removed or collapsed, 0=No change
   * - ``screening_condition_altered``
     - Select One
     - Yes
     - 1=Screens newly installed, 2=Screens damaged or removed, 0=No change
   * - ``additional_sleeping_rooms``
     - Select One
     - Yes
     - Additional sleeping rooms built (1=Yes, 0=No)
   * - ``total_rooms_count``
     - Integer
     - No
     - Current total room count
   * - ``sleeping_rooms_count``
     - Integer
     - No
     - Current sleeping room count

Section 4: Demographics, Bed Nets & Vector Control Updates
----------------------------------------------------------

.. list-table::
   :widths: 25 20 20 35
   :header-rows: 1

   * - Field Name
     - Type
     - Required
     - Description / Choice List
   * - ``total_occupants_night``
     - Integer
     - Yes
     - Total occupants sleeping in the dwelling last night
   * - ``males_occupants_night``
     - Integer
     - No
     - Male occupants sleeping last night
   * - ``females_occupants_night``
     - Integer
     - No
     - Female occupants sleeping last night
   * - ``new_nets_acquired``
     - Select One
     - Yes
     - New bed nets acquired since last round (1=Yes, 0=None)
   * - ``new_nets_count``
     - Integer
     - No
     - Number of new nets acquired
   * - ``vector_interventions_introduced``
     - Select One
     - Yes
     - New interventions introduced (1=Yes, 0=None; specify ITN, IRS, LSM, MDA-Ivermectin)
   * - ``livestock_enclosure_altered``
     - Select One
     - Yes
     - Livestock enclosure status (1=Newly constructed, 2=Removed or dismantled, 0=Unchanged)
   * - ``livestock_present``
     - Select One
     - Yes
     - Livestock kept near house (1=Yes, 0=No)
   * - ``livestock_types``
     - Select Multiple
     - No
     - Cattle, Goats, Chickens, Pigs, Other
   * - ``new_breeding_sites_nearby``
     - Select One
     - Yes
     - New water bodies observed within 100 meters (1=Yes, 0=None observed)
