##### Which Shell Am I Running?
You can usually tell which family your shell belongs to by a character in the prompt it displays. 
* Bourne-type shells, such as bash , usually have $ in the prompt. 
* The C shell uses % 
* tcsh users often use >

``` sh
$ grep "mani" /etc/passwd
mani:x:1000:1000:Mani,,,:/home/mani:/bin/bash
```
You should get back the contents of your entry in the system password file as I got mine above. 
The fields are separated by colons, and the default shell is usually specified in the last field. As you can see my shell is **bash**