import re
from dataset import ans
from wedontwant import those_words
from greetings import greet
from actions import weird
import random
from actions import pact
from actions import nact
b=[]
my_list=[]
m=''
foo = ['Moreover', 'Furthermore', 'Also', 'And']
counter=0
def query(counter):
    global my_list
    c=my_list[counter]
    #countpact=0
    countnact=0
    #print('You mentioned '+c)
    global b
    for x in b:
        #if pact.__contains__(x):
            #countpact+=1
        if nact.__contains__(x):
            countnact+=1
    #if(pact>=1):
        #print(ans[c])
    if(countnact==0):
        print(ans[c])
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
            print('Maybe I misunderstood you.\nFor this query you can contact the reception to get your answer. The number is: 9876543210')
        elif(flag==1):
            print(ans[c])
        else:
            print('Sorry I don\'t understand you.\nFor this query you can contact the reception to get your answer. The number is: 9876543210')
    return
def main_like():
    a=input().lower()
    #a=a+' '
    if(a==''):
        main_like()
        return
    global b
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
    global my_list
    my_list=[]
    for x in b:
        if ans.__contains__(x):
            my_list.append(x)
    my_list=list(set(my_list))
    count=len(my_list)
    if count==1:
        query(0)
    elif count==0 and count2==0:
        print("Sorry i don't understand you.\nYou can call the college reception to get your answer.\nThe number is: 9876543210.")
    elif count2!=0:
        print('You can ask me queries related to new admissions.\nI can also tell you about Faculty members and placements!!')
    else:
        for yo in range(0,count):
            global foo
            if(yo==count-1):
                print("Lastly,")
            elif(yo!=0):
                print(random.choice(foo)+',')
            query(yo)
    return
print('======================= Welcome to JUET FAQ Service ========================')
print('========================= I am a Reception Bot!!! ==========================')
print("====================I'll be taking new admission queries====================")
print("==You can also ask me about courses offered, placement and faculty members==")
print('================== Please try to make meaningful Queries ===================')
print('============================ I am still learning ===========================')
print("How may I help you?")
while True:
    main_like()

