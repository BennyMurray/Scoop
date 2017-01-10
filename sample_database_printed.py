import pickle
dict = pickle.load(open( "sample_DB.p", "rb" ))

for i in dict[0]:
    print i
