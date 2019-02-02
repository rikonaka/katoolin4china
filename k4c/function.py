#!/usr/bin/env python3

'''
Module docstring:

Place some core function here
'''

import subprocess
import sys
import os

# Custom module
from . import toollist
from . import interface


def init_apt():
    '''
    Change the /etc/apt/sources.list here

    Add the tuna repositories
    '''

    try:
        # This command is add the pgp keys
        # If NOT add
        # We will see ' GPG error'
        # subprocess.check_call(
        #     'apt-key adv --keyserver pgp.mit.edu --recv-keys ED444FF07D8D0BF6', shell=True)
        # use the new key server
        subprocess.check_call(
            'apt-key adv --keyserver keys.gnupg.net --recv-keys 7D8D0BF6', shell=True)
    except subprocess.CalledProcessError as error_output:
        print('Call error: {0}'.format(error_output))

    try:
        # Here we back up the original config file
        subprocess.check_call(
            'cp /etc/apt/sources.list /etc/apt/sources.list.bak', shell=True)
    except subprocess.CalledProcessError as error_output:
        print('Copy apt file error: {0}'.format(error_output))

    try:
        # Add the repositories in /etc/apt/sources.list
        subprocess.check_call(
            "echo '# Kali repositories in China | Added by Katoolin4China\ndeb http://mirrors.tuna.tsinghua.edu.cn/kali kali-rolling main contrib non-free' >> /etc/apt/sources.list", shell=True)
    except subprocess.CalledProcessError as error_output:
        print('Call error: {0}'.format(error_output))


def add_apt():
    '''
    Add the repositories manual
    '''

    try:
        # Here we back up the original config file
        subprocess.check_call(
            'cp /etc/apt/sources.list /etc/apt/sources.list.bak', shell=True)
    except subprocess.CalledProcessError as error_output:
        print('Copy apt file error: {0}'.format(error_output))

    try:
        # Add the repositories in /etc/apt/sources.list
        subprocess.check_call(
            "echo '# Kali repositories in China | Added by Katoolin4China\ndeb http://mirrors.tuna.tsinghua.edu.cn/kali kali-rolling main contrib non-free' >> /etc/apt/sources.list", shell=True)
    except subprocess.CalledProcessError as error_output:
        print('Call error: {0}'.format(error_output))


def loop():

    while True:
        # Print the start menu here
        interface.pstart()
        uselect = input('\033[1;36mkat > \033[1;m')
        '''
        1) Kali repositories setting     (add the tuna repositories)
        2) Install tools                 (show the Kali tool menu)
        3) Help                          (as you see)
        4) Quit                          (quit the programer)
        '''
        while uselect == '1':
            '''
            1) Update                                      (execute the sudo apt-get update)
            2) Remove all Kali repositories                (remove the Kali repositories)
            3) View the contents of sources.list file      (show the sources.list)
            4) Add Kali repositoried manual                (do it again)
            '''
            interface.repo_setting()
            uselect_is_1 = input(
                '\033[1;36mWhat do you want to do? > \033[1;m')

            if uselect_is_1 == '1':
                try:
                    subprocess.check_call('apt-get update -m', shell=True)
                except subprocess.CalledProcessError as error_output:
                    print('Apt error: {0}'.format(error_output))
                    sys.exit(1)

            elif uselect_is_1 == '2':
                try:
                    subprocess.check_call(
                        'rm -f /etc/apt/sources.list', shell=True)
                except subprocess.CalledProcessError as error_output:
                    print(
                        'Remove the /etc/apt/sources.list failed: {0}'.format(error_output))
                    sys.exit(1)

                try:
                    subprocess.check_call(
                        'cp /etc/apt/sources.list.bak /etc/apt/sources.list', shell=True)
                except subprocess.CalledProcessError as error_output:
                    print('Copy back up file failed: {0}'.format(error_output))
                    sys.exit(1)

                try:
                    subprocess.check_call(
                        'mv /etc/apt/sources.list.bak /etc/apt/sources.list.katoolin4cina', shell=True)
                except subprocess.CalledProcessError as error_output:
                    print('Katoolin4china backup filed: {0}'.format(
                        error_output))
                    sys.exit(1)

                print(
                    '\033[1;31m\nAll Kali repositories have been deleted!\n\033[1;m')

            elif uselect_is_1 == 'back':
                # main loop
                loop()

            elif uselect_is_1 == 'home':
                loop()

            elif uselect_is_1 == '3':
                file = open('/etc/apt/sources.list', 'r')
                print(file.read())

            elif uselect_is_1 == '4':
                add_apt()

            else:
                print('\033[1;31mSorry, that was an invalid command!\033[1;m')

        if uselect == '2':
            loop_2()

        elif uselect == '3':
            interface.phelp()

        elif uselect == '4':
            try:
                subprocess.check_call(
                    'cp /etc/apt/sources.list.bak /etc/apt/sources.list.k4c', shell=True)
            except subprocess.CalledProcessError as error_output:
                print('Make katoolin4china failed: {0}'.format(error_output))

            try:
                subprocess.check_call(
                    'cp /etc/apt/sources.list.bak /etc/apt/sources.list', shell=True)
            except subprocess.CalledProcessError as error_output:
                print(
                    'Copy /etc/apt/sources.list.bak failed: {0}'.format(error_output))

            print(
                '\033[1;31m\nAll Kali repositories have been deleted !\n\033[1;m')
            sys.exit(0)


def install_all(toollist):
    '''
    Install all the tools in toollist
    '''
    count = 1
    length = len(toollist)
    for tool in toollist:
        # Some unsupport package dict.values() return 0
        if tool != 0:
            print(
                '\033[1;36mInstall\033[1;m \033[1;32m{0}    {1}/{2}\033[1;m'.format(tool, count, length))
            try:
                subprocess.check_call(
                    'apt install -f -y {0}'.format(tool), shell=True)
            except subprocess.CalledProcessError as error_output:
                print('Install \033[1;31m{0}\033[1;m failed: {1}'.format(
                    tool, error_output))
            count += 1


def uninstall_all(toolist):
    '''
    Uninstall all the tools in toolist
    '''

    for tool in toolist:
        # Some unsupport package dict.values() return 0
        if tool != 0:
            print(
                '\033[1;36mRemove\033[1;m \033[1;32m{0}\033[1;m'.format(tool))
            try:
                subprocess.check_call(
                    'apt -y autoremove {0}'.format(tool), shell=True)
            except subprocess.CalledProcessError as error_output:
                print('Remove the {0} failed: {1}'.format(
                    tool, error_output))


def every_select(toolswitcher, specialtoolswitcher):
    '''
    Solve repetitive code issues
    '''

    print(
        '\033[1;32mInsert the number of the tool to install it.\n\033[1;m')
    eselect = input('\033[1;36mkat > \033[1;m')

    if eselect == 'back':
        loop()

    elif eselect == 'home':
        loop()

    elif eselect == '0':
        toollist = toolswitcher.values()
        install_all(toollist)

    else:
        try:
            eselectnum = int(eselect)
        except IOError as error_output:
            print('\033[1;31mInvalid command!\033[1;m')
            print('Error: {0]'.format(error_output))

        package_name = toolswitcher.get(
            eselectnum, 'nothing')

        if package_name != 0 and package_name != 'nothing':
            try:
                subprocess.check_call(
                    'apt install {0}'.format(package_name), shell=True)
            except subprocess.CalledProcessError as error_output:
                print('Install \033[1;31m{0}\033[1;m failed: {1}'.format(
                    package_name, error_output))

        elif package_name == 0:
            # Find the install way in specialtoolswitcher
            install_way = specialtoolswitcher.get(
                eselectnum, '\033[1;31mSorry, This package is not supportd\033[1;m'
            )
            print(install_way)

        elif package_name == 'nothing':
            print('\033[1;31mInvalid command!\033[1;m')


def loop_2():
    '''
    Install loop
    '''

    interface.pinstall()
    # 1) Information Gathering            8) Exploitation Tools
    # 2) Vulnerability Analysis           9) Forensics Tools
    # 3) Wireless Attacks                 10) Stress Testing
    # 4) Web Applications                 11) Password Attacks
    # 5) Sniffing & Spoofing              12) Reverse Engineering
    # 6) Maintaining Access               13) Hardware Hacking
    # 7) Reporting Tools                  14) Extra
    # 0) Install all                      r) Remove all
    print(
        '\033[1;32mSelect a category or press (0) to install all Kali tools.\n\033[1;m')

    uselect_2 = input('\033[1;36mkat > \033[1;m')
    if uselect_2 == 'back':
        loop()

    elif uselect_2 == 'home':
        loop()

    elif uselect_2 == 'r':
        # Remove all the tools
        # Get the tool dict
        information_dict = toollist.information_gathering()
        vulnerability_dict = toollist.vulnerability_analysis()
        wireless_dict = toollist.wireless_attacks()
        web_dict = toollist.web_applications()
        sniffing_dict = toollist.sniffing_spoofing()
        maintaining_dict = toollist.maintaining_access()
        reporting_dict = toollist.reporting_tools()
        exploitation_dict = toollist.exploitation_tools()
        forensics_dict = toollist.forensics_tools()
        stress_dict = toollist.stress_testing()
        password_dict = toollist.password_attacks()
        reverse_dict = toollist.reverse_engineering()
        hardware_dict = toollist.hardware_hacking()
        extra_dict = toollist.extra()

        # Get the tool list
        information_list = information_dict.values()
        vulnerability_list = vulnerability_dict.values()
        wireless_list = wireless_dict.values()
        web_list = web_dict.values()
        sniffing_list = sniffing_dict.values()
        maintaining_list = maintaining_dict.values()
        reporting_list = reporting_dict.values()
        exploitation_list = exploitation_dict.values()
        forensics_list = forensics_dict.values()
        stress_list = stress_dict.values()
        password_list = password_dict.values()
        reverse_list = reverse_dict.values()
        hardware_list = hardware_dict.values()
        extra_list = extra_dict.values()

        uninstall_all(information_list)
        uninstall_all(vulnerability_list)
        uninstall_all(wireless_list)
        uninstall_all(web_list)
        uninstall_all(sniffing_list)
        uninstall_all(maintaining_list)
        uninstall_all(reporting_list)
        uninstall_all(exploitation_list)
        uninstall_all(forensics_list)
        uninstall_all(stress_list)
        uninstall_all(password_list)
        uninstall_all(reverse_list)
        uninstall_all(hardware_list)
        uninstall_all(extra_list)

    elif uselect_2 == '0':
        # Install all the tools
        # Get the tool dict
        information_dict = toollist.information_gathering()
        vulnerability_dict = toollist.vulnerability_analysis()
        wireless_dict = toollist.wireless_attacks()
        web_dict = toollist.web_applications()
        sniffing_dict = toollist.sniffing_spoofing()
        maintaining_dict = toollist.maintaining_access()
        reporting_dict = toollist.reporting_tools()
        exploitation_dict = toollist.exploitation_tools()
        forensics_dict = toollist.forensics_tools()
        stress_dict = toollist.stress_testing()
        password_dict = toollist.password_attacks()
        reverse_dict = toollist.reverse_engineering()
        hardware_dict = toollist.hardware_hacking()
        extra_dict = toollist.extra()

        # Get the tool list
        information_list = information_dict.values()
        vulnerability_list = vulnerability_dict.values()
        wireless_list = wireless_dict.values()
        web_list = web_dict.values()
        sniffing_list = sniffing_dict.values()
        maintaining_list = maintaining_dict.values()
        reporting_list = reporting_dict.values()
        exploitation_list = exploitation_dict.values()
        forensics_list = forensics_dict.values()
        stress_list = stress_dict.values()
        password_list = password_dict.values()
        reverse_list = reverse_dict.values()
        hardware_list = hardware_dict.values()
        extra_list = extra_dict.values()

        install_all(information_list)
        install_all(vulnerability_list)
        install_all(wireless_list)
        install_all(web_list)
        install_all(sniffing_list)
        install_all(maintaining_list)
        install_all(reporting_list)
        install_all(exploitation_list)
        install_all(forensics_list)
        install_all(stress_list)
        install_all(password_list)
        install_all(reverse_list)
        install_all(hardware_list)
        install_all(extra_list)

    while uselect_2 == '1':
        # Show the menu of infromation gathering
        interface.pinstall_information()
        switcher = toollist.information_gathering()
        special_switcher = {
            5: 'Use: wget http://www.morningstarsecurity.com/downloads/bing-ip2hosts-0.4.tar.gz && tar -xzvf bing-ip2hosts-0.4.tar.gz && cp bing-ip2hosts-0.4/bing-ip2hosts /usr/local/bin/'
        }
        every_select(switcher, special_switcher)

    while uselect_2 == '2':
        # Show the menu of Vulnerability Analysis
        interface.pinstall_vulnerability()
        switcher = toollist.vulnerability_analysis()
        special_switcher = {
            8: 'Use: apt install git && git clone https://github.com/stasinopoulos/commix.git commix && cd commix && python ./commix.py --install',
            9: 'Download page: http: // www.cqure.net/wp/tools/database/dbpwaudit/',
            13: 'Use: apt install git && git clone git://git.kali.org/packages/gsd.git',
            15: 'Download page: http://inguma.sourceforge.net',
        }
        every_select(switcher, special_switcher)

    while uselect_2 == '3':
        interface.pinstall_wireless()
        switcher = toolist.wireless_attacks()
        special_switcher = {
            4: 'Use: apt install git && git clone git://git.kali.org/packages/bluemaho.git',
            5: 'Use apt install git && git clone git://git.kali.org/packages/bluepot.git',
            15: 'Use: apt install git && git clone git://git.kali.org/packages/gqrx.git',
            16: 'Use: apt-get install git && git clone git://git.kali.org/packages/gr-scan.git',
        }
        every_select(switcher, special_switcher)

    while uselect_2 == '4':
        interface.pinstall_web()
        switcher = toollist.web_applications()
        special_switcher = {
            7: 'Use: apt install git && git clone https://github.com/stasinopoulos/commix.git commix && cd commix && python ./commix.py --install',
            36: 'Use: apt install git && git clone git://git.kali.org/packages/webslayer.git',
        }
        every_select(switcher, special_switcher)

    while uselect_2 == '5':
        interface.pinstall_sniffing()
        switcher = toollist.sniffing_spoofing()
        special_switcher = {
            9: 'Use: apt install git && git clone git://git.kali.org/packages/isr-evilgrade.git'
        }
        every_select(switcher, special_switcher)

    while uselect_2 == '6':
        interface.pinstall_maintaining()
        switcher = toollist.maintaining_access()
        special_switcher = {}
        every_select(switcher, special_switcher)

    while uselect_2 == '7':
        interface.pinstall_reporting()
        switcher = toollist.reporting_tools()
        special_switcher = {}
        every_select(switcher, special_switcher)

    while uselect_2 == '8':
        interface.pinstall_exploitation()
        switcher = toollist.exploitation_tools()
        special_switcher = {
            8: 'Use: apt install git && git clone https://github.com/stasinopoulos/commix.git commix && cd commix && python ./commix.py --install'
        }
        every_select(switcher, special_switcher)

    while uselect_2 == '9':
        interface.pinstall_forensics()
        switcher = toollist.forensics_tools()
        special_switcher = {
            3: 'Use: apt install git && git clone git://git.kali.org/packages/capstone.git',
            9: 'Use apt install git && git clone git://git.kali.org/packages/distorm3.git',
        }
        every_select(switcher, special_switcher)

    while uselect_2 == '10':
        interface.pinstall_stress()
        switcher = toollist.stress_testing()
        special_switcher = {
            4: 'Use: apt install git && git clone git://git.kali.org/packages/inundator.git',

        }
        every_select(switcher, special_switcher)

    while uselect_2 == '11':
        interface.pinstall_password()
        switcher = toollist.password_attacks()
        special_switcher = {
            9: 'Use: apt install git && git clone git://git.kali.org/packages/dbpwaudit.git',
            14: 'please visit: http://www.leidecker.info/projects/phrasendrescher/index.shtml',
            25: 'Use: apt install git && git clone git://git.kali.org/packages/phrasendrescher.git',
            30: 'Use: apt install git && git clone git://git.kali.org/packages/sqldict.git',
        }
        every_select(switcher, special_switcher)

    while uselect_2 == '12':
        interface.pinstall_reverse()
        switcher = toollist.reverse_engineering()
        special_switcher = {}
        every_select(switcher, special_switcher)

    while uselect_2 == '13':
        interface.pinstall_hardware()
        switcher = toollist.hardware_hacking()
        special_switcher = {}
        every_select(switcher, special_switcher)

    while uselect_2 == '14':
        interface.pinstall_extra()
        switcher = toollist.extra()
        special_switcher = {
            1: 'Use: apt install git && git clone https://github.com/LionSec/wifresti.git && cp wifresti/wifresti.py /usr/bin/wifresti && chmod +x /usr/bin/wifresti && wifresti'
        }
        every_select(switcher, special_switcher)
