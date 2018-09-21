Study specification
*******************
:order: 440

The study specification consists of JSON files in the study raw dataset and
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
However, the automatic creation will likely be incomplete or even incorrect,
depending on your needs. Therefore those specifications needs to be edited
before converting the dataset. Since those files are simple JSON files, you can
change them programmatically, edit the manually with any kind of editor you like
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
   "converter":{"approved":false,"value":"heudiconv"},
   "description":{"approved":true,"value":"MoCoSeries_DiCo"},
   "id":{"approved":false,"value":9},
  }

Note, that the first five entries are aforementioned non-editable fields. They
are created by the import routine for DICOMs and supposed to be changed.
"location", "type", "dataset_id", "dataset_refcommit" are expected in every
snippet independent on the type of data this specification is about.

"location" is a path to the actual data relative to the specification file
containing this very snippet. It might refer to a single file or a directory.

"comment" is field with no implications in how this snippet or the data it is
about is dealt with. It is meant to provide a place to put notes regarding the
data or TODOs or whatever you might need in order to finish creating the study
raw dataset and preparing conversion.

All keys starting with `bids_` are referring to the terms used in the BIDS
standard and are used for conversion. Many of those are optional and therefore
can have a value of `null` or not appear in the specification at all. In this
example the values were automatically derived from DICOM metadata (note, that
they are not yet "approved"), most importantly from the DICOM field `ProtocolName`.
For conversion of DICOMS currently supported BIDS keys are:

    'bids_session'
    'bids_task'
    'bids_run'
    'bids_modality'
    'bids_acquisition'
    'bids_scan'
    'bids_contrast_enhancement'
    'bids_reconstruction_algorithm'
    'bids_echo'
    'bids_direction'

The value of "description" comes from DICOM's `SeriesDescription` and "id" is
prefilled with the value of `SeriesNumber`. It's worth noting, that this "id"
has no technical meaning for datalad-hirni's commands. It is meant to provide
you with a human-readable identification of this DICOM series to ease editing of
the snippet.

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
   "bids_task":{"approved":true,"value":"001"},
   "converter":{"approved":true,"value":"{_hs[converter_path]} {_hs[location]} {_hs[bids_subject]} {_hs[bids_task]} {_hs[bids_run]}"},
   "converter_path":{"approved":true,"value":"../code/convert_physio"},
  }

Note, that the fields "converter" and "converter_path" allow to include custom
converters for your data by specifying where to find the executable
(`code/convert_physio` within the study raw dataset in this case) and how to
call it in order to convert this particular data.


*TODO:* Explanation of "converter" format string here, on import site or conversion?
