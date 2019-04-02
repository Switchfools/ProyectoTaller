#!/bin/sh
git add *
mv FotosEntrada/foto5.png FotosEntrada/`date +%F-%T`.png
git commit -m "autoupdate `date +%F-%T`"
git push
