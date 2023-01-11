# Random-sheet-music-generator

This project is aimed to generate a random sheet music for string quartet in 5 files (all parts connected and 4 separate files, for each instrument), using lilypond & python. 

The goal is to be able to generate large amounts of random sheet music files and convert them to graphical format.

Eventually this is going to serve as a learning dataset for a neural network, which is supposed to split a sheet music for string quartet into 4 separate parts (vl1-vl2-vla-vlc).

There is a substantial amount of such sets (combined parts + vl1 part + vl2 part + vla part + vlc part) available on the internet, but are very scattered on different sites & servers, have various looks and formats and usually hidden behind a paywall anyway.

Neural network won't care if the music makes sense, so it's logical to build a random generator instead of spending days and days on downloading separate files.

The use of perlin noise should give each line an illusion of structure and idea.

# I'm back!

After like a year I came back. I fixed the random music generator, so that it stays within certain range. Now I am able to generate infinite staffs of random quarter-notes.

I will now be trying to make a recognition algorithm so that it transforms staff into usable, editable lilypond text.

I am unsure how to deal with variating lengths. Some staffs can contain 16 notes, some 10, some 47.

I can either go note-by-note, build a net to separate a staff into individual notes, and then a net to recognize eis,,16 from d'2

Or I can try for now to build a net to grab the whole staff at once and output the whole thing as a single list of notes.

Won't bother with the lengths for now.

I will have to split the PDF I am generating into separate images of staffs, but that's some scripting with PIL. 
