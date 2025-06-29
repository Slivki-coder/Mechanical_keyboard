---
title: "Oliver_QMK_keyboard"
author: "Oliver  Lacika"
description: "A custom designed mechanical keyboard. Not sure yet if I will be able to add any features like rbg or rotary knobs"
created_at: "2025-06-26"
---
# June 26th: Started working on the pcb, mainly the schematic.

I watched and read a few tutorials on how to design a keyboard before beginning to do so myself. I tried multiple approaches, for example using an STM32 microchip for controlling, but that seemed too complicated for my skill level, and since I didnt want to copy someone else's work, I opted for using the raspberry pi pico. After this, I designed the schematic.

![image](https://github.com/user-attachments/assets/090fa1db-f793-48ed-979a-0b9e558d6d52)


**Total time spent: 5h**
# June 27th: Finished wiring the PCB

I wired all the switches on my PCB to my controller

![image](https://github.com/user-attachments/assets/ae7b270b-8baa-46b2-9920-89d8375cc2eb)


**Total time spent: 8h**
# June 29th: Redesigned everything because the pcb was too messy

My previous attempt required 4 layers, had traces going everywhere and like 5 vias per trace. Because of that, I decided to redesign my schematic (this time keeping the final layout in mind) and then also completely redo the PCB. Now I only need 2 layers, 0 vias and the traces are pretty organised.

![image](https://github.com/user-attachments/assets/15dacf79-3c77-4327-bccd-7a6096c74d43)
![image](https://github.com/user-attachments/assets/a26a1317-221c-4617-982f-90fe2be8e7df)


**Total time spent: 6h**
