import tkinterSearch as tS

if __name__ == '__main__':
    print("Unit tests for ZZZ-earch")
    STOP_WORDS = ["the", "or", "and"]
    print("Test ngram()")

    ngramTest1 = "somebody once told me the world was gonna roll me"
    correctResult1 = ["somebody once", "once told", "told me", "world was", "was gonna", "gonna roll", "roll me"]

    ngramTest2 = "i ain't the sharpest"
    correctResult2 = ["i ain't"]

    ngramTest3 = "tool in the shed"
    correctResult3 = ["tool in"]

    ngramTest4 = "hey now"
    correctResult4 = ["hey now"]

    ngramTest5 = "your'e an all-star"
    correctResult5 = ["your'e an", "an all-star"]

    assert(correctResult1 == tS.ngram(2, ngramTest1, STOP_WORDS))
    assert(correctResult2 == tS.ngram(2, ngramTest2 , STOP_WORDS))
    assert(correctResult3 == tS.ngram(2, ngramTest3,STOP_WORDS))
    assert(correctResult4 == tS.ngram(2, ngramTest4, STOP_WORDS))
    assert(correctResult5 == tS.ngram(2, ngramTest5, STOP_WORDS))


    print("Test stripPunctuation()")

    print("Test extractKeywords()")

    print("Test alias()")
