To install:

    pip3 install python-Levenshtein
    python3 setup.py build
    sudo python3 setup.py install

To run:

    megahal -h

As a lib:

    from megahal import *
    megahal = MegaHAL()
    megahal.train('/path/to/some/file')
    megahal.learn('some phrase')
    print megahal.get_reply('hey, wazzap')
    megahal.sync()  # flush any changes to disc
    megahal.close()  # flush changes and close


example of usage:

$ python3 pymegahal.py -b brain3.brn
Transcription has began

> wow, I'm impressed

That is a relief.

> taking the exit

Why are you soooo slooooooooooow

> Closing transcript

Closing database

