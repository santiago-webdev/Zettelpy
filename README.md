# Zettelpy
A personal knowledge management system based on Zettelkasten, the name it's
basically because it's written mostly in Python, but there's some functions
that I find easier to automate with shell scripting

# The project is a mess
Yes, it's a mess, I don't even know what I'm trying to accomplish in here, this
is going to be another one of those projects. Just don't use it because there's
a lot of things that I'm not providing to make it work correctly and safely.

# Where are the notes getting stored?
By default everything will go into .local/share/zettelpy

## How to install

*Check the dependencies below first, they will eventually change, I just need
to think how to. Maybe I'll add a config file, but not for now.*

You can either delete the repo because the program gets installed locally on
.local/lib/python3.9/site-packages/ with this command:
```bash
pip install .
```

And to update it.
```bash
pip install --upgrade .
```

Or use the repo as the install directory, just git pull each time you want to update.
```bash
pip install -e .
```

Then install python requirements, and then check the dependencies
```bash
pip install -r requirements.txt
```

Now that you have everything related to python installed, you need to run
zettelpy once:
```bash
zettelpy # And quit inmediately
```

The program will create the basic structure and folders, but you need to
enable/install the other features, so that the program behaves properly, that's
why I said quit immediately, so after this you need to install everything
else, it's just files for ctags to detect tags properly, another shell script
that I use on the program to clean empty files and a file that ripgrep uses
to ignore directories so that they don't appear when searching by ID.

```bash
./install.sh
```

And now it should supposedly work fine.

## Dependencies
- Python 3, there's some function that I think are not present on Python 2.
- Having an $EDITOR setted up. I'm using Neovim in here
- For identifying the Luhmann-ID I'm using ctags, it works well with Neovim.
- Ripgrep, to search for the ID from outside
- Okular (I would find a way to change this in the meantime just don't use
  "-v" if you don't like it)
- For creating the index.md I'm using a command called exa, it probably is in
  your distro's repo

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
useful to connect each note between each other, and to search for them
```bash
zettelpy @1b2e # It will try to locate a note that on the second line has a ## @1b2e
```

### Access to the last edited/viewed note
As with the fleeting notes, you can type *lastOpenedNote* and it would open the
last note that you access, as it happens with *Fleeting*, you can't have a note
called *lastOpenedNote* on the root of you directory of notes, because it will
launch the mode, not the note of the same name.
```bash
zettelpy lastOpenedNote
```

## Flags
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

# Things that I need to add
There's a bunch of them, honestly I only made this program to see if I liked
Python, I will add them while I'm learning about it.

I will list them in here:
- Add a warning and create a note with that tag instead of throwing an
  error when introducing a non existing ID(tags)
- Show a list of notes by ID and title
- Create tab completion for notes already created
- Create a krunner plugin
- Make okular be easily changeable
- How to execute zettelpy from krunner without a plugin
- Install dependencies based on the distro
- Define dependencies for python

## Notes
- Change Title on the permanent notes to the actual name of the note introduced
This is a problem that I don't really know how to "fix", now when you create a
new note the file name will get inserted, with extension included, I know I can
use [:2] to ignore the .md extension, but what about other names an extensions?
I don't think I understand enough of this to deal with it so I'll leave it like
that, beacause at least now it doesn't just say '# Title'.
