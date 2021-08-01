[![Downloads](http://pepy.tech/badge/emot)](http://pepy.tech/project/emot) 

[![Documentation Status](http://readthedocs.org/projects/emot/badge/?version=latest)](https://emot.readthedocs.io/en/latest/?badge=latest)

Description of the emot:3.0 library
===============================

Emot is a python library to extract the emojis and emoticons from a
text(string). All the emojis and emoticons are taken from a reliable
source details are listed in source section.

Emot 3.0 release moto is: high-performance detection library for data-science specially for large scale datasets of text.

Emot use advance dynamic pattern generation. It means everytime when you create object it generate pattern
based on the database(emo_unicode.py). You can add/delete/modify that file under library to create other dynamic pattern.

3.0 version provide more option such as bulk processing. It is useful when you have long list of "sentence or word" 
and want to use multiprocessing power to speedup the process.

It means you can dynamically create pattern for the emoji or emoticons and run it in multiprocessing to get maximum 
performance from multiple cores.

Again, I am thankful for all support and help from the community around the world. I hope this will help and make your 
life easier.

Compatibility
-------------

version 3.0 only support python 3.X.

Python 2.X is no longer supported.

Working
-------

The Emot library takes a string/list of string as an input and returns a dictonary.

Example
-------

    >>> import emot 
    >>> emot_obj = emot.emot() 
    >>> text = "I love python ☮ 🙂 ❤ :-) :-( :-)))" 
    >>> emot_obj.emoji(test) 
    >>> {'value': ['☮', '🙂', '❤'], 'location': [[14, 15], [16, 17], [18, 19]], 'mean': [':peace_symbol:', 
    ':slightly_smiling_face:', ':red_heart:'], 'flag': True} 
    >>> emot_obj.emoticons(test) >>> {'value': [':-)', ':-(', ':-)))'], 'location': [[20, 23], [24, 27], [28, 33]], 
    'mean': ['Happy face smiley', 'Frown, sad, andry or pouting', 'Very very Happy face or smiley'], 'flag': True} 

    
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

Sources
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
