import fasttext
model1=fasttext.train_unsupervised('hindi-train.csv')
model.words[u'the', u'of', u'one', u'zero', u'and', u'in', u'two', u'a', u'nine', u'to', u'is', ...
model1.save_model("result/r1")
model2=fasttext.train_unsupervised('scrp.txt');
model.words[u'the', u'of', u'one', u'zero', u'and', u'in', u'two', u'a', u'nine', u'to', u'is', ...
model2.save_model("result/r2")
            
