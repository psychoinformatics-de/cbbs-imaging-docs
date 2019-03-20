BIDS Conversion
***************
:order: 450

The conversion of a `study raw dataset <{filename}study_setup.rst>`_ to a BIDS
compliant dataset relies on a proper `specification <{filename}study_specification.rst>`_.
The outcome of such a conversion is again a datalad dataset. It contains a
reference to the study dataset it was build from, but can be used and shared
without access to the study dataset.


Dataset creation
----------------
First, create the to-be BIDS dataset pretty much the same way as you
`create a study dataset <{filename}study_setup.rst>`_::

  datalad rev-create [TARGET-DIR]

If you don't provide a target dir, the dataset will be created in the current
working directory. This will create an empty datalad dataset.

To preconfigure it to be a *BIDS dataset* however, you need to run a dedicated
setup procedure from within the dataset::

  cd [TARGET-DIR]
  datalad run-procedure setup_bids_dataset

Reference needed input
----------------------
Now the study dataset to be converted is needed. Install it as a subdataset
`sourcedata` into the BIDS dataset::

  datalad install -d . -s [PATH TO STUDY DATASET] sourcedata

Note, that we are assuming you created your study dataset according to the `setup page <{filename}study_setup.rst>`_ or the accompanying `demo <{filename}study_setup.rst#step-by-step-demo>`_.
That is, it has the `toolbox <{filename}tools/toolbox.rst>`_ installed as a subdataset.

Conversion
----------
Assuming that the study dataset comes with a proper study specification, you can
now convert it by calling::

  datalad hirni-spec2bids --anonymize sourcedata/studyspec.json sourcedata/*/studyspec.json

Several things are to be noted here. First, there is a switch ``--anonymize``.
This is optional and ensures that within the resulting BIDS dataset subjects are
referred to only by their `anon_subject` ID according to the specification.
There shouldn't be any hint on the original subject ID in the commit messages or
paths in the new dataset. By default this should also run a defacing routine, that should be specified in an acquisition's specification file within a snippet of type `dicomseries:all`.
You can change this by editing this specification.

Furthermore, you may notice that the call as shown above references not the
study dataset to be converted but the specification files. This means, you don't
need to convert the entire dataset at once. You can also convert a single
acquisition instead. In fact, you can even have several specification files per acquisition and run a conversion based on a single file. Further limitation is available via the option ``--only-type``, which allows to convert only snippets of that particular type.

Dropping raw data
-----------------
Finally, you can uninstall the source dataset by running::

  datalad uninstall -d . -r --nocheck sourcedata

This will leave you with just the BIDS dataset. It still contains a reference to
the data it was derived from, but doesn't contain that data.


.. include:: demos/conversion.rst.in

