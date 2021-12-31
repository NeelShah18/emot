[![Downloads](http://pepy.tech/badge/emot)](http://pepy.tech/project/emot) [![GitHub issues](https://img.shields.io/github/issues/NeelShah18/emot)](https://github.com/NeelShah18/emot/issues) [![GitHub forks](https://img.shields.io/github/forks/NeelShah18/emot)](https://github.com/NeelShah18/emot/network) [![GitHub stars](https://img.shields.io/github/stars/NeelShah18/emot)](https://github.com/NeelShah18/emot/stargazers) [![GitHub license](https://img.shields.io/github/license/NeelShah18/emot)](https://github.com/NeelShah18/emot/blob/master/LICENSE)

Description of the emot:3.1 library
===============================

Emot is a python library to extract the emojis and emoticons from a
text(string). All the emojis and emoticons are taken from a reliable
source details are listed in source section.

Emot 3.1 release moto is: high-performance detection library for data-science specially for large scale datasets of text.

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

There are one class name emot containing four different function.

emot.emoji:

- Input: It has one input: string
- Output: It will return dictionary with 4 different value: dict
  - value = list of emojis
  - location = list of location list of emojis
  - mean = list of meaning
  - flag = True/False. False means library didn't find anything and True means we find something.

emot.emoticons

- Input: It has one input: string
- Output: It will return dictionary with 4 different value: dict
  - value = list of emoticons
  - location = list of location list of emoticons
  - mean = list of meaning
  - flag = True/False. False means library didn't find anything and True means we find something.

emot.bulk_emoji

- Input: Two input: List of string and CPU cores pool: list[], int
  - By default CPU cores pool value is half of total available cores: multiprocessing.cpu_count()/2 
- Output: It will return **list of dictionary** with 4 different value: list of dict
  - value = list of emojis
  - location = list of location list of emojis
  - mean = list of meaning
  - flag = True/False. False means library didn't find anything and True means we find something.

emot.bulk_emoticons

- Input: Two input: List of string and CPU cores pool: list[], int
  - By default CPU cores pool value is half of total available cores: multiprocessing.cpu_count()/2 
- Output: It will return **list of dictionary** with 4 different value: list of dict
  - value = list of emoticons
  - location = list of location list of emoticons
  - mean = list of meaning
  - flag = True/False. False means library didn't find anything and True means we find something.


Example
-------

    >>> import emot 
    >>> emot_obj = emot.core.emot() 
    >>> text = "I love python ☮ 🙂 ❤ :-) :-( :-)))" 
    >>> emot_obj.emoji(text) 
    >>> {'value': ['☮', '🙂', '❤'], 'location': [[14, 15], [16, 17], [18, 19]], 'mean': [':peace_symbol:', 
    ':slightly_smiling_face:', ':red_heart:'], 'flag': True} 
    >>> emot_obj.emoticons(test) >>> {'value': [':-)', ':-(', ':-)))'], 'location': [[20, 23], [24, 27], [28, 33]], 
    'mean': ['Happy face smiley', 'Frown, sad, andry or pouting', 'Very very Happy face or smiley'], 'flag': True} 

    Running bulk string emoji and emoticons detection. When user has access multiple processing cores.
    
    >>> import emot 
    >>> emot_obj = emot.core.emot() 
    >>> bulk_test = ["I love python ☮ 🙂 ❤ :-) :-( :-)))", "I love python 
    🙂 ❤ :-) :-( :-)))", "I love python ☮ ❤ :-) :-( :-)))", "I love python ☮ 🙂 :-( :-)))"] 
    >>>
    >>> emot_obj.bulk_emoji(bulk_test) 
    >>> [{'value': ['☮', '🙂', '❤'], 'location': [[14, 15], [16, 17], [18, 19]], 
        'mean': [':peace_symbol:', ':slightly_smiling_face:', ':red_heart:'], 'flag': True}, {'value': ['🙂', '❤'], 
        'location': [[14, 15], [16, 17]], 'mean': [':slightly_smiling_face:', ':red_heart:'], 'flag': True}, {'value': [
        '☮', '❤'], 'location': [[14, 15], [16, 17]], 'mean': [':peace_symbol:', ':red_heart:'], 'flag': True}, 
        {'value': ['☮', '🙂'], 'location': [[14, 15], [16, 17]], 'mean': [':peace_symbol:', ':slightly_smiling_face:'], 
        'flag': True}] 
    >>>
    >>> emot_obj.bulk_emoticons(bulk_test)
    >>> [{'value': [':-)', ':-(', ':-)))'], 'location': [[20, 23], [24, 27], [28, 33]], 'mean': ['Happy face smiley', 
        'Frown, sad, andry or pouting', 'Very very Happy face or smiley'], 'flag': True}, {'value': [':-)', ':-(', ':-)))'], 
        'location': [[18, 21], [22, 25], [26, 31]], 'mean': ['Happy face smiley', 'Frown, sad, andry or pouting', 'Very 
        very Happy face or smiley'], 'flag': True}, {'value': [':-)', ':-(', ':-)))'], 'location': [[18, 21], [22, 25], 
        [26, 31]], 'mean': ['Happy face smiley', 'Frown, sad, andry or pouting', 'Very very Happy face or smiley'], 
        'flag': True}, {'value': [':-(', ':-)))'], 'location': [[18, 21], [22, 27]], 'mean': ['Frown, sad, andry or 
        pouting', 'Very very Happy face or smiley'], 'flag': True}]

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
