def comma(mylist):
    sentence = ''
    for listedItem in mylist:
        if mylist.index(listedItem) == len(mylist) -1:
            sentence += 'and ' + listedItem
            return(sentence)
        else:
            sentence += listedItem + ', '

spam = ['apples', 'bananas', 'tofu', 'cats']
print(comma(spam))
