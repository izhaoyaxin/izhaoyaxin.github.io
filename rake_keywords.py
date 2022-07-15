from nlp_rake import Rake
import operator
import sys
#sys.path.append("/Users/zhaoyaxin/exp/UnsupervisedQA")
#from unsupervisedqa.generate_synthetic_qa_data import *

stoppath = 'data/smart_stoplist.txt'

rake = Rake()

#rake_object = rake.Rake(stoppath, 5, 3, 4)

#sample_file = open("data/docs/fao_test/w2167e.txt", 'r', encoding="iso-8859-1")
#text = sample_file.read()
text = "European Union law is a body of treaties and legislation, such as Regulations and Directives, which have direct effect or indirect effect on the laws of European Union member states. The three sources of European Union law are primary law, secondary law and supplementary law. The main sources of primary law are the Treaties establishing the European Union. Secondary sources include regulations and directives which are based on the Treaties. The legislature of the European Union is principally composed of the European Parliament and the Council of the European Union, which under the Treaties may establish secondary law to pursue the objective set out in the Treaties."
#text="Anarchism is a political philosophy and movement that is sceptical of authority and rejects all involuntary, coercive forms of hierarchy. Anarchism calls for the abolition of the state, which it holds to be unnecessary, undesirable, and harmful. As a historically left-wing movement, placed on the farthest left of the political spectrum, it is usually described alongside communalism and libertarian Marxism as the libertarian wing (libertarian socialism) of the socialist movement, and has a strong historical association with anti-capitalism and socialism."

keywords = rake.apply(text)

# 3. print results
for keyword in keywords:
    print(keyword)

sents = text.strip().split(".")[:-1]
print(sents)

ans = "three"

cloze_sents = []
clozes = []

for sent in sents:
    if operator.contains(sent,ans):
        cloze_sents.append(sent)
        clozes.append(sent.replace(ans,"[mask]"))
print(cloze_sents)
print(clozes,ans)

# get_questions_for_clozes(clozes,args.use_subclause_clozes,
#         args.use_named_entity_clozes,
#         args.use_wh_heuristic,
#         args.translation_method)

#get_questions_for_clozes(clozes,1,1,1,'unmt')


