import string
import sys
from smartBuy.resources.ManagingData import *
import pandas as pd
from smartBuy.Attribute import Attribute as attr


def grokIt(text,patterns):
    '''

    :param text to grok:
    :param few possible patterns:
    :return the longest result json possible :
    sample
        text ='720 x 1280 pixels (~210 ppi pixel density)'
        patterns = ['%{NUMBER:height} x %{NUMBER:width} pixels ~%{NUMBER:ppi} ppi pixel density','%{NUMBER:height} x %{NUMBER:width}']

    '''
    from pygrok import Grok
    try:
        for pattern in patterns:
            grok = Grok(pattern)
            text = text.replace("(", "")
            result = grok.match(text)
            print (result)
            return result
    except Exception as e:
        print(e)
        send_mail("no patterns where found for {}".format(text))
        sys.exit(1)


def createDict(*args):
    return dict(((k, eval(k)) for k in args))


def function1():
    print ("called function 1")



def function2():
    print ("called function 2")


def function3():
    print ("called function 3")
dictionary = {"pc":{"functions":[function1,function2,function3]}}
def execute_actions(dictionary , item):
    for func in dictionary[item]["functions"]:
        func()
'''
    :param dictionary: 
    :param item: 
    :return: 
'''

def set_request_values(dictionary , type , attr_name , attr_value):

    if attr_name in dictionary:
        c_attr_value = dictionary[attr_name]
        C_attr = Attribute(type ,attr_name, c_attr_value)
        O_attr = Attribute(type ,attr_name, attr_value)
        if O_attr > C_attr :
            dictionary[attr_name] = attr_value

    else:
        dictionary[attr_name] = attr_value








#execute_actions(dictionary,"pc")



def convert_csv_title_to_dictionary(path):
    data = pd.read_csv(path, error_bad_lines=False)
    data.head(0)
    y = 0
    name_list = data.columns[2:].values.tolist()
    features = list(map(lambda x:{x:name_list.index(x)},name_list))
    #print (features)
    return features
def get_item_feature_grade(max_value , item_value):
    print ((max_value-item_value)/max_value)

    return ((max_value-item_value)/max_value)
def send_mail(iSubject,iBody,to="sharon.moshe@gmail.com"):
    import smtplib

    gmail_user = 'sharon.moshe@gmail.com'
    gmail_password = 'mordsmi3'

    sent_from = gmail_user
    #to = ['sharon.moshe@gmail.com', '']
    subject = iSubject
    body = iBody

    email_text = """\  
    From: %s  
    To: %s  
    Subject: %s

    %s
    """ % (sent_from, ", ".join(to), subject, body)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()

        print ('Email sent!')
    except:
        print ('Something went wrong...')
#convert_csv_title_to_dictionary("/home/moshe/workspace/projects/smartBuy/phone_dataset.csv")
#get_item_feature_grade(2000,1770)



