from core import emot
import cProfile


def test_emo():
    emot_obj = emot()
    test = "I love it, 👨 :-) 🏁:-) :-)🏁 :-) 🏁 <3 oo oO "
    print(emot_obj.emoji(test))
    print(emot_obj.emoticons(test))
    print(test[27:30])
    print(test[17])
    return None


def main():
    cProfile.run('test_emo()', sort='time')
    return None


if __name__ == "__main__":
    main()
