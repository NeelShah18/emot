import multiprocessing as mp

try:
    from . import emo_unicode, pattern_generator
    import re
except Exception as E:
    print("Issue with loading of the library: " + str(E))

'''emot library to detect emoji and emoticons.

    >>> import emot 
    >>> emot_obj = emot.emot() 
    >>> text = "I love python ☮ 🙂 ❤ :-) :-( :-)))" 
    >>> emot_obj.emoji(test) 
    >>> {'value': ['☮', '🙂', '❤'], 'location': [[14, 15], [16, 17], [18, 19]], 'mean': [':peace_symbol:', 
    ':slightly_smiling_face:', ':red_heart:'], 'flag': True} 
    >>> emot_obj.emoticons(test) >>> {'value': [':-)', ':-(', ':-)))'], 'location': [[20, 23], [24, 27], [28, 33]], 
    'mean': ['Happy face smiley', 'Frown, sad, andry or pouting', 'Very very Happy face or smiley'], 'flag': True} 
    
    Running bulk string emoji and emoticons detection. When user has access multiple processing cores.
    
    >>> import emot 
    >>> emot_obj = emot.emot() 
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

'''


class emot:
    def __init__(self):
        global pattern_generator_emoticons_obj, pattern_generator_emoji_obj
        try:
            pattern_generator_emoji_obj = pattern_generator.pattern_generator()
        except Exception as E:
            print("Issue with creating pattern generator object emoji: " + str(E))

        try:
            for keys, values in emo_unicode.EMOJI_UNICODE.items():
                pattern_generator_emoji_obj.add(values)

            for keys, values in emo_unicode.EMOJI_ALIAS_UNICODE.items():
                pattern_generator_emoji_obj.add(values)

            self.compiled_pattern_emoji = re.compile(pattern_generator_emoji_obj.pattern())
        except Exception as E:
            print("Issue with Generating pattern: " + str(E))

        try:
            pattern_generator_emoticons_obj = pattern_generator.pattern_generator()
        except Exception as E:
            print("Issue with creating pattern generator object emoticons: " + str(E))

        try:
            for keys, values in emo_unicode.EMOTICONS_EMO.items():
                pattern_generator_emoticons_obj.add(keys)

                self.compiled_pattern_emoticons = re.compile(pattern_generator_emoticons_obj.pattern())
        except Exception as E:
            print("Issue with Generating pattern: " + str(E))

    def emoji(self, string):
        """emot.emoji is use to detect emoji from text

            >>> import emot
            >>> emot_obj = emot.emot()
            >>> text = "I love python ☮ 🙂 ❤ :-) :-( :-)))"
            >>> emot_obj.emoji(text)
            >>> {'value': ['☮', '🙂', '❤'], 'location': [[14, 15], [16, 17], [18, 19]], 'mean': [':peace_symbol:',
            ':slightly_smiling_face:', ':red_heart:'], 'flag': True}
        """
        __entities = {}
        __value = []
        __location = []
        __mean = []
        __flag = False
        try:
            processed_string = str(string)
            matches = self.compiled_pattern_emoji.finditer(str(processed_string))
            for et in matches:
                __value.append(et.group().strip())
                __location.append([et.start(), et.end()])
                __mean.append(emo_unicode.UNICODE_EMOJI[et.group().strip()])
        except Exception as E:
            print("Issue with internal pattern finding emoji: " + str(E))

        if len(__value) > 0:
            __flag = True

        __entities = {
            'value': __value,
            'location': __location,
            'mean': __mean,
            'flag': __flag
        }

        return __entities

    def emoticons(self, string):
        """emot.emoticons is use to detect emoticon from text

            >>> import emot
            >>> emot_obj = emot.emot()
            >>> text = "I love python ☮ 🙂 ❤ :-) :-( :-)))"
            >>> emot_obj.emoji(text)
            >>> emot_obj.emoticons(text) >>> {'value': [':-)', ':-(', ':-)))'], 'location': [[20, 23], [24, 27], [28, 33]],
                'mean': ['Happy face smiley', 'Frown, sad, andry or pouting', 'Very very Happy face or smiley'], 'flag': True}
        """
        __entities = {}
        __value = []
        __location = []
        __mean = []
        __flag = False
        try:
            processed_string = str(string)
            matches = self.compiled_pattern_emoticons.finditer(str(processed_string))
            for et in matches:
                __value.append(et.group().strip())
                __location.append([et.start(), et.end()])
                __mean.append(emo_unicode.EMOTICONS_EMO[et.group().strip()])
        except Exception as E:
            print("Issue with internal pattern finding emoticons: " + str(E))

        if len(__value) > 0:
            __flag = True

        __entities = {
            'value': __value,
            'location': __location,
            'mean': __mean,
            'flag': __flag
        }

        return __entities

    def bulk_emoji(self, string_list, multiprocessing_pool_capacity=int(mp.cpu_count()/2)):
        """emot.bult_emoji is use to detect emoticon from list of string

                    Here, we have two input for bulk_emoticons: list of string and multiprocessing_pool_capacity.
                    list of string = [string1, string2, ...]
                    multiprocessing_pool_capacity = multi processing pool user want to provide for the computation.
                        By defaul the pool capacity is half of the total cores in the system.

                    >>> import emot
                    >>> emot_obj = emot.emot()
                    >>> bulk_test = ["I love python ☮ 🙂 ❤ :-) :-( :-)))", "I love python 🙂 ❤ :-) :-( :-)))", "I love
                        python ☮ ❤ :-) :-( :-)))", "I love python ☮ 🙂 :-( :-)))"]
                    >>> emot_obj.bulk_emoji(bulk_test, multiprocessing_pool_capacity=2)
                    >>> [{'value': ['☮', '🙂', '❤'], 'location': [[14, 15], [16, 17], [18, 19]],
                        'mean': [':peace_symbol:', ':slightly_smiling_face:', ':red_heart:'], 'flag': True}, {'value': ['🙂', '❤'],
                        'location': [[14, 15], [16, 17]], 'mean': [':slightly_smiling_face:', ':red_heart:'], 'flag': True}, {'value': [
                        '☮', '❤'], 'location': [[14, 15], [16, 17]], 'mean': [':peace_symbol:', ':red_heart:'], 'flag': True},
                        {'value': ['☮', '🙂'], 'location': [[14, 15], [16, 17]], 'mean': [':peace_symbol:', ':slightly_smiling_face:'],
                        'flag': True}]
                """
        processor_pool = mp.Pool(multiprocessing_pool_capacity)
        __entities = processor_pool.map(self.emoji, string_list)
        return __entities

    def bulk_emoticons(self, string_list, multiprocessing_pool_capacity=int(mp.cpu_count()/2)):
        """emot.bult_emoticons is use to detect emoticon from list of string

            Here, we have two input for bulk_emoticons: list of string and multiprocessing_pool_capacity.
            list of string = [string1, string2, ...]
            multiprocessing_pool_capacity = multi processing pool user want to provide for the computation.
                By defaul the pool capacity is half of the total cores in the system.

            >>> import emot
            >>> emot_obj = emot.emot()
            >>> bulk_test = ["I love python ☮ 🙂 ❤ :-) :-( :-)))", "I love python 🙂 ❤ :-) :-( :-)))", "I love python
                ☮ ❤ :-) :-( :-)))", "I love python ☮ 🙂 :-( :-)))"]
            >>> emot_obj.bulk_emoticons(bulk_test, multiprocessing_pool_capacity=2)
            >>> [{'value': [':-)', ':-(', ':-)))'], 'location': [[20, 23], [24, 27], [28, 33]], 'mean': ['Happy face smiley',
                'Frown, sad, andry or pouting', 'Very very Happy face or smiley'], 'flag': True}, {'value': [':-)', ':-(', ':-)))'],
                'location': [[18, 21], [22, 25], [26, 31]], 'mean': ['Happy face smiley', 'Frown, sad, andry or pouting', 'Very
                very Happy face or smiley'], 'flag': True}, {'value': [':-)', ':-(', ':-)))'], 'location': [[18, 21], [22, 25],
                [26, 31]], 'mean': ['Happy face smiley', 'Frown, sad, andry or pouting', 'Very very Happy face or smiley'],
                'flag': True}, {'value': [':-(', ':-)))'], 'location': [[18, 21], [22, 27]], 'mean': ['Frown, sad, andry or
                pouting', 'Very very Happy face or smiley'], 'flag': True}]
        """
        processor_pool = mp.Pool(multiprocessing_pool_capacity)
        __entities = processor_pool.map(self.emoticons, string_list)
        return __entities


def test_emo():
    emot_obj = emot()
    test = "I love python ☮ 🙂 ❤ :-) :-( :-)))"
    bulk_test = ["I love python ☮ 🙂 ❤ :-) :-( :-)))", "I love python 🙂 ❤ :-) :-( :-)))", "I love python ☮ ❤ :-) :-( :-)))", "I love python ☮ 🙂 :-( :-)))"]
    print(emot_obj.emoticons(test))
    print(emot_obj.emoji(test))
    print(emot_obj.bulk_emoji(bulk_test))
    print(emot_obj.bulk_emoticons(bulk_test))
    return None


def about():
    text = "emot library: emoji and emoticons library for python. It return emoji or emoticons from string with " \
           "location of it. \nAuthors: \n Neel Shah: neelknightme@gmail.com or https://github.com/NeelShah18 "
    print(text)
    return None


if __name__ == '__main__':
    test_emo()
    about()
