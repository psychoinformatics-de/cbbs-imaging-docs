Import DICOMs
*************
:order: 420

`datalad-hirni <https://github.com/psychoinformatics-de/datalad-hirni>`_
provides a command to import a DICOM tarball for an acquisition into a
`study dataset <{filename}study_setup.rst>`_. The command to be used for that is::

  datalad hirni-import-dcm [TARBALL] [ACQUISITION ID]

from within your study dataset.  This will result in a subdirectory
`ACQUISITION ID` in your study dataset and a subdataset `dicoms` beneath with the
DICOMs in it, that provides the DICOM metadata for easy access via `datalad`. In
addition a prefilled specification for each series in the tarball is created and
stored in the acquisition's `specification file <{filename}study_specification.rst>`_ .

If you don't provide an acquisition identifier, a name like `xx99_0123` will be
determined from the DICOM metadata. By default this is the value of field
`PatientID`. However, there are special rules in place (and to further be
developed) to be applied based on the scanner the data was acquired with. This
mechanism allows for different rules per scanner, institution or any other
category that can be identified by the DICOM metadata.

Use ``--subject`` to provide a subject ID. Otherwise the import routine will try
to derive the subject ID from the DICOM metadata. A typical case would be the
aforementioned acquisition `xx99_0123` with a corresponding subject ID `xx99`.
Optionally, you can use ``--anon-subject`` to additionally provide an anonymized
subject ID. When `converting <{filename}conversion.rst>`_ the dataset to BIDS,
the switch ``--anonymize`` will then determine which subject ID to use for the
converted dataset.

Generally, the option ``--properties`` allows to add and/or overwrite the
`specification <{filename}study_specification.rst>`_ to be created for this
acquisition by passing either a JSON string or a path to a JSON file.
Thereby you can assign a task label for example, if it can not be derived from the DICOM metadata by the rules inplace::


  datalad hirni-import-dcm --subject xx99 --anon-subject 007 \
  --properties '{"bids_task": "dofancystuff", \
                 "comment": "something unusual happened during this acquisition"}' \
  /path/to/tarball

DICOM subdatasets can be archived separately to, for example, build raw data
archives (for a lab, a scanner, an institution) that can be easily queried for
scan with particular properties (see `this demo <{filename}demo_scandb.rst>`_
for an example).


*TODO: Notes on how and what to drop/clean up*