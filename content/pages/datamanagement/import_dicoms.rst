Import DICOMs
*************
:order: 420

The above mentioned container also provides a command to import a tarball for a session.
This will result in a subdataset with the DICOMs in it, that provides the DICOM metadata for easy access via `datalad`.

To import such a tarball just run
``singularity run [--bind=/path/to/tarball] INSTALL-DIR/cbbs-imaging.simg import [TARBALL]``
from within your study dataset. You don't need to be at its root directory, but you need to make sure, you aren't accidentally in a subdataset. Therefore the study dataset's root is a safe practice to follow.

Note, that TARBALL needs to be an absolute path at the moment.
Particularly if TARBALL is located outside your HOME directory, you may need to provide its location to the container via the `--bind` option.


A session name like `af29_0678` will be derived from the dicoms' metadata and a subdirectory with that is created.
In that subdirectory you should then find a `studyspec.json`, which is needed for conversion later on and a subdirectory `dicoms`, which is in fact a subdataset containing the actual dicoms.
