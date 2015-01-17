#####  The man Command
The basis for Unix's online documentation is the man command. Most simply, you use it as follows:
``` sh
$ man topic
```
For example, if you want to read documentation about the passwd command
``` sh
$ man s -5 passwd
```
configuration file for man is **/etc/manpath.config ** on ubuntu system.
Reading it will show you the directories in which manpages are stored, the order in which manpages are searched by default.

**man** command understands the **MANPATH**  environment variable, a list of where man should search.



