#!/bin/bash

if [[ `git status --porcelain` ]];then
    cd ../weihuayi.github.io/
    git pull
    cd ../numal/
    git add .
    git commit -m "update" 
    git pull
    git push 
    gitbook build
    cp -r _book/* ../weihuayi.github.io/math/numal/
    cd ../weihuayi.github.io/
    git add .
    git commit -m "update" 
    git push 
else
    git pull
fi
