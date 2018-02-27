Demo: DICOM DB
**************
:order: 491

DICOM datasets that have been `imported into a study raw dataset
<{filename}import_dicoms.rst>`_ can (additionally) be collected in scanner (or
institution or lab) specific superdatasets. This allows for convenient record
keeping of all relevant MR data acquisitions ever made in a given context.  The
example script at the bottom of this page shows how to bootstrap such a
database.

Such superdatasets are lightweight, as they do not contain actual imaging data,
and can be queried using a flexible language. In the DICOM context it is often
desired to limit the amount of metadata to whole datasets and they image
series. This can be achieved using the following configuration::

   % cat .datalad/config
   [datalad "dataset"]
           id = 349bb81a-1afe-11e8-959f-a0369f7c647e
   [datalad "search"]
           index-autofield-documenttype = datasets
           default-mode = autofield

With this setup the DataLad `search` command will automatically discover
metadata for any contained image series, and build a search index that can be
queried for values in individual DICOM fields. This alles for a variety of
useful queries. Here are a few examples:

Report scans made on any male patients in a given time span::

   % datalad search dicom.Series.AcquisitionDate:'[20130410 TO 20140101]' dicom.Series.PatientSex:'M'
   search(ok): lin/7t/xx99_2022/dicoms (dataset)

Report any scans for a particular subject ID::

   % datalad search 'xx99*'
   [INFO   ] Query completed in 0.019682836998981657 sec. Reporting up to 20 top matches. 
   search(ok): lin/7t/xx99_2022/dicoms (dataset)
   search(ok): lin/7t/xx99_2014/dicoms (dataset)
   search(ok): lin/7t/xx99_2015/dicoms (dataset)
   search(ok): lin/3t/xx99_0138/dicoms (dataset)
   search(ok): lin/3t/xx99_0139/dicoms (dataset)
   search(ok): lin/3t/xx99_0140/dicoms (dataset)
   action summary:
     search (ok: 6)


Example script to bootstrap a DICOM database from scan tarballs
---------------------------------------------------------------

The following script shows how a bunch of DICOM tarballs from two different
scanners can be imported into a DataLad superdataset for each scanner. Those
two scanner datasets are than assembled into a joint superdataset for
acquisition hardware of the LIN. Metadata from any acquisition session can then
be aggregated into this dataset, to track all acquisitions made on those
devices, as well as to be able to query for individual scan sessions, DICOM
series, or individual DICOM images. Such query only require the presence of
metadata, and do not depend on the availability of actual raw data.

.. code-block:: sh

   # get the tools
   datalad install -s https://github.com/psychoinformatics-de/cbbs-imaging-container-import import
   datalad get import/cbbs-imaging.simg

   # create a super dataset that will have all acquisitions the 7T ever made
   singularity run import/cbbs-imaging.simg create 7t
   cd 7t
   # import a bunch of DICOM tarballs (simulates daily routine)
   singularity run ../import/cbbs-imaging.simg import \
    /home/data/psyinf/forrest_gump/pandora/data/xx99/raw/dicom/xx99_2022.20130410.103515.930000.tar.gz
   singularity run ../import/cbbs-imaging.simg import \
    /home/data/psyinf/forrest_gump/7T_ad/data/xx99/raw/dicom/xx99_2014.20130408.123933.087500.tar.gz
   singularity run ../import/cbbs-imaging.simg import \
    /home/data/psyinf/forrest_gump/7T_ad/data/xx99/raw/dicom/xx99_2015.20130408.140515.147500.tar.gz

   # done for now
   cd ..
   # now the same for 3t
   singularity run import/cbbs-imaging.simg create 3t
   cd 3t
   # import a bunch of DICOM tarballs
   singularity run ../import/cbbs-imaging.simg import \
    /home/data/psyinf/forrest_gump/3T_av_et/mri/xx99_0138.20140425.121603.06.tar.gz
   singularity run ../import/cbbs-imaging.simg import \
    /home/data/psyinf/forrest_gump/3T_av_et/mri/xx99_0139.20140425.142752.07.tar.gz
   singularity run ../import/cbbs-imaging.simg import \
    /home/data/psyinf/forrest_gump/3T_visloc/mri/xx99_0140.20140425.155736.23.tar.gz

   # done
   cd ..

   # one dataset for the entire institute's scan (could in turn be part of one that also
   # includes other modalities/machines)
   # this first part only needs to be done once
   datalad create lin
   cd lin
   datalad install -d . -s ../7t
   datalad install -d . -s ../3t

   # this second part needs to be done everytime the metadata DB shall be updated
   # get the latest state of the scanner datasets (no heavy stuff is moved around)
   datalad update --merge -r
   # aggregate from the aggregated metadata
   datalad aggregate-metadata -r
   # ready to search
