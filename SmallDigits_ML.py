from math import log
# encodes vector of 0's and 1's => indicatoing the words presence in the sentence


def Encode(sent, wordls):
    returnls = []
    words = sent.split()[1:]
    encountered = []
    for word in wordls:
        if word in encountered:
            continue
        if word in words:
            returnls += [1]
        else:
            returnls += [0]
        encountered += [word]

    return returnls


# generate a list of 2D vectors which correspond to the good/bad inferences of the statement
def Inference(TestSent, wordls, good_dict, bad_dict):
    wordls = list(wordls)
    inferences = []

    for sent in TestSent:
        encoding = Encode(sent, wordls)
        prob_good = 0
        prob_bad = 0
        # use logs to counteract underflow
        for i in range(len(encoding)):
            if encoding[i] == 1:
                # contains word
                prob_good += log(good_dict[wordls[i]], 10)
                prob_bad += log(bad_dict[wordls[i]], 10)
            else:
                # dos not contain word
                prob_good += log((1 - good_dict[wordls[i]]), 10)
                prob_bad += log((1 - bad_dict[wordls[i]]), 10)
        # add calculated probs to list
        inferences += [[10 ** prob_good, 10 ** prob_bad]]
    return inferences

# calcs prob P(good|x)


def Calc_prob(inferences, good_prob, bad_prob):
    num = inferences[0] * good_prob
    den = ((inferences[0] * good_prob) + (inferences[1] * bad_prob))
    ans = (num / den)
    ans *= 100
    return round(ans, 2)


# MAIN
if __name__ == "__main__":
    # capture input
    raw_training_data = []  # array of arrays containing raw words per review
    with open("Small_dig.txt") as f:
        contents = f.readline()
        dig=contents.split(",")

        print(dig)
   