# PasswordChecker
Check if your passwords have ever been hacked.

Check if your passwords have ever been a part of a security breach.</br>
All the passwords that have been leaked by major companies when their databases get hacked are stored in a database. Check wheather yours is a part of it.</br>

This script uses PawndPasswords API to find the number of times your password has been hacked.(https://haveibeenpwned.com/Passwords)</br>
Pwned Passwords are 613,584,246 real world passwords previously exposed in data breaches. This exposure makes them unsuitable for ongoing use as they're at much greater risk of being used to take over other accounts. They're searchable online below as well as being downloadable for use in other online systems.</br>

How to use:</br>
<ol>
<li>Install necessary Packages.</br></li>
<li>Run the script as your password/s as arguments.<br></li>
eg:

	python PasswordChecker.py hello123
or<br>

	python PasswordChecker.py hello123 example2 example3
</ol>


# PasswordCheckerV2
<br>
How to use:</br>
<ol>
<li>If you have a txt file with list of passwords.<br></li>
<li>Run the script as your txt file as arguments.<br></li>
eg:
		
	python PasswordChecker.py pass.txt
</ol>