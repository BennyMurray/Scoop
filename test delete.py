import pickle


f = open('sample__visitor_database.p', 'rb')
sample_visitor_database = pickle.load(f)
f.close()
