
###  script installation
    how to install tools from github or other source
to install scripts from github
    **git clone github_link_of_the_file
    
### to install dependency for scripts
 - for python
     **pip install -r requirment.txt
- go
     **go install module_name
- Ruby
     **gem install module_name

#### python scripts installation
 - **pip install  script_name
 
 - if it doesn't work use command **pip install  script_name --break-system-package
 - if pip comand is not installed we must install it first
 - if pip is not working there is other commandthat's **pipx

#### go scripts installation
old version **go get github_link
new version **go install github_link
first move file from its default path to ~/user/bin to make it work

### asking help from linux
- **man command_name
     tell us everything about the command about 
- command_name -h
-  command_name -help
-  command_name --help
**we use them depending on the command and they will tell us all options for the command.

## linux_process_and_service
### processes 
- **these programs that's instantly we are using
- to see running programs **ps
- **ps -A    all running processes
- **ps -u user_name           to see processes running on the specific user
- **ps aux--------------to see processes with their pricess id
### service(daemons)
- background programs

### managing processes
 ####  **kill       ---to stop running processes
 pid          ----process id
 ppid        parent process id  when ONE process run other by itself
 - **kill -19 pid  -------------- to stop process
 - **kill -18 pid ------------to resume the process that we stopped before
 - **kill -9 -------------stop process immediately(force fully)
 - **killall  program_name------ when to stop all processes related to the program

#### ps command is not real time 
- because is will show us processes when we write ps command so we need other command
#### top(pre inistalled in our linux)
just write command   **top

#### htop(not pre inistalled in our linux)
first download it using **sudo apt install htop
just write command   **htop

### foreground & background
to make command in background using **command&
to make it back --------- fg pid

fgcommand &-------------to open file in the background

## service
### managing service
- **sudo systemctl start  service_name------------temporary start 
- **sudo systemctl stop  service_name------------temporary stop
- **sudo systemctl enable  service_name------------permanent on unless we edit 
- **sudo systemctl disable  service_name------------permanently of unless we edit
- - **sudo systemctl status  service_name------------to see status of te service(daemon)

** sudo service start/stop service_nama--------only temporary like systemctl stop/start

### null device(black hole)(bit pocket)
- file found in /dev/null
- it's used to ignore any command out put
- when we don't want to see errors
- **two things use this time

   - STDERR=2---------select the error and redirect it to where we want
     **sudo command 2> where_we-want
   - STDOUT=1--------select the not error  part of result then redirect it to where we want
      **sudo command 1> where_we-want
      
### symbolic linking(creating shortcut for long paths)
- when we see files detail using ls -l   their  permission starts with -(file) or d(directory)
- but for symbolic linked files there is no - or d they start with l
#### how to create symbolic linked files
  - **ln -s  path symbol
  - ex. **ln -s tedy/diau/deudh/dfhfd/dshid/bbb.txt short_cut
  - then we can see the linkage using **ls -l short_cut
  - linked shortcuts can done only in the home directory
  - to delete linkage **rm short_cut

### alias
- to make shortcut for long commands
##### to creat shortcut for commands for opened terminal only(temporary)
- **alias short_cut_command_name='command'
- 
#### to make it permanent add it in our configuration file
to add 
**nano ~/.bashrc
then add alias shortcut there like this
#alias_modification
alias  new_name="command"

## Tmux(terminal multiplexer)
- **nano.tmux.conf
- add this text  to it
- **unbind C-b
  unbind l
  set -g prefix C-a
  unbind %
  bind e split-window -h
  bind o split-window -v
  set -g base-index 1
  setw -g pane-base-index 1
- then update source code using this command
     **tmux source-file ~/.tmux.conf
### then use tmux
tmux--------------to open tmux then
ctrl+a then o  ----------vertical split
ctrl+a then e -----------side split
ctrl+a then x-------------to exit
ctrl+a then c------------- to create tab
**at the end of the tab name we are in tab if there is*
ctrl+a then ,-------------to rename the tab name
ctrl+a then tab_no------------to move from one tab to another
ctrl+a then <  \\/ >/\\------------- to move from one trminal to the other splited terminal

###  **wget 
- to install files from different servers by using
- **wget  link_of_file

### **find
- to find any file,permissions, in our linux system
- **find path option search_word
- ex.
     find / -name "linux"
     find /home -perm 777
     find -type f ------------find all files int the directorry
     find -type d------------find all folders int the directorry
     find /-type f -perm/4000------------find all files that have special file permission
     
     







