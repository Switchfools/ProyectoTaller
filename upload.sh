#!/bin/sh
git add *
git status
git commit -m "autoupdate `date +%F-%T`"
git push
