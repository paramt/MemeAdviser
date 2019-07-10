#!/bin/bash
cd /home/param/meme/MemeAdviser4/MemeAdviser
git pull
run-one python3 -m src.app >> /home/param/meme/MemeAdviser4/cron.log 2>&1
