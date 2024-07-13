# Mercury Engine Data Structures
Construct type definitions for Mercury Engine

| Format    | Dread ExeFS File Name | Samus Returns (Read) | Samus Returns (Write) | Dread (Read) | Dread (Write) |
|-----------|-----------------------|----------------------|-----------------------|--------------|---------------|
| BAPD      | audiopreset           | Missing              | Missing               | &cross;      | &cross;       |
| BCCAM     | canim                 | &cross;              | &cross;               | &cross;      | &cross;       |
| BCLGT     | lighting              | &cross;              | &cross;               | Missing      | Missing       |
| BCMDL     | model                 | &cross;              | &cross;               | &check;      | &cross;       |
| BCPTL     | fx                    | &cross;              | &cross;               | &cross;      | &cross;       |
| BCSKLA    | anim                  | &cross;              | &cross;               | &cross;      | &cross;       |
| BCTEX     | tex                   | &cross;              | &cross;               | &check;      | &cross;       |
| BCURV     | curve                 | Missing              | Missing               | &cross;      | &cross;       |
| BCUT      |                       | &cross;              | &cross;               | Missing      | Missing       |
| BCWAV     |                       | &cross;              | &cross;               | Missing      | Missing       |
| BFGRP     |                       | Missing              | Missing               | &cross;      | &cross;       |
| BFONT     | font                  | &cross;              | &cross;               | &cross;      | &cross;       |
| BFSAR     | atkprj                | Missing              | Missing               | &cross;      | &cross;       |
| BFSTM     |                       | Missing              | Missing               | &cross;      | &cross;       |
| BGSNDS    | gamesnds              | Missing              | Missing               | &cross;      | &cross;       |
| BLDEF     | lightsdef             | Missing              | Missing               | &check;      | &check;       |
| BLSND     | sndlimits             | &check;              | &check;               | &check;      | &check;       |
| BLUT      | lut (lookup table?)   | Missing              | Missing               | &cross;      | &cross;       |
| BMBLS     | blendspace            | Missing              | Missing               | &check;      | &check;       |
| BMDEFS    | musicdefs             | &cross;              | &cross;               | &cross;      | &cross;       |
| BMMAP     | minimap               | Missing              | Missing               | &check;      | &check;       |
| BMMDEF    | mmapdef               | Missing              | Missing               | &check;      | &check;       |
| BMSAD     | actordef              | &check;              | &check;               | &check;      | &check;       |
| BMSAS     | actionset             | Missing              | Missing               | &check;      | &check;       |
| BMSAT     | animtree              | &cross;              | &cross;               | &cross;      | &cross;       |
| BMSBK     | mapbreak              | &check;              | &check;               | Missing      | Missing       |
| BMSCC     | mapcamcoll            | &check;              | &check;               | &check;      | &check;       |
| BMSCD     | colldata              | &check;              | &check;               | &check;      | &check;       |
| BMSCP     | composition           | Missing              | Missing               | &check;      | &check;       |
| BMSCU     | cutscene              | &cross;              | &cross;               | &check;      | &check;       |
| BMSEM     |                       | &cross;              | &cross;               | Missing      | Missing       |
| BMSES     |                       | &check;              | &check;               | Missing      | Missing       |
| BMSEV     |                       | &cross;              | &cross;               | Missing      | Missing       |
| BMSLD     | leveldef              | &check;              | &check;               | Missing      | Missing       |
| BMSLGROUP | slinkgroup            | Missing              | Missing               | &check;      | &check;       |
| BMSLINK   | slinkrules            | Missing              | Missing               | &check;      | &check;       |
| BMSMD     |                       | &check;              | &check;               | Missing      | Missing       |
| BMSMSD    |                       | &check;              | &check;               | Missing      | Missing       |
| BMSNAV    | navmesh               | &cross;              | &cross;               | &check;      | &check;       |
| BMSND     |                       | &cross;              | &cross;               | Missing      | Missing       |
| BMSSA     |                       | &cross;              | &cross;               | Missing      | Missing       |
| BMSSD     | mapscene              | &cross;              | &cross;               | &check;      | &check;       |
| BMSSH     | shape                 | Missing              | Missing               | &cross;      | &cross;       |
| BMSSK     | skin                  | Missing              | Missing               | &check;      | &check;       |
| BMSSS     | sprite_sheet          | Missing              | Missing               | &check;      | &check;       |
| BMSSTOC   |                       | Missing              | Missing               | &cross;      | &cross;       |
| BMTRE     | behtree               | &cross;              | &cross;               | &check;      | &check;       |
| BMTUN     |                       | &check;              | &check;               | Missing      | Missing       |
| BNVIB     | rumble                | Missing              | Missing               | &cross;      | &cross;       |
| BPSI      | packsets              | &cross;              | &cross;               | &cross;      | &cross;       |
| BPTDAT    | playdata              | Missing              | Missing               | &cross;      | &cross;       |
| BPTDEF    | playdef               | Missing              | Missing               | &cross;      | &cross;       |
| BREM      | mapenvmus             | Missing              | Missing               | &check;      | &check;       |
| BRES      | mapenvsnd             | Missing              | Missing               | &check;      | &check;       |
| BREV      | mapenv                | Missing              | Missing               | &check;      | &check;       |
| BRFLD     | leveldef              | Missing              | Missing               | &check;      | &check;       |
| BRSA      | subarearef            | Missing              | Missing               | &check;      | &check;       |
| BRSPD     | shotsnds              | Missing              | Missing               | &cross;      | &cross;       |
| BSHDAT    | program               | &cross;              | &cross;               | &cross;      | &cross;       |
| BSMAT     | material              | Missing              | Missing               | &check;      | &check;       |
| BTUNDA    | tunables              | Missing              | Missing               | &check;      | &check;       |
| BUCT      | glyphs                | &cross;              | &cross;               | &cross;      | &cross;       |
| INI       |                       | Missing              | Missing               | &check;      | &check;       |
| LC        | script                | &check;              | &check;               | &check;      | &check;       |
| PKG       | pack                  | &check;              | &check;               | &check;      | &check;       |
| TOC       |                       | &check;              | &check;               | &check;      | &check;       |
| TXT       | txt                   | &check;              | &check;               | &check;      | &check;       |
| WEBM      |                       | Missing              | Missing               | &cross;      | &cross;       |



## Example Usage

```python
# TODO
```

## Colors for Text

Metroid Dread uses the following annotations in text to change color:

| Code | Color       |              |
|------|-------------|--------------|
| {c0} | White       | (Default)    |
| {c1} | Yellow      |              |
| {c2} | Red         |              |
| {c3} | Pink        |              |
| {c4} | Green       |              |
| {c5} | Blue        |              |
| {c6} | UI Active   | (Light blue) |
| {c7} | UI Inactive | (Dim blue)   |
