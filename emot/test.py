import core as emo
import cProfile

def test_emo():
    test = "I love it, 👨 :-) 🏁:-) :-)🏁 :-) 🏁 <3"
    print(emo.emoji(test))
    print(emo.emoticons(test))
    print(test[27:30])
    print(test[17])
    return None


def main():
    cProfile.run('test_emo()',sort = 'time')
    return None

if __name__=="__main__":
    main()
