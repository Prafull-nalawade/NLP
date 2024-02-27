 

#What is natural language processing (NLP)?
#-> Natural language processing (NLP) refers to the 
#branch of computer science and more specifically, 
#the branch of artificial intelligence or AIconcerned
#with giving computers the ability to understand text 
#and spoken words in much the same way human beings can.



#Natural Language Processing (NLP) is a field of AI
 #that enables computers to understand and process 
 #human language, both written and spoken. It combines
 #linguistics, machine learning, and deep learning to 
 #make computers capable of tasks like translation, 
 #voice commands, and text summarization. NLP powers
 #voice assistants, chatbots, and business solutions.



#**********************************************************************



import re
text1=''' Elon musk's phone number is 9991116666, call him if you have any questions on dodgecoin. Tesla's revenue is 40 billion
Tesla's CFO number (999)-333-7777 and tesla's revenue is 20 billion
'''
pattern=r'\d\d\d\d\d\d\d\d\d\d'
matches=re.findall(pattern,text1)
matches 


**********************************************************************


import re
text1=''' Elon musk's phone number is 9991116666, call him if you have any questions on dodgecoin. Tesla's revenue is 40 billion
Tesla's CFO number (999)-333-7777 and tesla's revenue is 20 billion
'''
pattern=r'\d{10}'
matches=re.findall(pattern,text1)
matches 


**********************************************************************

pattern = '\d{3}\)-\d{3}-\d{4}'
mataches = re.findall(pattern,text)
matches


import re

text= ''' Elon musk's phone number is 9991116666, call him if you have any questions on dodgecoin. Tesla's revenue is 40 billion
Tesla's CFO number (999)-333-7777 and tesla's revenue is 20 billion'''

pattern=r'\(\d{3}\)-\d{3}-\d{4}'
matches=re.findall(pattern,text)
matches


**********************************************************************


import re

text= ''' Elon musk's phone number is 9991116666, call him if you have any questions on dodgecoin. Tesla's revenue is 40 billion
Tesla's CFO number (999)-333-7777 and tesla's revenue is 20 billion'''

pattern=r'\(\d{3}\)-\d{3}-\d{4} | \d{10}'
matches=re.findall(pattern,text)
matches

**********************************************************************


let us try
A protracted; legal battle; over a 32-carat;
 Golconda diamond-
 we want any charecter except ; and - pattern will be[^;-]
 


import re

text= ''' A protracted; legal battle; over a 32-carat;
 Golconda diamond-'''

pattern=r'[^;-]'
matches=re.findall(pattern,text)
matches


**********************************************************************
#when you want one line and not line then use [\n] in python

import re

text2 = '''Note 1 - Summary of Significant Accounting Policies
Unaudited Interim Financial Statements
The consolidated financial statements of Tesla, Inc. (“Tesla”, the “Company”, “we”, “us” or “our”), including the consolidated balance sheet as of
June 30, 2023, the consolidated statements of operations, the consolidated statements of comprehensive income, the consolidated statements of
redeemable noncontrolling interests and equity for the three and six months ended June 30, 2023 and 2022, and the consolidated statements of cash
flows for the six months ended June 30, 2023 and 2022, as well as other information disclosed in the accompanying notes, are unaudited. The
consolidated balance sheet as of December 31, 2022 was derived from the audited consolidated financial statements as of that date. The interim
consolidated financial statements and the accompanying notes should be read in conjunction with the annual consolidated financial statements and the
accompanying notes contained in our Annual Report on Form 10-K for the year ended December 31, 2022.
The interim consolidated financial statements and the accompanying notes have been prepared on the same basis as the annual consolidated
financial statements and, in the opinion of management, reflect all adjustments, which include only normal recurring adjustments, necessary for a fair
statement of the results of operations for the periods presented. The consolidated results of operations for any interim period are not necessarily
indicative of the results to be expected for the full year or for any other future years or interim periods.
'''
pattern = 'Note \d - [^\n]+'
matches =re.findall(pattern,text2)
matches



********************************************************************************************
#when you want one line and not line then use [\n] in python


import re

text2 = '''Note 1  Summary of Significant Accounting Policies
Unaudited Interim Financial Statements
The consolidated financial statements of Tesla, Inc. (“Tesla”, the “Company”, “we”, “us” or “our”), including the consolidated balance sheet as of
June 30, 2023, the consolidated statements of operations, the consolidated statements of comprehensive income, the consolidated statements of
redeemable noncontrolling interests and equity for the three and six months ended June 30, 2023 and 2022, and the consolidated statements of cash
flows for the six months ended June 30, 2023 and 2022, as well as other information disclosed in the accompanying notes, are unaudited. The
consolidated balance sheet as of December 31, 2022 was derived from the audited consolidated financial statements as of that date. The interim
consolidated financial statements and the accompanying notes should be read in conjunction with the annual consolidated financial statements and the
accompanying notes contained in our Annual Report on Form 10-K for the year ended December 31, 2022.
The interim consolidated financial statements and the accompanying notes have been prepared on the same basis as the annual consolidated
financial statements and, in the opinion of management, reflect all adjustments, which include only normal recurring adjustments, necessary for a fair
statement of the results of operations for the periods presented. The consolidated results of operations for any interim period are not necessarily
indicative of the results to be expected for the full year or for any other future years or interim periods.
'''
pattern = 'Note \d  [^\n]'
matches =re.findall(pattern,text2)
matches





********************************************************************************************





import re

text2 = '''Note 1 - Summary of Significant Accounting Policies
Unaudited Interim Financial Statements
The consolidated financial statements of Tesla, Inc. (“Tesla”, the “Company”, “we”, “us” or “our”), including the consolidated balance sheet as of
June 30, 2023, the consolidated statements of operations, the consolidated statements of comprehensive income, the consolidated statements of
redeemable noncontrolling interests and equity for the three and six months ended June 30, 2023 and 2022, and the consolidated statements of cash
flows for the six months ended June 30, 2023 and 2022, as well as other information disclosed in the accompanying notes, are unaudited. The
consolidated balance sheet as of December 31, 2022 was derived from the audited consolidated financial statements as of that date. The interim
consolidated financial statements and the accompanying notes should be read in conjunction with the annual consolidated financial statements and the
accompanying notes contained in our Annual Report on Form 10-K for the year ended December 31, 2022.
The interim consolidated financial statements and the accompanying notes have been prepared on the same basis as the annual consolidated
financial statements and, in the opinion of management, reflect all adjustments, which include only normal recurring adjustments, necessary for a fair
statement of the results of operations for the periods presented. The consolidated results of operations for any interim period are not necessarily
indicative of the results to be expected for the full year or for any other future years or interim periods.
'''
pattern = 'Note \d - ([^\n]+)'
matches =re.findall(pattern,text2)
matches




********************************************************************************************


import re

text2 = '''The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 Q4 it was $3 billion. The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 Q4 it was $3 billion'''
pattern = 'FY\d{4}.Q\d'
matches =re.findall(pattern,text2)
matches


********************************************************************************************


import re

text2 = '''The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 Q4 it was $3 billion. The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 Q4 it was $3 billion'''
pattern = 'FY\d{4}.Q[1-4]'
matches =re.findall(pattern,text2)
matches


********************************************************************************************

#re.IGNORECASE use in databse Q captial or q small the o/p is print

import re

text2 = '''The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 q4 it was $3 billion. The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 q4 it was $3 billion'''
pattern = 'FY\d{4}.Q[1-4]'
matches =re.findall(pattern,text2,re.IGNORECASE)
matches


********************************************************************************************

#In order to solve these issue re,IGNORECASE

import re

text2 = '''The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 Q4 it was $3 billion. The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 Q4 it was $3 billion'''
pattern = 'FY\d{4}.Q[1-4] |fy\d{4} Q[1-4]'
matches =re.findall(pattern,text2)
matches

********************************************************************************************

pattern = 'FY\d{4}.Q[1-4] |fy\d{4} Q[1-4]'
matches =re.findall(pattern,text2,re.IGNORECASE)
matches


********************************************************************************************

# now let assume we wont find finicial number

pattern = '\$[0-9\.]+'
matches =re.findall(pattern,text2)
matches


********************************************************************************************

import nltk


x="they are running dancing and jumping on track"
revnge= nltk

































































