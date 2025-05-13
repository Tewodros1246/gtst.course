#### command
 - command to see who is the user
     whoami
#### users
- root users(id=0)
     - have a power to do any thing
     - created when we are installing our linux machine
- normal users(id=1-999)
     - created by root user
	 - the first created user have more power than other users and local user
     - users can have power as a root when it uses sudo 
#### to see users
cd /
### to add user 
 - useradd user_name
     - add simply and the user is hidden(not discoverable)
     
 - adduser user_name
     - add and tell us all details
- to see users file
     cat /etc/passwd
- to see users password in their encrypted form
     sudo cat/etc/passwd
- to see id
     id
- to see other users id
     id user_name 
#### being as root
 - sudo su ------command to be root
   - exit--------- to exit

   