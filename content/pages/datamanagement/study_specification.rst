Study Metadata
**************
:order: 415

The study specification consists of JSON files in the `study raw dataset <{filename}study_setup.rst>`_ and
provides metadata needed for conversion. The tools provided by datalad-hirni aim
to help to (automatically) create and curate those files and convert a study raw
dataset (or single acquisition) based on them.
Each acquisition in a study raw dataset contains such a file. Its default name
is `studyspec.json` directly underneath the acquisition's directory. It's a
JSON-stream consisting of one dictionary per line. We are referring to those
dictionaries as `snippets`. For any data entity in an acquisition (at least any
that is to be converted) there should be such a snippet. Those snippets are
automatically created when you `import a DICOM tarball <{filename}import_dicoms.rst>`_
or `import other data <{filename}import_other.rst>`_ into your study raw dataset.
However, the automatic creation may be incomplete or even incorrect,
depending on your needs. Therefore those specifications need to be edited
before converting the dataset. Since those files are simple JSON files, you can
change them programmatically, edit them manually with any kind of editor you like
or use datalad-hirni's webUI to do so.

The specification snippets have keys, that are meant to be edited and some
special keys, that are not supposed to be changed, but only to automatically be
set on creation. The editable ones have values that are again a dictionary with
two keys: `value` and `approved`, where `approved` is a flag signalling whether
or not the value is just an automatic guess, that needs to either be confirmed
or changed. This is meant to help curation.

Generally, a snippet for a dicom series looks like this::

  {"location":"dicoms",
   "type":"dicomseries",
   "uid":"1.3.10.2.1102.5.2.34.18716.201347010933155397510580.0.0.0",
   "dataset_id":"42bc01a0-a6c3-11e8-9a5b-a0389fb56dc0",
   "dataset_refcommit":"a771150f0e15f309212bc83186d893c65f731d9c",
   "comment":{"approved":false,"value":""},
   "subject":{"approved":false,"value":"df37"},
   "anon_subject":{"approved":false,"value":"002"},
   "bids_modality":{"approved":false,"value":"bold"},
   "bids_run":{"approved":false,"value":"01"},
   "bids_session":{"approved":false,"value":null},
   "bids_task":{"approved":true,"value":"001"},
   "description":{"approved":true,"value":"MoCoSeries_DiCo"},
   "id":{"approved":false,"value":9},
   "procedures":[{"procedure-name": {"approved": false, "value": ""},
                  "procedure-call": {"approved": false, "value": ""},
                  "on-anonymize": {"approved": false, "value": false}
                  }]
   "tags":[]
  }

Note, that the first five entries are aforementioned non-editable fields. They
are created by the import routine for DICOMs and supposed to not be changed.
"location", "type", "dataset_id", "dataset_refcommit" are expected in every
snippet independent on the type of data this specification is about.

"location" is a path to the actual data relative to the specification file
containing this very snippet. It might refer to a single file or a directory.

"comment" is a field with no implications in how this snippet or the data it is
about is dealt with. It is meant to provide a place to put notes regarding the
data or TODOs or whatever you might need in order to finish creating the study
raw dataset and preparing conversion.

All keys starting with `bids_` are referring to the terms used in the BIDS
standard and are used for conversion. Many of those are optional and therefore
can have a value of `null` or not appear in the specification at all. In this
example the values were automatically derived from DICOM metadata (note, that
they are not yet "approved"), most importantly from the DICOM field `ProtocolName`.
For conversion of DICOMS currently supported BIDS keys are:

- 'bids_session'
- 'bids_task'
- 'bids_run'
- 'bids_modality'
- 'bids_acquisition'
- 'bids_scan'
- 'bids_contrast_enhancement'
- 'bids_reconstruction_algorithm'
- 'bids_echo'
- 'bids_direction'

For details on their meaning please refer to the `BIDS standard`_.

The value of "description" comes from DICOM's `SeriesDescription` and "id" is
prefilled with the value of `SeriesNumber`. It's worth noting, that this "id"
has no technical meaning for datalad-hirni's commands. It is meant to provide
you with a human-readable identification of this DICOM series to ease editing of
the snippet.

"procedures" defines a list of `datalad-procedures`_ to be executed during conversion.
Besides its name such a procedure definition provides the option to overwrite the way it is called ("procedure-call") by passing an alternative format string and a flag to signal whether or not it is to be called only if the conversion with ``datalad hirni-spec2bids`` is called with the option ``--anonymize``,
which can be used to apply a defacing routine for example.
An example for such a format string can be found within the `study dataset demo <{filename}demo_study.rst>`_. Such a format string is first and foremost meant to provide arguments to the call for a procedure and the mechanism as provided by datalad itself (see `datalad-procedures`_ for reference) is enhanced by datalad-hirni.
This enhancements makes other fields of the specification snippet available via additional placeholders. Enclose any key of the snippet in double curly brackets and it will be replaced by the value of that key when the procedure is called.
Procedures are available through hirni's toolbox dataset, but can also be provided by yourself. Any datalad-procedure is valid for this specification.
With respect to the example snippet above, note that there is no conversion procedure defined for the dicomseries. This is because of the default routine hirni uses. This is a containerized version of `heudiconv`_ provided by the toolbox.
The respective procedure is called `hirni-dicom-converter` and is only called once per acquisition. This will convert all the dicomseries within that acquisition. Hence any procedure you add to a particular dicomseries will be called after the conversion and usually there shouldn't be a need to do so.
You can however *exclude* a dicomseries from conversion by adding the tag `hirni-dicom-converter-ignore` to its specification snippet.
The conversion routine for the dicomseries is specified in an additional snippet (created automatically during `import <{filename}import_dicoms.rst>`_) of type `dicomseries:all`.


Similarly, a snippet for a physio file may look like this::

  {"location":"physio/df37_200Hz_1.txt",
   "type":"physio_file",
   "dataset_id":"42bc01a0-a6c3-11e8-9a5b-a0389fb56dc0",
   "dataset_refcommit":"a771150f0e15f309212bc83186d893c65f731d9c",
   "comment":{"approved":false,"value":""},
   "subject":{"approved":false,"value":"df37"},
   "anon_subject":{"approved":false,"value":"002"},
   "bids_run":{"approved":false,"value":"01"},
   "bids_session":{"approved":false,"value":null},
   "bids_task":{"approved":true,"value":"oneback"},
   "sampling-frequency": {"approved": true, "value": "200Hz"},
   "procedures":[{"procedure-name":{"approved":true,"value":"hirni-physiobox-converter"}}],
  }

Something like this is typically created when `importing <{filename}import_other.rst>`_ other data than DICOM files by calling ``datalad hirni-spec4anything``.



.. _BIDS standard:   http://bids.neuroimaging.io/
.. _datalad-procedures: http://docs.datalad.org/en/latest/generated/man/datalad-run-procedure.html
.. _heudiconv: https://github.com/nipy/heudiconv
