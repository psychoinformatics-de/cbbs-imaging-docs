Import additional data
**********************
:order: 430

Apart from DICOM files, you can add any additional data into a study dataset.
Information corresponding to any of the MR data acquisitions must be added into
the respective directory. This can be stimulation logs, behavioral response logs,
or other simultaneously acquired data. To simply add the files to the dataset,
copy or move them to the appropriate location and use ``datalad add`` to make
them part of the dataset.
*TODO: this prob. needs a link to tools/datalad and an explanation therein*

However, in order to include the data in the conversion later on, you need to
create a `specification <{filename}study_specification>`_ for it. This is what
``datalad hirni-spec4anything`` is for. This will create a snippet for the data
component, containing the mandatory pieces and lets you specify all properties
of the specification needed for conversion via the same option `--properties`,
that is available when `importing DICOM archives <{filename}import_dicoms.rst>`_.

Let's say you added a file ``physio/df37_200Hz_1.txt`` to an acquisition. To
create a proper specification snippet for that file, from within the acquisition
directory you'd call::

  datalad hirni-spec4anything physio/df37_200Hz_1.txt \
  --properties "{\"converter_path\": \"../code/convert_physio",
                 \"converter\": \"{_hs[converter_path]} {_hs[location]} \
                                  {_hs[bids_subject]} {_hs[bids_task]} \
                                  {_hs[bids_run]} ${freq}\", \
                 \"bids_run\": \"01\",
                 \"type\": \"physio_file\"}"

to create the snippet as shown on the `specification page <{filename}study_specification>`_::

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

Note, that the keys "subject", "anon_subject", "bids_task" were not specified in
the call but still created for this snippet. Whenever you use
``datalad hirni-spec4anything`` to add a snippet to an acquisition's specification,
the command will conclude the values for keys if the value is unambiguous
throughout the already existing specification of that acquisition. If there was
only one run in the existing data there would also be no need to specify it in
the call to `spec4anything`.

There are two fields to specify a custom converter for any data component:
`converter` and `converter_path`. `converter_path` contains the path referring
to the executable. Note, that this path is relative to the location of the
specification file (by default right in the acquisition directory) as is the
path to the data itself (key "location" in the snippet).
The second field `converter` is a format string specifying how to call that
executable to convert the file referred to by this snippet. The curly brackets
indicate something to dynamically be replaced. This follows the same concept
used by ``datalad run``. As a replacement symbol the dictionary ``_hs`` is
available. This allows to reference any key in this very snippet. So,
``{_hs[converter_path]}`` is replaced by the path to the executable and
``{_hs[bids_run]}`` by the value `01`. That way, the string for the `converter`
field can be figured out once per converter and all snippets using it will cause
the conversion routine to replace those symbols with the values belonging to the
currently converted data component.





