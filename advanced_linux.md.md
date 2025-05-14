- further on user
- ownership and permmission
### user management further
 - change password of user
     - give password to users created by command **useradd
         sudo passwd name_user
     - change paswword of users
         **sudo passwd user_name
         
- change id
     - to change user id **sudo usermod -u new_id user_name
     - to change group id **sudo usermod -g new_id user_name
     
- to delete user
     **sudo userdel -r user_name
     -r  --------to delete all files inside  it
     
- login to users 
     - **su - user_name-----------by asking password
     -  **sudo su - user_name -----with out asking password
     if i haven't password just click enter
     - exit-------to get back to our local user
- to unhide hidden users
     - **sudo mkhomedir_helper user_name
     
- change shell type
     - **sudo usermod user_name -s /bin/shell_type
     
#### if user havent group 
-  to creat group
     - sudo groupadd group_name
- to add user to the group
     - **sudo usermod -aG group_name user_name
- to delete users from group
     - **sudo gpasswd -d  user_name group_name
 
## sudoers file
 - every user other than local users can't use use unless we add them to sudoers file
 - to enter to sudoers file
     **sudo visudo
    then edit the privilage and give users root privilage

## linux file permission
- every file have owner and permission
- when we apply command ls-l to see file details we got 5 parts
1,permission   2,ownership   3,date   4,size    5,filename
-rwxrwxrwx 1   kali kali       
#### ownership
- who's the creator(user owner)   and its group owner
- to change user ownership and group ownership of file
     **sudo chon user:group file_name
     
#### permission
read(r) 4 
write(w) 2
execute(x) 1
- they will given to **user(u) group(g) and other(o)   all(a)
###### chmod
helps to change file permission
##### changing permission
- symbolic add permission
      sudo chmod a+x file_name
      sudo chmod o+w file_name
      sudo chmod u+r file_name
      sudo chmod a+ rwx file_name
      ....
      '''
    - we can use many modifications using comma(,) example
          **sudo chmod a+rwx,u-r,o-x,,,, file name
          sudo chmod a-rwx,u+r,o+x,,,, file name
          

- **numeric add permission
     sudo chmod 654 file_name
       mean 
        6 for user =4+2  mean read and write
        5 for group=4+1 mean read and execute
        4 for others mean read
    sudo chmod 777 file_name

 