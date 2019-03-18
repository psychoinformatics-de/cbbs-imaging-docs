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

- Milestone: Conversion to BIDS data structure [**BETA RELASE AVAILABLE**]
  (https://github.com/psychoinformatics-de/datalad-hirni)

- Milestone: Analysis pipelines [**IN PROGRESS**]

  - Support for BIDS-app compatible analysis implementations

  - Community demands (based on a survey):

    - decoding analysis

    - RSA analysis

    - automated, versatile pre-processing options

    - cortical surface reconstruction

    - denoising (physiological artifact detection/correction)

    - standard GLM analysis (FSL)

    - automated quality control analysis

- ...

Accomplished milestones
=======================

- Developed a software package for remote/parallel execution of arbitrary
  algorithm on batch systems, and/or grid/cloud computing infrastructure.
  (https://github.com/datalad/datalad-htcondor). This is the technological
  foundation of data analysis pipeline execution with comprehensive provenance
  capture support.

- Developed framework for the rapid construction of tailored graphical user interfaces
  (GUI) for controlling and data entry via a REST-API for browser-based interaction
  with datasets (https://github.com/datalad/datalad-webapp). Targeted web user interfaces  (WUI) have been implemented for:

  - study metadata entry

  - curation of all digital artifacts of an imaging data acqusitions (medical images,
    physiological recordings, stimulation and behavioral response logs) into a
    concise, indexable, and archivable representation of a study

- Developed open-source DataLad extension for command execution in containerized
  environments that are tracked alongside other dataset content:
  https://github.com/datalad/datalad-container

- Developed a dataset structure for studies

  - binds together all produced data: MRI, behavioral log files, other
    modalities, results

  - referencing a well-defined software environment for each step of data
    processing from importing raw data to data conversion to analyses in order
    to enable full computational reproducibility a point immediately after raw
    data acquisition.

- Automatic DICOM import and metadata extraction

  - DICOM metadata can be queried across all acquisitions of a study, made by a
    particular scanner, or at a given institution (see `demo
    <{filename}datamanagement/demo_scandb.rst>`_).
