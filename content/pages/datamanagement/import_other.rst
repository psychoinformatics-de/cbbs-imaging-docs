Non-DICOM Data
**************
:order: 430

Apart from DICOM files, you can (and should) add any additional data into a study dataset.
Information corresponding to any of the MR data acquisitions must be added into
the respective directory. This can be stimulation logs, behavioral response logs,
or other simultaneously acquired data. To simply add the files to the dataset,
copy or move them to the appropriate location and use ``datalad rev-save`` to make
them part of the dataset. Have a look at the `study dataset demo <{filename}study_setup.rst#step-by-step-demo>`_ for an example.

However, in order to include the data in the conversion later on, you need to
create a `specification <{filename}study_specification.rst>`_ for it. This is what
``datalad hirni-spec4anything`` is for. This will create a snippet for the data
component, containing the mandatory pieces and lets you specify all properties
of the specification needed for conversion via the same option `--properties`,
that is available when `importing DICOM archives <{filename}import_dicoms.rst>`_.

Let's say you added a file ``physio/df37_200Hz_1.txt`` to an acquisition. To
create a proper specification snippet for that file, from within the acquisition
directory you'd call::

  datalad hirni-spec4anything physio/df37_200Hz_1.txt \
  --properties "{'type': 'physio_file', \
                 'bids_run': '01', \
                 'procedures': [{'procedure-name': 'hirni-physiobox-converter'}], \
                 'sampling-frequency': '200Hz'}"


Note, that the specified type is an arbitrary label you can choose to distinguish different kinds of files.
It can be used to run a conversion on that type only or to ease programmatic curation of specifications.
``datalad hirni-spec4anything`` will also prefill the specification with values that are unambiguous throughout the already existing snippets in the respective specification file.
Hence, if you already have imported the corresponding DICOMs, things like the subject ID or a possible task label that are the same for all the specification snippets derived from the DICOM metadata will be filled into your snippet for that physio file.
You can overwrite them of course, by passing new values via that ``--properties`` option, which takes precedence over the defaults.
The result will be a snippet in the acquisitions specification file as shown on the `specification page <{filename}study_specification.rst>`_::

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


Note, that the keys "subject", "anon_subject", "bids_task" were not specified in
the call but still created for this snippet (assuming they can be concluded as described above).
If there was only one run in the existing data there would also be no need to specify it in
the call to `spec4anything`.

The field ``procedures`` defines a list of datalad-procedures to be called on conversion.
They can refer to procedures provided by datalad-hirni's toolbox or any other procedure you defined.
For details on how to this, please refer to ``datalad run-procedure --help``.

Note, that the procedure in this example (`hirni-physiobox-converter`) is provided by the toolbox and expects a field `sampling-frequency` in the specification snippet.
You might need different values and/or keys depending on your data. Generally, you can add arbitrary fields to the specification whether or not they are currently needed by any procedure.
Thereby you can enhance metadata for everything within your study dataset in a machine-readable shape, that potentially can be processed later on.
