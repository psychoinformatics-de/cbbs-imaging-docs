Demo Study
**********
:order: 481


.. class:: todo

    **TODO**: title and introductory description of what this is about*

Creating a raw dataset
----------------------



First off, we need a study raw dataset to bundle all raw data in a structured way::

  datalad create my_raw_dataset
  cd my_raw_dataset
  datalad run-procedure setup_study_dataset


.. class:: todo

    **TODO**: Already start editing study metadata here?

From within the dataset add our toolbox by calling::

  datalad install --dataset . --source https://github.com/psychoinformatics-de/cbbs-toolbox.git code/toolbox


Acquiring data
--------------

From the scanner, we'd usually get a tarball containing the DICOMs of an acquisition. For this demo we can get such a tarball via::

  wget https://github.com/datalad/example-dicom-functional/archive/half.tar.gz


*TODO: acquisition ID, since DICOM contains subject ID only, which would become the acquisition ID as well*
Now, as soon as we have an acquisition's data, we import it into the raw dataset
to make sure, we get its metadata as well as the correct starting point for the
data versioning.
From within the ``my_raw_dataset`` directory we run::

  datalad hirni-import-dcm /path/to/downloaded/half.tar.gz


.. class:: todo

    **TODO**: Note on ReproIn Convention (https://github.com/repronim/reproin#overall-workflow)


.. class:: todo

  **TODO**: Import of additional data




Editing the specification
-------------------------

This step isn't actually required in case of this example. However, if there was
a need to change the specification of the study (or a single acquisition), you
can either edit the JSON files directly or use the WebUI::

  % datalad webapp --dataset . hirni

Output ends with::

 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

Now this address can be opened in a browser and should look like this:

.. image:: /theme/img/webui_index.png

Click on "Edit acquisition metadata" and select acquisition "02" to get to the
editing mask for this acquisition:

.. image:: /theme/img/webui_edit_acq.png

You can also edit more general information about the study, if you choose to
edit study metadata:

.. image:: /theme/img/webui_edit_study.png


Conversion to BIDS
------------------

In order to get a BIDS dataset from the raw dataset, create a new dataset and
set it up to become a BIDS dataset::

  datalad create bids
  cd bids
  datalad run-procedure setup_bids_dataset

Now, install input data as a subdataset::

  datalad install --dataset . --source ../study_ds sourcedata
  datalad install sourcedata/code/toolbox


If the specification wasn't altered, the actual conversion is done by::

  datalad hirni-spec2bids sourcedata/02/studyspec.json

Note, that this command takes a list of specification files (each expected to be
an acquisition specification) and converts the respective acquisitions. If you
want to convert a dataset with multiple acquisitions at once, just use::

  datalad hirni-spec2bids sourcedata/*/studyspec.json


