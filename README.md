[![Downloads](http://pepy.tech/badge/emot)](http://pepy.tech/project/emot)

Description of the emot library
===============================

Emot is a python library to extract the emojis and emoticons from a
text(string). All the emojis and emoticons are taken from a reliable
source i.e. Wikipedia.org.

Compatibility
-------------

It works fine in any Python 2.xx and 3.xx.

Working
-------

The Emot library takes a string as an input and returns a list of
dictonary.

Example
-------

    >>> import emot
    >>> text = "I love python 👨 :-)"
    >>> emot.emoji(text)
    >>> [{'value': '👨', 'mean': ':man:', 'location': [14, 14], 'flag': True}]
    >>> emot.emoticons(text)
    >>> {'value': [':-)'], 'location': [[16, 19]], 'mean': ['Happy face smiley'], 'flag': True}

New version 2.0 of emot library return dictonary of and you can loop every data based on below example.
Here, value, location, mean are list and flag is boolean. 

    >>> text = "I love python 👨 :-)"
    >>> ans = emot.emoticons(text)
    >>> ans
    {'value': [':-)'], 'location': [[16, 19]], 'mean': ['Happy face smiley'], 'flag': True}
    >>> ans['value']
    ':-)'
    >>> ans['location']
    [16, 19]
    >>> ans['mean']
    ['Happy face smiley']
    >>> ans['flag']
    True
    
Installation
------------

Via pip:

    $ pip install emot --upgrade

From master branch:

    $ git clone https://github.com/NeelShah18/emot.git
    $ cd emot
    $ python setup.py install

Developing
----------

    $ git clone https://github.com/NeelShah18/emot.git
    $ cd emot

Links
-----

[Emoji Cheat Sheet]

[Official unicode list]

[official emoticons list]

Authors
-------

Neel Shah / [@NeelShah18]

Shubham Rohilla / [@kakashubham]

  [Emoji Cheat Sheet]: http://www.emoji-cheat-sheet.com/
  [Official unicode list]: http://www.unicode.org/Public/emoji/1.0/full-emoji-list.html
  [official emoticons list]: https://en.wikipedia.org/wiki/List_of_emoticons
  [@NeelShah18]: https://github.com/NeelShah18
  [@kakashubham]: https://github.com/kakashubham
