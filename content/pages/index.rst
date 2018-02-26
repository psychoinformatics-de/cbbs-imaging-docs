The CBBS imaging platform
*************************
:save_as: index.html
:url: index.html
:status: hidden
:order: 001

This platform aims to provide open-source tools and services for MR data
management and analysis. One major goal is to streamline routine data
processing to maximize efficiency (time-to-results), minimize human error, and
meet today's standards regarding the computational reproducibility of imaging
data analysis.  Users can utilize this platform to meet the preproducibility
and availability requirements of funders and publishers. Moreover, the platform
employs a standardized interface to apply tailored implementations of
cutting-edge data analysis technique to a wide variety of datasets acquired in
Magdeburg in order to facilitate the development and dissemination of novel
research methods.


Roadmap
=======

- Milestone: Automatic DICOM import and metadata extraction [**DONE**]

  - DICOM metadata can be queried across all acquisitions of a study, made by a
    particular scanner, or at a given institution.

  - Import and extraction are performed in a `common computational environment
    for raw data handling <{filename}containers/rawimport.rst>`_ that is
    identical regardless of the particular machine the procedure is performed
    on.

- Milestone: Conversion to BIDS data structure [**IN PROGRESS**]

  - Support for a study specification to identify simultaneously acquired data,
    and to associate particular conversion procedures with individual data
    formats.

- Milestone: Support for BIDS-app compatible analysis implementations

- Milestone: Analysis pipelines

  - Upcoming event: coding sprint at BrainHack Magdeburg (May 2018)

  - Community demands (based on a survey):

    - decoding analysis

    - RSA analysis

    - automated, versatile pre-processing options

    - cortical surface reconstruction

    - denoising (physiological artifact detection/correction)

    - standard GLM analysis (FSL)

    - automated quality control analysis

- ...

