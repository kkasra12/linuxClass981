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

$ tr BCJ bc < list0
555-2397 beckett, barry
555-5116 carter, Gertrude
555-7929 cones, Theresa
555-9871 Orwell, Samuel
```

**some useful arguments**
```bash
-t, --truncate-set1
      first truncate SET1 to length of SET2
-d, --delete
      delete characters in SET1, do not translate
-c, -C, --complement
      use the complement of SET1
```

**Question:** Convert all numbers into X\
**Question:** Lower-case all of the text\
**Question:** Upper-case all of the text\
**Question:** Delete everything except numbers


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
**Question:** use `head` and `tail` to show the first 10 lines and last 15 lines(use one of the files in `bigFiles` folder)\
**Question:** use `head` and `tail` to display lines between 20 till 60

# File-Summarizing Commands
#### cut
```bash
$ echo "some text for test"|cut -d " " -f 1
$ echo "some text for test"|cut -d " " -f 2
$ echo "some text for test"|cut -d " " -f 5
$ echo "some text for test"|cut -d " " -f 1-5
$ echo "some text for test"|cut -d " " -f -5
$ echo "some text for test"|cut -d " " -f 5-
$ echo "some text for test"|cut -c 2
$ echo "some text for test"|cut -c 3
$ echo "some text for test"|cut -c 6
$ echo "some text for test"|cut -c 2-10
```

#### wc
```
-c, --bytes            print the byte counts
-m, --chars            print the character counts
-l, --lines            print the newline counts
-L, --max-line-length  print the maximum display width
-w, --words            print the word counts
```

# Using Regular Expressions

**First of all learn regex...**

here are some usefull links:
- [regexr.com](https://regexr.com)
- [regex101.com](https://regex101.com)
- [regex cheatsheet for js](https://dev.to/catherinecodes/a-regex-cheatsheet-for-all-those-regex-haters-and-lovers--2cj1)
- [regex quick start](www.rexegg.com/regex-quickstart.html)

#### grep

```bash
$ grep [options] regexp [files]
```

**some useful arguments:**
```bash
-c, --count               print only a count of selected lines per FILE
-i, --ignore-case         ignore case distinctions
-r, --recursive           like --directories=recurse
-F, --fixed-strings       PATTERN is a set of newline-separated strings
```
<br>\
**Describe these commands:**
```bash
$ grep -r eth0 /etc/*
$ grep eth[01] /etc/*
ps aux|grep -E python
ps aux|grep -E "python|COMMAND"
```
