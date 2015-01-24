### Making Directories Made Easier
It's easy. Use the mkdir command, followed by the name of your new directory:
```sh
$ mkdir <directory_name>
```
If the parent directory does not exist then you can add -p (parent) option to create directories
```sh
$ mkdir -p library/books/danbrown/deception
```
On some mkdirs, you can also supply the file protection mode to be assigned to the directory. To do so, use the -m option. For example:

```sh
$  mkdir -m 755 -p library/books/danbrown/deception
 ```