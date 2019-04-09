#!/bin/sh
mv FotosEntrada/foto5.png FotosEntrada/`date +%Y-%m-%d-%H-%M-%S`.png
git add *
git commit -m "autoupdate `date +%F-%T`"
git push
