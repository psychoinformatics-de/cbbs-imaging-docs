Data Management
***************
:order: 400

The fundamental concept of this platform is that data are first transformed
into a standard layout using common file formats, so that all processing
pipelines can expect a deterministic, well described data structure. This setup
enables the development of data processing components that are agnostic of the
peculiarities of individual studies, as long as all relevant aspects of a study
are properly described. The necessary data conversion and layout are performed
largely automatic. The procedures are tuned for data acquired in Magdeburg,
but with minor extra effort data from other sources can be processed too.

For each study the following steps will be performed:

1. Initial study setup: `create a study raw dataset <{filename}datamanagement/study_setup.rst>`_

2. Import a new acquisition (repeated as necessary):

   - `Import a DICOM dataset <{filename}datamanagement/import_dicoms.rst>`_
   - `Import other data modalities <{filename}datamanagement/import_other.rst>`_

3. Complete study description (if necessary):

   - Identify data that were acquired simultaneously during an acquisition

   - Associate stimulation and behavior logs with (MR) data acquisitions

   - Identify data formats/converters for non-standard acquisitions (e.g. custom hardware)

4. Convert raw data into the common data structure

   - Verify result of automatic conversion (automatic validation tools are available)

5. Apply analysis procedure
