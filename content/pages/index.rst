Welcome
*******
:save_as: index.html
:url: index.html
:status: hidden
:order: 001

Add high-level description on what this does, for whom, under which conditions.

Roadmap
=======

- Milestone: Support for BIDS-app compatible analysis implementations

- Milestone: Conversion to BIDS data structure [**IN PROGRESS**]

  - Support for a study specification to identify simultaneously acquired data, and to associate
    particular conversion procedures with individual data formats.

- Milestone: Automatic DICOM import and metadata extraction [**DONE**]

  - DICOM metadata can be queried across all acquisitions of a study, made by a particular
    scanner, or at a given institution.

  - Import and extraction are performed in a `common computational environment for raw data handling
    <{filename}containers/rawimport.rst>`_ that is identical regardless of the particular machine the
    procedure is performed on.
