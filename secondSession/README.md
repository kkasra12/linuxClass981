# BackTick

```bash
find / -user Christine | xargs -d "\n" rm
rm `find ./ -user Christine`
```
both of them are same.

backTick and `xargs` has two main differences.

But its better to use `xargs`.

Use of the backtick is falling out of favor because backticks are so often
confused with single quotation marks. In several shells, you can use $()
instead. For instance, the backtick example used in the preceding example
would be changed to
```bash
rm $(find ./ -user Christine)
```
This command works just as well, and it is much easier to read and
understand.

# Processing Text Using Filters


#### cat
```
-E, --show-ends          display $ at end of each line
-n, --number             number all output lines
-s, --squeeze-blank      suppress repeated empty output lines
-T, --show-tabs          display TAB characters as ^I
```
#### tac

#### join and paste
```bash
$ cat list0
555-2397 Beckett, Barry
555-5116 Carter, Gertrude
555-7929 Jones, Theresa
555-9871 Orwell, Samuel

$ cat list2
555-2397 unlisted
555-5116 listed
555-7929 listed
555-9871 unlisted

$ join listing1.1.txt listing1.2.txt
555-2397 Beckett, Barry unlisted
555-5116 Carter, Gertrude listed
555-7929 Jones, Theresa listed
555-9871 Orwell, Samuel unlisted

$ paste listing1.1.txt listing1.2.txt
555-2397 Beckett, Barry 555-2397 unlisted
555-5116 Carter, Gertrude 555-5116 listed
555-7929 Jones, Theresa 555-7929 listed
555-9871 Orwell, Samuel 555-9871 unlisted
```
# File-Transforming Commands

#### expand and unexpand

```bash
-t, --tabs=N
       have tabs N characters apart, not 8
```

#### od (Octal Dump)

#### sort
```bash
-f, --ignore-case
      fold lower case to upper case characters
-M, --month-sort
      compare (unknown) < 'JAN' < ... < 'DEC'
-n, --numeric-sort
      compare according to string numerical value
-r, --reverse
      reverse the result of comparisons
-k, --key=KEYDEF
      sort via a key; KEYDEF gives location and type
```

#### split
```bash
SYNOPSIS
      split [OPTION]... [FILE [PREFIX]]
-b, --bytes=SIZE
      put SIZE bytes per output file
-l, --lines=NUMBER
      put NUMBER lines/records per output file
```
#### tr
The `tr` command changes individual characters from standard input. Its syntax is as follows:\
`tr [options] SET1 [SET2]`

```bash
$ cat list0
555-2397 Beckett, Barry
555-5116 Carter, Gertrude
555-7929 Jones, Theresa
555-9871 Orwell, Samuel

$ tr BCJ bc < listing1.1.txt
555-2397 beckett, barry
555-5116 carter, Gertrude
555-7929 cones, Theresa
555-9871 Orwell, Samuel
```

**some usefull Commands**
```bash
-t, --truncate-set1
      first truncate SET1 to length of SET2
-d, --delete
      delete characters in SET1, do not translate
```

**Question:** Convert all numbers into X
**Question:** Lower-case all of the text
**Question:** Upper-case all of the text


# File-Viewing Commands
### head
```bash
-c, --bytes=[-]NUM       print the first NUM bytes of each file;
      with the leading '-', print all but the last
      NUM bytes of each file
-n, --lines=[-]NUM       print the first NUM lines instead of the first 10;
      with the leading '-', print all but the last
      NUM lines of each file
```

#### tail
```bash
-f, --follow[={name|descriptor}]
      output appended data as the file grows;
      an absent option argument means 'descriptor'
-n, --lines=[+]NUM       output the last NUM lines, instead of the last 10;
      or use -n +NUM to output starting with line NUM

```
