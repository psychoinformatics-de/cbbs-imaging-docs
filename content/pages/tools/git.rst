Git
***
:order: 620

Git enables you to track the changes made to files over time — specifically:
what changed, by whom, when, and why. It also gives you the capability to revert
files back to a previous state. Over time, as your project evolves, you can edit
your files with confidence knowing that at any point you can look back and
recover a previous version.

Install
-------
**Debian/Ubuntu**
  .. code::

    sudo apt-get install git

**macOS**
  Download the installer at: `<https://git-scm.com/download/mac>`_

**Windows**
  Download the installer at: `<https://git-scm.com/download/win>`_

Setup
-----
Once Git is installed, configure it with your name and email address. This lets
Git know who you are so that it can associate you with the commits you make.

.. code::

  git config --global user.name "John Doe"
  git config --global user.email johndoe@example.com

Basic Commands
--------------
``git init``
  Tells git to enable tracking of changes that happen in this folder.

``git clone <url> | <user@server:path/to/repo.git>``
  Makes a full copy of an existing `git repository
  <https://help.github.com/articles/github-glossary/#repository>`_ — all
  files, folders, changes, history, etc.

``git status``
  Lists which files are in which state — if there have been changes made, new
  files added or deleted, etc.

``git add <file>``
  To begin tracking a new file. Once you run ``git add``, your file will be
  tracked and **staged** to be committed.

  ``git add -p``
    Review the changes you've made and select which will be **staged**.

``git commit``
  Commits all the **staged** changes (done with ``git add``). It will prompt you
  for a **commit message**, which should be a terse but descriptive note about
  the changes contained in the commit. These commit messages are your project's
  history.

``git rm <file>``
  Stages the file to be removed. After you commit, the file will be removed and
  no longer tracked. But the file does remain in the project history.

``git mv <file-from> <file-to>``
  Moves/renames a file.

``git log``
  Lists your commit history. It's not as user-friendly or easy-to-navigate as
  ``tig``.

``tig``
  A text-mode interface for git that allows you to easily browse through your
  commit history. It is not part of git and will need to be installed (``apt-get
  install tig`` for Debian/Ubuntu; `Homebrew instructions
  <https://github.com/jonas/tig/blob/master/INSTALL.adoc#installation-using-homebrew>`_
  for macOS)

``git push``
  Push your local changes to another repository, for example on GitHub.

``git pull``
  Pull changes from another repository to your local repository.

GitHub
------
GitHub is an online platform where you can store and share your projects; it is
especially well suited for working on a project with several other people. It
acts as a central place where everyone can access/contribute to the project and
offers several useful tools (issues, wikis, project milestones, user management,
etc) that make collaboration simple and easy.

To create a profile, go to `GitHub
<https://github.com/join?source=header-home>`_, and from there, follow the
prompts to create your account.

Resources
---------
GitHub offers an `interactive Git tutorial
<https://try.github.io/levels/1/challenges/1>`_ that is a great starting point
for beginners.

The free `Pro Git Book <https://git-scm.com/book/en/v2>`_ covers just about
everything Git has to offer using clear and easy-to-understand language. It
starts with the basics, but builds up to some of Git's more complex features.

If you like video tutorials, the `Intro to Git and GitHub
<https://youtu.be/PFwUHTE6mFc>`_ and `The Basics of Git and GitHub
<https://youtu.be/u6G3fbmpWr8>`_ videos are worth watching if you're still
unsure about the basics of Git and GitHub and want a step-by-step explanation of
how to get started.

For any questions you might have about using GitHub, see `GitHub Help
<https://help.github.com/>`_.

The `Git Reference Manual <https://git-scm.com/docs>`_ is the official docs for
Git. It has all the information you could want to know about Git, but is pretty
dense and better suited for intermediate and advanced users.
