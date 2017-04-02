# pi-cision-shooting
Raspberry Pi powered hockey accuracy shooting competition

## Install Dependencies
    pip install -r requirements.txt

## Install Touch Screen Keyboard
    sudo apt-get update
    sudo apt-get upgrade
    sudo apt-get install matchbox-keyboard

## Run pi-cision-shooting from Terminal

From the `scripts` directory run:

    ./target.py

## Run pi-cision-shooting w/ Keyboard from Terminal

From the `scripts` directory run:

    ./app.sh

## Create Desktop Shortcut

1. Update the paths in `assets/Pi-cisionShooting.desktop` to the location of the cloned repo
2. Copy the .desktop file to your desktop directory:

        cp assets/Pi-cisionShooting.desktop /home/pi/Desktop

## Building the Rig

A full parts list and description of building the rig can be found in [this blog post](https://www.asdfpublishing.com/single-post/2017/04/02/Pi-Day-Inspired-Hacking).
