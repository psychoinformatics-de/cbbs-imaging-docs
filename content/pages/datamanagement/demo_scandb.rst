Demo: DICOM DB
**************
:order: 491

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
    /home/data/psyinf/forrest_gump/pandora/data/yx11/raw/dicom/yx11_2022.20130410.103515.930000.tar.gz
   singularity run ../import/cbbs-imaging.simg import \
    /home/data/psyinf/forrest_gump/7T_ad/data/yx11/raw/dicom/yx11_2014.20130408.123933.087500.tar.gz
   singularity run ../import/cbbs-imaging.simg import \
    /home/data/psyinf/forrest_gump/7T_ad/data/yx11/raw/dicom/yx11_2015.20130408.140515.147500.tar.gz

   # done for now
   cd ..
   # now the same for 3t
   singularity run import/cbbs-imaging.simg create 3t
   cd 3t
   # import a bunch of DICOM tarballs
   singularity run ../import/cbbs-imaging.simg import \
    /home/data/psyinf/forrest_gump/3T_av_et/mri/yx11_0138.20140425.121603.06.tar.gz
   singularity run ../import/cbbs-imaging.simg import \
    /home/data/psyinf/forrest_gump/3T_av_et/mri/yx11_0139.20140425.142752.07.tar.gz
   singularity run ../import/cbbs-imaging.simg import \
    /home/data/psyinf/forrest_gump/3T_visloc/mri/yx11_0140.20140425.155736.23.tar.gz

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
