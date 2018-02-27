Import DICOMs
*************
:order: 420

The `raw data import <{filename}/pages/containers/rawimport.rst>`_ container
also provides a command to import a DICOM tarball for a session into a `study
dataset <{filename}study_setup.rst>`_. To import such a tarball just run::

  singularity run [--bind=/path/to/tarball] INSTALL-DIR/cbbs-imaging.simg import [TARBALL]

from within your study dataset.  This will result in a subdataset with the
DICOMs in it, that provides the DICOM metadata for easy access via `datalad`.

Note, that TARBALL needs to be an absolute path at the moment.  Particularly if
TARBALL is located outside your HOME directory, you may need to provide its
location to the container via the `--bind` option, in case the tarball is on a
different (network) drive.

A session name like `xx99_0123` will be determined from the DICOM metadata
(`PatientID`) and a subdirectory with this name is created. The subdirectory
contains a `studyspec.json` file with session-related metadata (info on DICOM
series to convert to NIfTI, other simultaneously acquired data modalities),
and a subdirectory `dicoms/`, with all DICOM data and metadata.

DICOM subdatasets can be archived separately to, for example, build raw data
archives (for a lab, a scanner, an institution) that can be easily queried for
scan with particular properties (see `this demo <{filename}demo_scandb.rst>`_
for an example).
