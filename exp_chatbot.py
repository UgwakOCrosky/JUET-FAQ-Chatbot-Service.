import re
from dataset import words
from wedontwant import those_words
from greetings import greet
from actions import weird
#from doub import doubl
#from doub import doublr
from actions import pact
from actions import nact
b=[]
my_list=[]
m=''
def main_like():
    a=input().lower()
    b=[x for x in re.split('\W',a) if x]
    y=len(b)
    for i in range(0,y):
        if(i<y-1 and weird.__contains__(b[i]) and b[i+1]=='t'):
            del b[i+1]
            b[i]=b[i]+"'"+"t"
    count1=0
    for x in b:
        if those_words.__contains__(x):
            count1+=1
    if count1==0:
        chatbatter(b)
    else:
        print('Please don\'t abuse!!! We at JUET don\'t tolerate it!!')
    return
def chatbatter(b):
    count2=0
    for x in b:
        if greet.__contains__(x):
            c=x
            count2+=1
    if count2!=0:
        print(greet[c])
    count=0
    my_list=[]
    for x in b:
        if words.__contains__(x):
            my_list.append(x)
            count+=1
    if count==1:
        c=my_list[0]
        #countpact=0
        countnact=0
        #print('You mentioned '+c)
        for x in b:
            #if pact.__contains__(x):
                #countpact+=1
            if nact.__contains__(x):
                countnact+=1
        #if(pact>=1):
            #print(words[c]['0'])
        if(countnact==0):
            print(words[c]['0'])
        else:
            flag=-1
            print('You mentioned '+c)
            print('But I am not sure if you really want to know about it.')
            print('Would you like to know about it??')
            temp=input().lower()
            if(temp=='y' or temp=='y '):
                flag=1
            if(temp=='n' or temp=='n '):
                flag=0
            if(flag==-1):
                count1=0
                right=[x for x in re.split('\W',temp) if x]
                for x in right:
                    if those_words.__contains__(x):
                        count1+=1
                if count1>0:
                    print('Please don\'t abuse!!! We at JUET don\'t tolerate it!!')
                    return
                if(right.__contains__('yes') or right.__contains__('yup')):
                    flag=1
                if(right.__contains__('no') or right.__contains__('nope')):
                    flag=0
            if(flag==0):
                print('Maybe I misunderstood you.\nPlease ask another query or contact the reception to get your answer. The number is: 9876543210')
            elif(flag==1):
                print(words[c]['0'])
            else:
                print('Sorry I don\'t understand you.\nPlease ask another query.')
        '''
        if len(words[c])>1:
            temp=input().lower()
            try:
                print(words[c][temp])
                if temp!='no' and temp!='n':
                    temp=input().lower()
                    if temp=='yes' or temp=='no' or temp=='0' or temp=='n' or temp=='y':
                        raise Exception("Sorry i don't understand you. Please make another query .\nYou can also call the college reception.\nThe number is: 9876543210.")
                    else:
                        try:
                            print(words[c][temp])
                        except:
                            print("Sorry i don't understand you. Please make another query.\nYou can also call the college reception.\nThe number is: 9876543210.")
            except:
                print("Sorry i don't understand you.Please make another query.\nYou can also call the college reception.\nThe number is: 9876543210.")
                '''
    elif count==0 and count2==0:
        print("Sorry i don't understand you.\nYou can call the college reception to get your answer.\nThe number is: 9876543210.")
    elif count2!=0:
        print('You can ask me queries related to new admissions.\nI can also tell you about Faculty members and placements!!')
    else:
        '''print('You have mentioned:-')
        i=1
        for x in my_list:
            print(str(i)+':'+x)
            i+=1
        '''
        print('You have asked {} queries at a time'.format(count))
        print('But I can help you one by one')
        print('So please ask a single query next time.')
        #print('So please select one entry at a time from the above')
        #main_like()
    return
print('========= Welcome to JUET FAQ Service =========')
print('=========== I am a Reception Bot!!! ===========')
print("I'll be taking new admission queries")
print("You can also ask me about courses offered, placements and faculty members")
print('==== Please try to make meaningful Queries ====')
print('============= I am still learning =============')
print("How may I help you?")
while True:
    main_like()

