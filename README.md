# katoolin for China
- Automatically install all Kali tools for Chinese user where visited the kali.org slowly.
- I also rewrote a list of functions and collation tools.
- So there will be a lot of defferences with the original version.
- The new version uses a very convenient pip3 to install the program.

```
 $$\   $$\             $$\                         $$\ $$\
 $$ | $$  |            $$ |                        $$ |\__|
 $$ |$$  /  $$$$$$\  $$$$$$\    $$$$$$\   $$$$$$\  $$ |$$\ $$$$$$$\
 $$$$$  /   \____$$\ \_$$  _|  $$  __$$\ $$  __$$\ $$ |$$ |$$  __$$\
 $$  $$<    $$$$$$$ |  Kali tools installer |$$ |$$ |$$ |  $$ |
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

![k4c](https://github.com/rikonaka/katoolin4china/blob/master/pic/howtouse.gif)

# Requirements
- Python 3.5 or later
- pip for Python3
- An operating system (tested on Ubuntu, but not tested on Debian)
- Not supprot CentOS or Redhat or Fedora

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

- Some software is no longer included in the latest version of the Kail
- So we will NOT install it into you system(actually we also cound't found it '.deb' package)
- But you can see at https://tools.kali.org/tools-listing

---

- Information Gathering

```
bing-ip2hosts
ntop
```

- Vulnerability Analysis
```
commix
DBPwAudit
GSD
Inguma
```

- Wireless Attack
```
BlueMaho
Bluepot
Gqrx
gr-scan
```

- Web Applications
```
Cutycapt
Webshag
WebSlayer
```

- Sniffing & Spoofing
```
isr-svilgrade
```

- Exploitation Tools
```
Nishange
```

- Forensics Tools
```
Capstone
DFF
diStorm3
RegRipper
```

- Stress Testing
```
Inundator
```

- Password Attacks
```
DBPwAudit
THC-Hydra
phrasendrescher
SQLdict
```

- Extra
```
Wifresti
```

# Video
- Not have yet

# Usage
- Typing the number of a tool will install it
- Typing 0 will install all Kali tools
- By installing armitage , you will install metasploit

# Hotkey
- back : Go back
- home : Go to the main menu

# Warning
- Before upgrade your system , please make sure you have removed all Kali-linux repositories in you /etc/apt/sources.list.

# Have questions?
- Please visit https://github.com/rikonaka/katoolin4china/issues

# Feature

[ ] Automatically test mirror site speed and latency and choose the best one.

[ ] Graphical interface implementation.

[ ] Remove installed kali package.