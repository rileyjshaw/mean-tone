mean-tone
=========
In a far-off galaxy, where alien ears can only hear the _average frequency_ of the songs around them, ___what would their music sound like___?!

As Plato and Einstein must have done before my time, I spent many sleepness nights tortured by this question. With this repo, I'm taking it head-on.

I blogged about it [here](http://www.rileyjshaw.com/taking-the-average-tone/).

## Usage
Open __main__.py and change `'wav/flute.wav'` to your input file, `'wav/flute_avg.wav'` to your output file, and `import_bpm` to your song's BPM.

## Troubleshooting
If you're getting weird errors about your input file, run it through Audacity and export it __with no metadata__. It's scipy's fault, not mine.

If you're getting any other errors and you've been at it for a while, it's probably best to just stop. I mean.. why are you even doing this? It's going to sound really terrible.
