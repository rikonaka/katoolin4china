# katoolin for China

```zsh
 $$\   $$\             $$\                         $$\ $$\
 $$ | $$  |            $$ |                        $$ |\__|
 $$ |$$  /  $$$$$$\  $$$$$$\    $$$$$$\   $$$$$$\  $$ |$$\ $$$$$$$\
 $$$$$  /   \____$$\ \_$$  _|  $$  __$$\ $$  __$$\ $$ |$$ |$$  __$$\
 $$  $$<    $$$$$$$ |  Kali tools installer |  $$ |$$ |$$ |      $$ |
 $$ |\$$\  $$  __$$ |  $$ |$$\ $$ |  $$ |$$ |  $$ |$$ |$$ |$$ |  $$ |
 $$ | \$$\ \$$$$$$$ |  \$$$$  |\$$$$$$  |\$$$$$$  |$$ |$$ |$$ |  $$ |
 \__|  \__| \_______|   \____/  \______/  \______/ \__|\__|\__|  \__|


               $$\                          $$$$$$$\ $$\
              $$  |                        $$ ______|$$ |     $$\
             $$  /_           $$    $$\   $$ /       $$ \     \__|         $$$$$$$\
          $$$$$$$  | $$$$$$\  $$\ $$ /    $$ |       $$$$$$\  $$\ $$$$$$ \ \_____$$\
            $$  __/ $$    $$\ $$$$ _/     $$ \       $$\__$$\ $$ |$$\__$$ | $$$$$$$ |
            $$ |    $$    $$ |$$  /       \$$ \      $$ | $$ |$$ |$$ | $$ |$$    $$ |
            $$ |    \$$$$$$$ |$$ |         \$$$$$$$$\$$ | $$ |$$ |$$ | $$ |\$$$$$$$ |
            \__|     \_______|\__|          \_______|\__| \__|\__|\__|  \_| \_______|
```

## What can this code do

- Automatically install all Kali tools for Chinese user where visited the kali.org slowly.

- Also, I rewrote a list of functions and collation tools.

- So there will be a lot of differences with the original version.

- The new version uses a very convenient pip3 to install the program.

---

## Support the legitimate rights and interests of programmers

Supporting the 996 prohibited license while not violating the GPLv2.0 license.

[![License: GPL v2](https://img.shields.io/badge/License-GPL%20v2-blue.svg)](https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html) [![996.icu](https://img.shields.io/badge/link-996.icu-red.svg)](https://996.icu) [![LICENSE](https://img.shields.io/badge/license-NPL%20(The%20996%20Prohibited%20License)-blue.svg)](https://github.com/996icu/996.ICU/blob/master/LICENSE)

# Requirements

- Python 3.5 or later.

- pip3 for Python3.

- An Debian and its derivatives operating system.

- Not supprot CentOS or RedHat or Fedora.

## Tested-Distribution

Distribution that have been tested and test videos will put here.

- <del>Ubuntu12.04</del> (Not support, too old)

- <del>Ubuntu14.04</del> (Not support, too old)

- Ubuntu16.04 (![ubuntu16.04 test video](xxxxxxxxxxxxxxxxxxx))

- Ubuntu18.04 (![ubuntu18.04 test video](xxxxxxxxxxxxxxxxxxx))

- Ubuntu18.10 (![ubuntu18.10 test video](xxxxxxxxxxxxxxxxxxx))

- Ubuntu19.04 (![ubuntu19.04 test video](xxxxxxxxxxxxxxxxxxx))

# Installation

- Here is a simple installation way use the pip

```
sudo apt-get install git
git clone https://github.com/rikonaka/katoolin4china.git
cd katoolin4china
sudo pip3 install .
```

- After this command, the k4c will installed in you system

# Uninstallation

- Here is a simple uninstallation way

```
sudo pip3 uninstall katoolin4china
rm -rf katoolin4china/
```

# Use-The-Tool

- Just input the k4c like this

```
sudo k4c
```

# Upgrade

```
cd katoolin4china/
git pull
sudo pip3 install --upgrade .
```

# Not-Support-Tool-List

- Some software is no longer included in the latest version of the Kail.

- So we will NOT install it into you system (actually we also cound't found it's .deb package).

- But you can see them at https://tools.kali.org/tools-listing (because the maintenance staff of the Kali website is lazy).

## - Information Gathering

```
bing-ip2hosts
ntop
```

## - Vulnerability Analysis
```
commix
DBPwAudit
GSD
Inguma
```

## - Wireless Attack
```
BlueMaho
Bluepot
Gqrx
gr-scan
```

## - Web Applications
```
Cutycapt
Webshag
WebSlayer
```

## - Sniffing & Spoofing
```
isr-svilgrade
```

## - Exploitation Tools
```
Nishange
```

## - Forensics Tools
```
Capstone
DFF
diStorm3
RegRipper
```

## - Stress Testing
```
Inundator
```

## - Password Attacks
```
DBPwAudit
THC-Hydra
phrasendrescher
SQLdict
```

## - Extra
```
Wifresti
```

---

# Other

## Installation-GIF

![how to install](https://github.com/rikonaka/katoolin4china/blob/master/pic/howtouse.gif)

## Hotkey

- back : Go back

- home : Go to the main menu

## Warning

- Before upgrade your system , please make sure you have removed all Kali-linux repositories in you /etc/apt/sources.list.

## Have questions?

- Please visit https://github.com/rikonaka/katoolin4china/issues

## Feature

- [x] Python3 and pip3 support.

- [ ] Automatically test mirror site speed and latency and choose the best one.

- [ ] Graphical interface implementation.

- [ ] Check installed kali package.
