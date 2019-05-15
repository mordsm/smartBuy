from pygrok import Grok
text = 'gary is male, 25 years old and weighs 68.5 kilograms'
pattern = '%{WORD:name} is %{WORD:gender}, %{NUMBER:age} years old and weighs %{NUMBER:weight} kilograms'

text ='720 x 1280 pixels (~210 ppi pixel density)'
text = text.replace("(","")
pattern = '%{NUMBER:height} x %{NUMBER:width} pixels ~%{NUMBER:ppi} ppi pixel density'
grok = Grok(pattern)
print (grok.match(text))
text ='720 x 1280 pixels ('
text = text.replace("(","")
pattern = '%{NUMBER:height} x %{NUMBER:width} pixels '
grok = Grok(pattern)
print (grok.match(text))
text = 'moshe is 61 years old'
pattern = '%{WORD:name} is %{NUMBER:age} years old'
grok = Grok(pattern)
print (grok.match(text))
text = 'gary is male, 25 years old and weighs 68.5 kilograms'
pattern = '%{WORD:name} is %{WORD:gender}, %{NUMBER:age} years old and weighs %{NUMBER:weight} kilograms'
grok = Grok(pattern)
print (grok.match(text))