##### pwd print working directory
##### echo [string] it takes string as an argument like
echo "my name is"
it will display the string
##### (>) or(>>) output redirecting sign used to output redirecting like
(>)to redirect outputs to not existing file
(>>)to redirect outputs to existing files
ex.
echo "myname and profile" > tedy.text
the echo output redirected to tedy.txt file


##### cat ,head,tail,less    display the contents of file
- cat displays content in the command line
- less uses another app to display contents of the file      ctrl+q to exit from the app
- head display the first 10 lines of the file contents
- tail displays the last 110 lines of the file contents
###### touch       tocreat empty file
##### mkdir      to creat empty directory
mkdir -p to creat directory after some path before moving inside
ex.   mkdir -p home/desctop/tedy/wfguer

##### clear ctrl+l
##### rm      to delete empty directory
##### rm -r    remove directory with its filesnand directories
##### rm -i     remove directory by asking permission
##### rm -f remove forcefully

##### cp to copy file and move to other
cp file new_file
cp -r to copy folder with its file
##### mv  to move file content to another 
mv file new_file

#### grep      to filter some thing from something

grep -i    our filter become case insensetive       
         ex. grep -i "teEdyeE" file_name
grep -c    count how many times we find things
         ex. grep -c "tedy" file_name   how many times tedy apear inside file file_name
grep -l    display file_name
grep -r    search text inside folder
grep -v    to display with out the term 
grep -n  in which number of line the term found
grep -o   display the specific term we find only
grep -a    search from inside binary files
grep -ran 
grep -rno

#### wc [option]  [file]
wc -l number line inside file
wc -w number of words inside file
wc -c the size of file in byte

## multiple command execution
- running two or more commands once
#### 3 ways to do it
- and(&&)      it will work when  all commands have  no error
- or(||)    run one(first) command if it work leave it at on if the first doesn't work it will run the next
- piping(|)       the first command output if as input for the next command

## text processing tools sed and awk

### sed/stream editor
- used to edit text with out opening text edtor
it can
1. replace words (substitute)
     - sed 's/old_word/new_word'
2. replace all occurance (substitute)
     - sed 's/old_word/new_word/g'
3.  to insert line
     -  above line--------------sed 'line_number i\new_line' file_name
     -   under line--------------sed 'line_number a\new_line' file_name
4. delete line
     - sed 'Nd' file_name
     - sed 'N,N,N,Nd' file name
5.  work with patterns



sed [option] "command"
### awk
1. to print column
     - awk '{print $N}'      n=column number
2. print entire line
     - awk '{print $0}'






