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
    >>> [{'value': '👨', 'location': [10, 10]}]
    >>> emot.emoticons(text)
    >>> [{'value': ':-)', 'location': [12, 15]}]

You can loop them as shown below. There are two details in each
dictonary (1) Value - Emoji or Emoticons and (2) Location - starting
position and the ending position of the emoji and emoticons. Below is
the example showing how you can loop it.

    >>> text = "I love python 👨 :-) :) "
    >>> emot.emoticons(text)
    [{'value': ':-)', 'location': [16, 19]}, {'value': ':)', 'location': [20, 22]}]
    >>> for data in emot.emoticons(text):
    ...     print('value ',data['value'])
    ...     print('starting point: ',data['location'][0])
    ...     print('ending point: ',data['location'][1])
    ...
    value :-)
    starting point:  16
    ending point:  19
    value :)
    starting point:  20
    ending point:  22

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
