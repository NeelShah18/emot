import re
from emot import emo_unicode
#import emo_unicode

'''emot library to detect emoji and emoticons.

    >>> import emot
    >>> text = "I love python 👨 :-)"
    >>> emot.emoji(text)
    >>> [{'value': '👨', 'location': [10, 10]}]
    >>> emot.emoticons(text)
    >>> [{'value': ':-)', 'location': [12, 15]}]
'''

__all__ = ['emoji','emoticons']

def emoji(string):
    '''emot.emoji is use to detect emoji from text

        >>> text = "I love python 👨 :-)"
        >>> emot.emoji(text)
        >>> [{'value': '👨', 'location': [10, 10]}]
    '''
    __entities = []
    pro_string = str(string)
    for pos,ej in enumerate(pro_string):
        if ej in emo_unicode.UNICODE_EMO:
            __entities.append({
                "value": ej,
                "location": [pos,pos]
                })
    return __entities

def emoticons(string):
    '''emot.emoticons is use to detect emoticons from text

        >>> text = "I love python 👨 :-)"
        >>> emot.emoticons(text)
        >>> [{'value': ':-)', 'location': [12, 15]}]
    '''
    __entities = []
    pattern = u'(' + u'|'.join(k for k in emo_unicode.EMOTICONS) + u')'
    __entities = []
    matches = re.finditer(r"%s"%pattern,str(string),re.IGNORECASE)
    for et in matches:
        __entities.append({'value': et.group().strip(),
        'location': [et.start(),et.end()]
        })
    return __entities

def test_emo():
    test = "I love python 👨 :-)"
    print(emoji(test))
    print(emoticons(test))
    return None

def about():
    text = "emot library: emoji and emoticons library for python. It return emoji or emoticons from string with location of it. \nAuthors: \n Neel Shah: neelknightme@gmail.com or https://github.com/NeelShah18 \n Subham Rohilla: kaka.shubham@gmail.com or https://github.com/kakashubham"
    print(text)
    return None
