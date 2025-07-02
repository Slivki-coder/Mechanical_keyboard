# qmk_keyboard

## CAD
I modeled all parts in Fusion 360. The case consists of 3 parts: The casing itself, a top plate for the switches and stabilizers and a stand to add a bit of incline to the keyboard. The stand and case each require 9 5x2mm magnets, which are used to attach the stand to the main body. It is also possible to add silicone feet to the stand to prevent it from sliding across the table. The top plate is fixed to the body with 7 M2.5x10 screws.

## PCB
The PCB & schematic was designed in KiCAD. The schematic is a bit confusing because some keys from col13 are shfted up one row.

## Firmware
The Firmware was created in python using the kmk library. It requires Circuitpython to be installed on the mcu to run. The Macro functions are currently empty, these can be set to any macro you want. KMK also does not have a Menu key so this one is currently set to KC.NO, but it can be repurposed as a layer switch for example.

## BOM
