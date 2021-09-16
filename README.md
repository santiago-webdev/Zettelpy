# Zettelpy
A personal knowledge management system based on Zettelkasten.

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

# Dependencies
- Having an $EDITOR setted up. I'm using neovim in here
- ctags, because the Luhmann-ID is being identified by ctags
- ripgrep, to search for the ID
- okular

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
- Indexing of the notes
- Change Title on the permanent notes to the actual name of the note introduced
