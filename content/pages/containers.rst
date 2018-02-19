Computational Environments
**************************
:order: 700

In order to faciliate the reproducibility of research computing, all data
processing is performed in containerized computational environments. These
environments can be archived alongside the results of the data processing
algorithms they have performed, in order to generate a complete record of the
processing history. Moreover, such computional environment can be tracked with
version control systems to capture which particular results were produced with
which software version, in case data processing pipelines have to be adjusted
throughout the lifetime of a project.

The CBBS imaging platform employs `Singularity <http://singularity.lbl.gov>`_
as the main workhorse for container-based data processing.
