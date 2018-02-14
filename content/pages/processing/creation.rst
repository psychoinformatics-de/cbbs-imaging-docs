Creating a study dataset
************************
:order: 410

Preparation
-----------
Start off by installing https://github.com/psychoinformatics-de/cbbs-imaging-container-import,
which also provides additional tools apart from sheer creation:
``datalad install -s https://github.com/psychoinformatics-de/cbbs-imaging-container-import [INSTALL-DIR]``

After successful installation run the following two commands:

``datalad siblings -d INSTALL_DIR add -s psydata --url http://psydata.ovgu.de/cbbs-imaging/conv-container/.git``
This will register the sibling hosted by OvGU, that serves as a data storage.

``datalad get INSTALL-DIR/cbbs-imaging.simg``
This one will finally get you the actual container.

Dataset creation
----------------
To create a study dataset you just need to run:
``singularity run INSTALL-DIR/cbbs-imaging.simg create [TARGET-DIR]``.
If you don't provide a target dir, the dataset will be created in the current working directory.

Adding an MRI session
---------------------

The above mentioned container also provides a command to import a tarball for a session.
This will result in a subdataset with the DICOMs in it, that provides the DICOM metadata for easy access via `datalad`.

To import such a tarball just run
``singularity run INSTALL-DIR/cbbs-imaging.simg import [TARBALL]``
from within your study dataset. You don't need to be at its root directory, but you need to make sure, you aren't accidentally in a subdataset. Therefore the study dataset's root is a safe practice to follow.

Note, that TARBALL needs to be an absolute path at the moment.
A session name like `af29_0678` will be derived from the dicoms' metadata and a subdirectory with that is created.
In that subdirectory you should then find a `studyspec.json`, which is needed for conversion later on and a subdirectory `dicoms`, which is in fact a subdataset containing the actual dicoms.
