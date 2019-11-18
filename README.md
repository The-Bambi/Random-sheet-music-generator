# Random-sheet-music-generator

This project is aimed to generate a random sheet music for string quartet in 5 files (all parts connected and 4 separate files, for each instrument), using lilypond & python. 

The goal is to be able to generate large amounts of random sheet music files and convert them to graphical format.

Eventually this is going to serve as a learning dataset for a neural network, which is supposed to split a sheet music for string quartet into 4 separate parts (vl1-vl2-vla-vlc).

There is a substantial amount of such sets (combined parts + vl1 part + vl2 part + vla part + vlc part) available on the internet, but are very scattered on different sites & servers, have various looks and formats and usually hidden behind a paywall anyway.

Neural network won't care if the music makes sense, so it's logical to build a random generator instead of spending days and days on downloading separate files.

The use of perlin noise should give each line an illusion of structure and idea.
