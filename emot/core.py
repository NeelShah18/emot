import re
from emot import emo_unicode
#import emo_unicode

'''emot library to detect emoji and emoticons.

    >>> import emot
    >>> text = "I love python 👨 :-)"
    >>> emot.emoji(text)
    >>> {'value': ['👨'], 'mean': [':man:'], 'location': [[14, 14]], 'flag': True}
    >>> emot.emoticons(text)
    >>> {'value': [':-)'], 'location': [[16, 19]], 'mean': ['Happy face smiley'], 'flag': True}
'''

__all__ = ['emoji','emoticons']

def emoji(string):
    '''emot.emoji is use to detect emoji from text

        >>> text = "I love python 👨 :-)"
        >>> emot.emoji(text)
        >>> {'value': ['👨'], 'mean': [':man:'], 'location': [[14, 14]], 'flag': True}
    '''
    __entities = {}
    __value = []
    __mean = []
    __location = []
    flag = True
    try:
        pro_string = str(string)
        for pos,ej in enumerate(pro_string):
            if ej in emo_unicode.UNICODE_EMO:
                try:
                    __value.append(ej)
                    __mean.append(emo_unicode.UNICODE_EMO[ej])
                    __location.append([pos,pos])
                except Exception as e:
                    flag = False
                    __entities.append({"flag": False})
                    return __entities

    except Exception as e:
        flag = False
        __entities.append({"flag": False})
        return __entities
    if len(__value) < 1:
        flag = False    
    __entities = {
        'value' : __value,
        'mean' : __mean,
        'location' : __location,
        'flag' : flag
    }

    return __entities

def emoticons(string):
    '''emot.emoticons is use to detect emoticons from text

        >>> text = "I love python 👨 :-)"
        >>> emot.emoticons(text)
        >>> {'value': [':-)'], 'location': [[16, 19]], 'mean': ['Happy face smiley'], 'flag': True}
    '''
    __entities = []
    flag = True
    try:
        pattern = u'(' + u'|'.join(k for k in emo_unicode.EMOTICONS) + u')'
        __entities = []
        __value = []
        __location = []
        matches = re.finditer(r"%s"%pattern,str(string),re.IGNORECASE)
        for et in matches:
            __value.append(et.group().strip())
            __location.append([et.start(),et.end()])
            
        __mean = []
        for each in __value:
            __mean.append(emo_unicode.EMOTICONS_EMO[each])
        
        if len(__value) < 1:
            flag = False
        __entities = {
        'value' : __value,
        'location' : __location,
        'mean' : __mean,
        'flag' : flag
        }
    except Exception as e:
        __entities = [{'flag' : False}]
        #print("No emoiticons found")
        return __entities

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

if __name__ == '__main__':
    test_emo()