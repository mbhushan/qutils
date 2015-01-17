#####  Internal and External Commands

> **Internal Commands**: means they are built into the shell, and it's the shell that performs the action. For example, the cd command is built-in. The shell doesn't start a separate process to run internal commands. 

> **External Commands**: require the shell to fork and exec anew subprocess. This takes some time, especially on a busy system. The **ls** command, is an external program stored in the file /bin/ls.



