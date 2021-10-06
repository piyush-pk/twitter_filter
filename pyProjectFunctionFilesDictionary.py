#opens a twitter data set of 20 tweets with retweets and tweet replies
projectTwitterDataFile = open("project_twitter_data.csv","r")
# resulting data file that we will use to visualise data
resultingDataFile = open("resulting_data.csv","w")


## a simple function to remove punctuations from a given string 
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
def strip_punctuation(strWord):
    for charPunct in punctuation_chars:
        strWord = strWord.replace(charPunct, "")
    return strWord


positive_words = []
##this list of positive words 
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

"""
which takes one parameter, a string which represents a one or more sentences,
and calculates how many words in the string are considered positive words
Use the list, positive_words to determine what words will count as positive
The function should return a positive integer denoting how positive a sentence is
"""
            
def get_pos(strSentences):
    strSentences = strip_punctuation(strSentences)
    listStrSentences= strSentences.split()
    
    count=0
    for word in listStrSentences:
        for positiveWord in positive_words:
            if word == positiveWord:
                count+=1
    return count

negative_words = []
##this list of negative words 
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

"""
which takes one parameter, a string which represents a one or more sentences,
and calculates how many words in the string are considered negative words
Use the list, negative_words to determine what words will count as negative
The function should return a positive integer denoting how negative a sentence is
"""
            
def get_neg(strSentences):
    strSentences = strip_punctuation(strSentences)
    listStrSentences = strSentences.split()
    
    count=0
    for word in listStrSentences:
        for negativeWord in negative_words:
            if word == negativeWord:
                count+=1
    return count

    

def writeInDataFile(resultingDataFile):
    resultingDataFile.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
    resultingDataFile.write("\n")

    linesPTDF =  projectTwitterDataFile.readlines()
    headerDontUsed= linesPTDF.pop(0)
    for linesTD in linesPTDF:
        listTD = linesTD.strip().split(',')
        positive_score=get_pos(listTD[0])
        negative_score=get_neg(listTD[0])
        net_score=positive_score-negative_score
        resultingDataFile.write("{}, {}, {}, {}, {}".format(listTD[1], listTD[2],positive_score,negative_score,net_score))    
        resultingDataFile.write("\n")

#listTD[1] is no. of retweets
#listTD[2] is no. of replies

writeInDataFile(resultingDataFile)
projectTwitterDataFile.close()
resultingDataFile.close()
