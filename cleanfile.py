def cleanfile(text, interviewee):
    from nltk import PorterStemmer
    from nltk.tokenize import sent_tokenize, word_tokenize
    import string
    #defining a dictionary of contractions
    contractions = { 
    "ain't": "am not; are not; is not; has not; have not",
    "aren't": "are not; am not",
    "can't": "cannot",
    "can't've": "cannot have",
    "'cause": "because",
    "could've": "could have",
    "couldn't": "could not",
    "couldn't've": "could not have",
    "didn't": "did not",
    "doesn't": "does not",
    "don't": "do not",
    "hadn't": "had not",
    "hadn't've": "had not have",
    "hasn't": "has not",
    "haven't": "have not",
    "he'd": "he had / he would",
    "he'd've": "he would have",
    "he'll": "he shall / he will",
    "he'll've": "he shall have / he will have",
    "he's": "he has / he is",
    "how'd": "how did",
    "how'd'y": "how do you",
    "how'll": "how will",
    "how's": "how has / how is / how does",
    "i'd": "i had / i would",
    "i'd've": "i would have",
    "i'll": "i shall / i will",
    "i'll've": "i shall have / i will have",
    "i'm": "i am",
    "i've": "i have",
    "isn't": "is not",
    "it'd": "it had / it would",
    "it'd've": "it would have",
    "it'll": "it shall / it will",
    "it'll've": "it shall have / it will have",
    "it's": "it has / it is",
    "let's": "let us",
    "ma'am": "madam",
    "mayn't": "may not",
    "might've": "might have",
    "mightn't": "might not",
    "mightn't've": "might not have",
    "must've": "must have",
    "mustn't": "must not",
    "mustn't've": "must not have",
    "needn't": "need not",
    "needn't've": "need not have",
    "o'clock": "of the clock",
    "oughtn't": "ought not",
    "oughtn't've": "ought not have",
    "shan't": "shall not",
    "sha'n't": "shall not",
    "shan't've": "shall not have",
    "she'd": "she had / she would",
    "she'd've": "she would have",
    "she'll": "she shall / she will",
    "she'll've": "she shall have / she will have",
    "she's": "she has / she is",
    "should've": "should have",
    "shouldn't": "should not",
    "shouldn't've": "should not have",
    "so've": "so have",
    "so's": "so as / so is",
    "that'd": "that would / that had",
    "that'd've": "that would have",
    "that's": "that has / that is",
    "there'd": "there had / there would",
    "there'd've": "there would have",
    "there's": "there has / there is",
    "they'd": "they had / they would",
    "they'd've": "they would have",
    "they'll": "they shall / they will",
    "they'll've": "they shall have / they will have",
    "they're": "they are",
    "they've": "they have",
    "to've": "to have",
    "wasn't": "was not",
    "we'd": "we had / we would",
    "we'd've": "we would have",
    "we'll": "we will",
    "we'll've": "we will have",
    "we're": "we are",
    "we've": "we have",
    "weren't": "were not",
    "what'll": "what shall / what will",
    "what'll've": "what shall have / what will have",
    "what're": "what are",
    "what's": "what has / what is",
    "what've": "what have",
    "when's": "when has / when is",
    "when've": "when have",
    "where'd": "where did",
    "where's": "where has / where is",
    "where've": "where have",
    "who'll": "who shall / who will",
    "who'll've": "who shall have / who will have",
    "who's": "who has / who is",
    "who've": "who have",
    "why's": "why has / why is",
    "why've": "why have",
    "will've": "will have",
    "won't": "will not",
    "won't've": "will not have",
    "would've": "would have",
    "wouldn't": "would not",
    "wouldn't've": "would not have",
    "y'all": "you all",
    "y'all'd": "you all would",
    "y'all'd've": "you all would have",
    "y'all're": "you all are",
    "y'all've": "you all have",
    "you'd": "you had / you would",
    "you'd've": "you would have",
    "you'll": "you shall / you will",
    "you'll've": "you shall have / you will have",
    "you're": "you are",
    "you've": "you have"
    }
    snowball=['i', 'me', 'my', 'myself', 'we', 'us', 'our', 'ourselves', 'ours', 'you', 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'will', 'would', 'should', 'could', 'ought', "i'm", "you're", "he's", "she's", "it's", "we're", "they're", "i've", "you've", "we've", "they've", "i'd", "you'd", "he'd", "she'd", "we'd", "they'd", "i'll", "you'll", "he'll", "she'll", "we'll", "they'll", "isn't", "wasn't", "weren't", "hasn't", "haven't", "hadn't", "doesn't", "don't", "didn't", "won't", "wouldn't", "shan't", "shouldn't", "can't", "cannot", "couldn't", "mustn't", "let's", "that's", "who's", "what's", "here's", "there's", "when's", "where's", "why's", "how's", "daren't", "needn't", "oughtn't", "mightn't", "a", "an", "the", "etc", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "during", "through", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "not", "nor", "only", "own", "same", "so", "than", "too", "very", "one", "every", "least", "less", "many", "now", "ever", "never", "say", "says", "said", "also", "get", "go", "goes", "just", "made", "make", "put", "see", "seen", "whether", "like", "well", "back", "even", "still", "way", "take", "since", "another", "however", "two", "three", "four", "five", "first", "second", "new", "old", "high", "long", "yeah", "oh", "uh"]
    punct=set(string.punctuation)
    words = text.split(":")
    interviewer=words[0]
    wordsclean=[]
    #picking out words by interviewee only
    for i in range(len(words)-1):
        if words[i].split(" ")[-1]==interviewee:
            wordsclean.append(words[i+1]) 
    if len(wordsclean)!=0:
        words=[]
        #taking out extra names that appear at the end of each interviewer's content
        for i in range(len(wordsclean)-1):
            temp=wordsclean[i].split(" ")
            del temp[-1]
            words.append(" ".join(temp))
        words.append(wordsclean[-1])
        #stripping out of extra wgite spaces
        for i in range(len(words)):
            words[i]=words[i].strip() 
        #take out snowball words
        words=[x for x in words if x not in snowball]
        
        text = " ".join(words)
        #substitute temporarily ' by 97401 to avoid destroying contractions
        text=text.replace("'","97401")
        #taking out punctuations except for the ' that have been substituted by 97401
        textclean=''.join(x for x in text if x not in punct)
        text=textclean.strip()
        #substitute back ' to where they appear
        text=text.replace("97401","'")
        #taking out interviewer names in case any left
        text=text.replace(interviewer, "")
        words=text.split(" ")
        #taking out contractions
        for i in range (len(words)):
            if words[i] in contractions:
                words[i]=contractions[words[i]]
                words[i]=words[i].strip()
        #taking out numbers/digits
        text = " ".join(words)
        text=''.join([x for x in text if not x.isdigit()])
        #taking out extra white spaces
        wordsnew=[]
        words=text.split(" ")
        for i in range (len(words)):
            if words[i]!='':
                wordsnew.append(words[i])
        #taking out punctuations, specifically ' that are not a part of a contraction
        text=' '.join(wordsnew)
        textclean=''.join(x for x in text if x not in punct)
        text=textclean.strip()
        saveforlater=text
        #downloading stop word list
        import nltk
        from nltk.corpus import stopwords
        nltk.download("stopwords")
        #taking out stop words
        stop = set(stopwords.words('english'))
        text=text.split(" ")
        text=[x for x in text if x!=""]
        text=[x for x in text if x not in snowball]
        textclean=' '.join(x for x in text if x not in stop)
       
        ##stemming every word
        ps = PorterStemmer()
        temp=textclean.split()
        for i in range (len(temp)):
            temp[i]=ps.stem(temp[i])
            if(temp[i]==' '):
                temp[i]=''
        textclean=' '.join(temp)
        return textclean
    else:
        return ''
