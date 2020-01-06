# Password Strength Tester (Brute-force/Dictionary attacks)

## Description:
The goal of this project was to make a tool to test the strength of a password hash against password cracking attacks such as Brute-force, Dictionary attacks. Warning: The longer your password will be, the longer it will take time to crack it (only in Brute-force mode).

## Prerequisites

<ul>
<li>Windows 7/8/10</li>
</ul>

## Run
Execute the file **Password_Strength_Tester.exe**.

## Prerequisites (with python)
<ul>
<li>Windows 7/8/10 or MacOs or Linux</li>
<li>python 3.5-3.7</li>
</ul>

## Installation
Enter the following command:
```bash
pip install requirements.txt
``` 

## Run
Enter the following command:
```bash
python Password_Strength_Tester.py
``` 

## Manual

### Step 1: Inputs
First enter your password into the password input field, then enter the limit of time you want to impose to crack the password. Finally choose the type of attack you want to test (Modes: Brute-force, Dictionary).

### Step 2: Computation speed
Click on the button **Get Computation speed** to know how much time it would take to crack your password in the different modes.

### Step 3: Test against cracking attacks
When you are done please click on the button **Crack** to start the attack.

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
