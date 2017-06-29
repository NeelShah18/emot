import logging
import re
import emo_unicode
#import emo

__all__ = ['emoji','emoticons']

def emoji(string):
    __entities = []
    pro_string = str(string)
    for pos,ej in enumerate(pro_string):
        if ej in emo_unicode.UNICODE_EMO:
            __entities.append({
                "value": ej,
                "str_span": [pos,pos]
                })
    return __entities

def emoticons(string):
    __entities = []
    pattern = u'(' + u'|'.join(k for k in emo_unicode.EMOTICONS) + u')'
    __entities = []
    matches = re.finditer(r"%s"%pattern,str(string),re.IGNORECASE)
    for et in matches:
        __entities.append({'value': et.group().strip(),
        'str_span': [et.start(),et.end()]
        })
    return __entities

def main():
    test = "I love it, 👨 :-) 🏁:-) :-)🏁 :-) 🏁"
    print(emoji(test))
    print(emoticons(test))
    print(test[27:30])
    print(test[17])

    return None

if __name__=="__main__":
    main()
