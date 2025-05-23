### special file permissition
     power full file permmissions 
     SUID bits(s)------set user id bit(4) 
     SGID bits(s)------set group id bit(2)
     Sticky bits(t) -----set other id bit(1)
these permissions are used to files that are executable they replace **execute
they written before the other permission like
4777,2333,4333............. mean giving additional (special) permissions
- when permission starts with 4(SUID) --------mean giving full permission to run for user **sudo chmod u+s file_name
- when permission starts with 2(SGID) --------mean giving full permission to run for groups **sudo chmod g+s file_name
- when permission starts with 1(Sticky) --------mean giving full permission to run for others **sudo chmod +t file_name

### package installation
#### - package mannegerrs
     - apt and dpkg for debian besed distribution
     to install packages from online server and remove packages 
#### apt       apt-get --------- older version of apt
- it need internet to download packages and but not to delete packages
- **sudo apt update--------- tell us if there is update for softwares in our linux machin
- **sudo apt upgrade software_name ------- install updates
- [ ] **sudo apt search software_name   to search packages
- **sudo apt install software_name   to install packages
- **sudo apt remove software_name   -----delate software or package only
- **sudo apt purge software_name ----- delate software and its related files
- **sudo apt autoremove -------to remove files that have not functional or haven't their package

#### packages dependencies(modules)
    they are needed to make the package functional
    they are like related files for the packages

**errors when installation
- if we try to install two or more apt at a time
     - 
- if we try to use apt with out sudo unless we are local user
- if we made mistake in the name of the package or it doesn't exist
- if linux repository configuration link is not normal or outdated o
     to see   **sudo nano /etc/apt/sources
     or     sudo apt edit-source

#### dpkg
**after downloading .deb files
- ofline package manager
- it does install file only file having .deb extension in our machine
- **sudo dpkg -i  software_name ------install packages
- **sudo dpkg -r  software_name ------remove package
- **sudo dpkg -p  software_name ------to see(print) package info
