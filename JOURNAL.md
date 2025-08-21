---
title: "Oliver_QMK_keyboard"
author: "Oliver  Lacika"
description: "A custom designed mechanical keyboard. Not sure yet if I will be able to add any features like rbg or rotary knobs"
created_at: "2025-06-26"
Total Time: "~33hours"
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
# June 30th: Started working on the 3d model

I started working on the case for the keyboard. I finished the top plate and also started working on the main casing. (The screenshots were made on a later date since I forgot to take them at that time, so some changes may be present which I added a day later)

![image](https://github.com/user-attachments/assets/7fbc516b-95d8-4e0a-949b-a8cc65879764)
![image](https://github.com/user-attachments/assets/09f69211-475a-43dc-95ab-3a8dfa7a52f0)


**Total time spent: 8h**
# July 1st: Finished 3d modeling and created the firmware

I finished the 3d model of the case and added a stand to add a 6 degree slope to it. I also added small holes on the bottom of the case and the stand for magnets which are supposed to hold the 2 parts together, and slightly larger holes on the bottom of the stand to add silicone pads to stop it from sliding across the table.

![image](https://github.com/user-attachments/assets/144e8a5c-622e-4111-80e0-e683fd8c387d)
![image](https://github.com/user-attachments/assets/7635cb1c-831a-4457-ac45-62846b0589ac)
![image](https://github.com/user-attachments/assets/b0f255fa-f408-4e50-9c0a-fce6ad88e442)


**Total time spent: 6h**
# July 29th-31st: Added a logo and Name

I created an SVG logo and added it to the bottom of the stand, and also added my nickname (slivki) to the side of the main body. I then spnet a lot of time making sure the logo is printable (due to the overhandds created when printing vertically) which turned out to take much more time than expected

<img width="1461" height="934" alt="image" src="https://github.com/user-attachments/assets/7462e68e-8542-4ea8-bb26-374489a49eec" />
<img width="857" height="372" alt="image" src="https://github.com/user-attachments/assets/62255da1-59df-4f18-8f9e-59e272d52561" />


**Total time spent: 6h**
# August 18th: Started building the keyboard

I 3d printed all the files, and once the parts arrived from amazon, I started roughly assembling the keyboard

![WhatsApp Bild 2025-08-21 um 10 11 58_63fd9120](https://github.com/user-attachments/assets/d2fbf805-d2ec-4759-af5c-c943accb1ff1)
![WhatsApp Bild 2025-08-21 um 10 11 58_f0bbc097](https://github.com/user-attachments/assets/5d8d2d68-6b14-44e2-870e-91c2ca67a8a3)
![WhatsApp Bild 2025-08-21 um 10 11 58_a23e7fb0](https://github.com/user-attachments/assets/c14e0b58-0e15-4843-961d-47d5f3076a6b)


**Total time spent: 5h**
# August 19th: assembled the keyboard with the parts I already had, reprinted some parts

I connected the 2 parts of the main body of the keyboard, spray painted some screws to be less visible, and assembled the keyboard, but without the pcb since I did not have it yet.

![WhatsApp Bild 2025-08-21 um 10 11 58_49705b1e](https://github.com/user-attachments/assets/a8754c38-d13d-4b4d-a83a-eb0c1d8b68db)


**Total time spent: 4h**
# August 20th: assembled the pcb, uploaded firmware, etc. (finished project)

I finally received the pcb and soldered all components to it, uploaded the firmware to rpi pico, the did some minor debugging of both the hardware and the software

<img width="584" height="1600" alt="image" src="https://github.com/user-attachments/assets/2f45cd8c-872b-46ff-9901-4b973a48cadc" />
<img width="899" height="1599" alt="image" src="https://github.com/user-attachments/assets/0aad1a87-9162-4216-a633-b251b8ad6ed9" />

**Total time spent: 7h**

