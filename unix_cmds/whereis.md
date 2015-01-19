##### whereis: Finding Where a Command Is Located
The whereis command helps you to locate the executable file, source code, and manual pages for a program. 
Examples are:

``` sh
$ whereis grep
grep: /bin/grep /usr/share/man/man1/grep.1.gz

$ whereis find
find: /usr/bin/find /usr/bin/X11/find /usr/share/man/man1/find.1.gz

```
######Various options are:
```sh
-b
Only report the executable name
-m
Only report the location of the manual page
-s
Only search for source files
-u
Only issue a report if any of the requested information (executable, manual page, source) is missing
```
