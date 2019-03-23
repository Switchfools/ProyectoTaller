#!/bin/sh
git add foto.png
git commit -a -m "autoupdate `date +%F-%T`"
git push
