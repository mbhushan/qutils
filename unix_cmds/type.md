##### Which Version Am I Using?
Your system may have several versions of a particular command -- for instance, a BSD-compatible version in one directory and a System V-compatible version somewhere else (and you might have added a private version in your own bin directory). 

Which command you'll get depends on your PATH environment variable. It's often essential to know which version you're using. For example:

``` sh
$ type -all man
man is /usr/bin/man


$ type -all find
find is /usr/bin/find

$ type -all grep
grep is aliased to `grep --color=auto'
grep is /bin/grep

```
