# Pi-cision Shooting
Pi-cision Shooting is a Raspberry Pi powered hockey accuracy shooting competition. Players compete to see who can knock back targets mounted in each corner of a hockey goal the quickest. The GPIO pins on the Raspberry Pi are connected to a [Magnetic Door Switch Set](https://www.sparkfun.com/products/13247) mounted on each target so that it is able to monitor when a target has been hit. A full parts list and a description of the project itself can be found in [this blog post](https://www.asdfpublishing.com/single-post/2017/04/02/Pi-Day-Inspired-Hacking).

<img src="https://static.wixstatic.com/media/6361c8_16d7a1cb887945a4beb1a1fde07af10f~mv2.png/v1/fill/w_1200,h_800,al_c/6361c8_16d7a1cb887945a4beb1a1fde07af10f~mv2.png" height="240">

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
