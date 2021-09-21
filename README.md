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

You can delete the repo because the program gets installed locally on
.local/lib/python3.9/site-packages/
```bash
pip install .
```

To update it.
```bash
pip install --upgrade .
```

Use the repo as the install directory, just git pull each time you want to update.
```bash
pip install -e .
```

Install python requirements, and then check the dependencies
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
- Okular (I would find a way to change this in the mean time just don't use
  "-v")
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

### Notes with Title
You can create or view notes for a book, or about something that you want to
permanently save. Use quotes for names with spaces and add the extension.
```bash
zettelpy Books/"The Aleph.md"
```

### Notes by Luhmann-ID
On the notes that gets created automatically you would see that on the second
line there's an "## @", you can add your Luhmann-ID, i.e. ## @1b2e, so that
then when you search for it, it would be picked up by the program:
```bash
zettelpy @1b2e
```

### Access to the last edited/viewed note
As with the fleeting notes, you can type *lastOpenedNote* and it would open the
last note that you access, and you can't have a note on the root of your notes
that is called *lastOpenedNote* just like with *Fleeting*.

## Flags
As of right now I only have one flag on the program, the -v flag.
It doesn't matter the note that you were working on, it will open it with
okular, but you can easily change that if you open the code because okular
appears only once.
```bash
zettelpy Books/"The Aleph.md"
```

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
- The ctags configs in the installer
- Install dependencies based on the distro

## Notes
- Change Title on the permanent notes to the actual name of the note introduced
This is a problem that I don't really know how to "fix", now when you create a
new note the file name will get inserted, with extension included, I know I can
use [:2] to ignore the .md extension, but what about other names an extensions?
I don't think I understand enough of this to deal with it so I'll leave it like
that, beacause at least now it doesn't just say '# Title'.
