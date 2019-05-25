#!/bin/bash
cd /home/param/meme/MemeAdviser4/MemeAdviser.wiki/
git pull

if output=$(git status --porcelain) && [ -z "$output" ]; then
    :
else
    git add .
    git commit -m "Update log"
    git push
fi
