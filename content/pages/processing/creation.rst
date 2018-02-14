Creating a study dataset
************************
:order: 410

Start off with a clone of https://github.com/psychoinformatics-de/cbbs-imaging-container-import,
which also provides additional tools apart from sheer creation.

Then run ``singularity run cbbs-imaging-container-import/cbbs-imaging.simg create [TARGET-DIR]``.
If you don't provide a target dir, the dataset will be created in the current working directory.

Adding an MRI session
---------------------

The above mentioned container also provides a command to import a tarball for a session.
This will result in a subdataset with the DICOMs in it, that provides the DICOM metadata for easy access via `datalad`.

To import such a tarball run ``singularity run cbbs-imaging-container-import/cbbs-imaging.simg import [TARBALL]``.
Note, that TARBALL needs to be an absolute path at the moment.
A session name like `af29_0678` will be derived from the dicoms' metadata and a subdirectory with that is created.
In that subdirectory you should then find a `studyspec.json`, which is needed for conversion later on and a subdirectory `dicoms`, which is in fact a subdataset containing the actual dicoms.
