from tkinterSearch import ngram

if __name__ == '__main__':
    print("Unit tests for ZZZ-earch")
    STOP_WORDS = ["the", "or", "and"]
    print("Test ngram()")
    ## Long query
    ngramTest1 = "somebody once told me the world was gonna roll me"
    correctBigram1 = ["somebody once", "once told", "told me", "world was", "was gonna", "gonna roll", "roll me"]
    correctTrigram1 = ["somebody once told", "once told me", "world was gonna", "was gonna roll", "gonna roll me"]

    ngramTest2 = "i ain't the sharpest"
    correctBigram2 = ["i ain't"]

    ngramTest3 = "tool in the shed"
    correctBigram3 = ["tool in"]

    ngramTest4 = "hey now"
    correctBigram4 = ["hey now"]

    ngramTest5 = "your'e an all-star"
    correctBigram5 = ["your'e an", "an all-star"]
    correctTrigram5 = ["your'e an all-star"]
    print("Bigram tests...")
    assert(correctBigram1 == ngram(2, ngramTest1, STOP_WORDS))
    assert(correctBigram2 == ngram(2, ngramTest2 , STOP_WORDS))
    assert(correctBigram3 == ngram(2, ngramTest3,STOP_WORDS))
    assert(correctBigram4 == ngram(2, ngramTest4, STOP_WORDS))
    assert(correctBigram5 == ngram(2, ngramTest5, STOP_WORDS))
    print("Trigram tests...")
    assert(correctTrigram1 == ngram(3, ngramTest1, STOP_WORDS))
    assert([] == ngram(3, ngramTest2 , STOP_WORDS))
    assert([] == ngram(3, ngramTest3,STOP_WORDS))
    assert([] == ngram(3, ngramTest4, STOP_WORDS))
    assert(correctTrigram5 == ngram(3, ngramTest5, STOP_WORDS))

    print("All ngram() tests passed!")
    print("Test stripPunctuation()")

    print("Test extractKeywords()")

    print("Test alias()")
