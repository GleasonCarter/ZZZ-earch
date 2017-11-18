import textManipulation as tM

if __name__ == '__main__':
    print "Tests for punctuation strip:"
    str1 = "No change"
    str2 = ";Leading"
    str3 = "Trailing&"
    str4 = ".Remove Both,"
    str5 = "(.Remove Multiple!-"
    str6 = "!$#@><:}"
    str7 = "...................................."
    strings_to_test = [str1, str2, str3, str4, str5, str6, str7]

    for string in strings_to_test:
        print tM.stripPunctuation(string)
