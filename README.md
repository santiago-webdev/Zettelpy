# Zettelpy
A personal knowledge management system based on Zettelkasten, the name it's
basically because it's written mostly in Python, but there's some functions
that I find easier to automate with shell scripting

By default it uses markdown and it's not necessary to type the extension, if
you specify the extension another note with that extension will be created

*Some notes:*
- The creation of tags(basically linking notes between each other using ctags) you need to add them manually to the
  second line of each note, I haven't found a way of automating this as of right now.
- I think this cli only works in Linux and Neovim.
- I'm very open to PR or suggestions
- There's a todo list at the end of the file with things that I need to add

## How to install
*Check the dependencies below first*

### Install requirements for the program
```bash
pip install -r requirements.txt
```
This will install all the modules that my program uses.

Now move to the repo, and then follow this steps:

You can either use the repo as the install directory and use git pull to update
```bash
pip install -e .
```

Or install it locally in your machine
```bash
pip install .
pip install --upgrade . # To update the program from the repo
```

You already have everything related to python installed, now you need to run the
program once, this will generate a config file and exit the program so that you
can modify it
```bash
zettelpy # This will quit the program inmediately, read what it says
```

### This creates a config file
So basically you now have a file to configure the program, most of us will have
it in ~/.config/zettelpyrc.ini after this you need to go to the needed
directory inside this projects repo and copy _.ctags.d_ and _.rgignore_ to the
root of your notes directory.
```bash
cd needed
cp -r .ctags.d .rgignore ~/root/of/notes/directory
```

And now everything **should** work.

## Dependencies
- Python 3.4 or later, there's some function that I think are not present on versions below 3.4
- For identifying the Luhmann-ID I'm using ctags, it works well with Neovim
- Ripgrep, to search for the ID from outside
- Some program to view the notes, see the config file, by default I choosed
  okular beacuse it's what I use

# Usage:
### Fleeting notes
The everyday notes you take them with this mode. As you can see, you can't have
a note called Fleeting on the root directory of the notes.
```bash
zettelpy Fleeting
```

Or simply:
```bash
zettelpy
```

### Create notes with Title
You can create or view notes for a book, or about something that you want to
permanently save. Use quotes for names with spaces and add the extension.
```bash
zettelpy Books/"The Aleph.md"
```

### Search notes by the ID
When you are inside the note that you created, you will see on the second line
of the file there's a ## @ place holder, there you can put your ID, it would be
useful to connect each note between each other, and to search for them.
```bash
zettelpy @1b2e
```

This will try to locate a note that on the second line has a ## @1b2e

### Access to the last edited/viewed note
As with the fleeting notes, you can type *lastOpenedNote* and it would open the
last note that you access, as it happens with *Fleeting*, you can't have a note
called *lastOpenedNote* on the root of you directory of notes, because it will
launch the mode, not the note of the same name.
```bash
zettelpy lastOpenedNote
```

## Flags
### View
It doesn't matter the note that you were working on, it will open it with
okular.
```bash
zettelpy -v Books/"The Aleph.md"
```

```bash
zettelpy -v lastOpenedNote
```

```bash
zettelpy @3b7s -v
```
_I haven't put the effort to make it for you to change the default viewer
for now it's okular_

### Indexing
If you want to see the tree of notes pass the -i flag, it will throw you into
you editor(in my case neovim), where you could move to any file and gf to move
to the file

```bash
zettelpy -i
```
Note about this flag: *If you pass this flag it will ignore everything else,
it's just for cleaning the directory of empty files refreshing ctags and
showing you the index*

# The project is a mess
Yes, it's a mess, I don't even know what I'm trying to accomplish in here, this
is going to be another one of those projects. Just don't use it because there's
a lot of things that I'm not providing to make it work correctly and safely.

# Things that I need to add
There's a bunch of them, honestly I only made this program to see if I liked
Python, I will add them while I'm learning about it.

I will list them in here:
- Add a warning and create a note with that tag instead of throwing an
  error when introducing a non existing ID
- Automatic tag generation and insertion
- Define dependencies for python
