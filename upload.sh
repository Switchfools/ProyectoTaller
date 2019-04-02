#!/bin/sh
mv FotosEntrada/foto5.png FotosEntrada/`date +%F-%T`.png
git add *
git commit -m "autoupdate `date +%F-%T`"
git push
