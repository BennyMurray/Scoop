from AcidityAnalyser import analyseAcidity
from BitternessAnalyser import analyseBitterness
from ColourAnalyser import analyseColour
from StrengthAnalyser import analyseStrength


def getValues(word_list, abv, beerName):
    print "Generating ABV for ", beerName + "...",
    strength = analyseStrength(word_list, abv)
    print "success"

    print "Generating SRM for ", beerName + "...",
    colour = analyseColour(word_list)
    print "success"

    print "Generating IBU for ", beerName + "...",
    bitterness = analyseBitterness(word_list)
    print "success"

    print "Generating acidity for ", beerName + "...",
    acidity = analyseAcidity(word_list)
    print "success"

    return [strength, colour, bitterness, acidity]