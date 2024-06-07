# Random-sheet-music-generator

The goal of the project is to be able to generate mass amounts of random sheet music along with lilypond syntax, and use it as an input to a neural network.
The project is at a stage where I can start experimenting with some NNs, 

and try to speed-up the process of digitalization of sheet music and make it widely available, at least

to people who are still able to use lilypond and TeX to write sheet music.

Currently using ChatGPT for the basic NN setup. Unfortunately the architecture it is providing is not able to take care of the problem.

The obstacle may be in the dictionary it is grabbing from the text - like 
```{1: ' ',
 2: ',',
 3: '|',
 4: 'a',
 5: 'g',
 6: 'c',
 7: 'b',
 8: 'd',
 9: 'e',
 10: 'f',
 11: "'"}```
 is way too simple. I may need to work on the initial dictionary so that it is easier for the net to distinguish between "words".
 
 As of now I will keep the 2 projects together, as The Generator improves I might split it in the future.