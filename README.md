# Password Strength Tester (Brute-force/Dictionnary attacks simulation)

## Description:
The goal of this project was to make a tool to test the strength of a password hash against password cracking attacks such as Brute-force, Dictionnary or Rainbow table attack. Warning: The longer your password will be, the longer it will take time to crack it (only in simple and fast mode).

## Prerequisites

<ul>
<li>Windows 7/8/10 or Linux</li>
<li>python 3 (https://www.python.org/)</li>
<li>numpy (https://pypi.org/project/numpy/)</li>
<li>hashlib (https://pypi.org/project/hashlib/)</li>
</ul>

## Before you start
You can use this command to know how much time it would take for your computer to crack a given password:
```bash
$ python Password_Strength_Tester.py check password
```

## Run

To run this project enter this command:
```bash
$ python Password_Strength_Tester.py Mode Parameter1 Parameter2
```
### Modes:

<ul>
<li>simple : In this mode the project will simulate an incremental Brute-Force attack on the password hash.</li>
<li>fast : In this mode the project will simulate a Brute-Force attack with different arrays of characters (Upper letters, Lower letters, Numbers and Special characters). This type of attack is very effective against password which have 1 or 2 type of character(Upper letters, Lower letters, Numbers and Special characters).</li>
<li>word : In this mode the project will simulate Dictionnary attack on the password hash by using the passwords in the /passwords folder.</li>
</ul>

### Parameters:
<ul>
<li>Parameter1 : The plain password you want to test against attacks (type: STRING)</li>
<li>Parameter2 : The time limit you want to put on each attacks (type: INT > 0)</li>
</ul>

## Optional
If you want the word mode to be more effective, you can add txt files containing password to try in the /passwords folder. They must have the following format:
```txt
password1
password2
password3
password4
    .
    .
    .
```
Even if 2 or more files contain the same password, or if there are copy of the same password in a file it will be added only once to array containg the passwords to be used. 