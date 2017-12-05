#!/bin/bash
# simple script to use travis-encrypted github token and git user for updating docs folder whenever master branch was updated.
# It assumes that make was done before and therefore docs is up-to-date locally.

set -x
git --version

# set up git and github access
git config user.name $GIT_NAME
git config user.email $GIT_EMAIL
git config credential.helper "store --file=.git/credentials"
echo "https://${GH_TOKEN}:x-oauth-basic@github.com" > .git/credentials

# switch to branch gh-pages and get the fresh build
git remote -v show
git fetch origin --unshallow
git branch -a
git checkout origin/gh-pages
rsync -r docs/ .

# commit new docs folder and push
git add .
git commit -m "Automatically updated github page"
git push origin HEAD:gh-pages

rm .git/credentials


