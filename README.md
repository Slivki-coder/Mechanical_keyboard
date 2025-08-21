# Keyboard

This is a Mechanical keyboard which I designed for highway, an event by hackclub. It includes a standard 80% layout as well as 5 macro keys on the left.

![WhatsApp Bild 2025-08-21 um 10 07 07_0b671c8c](https://github.com/user-attachments/assets/b1b18930-5b7b-4ca9-ae9e-b7d459d31c8b)

## CAD
I modeled all parts in Fusion 360. The case consists of 3 parts: The casing itself, a top plate for the switches and stabilizers and a stand to add a bit of incline to the keyboard. The stand and case each require 9 5x2mm magnets, which are used to attach the stand to the main body. It is also possible to add silicone feet to the stand to prevent it from sliding across the table. The top plate is fixed to the body with 7 M2.5x10 screws.

![image](https://github.com/user-attachments/assets/4c5b50e1-e197-425b-a321-5df5b017ac8d)
![image](https://github.com/user-attachments/assets/2ce50790-c19f-4358-8761-7eab7cb244d8)
![image](https://github.com/user-attachments/assets/09a9d537-92cf-46b1-8555-03698aa71d8b)
![image](https://github.com/user-attachments/assets/6e9b3dd4-8d5f-457d-ae6b-6236d928ff65)
<img width="2559" height="1376" alt="image" src="https://github.com/user-attachments/assets/96666b45-c04c-4107-9787-60cabb741a5e" />
<img width="857" height="372" alt="image" src="https://github.com/user-attachments/assets/37c642e8-4815-4fff-9a77-25fb67aa9f9e" />
<img width="2559" height="1346" alt="image" src="https://github.com/user-attachments/assets/1b6c2662-7d80-4a21-a1c6-99a88217f689" />



## PCB
The PCB & schematic was designed in KiCAD. The schematic is a bit confusing because some keys from col13 are shfted up one row.

![image](https://github.com/user-attachments/assets/0582f0b7-fe37-4078-ab03-c6fc5e5c43f2)
![image](https://github.com/user-attachments/assets/05275983-f0ca-41cb-a112-1fb1ae274621)

## Firmware
The Firmware was created in python using the kmk library. It requires Circuitpython to be installed on the mcu to run. The Macro functions are currently empty, these can be set to any macro you want. KMK also does not have a Menu key so this one is currently set to KC.NO, but it can be repurposed as a layer switch for example.

## BOM

| Item           | Amount         | Total Price    | Required |
|----------------|----------------|----------------|----------|
| Neodymium Magnet 5x2mm  | 18  | 8€  | Yes |
| Rubber Pad 10mm | 2  | 4€  | Yes |
| M2.5x10 screw  | 7  | 11€  | Yes |
| Cherry MX switches | 92 | 75€ | Yes |
| Keycaps | 92 | 30€ | Yes |
| PCB | 1 | / | Yes |
| Raspberry Pi Pico | 1 | 10€ | Yes |
| 3d Printing Filament (any) | 1 spool | ~20€ | No |
| **Total** | | 158€ |

