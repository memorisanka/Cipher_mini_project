## Cipher Mini Project

### Content of Project
* [General info](#general-info)
* [Modules](#modules)
* [Technologies](#technologies)



## General info
<details>
<summary>Click here to see general information about <b>Project Cipher</b>!</summary>
<b>Project Cipher</b> is a project. It allows to 
encrypt the given strings with the ROT cipher. ROT 3, 
ROT 13, ROT 47 or ROT(1-25, the user specifies a shift) can be used. 
.
<br><br>
<b>Rot-N/Rot cipher (for Rotation)</b> is a simple character substitution based on a shift/rotation 
of N letters in an alphabet. E.g. one letter is replaced by another (always the same) that 
is located further (exactly N letters further) in the alphabet.<br><br>
<b>The Rot-47</b> is a shift cipher that improves the Rot-13 by allowing it to encode almost all visible ASCII characters 
(where Rot13 could only encode letters).
To achieve this, Rot47 uses a 94-character alphabet that is a subset of the ASCII table characters between the 
character 33 ! and the character 126 ~.
</details>

## Modules
<details><summary>Click here to see informations about <b>modules</b>!</summary>
The program consists of a login module and a manager. <br><br>
<b>The login module</b> uses the SQL lite database. The module checks if the data provided during logging in are identical 
to those in the database. There is also an option to create a new user. The module checks if the given username 
is available. The password stored in the database is encrypted.
<br><br>
<b>The manager</b> is responsible for the operation of the Cipher. It displays the menu, allows you to write encrypted 
words to json, decrypt a given word according to the index provided by the user.
</details>

## Technologies
<ul>
<li>Python</li>
<li>Pytest</li>
<li>SQL Lite</li>
</ul>

#### Sources
