# Shell variables

> Variables will be described in more details later

**How to define a variable?**
```bash
export name="kasra"
```
*or...*
```bash
name='kasra'
```
*or...*
```bash
name='kasra'
```


> Note: do not use extra spaces in your command. Despite of other programming languages bash commands will not ignore spaces.

**How to check variables value?**
```bash
echo $name
echo "my name is $name"
```

#### Special variables in system:

- PATH

- PWD

- HOME

- USER

- PS1

> **\u**: current username .<br>
 **\u**: Display the current username .<br>
 **\h**: Display the hostname. <br>
 **\W**: Print the base of current working directory.<br>
 **\\@**: Display current time in 12-hour am/pm format

#### env
shows all of the defined variables in current bash

#### unset
deletes a variable

# man

bash defines the some built-in commands. To see a short describe about them use the following command

```bash
$ man builtins
```

The man utility uses the less pager by default to display information. This program displays text a page at a time. Press the **spacebar** to move forward a page, **Esc** followed by **V** to move back a page, the **arrow keys** to move up or down a line at a time, the **slash (/) key** to search for text, and so on. (Type `man less` to learn all the details)

#### How to find a command from its details

```bash
$ man -k "system information"
dumpe2fs (8)         - dump ext2/ext3/ext4 filesystem information
inxi (1)             - Command line system information script for console and IRC
Lintian::Path::FSInfo (3) - File System information for Lintian::Path
sysinfo (2)          - return system information
uname (1)            - print system information
```
```bash
$man -k "package manager"
aptitude (8)         - high-level interface to the package manager
aptitude-curses (8)  - high-level interface to the package manager
dpkg (1)             - package manager for Debian
gem (1)              - frontend to RubyGems, the Ruby package manager
gem2.5 (1)           - frontend to RubyGems, the Ruby package manager
npm (1)              - javascript package manager
npm-README (1)       - a JavaScript package manager
```

```bash
man -k package
```

> NOTE: i didn't used any " in previous command, But i have used in the other commands. describe why " was important in last two commands?

#### Using `man` for other sections

There is a `passwd` command, which can change the system password for current user.
Also there is a password file in `/etc/passwd` which stores all system passwords for all users.
To this file content use `cat` command:
```bash
$ cat /etc/passwd
```

**How to ask more information about `/etc/passwd` file from man ?**

Linux man pages are organized into several sections, which are summarized in following table.

| Section Number | Description     |
| :------------- | :------------- |
| 1 | Executable programs and shell commands |
| 2 | System calls provided by the kernel |
| 3 | Library calls provided by program libraries |
| 4 | Device files (usually stored in /dev) |
| 5 | File formats |
| 6 | Games |
| 7 | Miscellaneous (macro packages, conventions, and so on) |
| 8 | System administration commands (programs run mostly or exclusively by root |
| 9 | Kernel routines |

According to this table, to find *man page* for `/etc/passwd` file this command seems to be usefull:
```bash
$ man 5 passwd
```
****
# Using Streams, Redirection, and Pipes

**Whats are default input and output devices?**

**Whats are usage of changing input and output devices?**

> LPIC official book says: "Part of the Unix philosophy to which Linux adheres is, whenever possible, to do complex things by combining multiple simple tools. Redirection and pipes help in this task by enabling simple programs to be combined together in chains, each link feeding off the output of the preceding link"

> NOTE: Linux handles all objects as files.

**File descriptors for STDIN, STDOUT and STDERR**

- Standard Input: 0
- Standard Output: 1
- Standard Error: 2

```bash
$ echo $PATH 1>path.txt
$ cat path.txt
```

*There is no need to mention the file descriptot or STDIN:*

```bash
$ echo $PATH > path.txt
$ cat path.txt
```

| operator     | description     |
| :-: | :- |
|>| Creates a new file containing standard output. If the specified file exists, it’s overwritten. No file descriptor necessary. |
| >>  | Appends standard output to the existing file. If the specified file doesn’t exist, it’s created. No file descriptor necessary. |
| 2>  | Creates a new file containing standard error. If the specified file exists, it’s overwritten. File descriptor necessary. |
| 2>> | Appends standard error to the existing file. If the specified file doesn’t exist, it’s created. File descriptor necessary. |
| &>  | Creates a new file containing both standard output and standard error. If the specified file exists, it’s overwritten. No file descriptors necessary. |
| <   | Sends the contents of the specified file to be used as standard input. No file descriptor necessary. |
| <<  | Accepts text on the following lines as standard input. No file descriptor necessary. |
| <>  | Causes the specified file to be used for both standard input and standard output. No file descriptor necessary. |


> A common trick is to redirect standard output or standard error to `/dev/null`. This file is a device that’s connected to nothing; it’s used when you want to get rid of data. For instance, if the whine program is generating too
many unimportant error messages, you can type
`whine 2> /dev/null` to run it and discard its error messages


# Piping Data between Programs

Simple piping:
```Shell
$ first | second
$ first | second | third | fourth | fifth [...]
```

For instance:
```Shell
$ echo $PATH | tee path.txt
$ hwinfo | grep -i graphics
```

# Generating Command Lines (xarges)
<br>

**Question:** <br>Consider about how inputs are passed to a command, what is the main difference between `rm` or `mkdir` and `grep` ?

*xargs [options] [command [initial-arguments]]*
