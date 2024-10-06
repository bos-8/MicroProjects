```yaml
tag:        [mini-project, keypress, osd]
title:      KeyPress OSD - PowerShell Script
date:       2024-07-23
update:     2024-07-23
version:    0x0010
author:     BO$
copyright:  BO$ <https://github.com/bos-8>
license:    AGPL 3.0
file:       key-displayer-1.ps1
```
# KeyPress OSD - PowerShell Script

## PURPOSE OF THE DOCUMENT
This document describes the KeyPress OSD script, which provides an On-Screen Display (OSD) of keyboard and mouse key presses. It is designed for use in presentations, tutorials, or to enhance accessibility for users.

## DESCRIPTION / TASK CONTENT
The KeyPress OSD script captures real-time keyboard and mouse activity, displaying the keys pressed in a minimal and unobtrusive on-screen window. This tool can be beneficial for educators, trainers, and anyone needing to demonstrate keyboard actions visually.

![KeyPress OSD Initial Window](./keydisplayer-1.jpg)

## TECHNOLOGIES / TOOLS
- PowerShell
- Windows Forms

## INSTALLATION
1. Download the `key-displayer-1.ps1` script from the repository.
2. Open PowerShell.
3. Navigate to the directory where the script is saved.
4. Execute the script using one of the following methods:
   - Using the command line:
     ```powershell
     .\key-displayer-1.ps1
     ```
   - Alternatively, you can right-click on the `key-displayer-1.ps1` file and select **Run with PowerShell** from the context menu.

## REQUIREMENTS
```yaml
system:     Windows 10/11
PowerShell: 5.1 or later
```

## EXECUTION / USAGE
1. **Run the Script**: Execute the script to open the initial window.
2. **Activate Key Displayer**: Click the button within the initial window to activate the key displayer.
   ![Key Displayer Active Window](./keydisplayer-2.jpg)
3. **Key Displayer Behavior**:
   - The key displayer window will remain on top of all other windows.
   - It will not respond to drag actions, ensuring it maintains its position.
4. **Deactivate Key Displayer**:
   - Click the key displayer window again.
   - Alternatively, press the NUM LOCK key on your keyboard to deactivate it.

## RESOURCES / LINKS / BIBLIOGRAPHY
[GitHub `bos-8` Repository Link](https://github.com/bos-8/MicroProjects/)

## CHANGES
|    # | VERSION  |             AUTHOR             |    DATE    | DESCRIPTION                     |
| ---: | :------: | :----------------------------: | :--------: | ------------------------------- |
|    1 | `0x0010` | BO$ <https://github.com/bos-8> | 2024-07-23 | Creation of KeyPress OSD script |
