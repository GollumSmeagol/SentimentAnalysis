#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!pip install tweepy
#!pip install regex
#!pip install text2emotion
#!pip install textblob
#!pip install pandas
#!pip install numpy
#!pip install matplotlib
#!pip install syspath
#!pip install python-csv
import math
import sys,tweepy,csv,re
import text2emotion as te
from textblob import TextBlob
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *
from tkinter import messagebox
import winsound
from PIL import Image
def quitar():
    if messagebox.askokcancel("Exit","Are you sure want to Quit?"):
        gui.destroy()


def cleanUpTweets(text):
        text = re.sub(r'@[A-Za-z0-9_]+', '', text)
        text = re.sub(r'#', '', text)
        text = re.sub(r'RT : ', '', text)
        text = re.sub(r'https?:\/\/[A-Za-z0-9\.\/]+', '', text)
        return text

def gettextSubjectivity(text):
        return TextBlob(text).sentiment.subjectivity

def percentagecalculator(list1):
        sum = 0
        for x in list1:
            sum = sum + x
        return sum

def generate_pie1():
    fig = plt.figure(figsize=(4, 4),dpi=100)
    y = np.array([happysum, sadsum, angersum, surprisesum, fearsum])
    mylabels = ["HAPPY", "SAD", "ANGRY", "SURPRISE", "FEAR"]
    colors = ['yellowgreen', 'lightcoral', 'gold', '#00ffff', '#4000ff']
    myexplode = [0.1, 0, 0, 0, 0]
    plt.pie(y, labels=mylabels, explode=myexplode, colors=colors, autopct='%1.1f%%', startangle=120)
    plt.legend(mylabels, loc=(-0.05, 0.05), shadow=True)
    plt.title('Reaction of '+ searchTerm1 +' by analyzing ' + str(NoOfTerms) + ' Tweets.')
    plt.axis('equal')
    canvasbar=FigureCanvasTkAgg(fig,master=subcmd)
    canvasbar.draw()
    canvasbar.get_tk_widget().place(x=50,y=100)

def generate_pie2():
    fig = plt.figure(figsize=(4, 4),dpi=100)
    y = np.array([happysum2, sadsum2, angersum2, surprisesum2, fearsum2])
    mylabels = ["HAPPY", "SAD", "ANGRY", "SURPRISE", "FEAR"]
    colors = ['yellowgreen', 'lightcoral', 'gold', '#00ffff', '#4000ff']
    myexplode = [0.1, 0, 0, 0, 0]
    plt.pie(y, labels=mylabels, explode=myexplode, colors=colors, autopct='%1.1f%%', startangle=120)
    plt.legend(mylabels, loc=(-0.05, 0.05), shadow=True)
    plt.title('Reaction of '+searchTerm2+ ' by analyzing ' + str(NoOfTerms) + ' Tweets.')
    plt.axis('equal')
    canvasbar=FigureCanvasTkAgg(fig,master=subcmd)
    canvasbar.draw()
    canvasbar.get_tk_widget().place(x=500,y=100)

def plotPieChart1():
    fig = plt.figure(figsize=(3.8, 4.6),dpi=100)

    labels = ['Positive [' + str(positive) + '%]', 'Weakly Positive [' + str(wpositive) + '%]','Strongly Positive [' + str(spositive) + '%]', 'Neutral [' + str(neutral) + '%]',
                  'Negative [' + str(negative) + '%]', 'Weakly Negative [' + str(wnegative) + '%]', 'Strongly Negative [' + str(snegative) + '%]']
    sizes = [positive, wpositive, spositive, neutral, negative, wnegative, snegative]
    colors = ['yellowgreen','lightgreen','darkgreen', 'gold', 'red','lightsalmon','darkred']
    myexplode = [0.1, 0, 0, 0,0,0,0]
    patches, texts = plt.pie(sizes, colors=colors, startangle=90)
    plt.legend(patches, labels, loc=(-0.05,0.05))
    plt.title('Reaction of ' + searchTerm1 + ' by analyzing ' + str(NoOfTerms) + ' Tweets.')
    plt.axis('equal')
    #plt.tight_layout()
    canvasbar=FigureCanvasTkAgg(fig,master=top)
    canvasbar.draw()
    canvasbar.get_tk_widget().place(x=35,y=110)

def plotPieChart2():
    fig = plt.figure(figsize=(3.8, 4.6),dpi=100)

    labels = ['Positive [' + str(positive2) + '%]', 'Weakly Positive [' + str(wpositive2) + '%]','Strongly Positive [' + str(spositive2) + '%]', 'Neutral [' + str(neutral2) + '%]',
                  'Negative [' + str(negative2) + '%]', 'Weakly Negative [' + str(wnegative2) + '%]', 'Strongly Negative [' + str(snegative2) + '%]']
    sizes = [positive2, wpositive2, spositive2, neutral2, negative2, wnegative2, snegative2]
    colors = ['yellowgreen','lightgreen','darkgreen', 'gold', 'red','lightsalmon','darkred']
    myexplode = [0.1, 0, 0, 0,0,0,0]
    patches, texts = plt.pie(sizes, colors=colors, startangle=90)
    plt.legend(patches, labels, loc=(-0.05,0.05))
    plt.title('Reaction of ' + searchTerm2 + ' by analyzing ' + str(NoOfTerms) + ' Tweets.')
    plt.axis('equal')
    #plt.tight_layout()
    canvasbar=FigureCanvasTkAgg(fig,master=top)
    canvasbar.draw()
    canvasbar.get_tk_widget().place(x=520,y=110)


def comp():
    global compa
    compa =Toplevel()
    compa.config(background="linen")
    compa.geometry("640x700")
    compa.title("Polarity graph")
    Label(compa,text="Polarity Comparision ",fg="maroon1",bg="linen",font="comicon 28 bold").place(x=170,y=20)
    generate_bar_p()



def generate_bar_p():
        barWidth = 0.25
        fig1 = plt.figure(figsize=(6, 6),dpi=100)

        #data31=['strongly negative','negative','weakly negative','neutral','weakly positive','positive','strongly positive']
        data32= [snegative,negative,wnegative,neutral,wpositive,positive,spositive]
        data33= [snegative2,negative2,wnegative2,neutral2,wpositive2,positive2,spositive2]

        br1 = np.arange(len(data32))
        br2 = [x + barWidth for x in br1]
        plt.bar(br1, data32, color ='r', width = barWidth,
		            edgecolor ='grey', label =searchTerm1)
        plt.bar(br2, data33, color ='g', width = barWidth,
		            edgecolor ='grey', label =searchTerm2)
        plt.xlabel('Polarity', fontweight ='bold', fontsize = 15)
        plt.xticks([r + barWidth for r in range(len(data32))],['strongly\n negative','negative','weakly\n negative','neutral','weakly\n positive','positive','strongly \npositive'])
        plt.legend()
        #plt.show()
        canvasbar=FigureCanvasTkAgg(fig1,master=compa)
        canvasbar.draw()
        canvasbar.get_tk_widget().place(x=20,y=90)
        



        #df3 = pd.DataFrame(
        #                          { 'Polarity' : data31 , 
        #                              'Trend1': data32 , 
        #                              'Trend2': data33})
        #print(df3)
        #ax = plt.gca()

        #df3.plot( x = 'Polarity' , y = 'Trend1', ax = ax )
        #df3.plot( x = 'Polarity' , y = 'Trend2' , ax = ax )
        #plt.show()
    
def generate_line_g():
    fig1 = plt.figure(figsize=(6, 6),dpi=100)
    data31=['HAPPY','SAD','SURPRISE','ANGER','FEAR']
    data311=[1,2,3,4,5]
    data32= [happysum,sadsum,surprisesum,angersum,fearsum]
    data33= [happysum2,sadsum2,surprisesum2,angersum2,fearsum2]
    df3 = pd.DataFrame(
                             { 'Polarity' : data31 , 
                                'dum'    :data311,
                                'Trend1': data32 , 
                                 'Trend2': data33})
    #print(df3)
    plt.plot(df3['Polarity'], df3['Trend1'])
    plt.plot(df3['Polarity'], df3['Trend2'],'-.')
    plt.legend([searchTerm1,searchTerm2])
    canvasbar=FigureCanvasTkAgg(fig1,master=lgraph)
    canvasbar.draw()
    canvasbar.get_tk_widget().place(x=20,y=80)

    #ax = plt.gca()

    #df3.plot( x = 'Polarity' , y = 'Trend1', ax = ax )
    #df3.plot( x = 'Polarity' , y = 'Trend2' , ax = ax )
    #plt.show()

def linegraph():
    global lgraph
    lgraph=Toplevel()
    lgraph.config(background="linen")
    lgraph.geometry("640x700")
    lgraph.title("Line graph of subjectivity")
    Label(lgraph,text="Line graph of subjectivity",fg="maroon1",bg="linen",font="comicon 28 bold").place(x=120,y=20)
    generate_line_g()



def detail_report_p1():
    global report_p1


    report_p1 = Toplevel()
    report_p1.geometry("600x500")
    report_p1.config(background="white")
    #fondoo = PhotoImage(file= r'C:\Users\Pawan Kumar\PycharmProjects\pythonProject1\img\bru.png')
    #background_label = Label(top, image=fondoo)
    #background_label.place(x=0, y=0, relwidth=1, relheight=1)
    report_p1.maxsize(600,500)
    report_p1.minsize(600,500)
    #winsound.PlaySound('C:\\Users\\Pawan Kumar\\PycharmProjects\\pythonProject1\\img\\win2sd.wav',winsound.SND_ALIAS | winsound.SND_ASYNC)
    #top.iconbitmap("C:\\Users\\Pawan Kumar\\PycharmProjects\\pythonProject1\\img\\icoo.ico")
    report_p1.title("Detailed report")
    Label(report_p1, text=" Polarity Analysis of "+searchTerm1, fg="white", bg="gold2", font="Aril 20 bold").place(x=125, y=40)

    
    Label(report_p1,text="positive=  \n\nweakly positive=  \n\nstrongly positive=  \n\nnegative=  \n\nweakly negative=  \n\nstrongly negative=  \n\nneutral=  ",fg="gold2",bg="white",font="comicon 15 bold").place(x=125,y=120)

    get_positive = Entry(report_p1, font="comincon 15 bold", fg="red", bg="white",width =17)
    get_wpositive = Entry(report_p1, font="comicon 15 bold", fg="red", bg="white", width=17)
    get_spositive = Entry(report_p1, font="comicon 15 bold", fg="red", bg="white", width=17)
    get_negative = Entry(report_p1, font="comicon 15 bold", fg="red", bg="white", width=17)
    get_wnegative = Entry(report_p1, font="comicon 15 bold", fg="red", bg="white", width=17)
    get_snegative = Entry(report_p1, font="comicon 15 bold", fg="red", bg="white", width=17)
    get_neutral = Entry(report_p1, font="comicon 15 bold", fg="red", bg="white", width=17)

    get_positive.place(x=300,y=125)
    get_wpositive.place(x=300,y=170)
    get_spositive.place(x=300,y=217)
    get_negative.place(x=300,y=263)
    get_wnegative.place(x=300,y=311)
    get_snegative.place(x=300,y=358)
    get_neutral.place(x=300,y=405)   

    get_positive.insert(0, str(positive))
    get_wpositive.insert(0, str(wpositive))
    get_spositive.insert(0, str(spositive))
    get_negative.insert(0, str(negative))
    get_wnegative.insert(0, str(wnegative))
    get_snegative.insert(0,str(snegative))
    get_neutral.insert(0,str(neutral))

def detail_report_p2():
    global report_p2
    
    report_p2 = Toplevel()
    report_p2.geometry("600x500")
    report_p2.config(background="white")
    #fondoo = PhotoImage(file= r'C:\Users\Pawan Kumar\PycharmProjects\pythonProject1\img\bru.png')
    #background_label = Label(top, image=fondoo)
    #background_label.place(x=0, y=0, relwidth=1, relheight=1)
    report_p2.maxsize(600,500)
    report_p2.minsize(600,500)
    #winsound.PlaySound('C:\\Users\\Pawan Kumar\\PycharmProjects\\pythonProject1\\img\\win2sd.wav',winsound.SND_ALIAS | winsound.SND_ASYNC)
    #top.iconbitmap("C:\\Users\\Pawan Kumar\\PycharmProjects\\pythonProject1\\img\\icoo.ico")
    report_p2.title("Detailed report")
    Label(report_p2, text=" Polarity Analysis of "+searchTerm2, fg="white", bg="gold2", font="Aril 20 bold").place(x=125, y=40)

    
    Label(report_p2,text="positive=  \n\nweakly positive=  \n\nstrongly positive=  \n\nnegative=  \n\nweakly negative=  \n\nstrongly negative=  \n\nneutral=  ",fg="gold2",bg="white",font="comicon 15 bold").place(x=125,y=120)

    get_positive2 = Entry(report_p2, font="comincon 15 bold", fg="red", bg="white",width =17)
    get_wpositive2 = Entry(report_p2, font="comicon 15 bold", fg="red", bg="white", width=17)
    get_spositive2= Entry(report_p2, font="comicon 15 bold", fg="red", bg="white", width=17)
    get_negative2 = Entry(report_p2, font="comicon 15 bold", fg="red", bg="white", width=17)
    get_wnegative2 = Entry(report_p2, font="comicon 15 bold", fg="red", bg="white", width=17)
    get_snegative2 = Entry(report_p2, font="comicon 15 bold", fg="red", bg="white", width=17)
    get_neutral2 = Entry(report_p2, font="comicon 15 bold", fg="red", bg="white", width=17)

    get_positive2.place(x=300,y=125)
    get_wpositive2.place(x=300,y=170)
    get_spositive2.place(x=300,y=217)
    get_negative2.place(x=300,y=263)
    get_wnegative2.place(x=300,y=311)
    get_snegative2.place(x=300,y=358)
    get_neutral2.place(x=300,y=405)   

    get_positive2.insert(0, str(positive2))
    get_wpositive2.insert(0, str(wpositive2))
    get_spositive2.insert(0, str(spositive2))
    get_negative2.insert(0, str(negative2))
    get_wnegative2.insert(0, str(wnegative2))
    get_snegative2.insert(0,str(snegative2))
    get_neutral2.insert(0,str(neutral2))

class SentimentAnalysis:
    

    def __init__(self):
        self.tweets = []
        self.tweetText = []
        
    global df
    global pf
    df = pd.DataFrame()
    pf= pd.DataFrame()
    happysum = 0
    sadsum = 0
    angersum = 0
    surprisesum = 0
    fearsum = 0
    def cleanTweet(self, tweet):
        # Remove Links, Special Characters etc from tweet
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) | (\w +:\ / \ / \S +)", " ", tweet).split())

    # function to calculate percentage
    def percentage(self, part, whole):
        temp = 100 * float(part) / float(whole)
        return format(temp, '.2f')

   

    def DownloadData(self):
        # authenticating
        consumerKey = 'NzlZ7EMQACK3Bd57PciFbDTo4'
        consumerSecret = '41x25GG8MGHcfIMpSF7iP23Jja523Vd7NPU8xfONtJyLcsErcM'
        accessToken = '1385823909434384385-h1uwrt1m7QjkHmO1dRIMTDZmWXo6bL'
        accessTokenSecret = 'llWi3oWxoLvDIDVLiQOqdynTts2Y5lyO6ENkT557Or7Mo'
        auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
        auth.set_access_token(accessToken, accessTokenSecret)
        api = tweepy.API(auth)
        global searchTerm1
        global searchTerm2
        global NoOfTerms
        searchTerm1 = entry_trend1.get()
        searchTerm2 = entry_trend2.get()
        NoOfTerms = int(entry_nooftweets.get())

        # searching for tweets
        self.tweets = tweepy.Cursor(api.search, q=searchTerm1, lang = "en").items(NoOfTerms)
        
               
        global df
        all_tweets=[]
        for tweet in self.tweets:
            all_tweets.append(tweet.text)
        df['Tweet']=all_tweets
        df['Tweet'] = df['Tweet'].apply(cleanUpTweets)
        df = df.drop(df[df['Tweet'] == ''].index)
        df['Subjectivity'] = df['Tweet'].apply(gettextSubjectivity)
       
        
        
        lt = df['Tweet']
        Happy = []
        Sad = []
        Angry = []
        Surprise = []
        Fear = []
        
        for text in lt:
            dict = te.get_emotion(text)
            for key in dict:
                if (key == "Happy"):
                     Happy.append(dict[key])
                elif (key == "Sad"):
                     Sad.append(dict[key])
                elif (key == "Angry"):
                     Angry.append(dict[key])
                elif (key == "Surprise"):
                     Surprise.append(dict[key])
                else:
                     Fear.append(dict[key])
        df['HAPPY'] = Happy
        df['SAD'] = Sad
        df['ANGRY'] = Angry
        df['SURPRISE'] = Surprise
        df['FEAR'] = Fear
        
        global happysum
        happysum = percentagecalculator(Happy)
        global sadsum
        sadsum = percentagecalculator(Sad)
        global angersum
        angersum = percentagecalculator(Angry)
        global surprisesum
        surprisesum = percentagecalculator(Surprise)
        global fearsum
        fearsum = percentagecalculator(Fear)
        total = 0
        totalsum = zip(Happy, Sad, Angry, Surprise, Fear)
        
        for x in totalsum:
            for y in x:
                total = total + y

        
        
        
                  
        # creating some variables to store info
        global  positive
        global  wpositive
        global  spositive
        global  negative
        global  wnegative
        global  snegative
        global  neutral
        polarity = 0
        positive = 0
        wpositive = 0
        spositive = 0
        negative = 0
        wnegative = 0
        snegative = 0
        neutral = 0
         
        self.tweets = tweepy.Cursor(api.search, q=searchTerm1, lang = "en").items(NoOfTerms)   #lets see    
        # iterating through tweets fetched
        for tweet in self.tweets:
            #Append to temp so that we can store in csv later. I use encode UTF-8
            self.tweetText.append(self.cleanTweet(tweet.text).encode('utf-8'))
            #print ('henlo',tweet.text.translate(non_bmp_map))    #print tweet's text
            analysis = TextBlob(tweet.text)
            # print(analysis.sentiment)  # print tweet's polarity
            polarity += analysis.sentiment.polarity  # adding up polarities to find the average later
            
            
            if (analysis.sentiment.polarity == 0):  # adding reaction of how people are reacting to find average later
                neutral += 1
            elif (analysis.sentiment.polarity > 0 and analysis.sentiment.polarity <= 0.3):
                wpositive += 1
            elif (analysis.sentiment.polarity > 0.3 and analysis.sentiment.polarity <= 0.6):
                positive += 1
            elif (analysis.sentiment.polarity > 0.6 and analysis.sentiment.polarity <= 1):
                spositive += 1
            elif (analysis.sentiment.polarity > -0.3 and analysis.sentiment.polarity <= 0):
                wnegative += 1
            elif (analysis.sentiment.polarity > -0.6 and analysis.sentiment.polarity <= -0.3):
                negative += 1
            elif (analysis.sentiment.polarity > -1 and analysis.sentiment.polarity <= -0.6):
                snegative += 1
        


        # finding average of how people are reacting
        positive = self.percentage(positive, NoOfTerms)
        wpositive = self.percentage(wpositive, NoOfTerms)
        spositive = self.percentage(spositive, NoOfTerms)
        negative = self.percentage(negative, NoOfTerms)
        wnegative = self.percentage(wnegative, NoOfTerms)
        snegative = self.percentage(snegative, NoOfTerms)
        neutral = self.percentage(neutral, NoOfTerms)

        # finding average reaction
        polarity = polarity / NoOfTerms


        x=" "
        if (polarity > -0.01 and polarity <= 0.01):
            x="Neutral"
        elif (polarity > 0.01 and polarity <= 0.3):
            x="Weakly Positive"
        elif (polarity > 0.3 and polarity <= 0.6):
            x="Positive"
        elif (polarity > 0.6 and polarity <= 1):
            x="Strongly Positive"
        elif (polarity > -0.3 and polarity <= -0.01):
            x="Weakly Negative"
        elif (polarity > -0.6 and polarity <= -0.3):
            x="Negative"
        elif (polarity > -1 and polarity <= -0.6):
            x="Strongly Negative"
        
        get_x.insert(0,str(x))





        
        self.tweets = tweepy.Cursor(api.search, q=searchTerm2, lang = "en").items(NoOfTerms)
        

          
        global pf
        all_tweets=[]
        for tweet in self.tweets:
            all_tweets.append(tweet.text)
        pf['Tweet2']=all_tweets
        pf['Tweet2'] = pf['Tweet2'].apply(cleanUpTweets)
        pf = pf.drop(pf[pf['Tweet2'] == ''].index)
        pf['Subjectivity2'] = pf['Tweet2'].apply(gettextSubjectivity)
       
        
        
        lt = pf['Tweet2']
        Happy = []
        Sad = []
        Angry = []
        Surprise = []
        Fear = []
        
        for text in lt:
            dict = te.get_emotion(text)
            for key in dict:
                if (key == "Happy"):
                     Happy.append(dict[key])
                elif (key == "Sad"):
                     Sad.append(dict[key])
                elif (key == "Angry"):
                     Angry.append(dict[key])
                elif (key == "Surprise"):
                     Surprise.append(dict[key])
                else:
                     Fear.append(dict[key])
        pf['HAPPY2'] = Happy
        pf['SAD2'] = Sad
        pf['ANGRY2'] = Angry
        pf['SURPRISE2'] = Surprise
        pf['FEAR2'] = Fear
        
        global happysum2
        happysum2 = percentagecalculator(Happy)
        global sadsum2
        sadsum2 = percentagecalculator(Sad)
        global angersum2
        angersum2 = percentagecalculator(Angry)
        global surprisesum2
        surprisesum2 = percentagecalculator(Surprise)
        global fearsum2
        fearsum2 = percentagecalculator(Fear)
        total = 0
        totalsum2 = zip(Happy, Sad, Angry, Surprise, Fear)
        
        for x in totalsum2:
            for y in x:
                total = total + y
        
        happypercent = (happysum2 / total) * 100
        happypercent=round(happypercent,2)
        #print('happy= ',happypercent,'%')
        sadpercent = (sadsum2 / total) *100
        sadpercent=round(sadpercent,2)
        #print('sad= ',sadpercent,'%')
        angerpercent = (angersum2 / total) * 100
        angerpercent=round(angerpercent,2)
        #print('angry= ',angerpercent,'%')
        surprisepercent = (surprisesum2 / total) * 100
        surprisepercent=round(surprisepercent,2)
        #print('surprise= ',surprisepercent,'%')
        fearpercent = (fearsum2 / total) * 100
        fearpercent=round(fearpercent,2)
        #print('fear= ',fearpercent,'%')
        
    
        
                  
        # creating some variables to store info
        global  positive2
        global  wpositive2
        global  spositive2
        global  negative2
        global  wnegative2
        global  snegative2
        global  neutral2
        polarity2 = 0
        positive2 = 0
        wpositive2 = 0
        spositive2= 0
        negative2 = 0
        wnegative2 = 0
        snegative2 = 0
        neutral2 = 0
         
        self.tweets = tweepy.Cursor(api.search, q=searchTerm2, lang = "en").items(NoOfTerms)   #lets see    
        # iterating through tweets fetched
        for tweet in self.tweets:
            #Append to temp so that we can store in csv later. I use encode UTF-8
            self.tweetText.append(self.cleanTweet(tweet.text).encode('utf-8'))
            #print ('henlo',tweet.text.translate(non_bmp_map))    #print tweet's text
            analysis = TextBlob(tweet.text)
            # print(analysis.sentiment)  # print tweet's polarity
            polarity += analysis.sentiment.polarity  # adding up polarities to find the average later
            
            
            if (analysis.sentiment.polarity == 0):  # adding reaction of how people are reacting to find average later
                neutral2 += 1
            elif (analysis.sentiment.polarity > 0 and analysis.sentiment.polarity <= 0.3):
                wpositive2 += 1
            elif (analysis.sentiment.polarity > 0.3 and analysis.sentiment.polarity <= 0.6):
                positive2 += 1
            elif (analysis.sentiment.polarity > 0.6 and analysis.sentiment.polarity <= 1):
                spositive2 += 1
            elif (analysis.sentiment.polarity > -0.3 and analysis.sentiment.polarity <= 0):
                wnegative2 += 1
            elif (analysis.sentiment.polarity > -0.6 and analysis.sentiment.polarity <= -0.3):
                negative2 += 1
            elif (analysis.sentiment.polarity > -1 and analysis.sentiment.polarity <= -0.6):
                snegative2 += 1
        
        # finding average of how people are reacting
        positive2 = self.percentage(positive2, NoOfTerms)
        wpositive2 = self.percentage(wpositive2, NoOfTerms)
        spositive2 = self.percentage(spositive2, NoOfTerms)
        negative2 = self.percentage(negative2, NoOfTerms)
        wnegative2 = self.percentage(wnegative2, NoOfTerms)
        snegative2 = self.percentage(snegative2, NoOfTerms)
        neutral2 = self.percentage(neutral2, NoOfTerms)

        # finding average reaction
        polarity2 = polarity2 / NoOfTerms
        
        y=" "
        if (polarity2 > -0.01 and polarity2 <= 0.01):
            y="Neutral"
        elif (polarity2 > 0.01 and polarity2 <= 0.3):
            y="Weakly Positive"
        elif (polarity2 > 0.3 and polarity2 <= 0.6):
            y="Positive"
        elif (polarity2 > 0.6 and polarity2 <= 1):
            y="Strongly Positive"
        elif (polarity2 > -0.3 and polarity2 <= -0.01):
            y="Weakly Negative"
        elif (polarity2 > -0.6 and polarity2 <= -0.3):
            y="Negative"
        elif (polarity2 > -1 and polarity2 <= -0.6):
            y="Strongly Negative"
        
        get_y.insert(0,str(y))
def correlation():
    global correlationn
    mean_x=(happysum+sadsum+fearsum+surprisesum+angersum)/5
    mean_y=(happysum2+sadsum2+fearsum2+surprisesum2+angersum2)/5

    sum_1=(happysum-mean_x)*(happysum2-mean_y)+(sadsum-mean_x)*(sadsum2-mean_y)+(fearsum-mean_x)*(fearsum2-mean_y)+(surprisesum-mean_x)*(surprisesum2-mean_y)+(angersum-mean_x)*(angersum2-mean_y)
    sum_2=math.sqrt(((happysum-mean_x)**2+(sadsum-mean_x)**2+(fearsum-mean_x)**2+(surprisesum-mean_x)**2+(angersum-mean_x)**2)*((happysum2-mean_x)**2+(sadsum2-mean_x)**2+(fearsum2-mean_x)**2+(surprisesum2-mean_x)**2+(angersum2-mean_x)**2))
    correlationn=sum_1/sum_2
    correlationn=round(correlationn,3)


def subjectivity_cmd():
    global subcmd
    subcmd =Toplevel()
    subcmd.geometry("950x700")
    subcmd.config(background="white")
    #subcmd.iconbitmap("C:\\Users\\Pawan Kumar\\PycharmProjects\\pythonProject1\\img\\icoo.ico")
    subcmd.title("Plots of Subjectivity")
    generate_pie1()
    generate_pie2()
    correlation()
    Label(subcmd,text="CORRELATION OF THE TWO GRAPHS IS: ",font="comicon 20 bold").place(x=100,y=500)
    line_graph=Button(master=subcmd, fg="blue", bg="SpringGreen2",font="comincon 18 bold",command=linegraph,text="Line Graph")
    
    get_correlation= Entry(subcmd, font="comicon 15 bold", fg="red", bg="white", width=17)
    get_correlation.place(x=700,y=500)   
    get_correlation.insert(0, str(correlationn))
    line_graph.place(x=400,y=600)
    







def open():
    global  top
    global  get_x
    global  get_y

    top = Toplevel()
    top.geometry("950x700")
    top.config(background="white")
    #fondoo = PhotoImage(file= r'C:\Users\Pawan Kumar\PycharmProjects\pythonProject1\img\bru.png')
    #background_label = Label(top, image=fondoo)
    #background_label.place(x=0, y=0, relwidth=1, relheight=1)
    #top.maxsize(1000,1000)
    #top.minsize(1000,1000)
    winsound.PlaySound('C:\\Users\\Pawan Kumar\\PycharmProjects\\pythonProject1\\img\\win2sd.wav',winsound.SND_ALIAS | winsound.SND_ASYNC)
    top.iconbitmap("C:\\Users\\Pawan Kumar\\PycharmProjects\\pythonProject1\\img\\icoo.ico")
    top.title("Plots of Sentiment analysis")
    Label(top, text="General Report  :", fg="green", bg="white", font="Aril 15 bold").place(x=50, y=40)
    Label(top, text="General Report  :", fg="green", bg="white", font="Aril 15 bold").place(x=545, y=40)
    get_x = Entry(top, font="comincon 15 bold", fg="red", bg="white",width =17)
    get_y = Entry(top, font="comincon 15 bold", fg="red", bg="white",width =17)
    detail_button1 = Button(master=top,height=1,width=20,command=detail_report_p1,text="More Detailed Report")
    detail_button2= Button(master=top,height=1,width=20,command=detail_report_p2,text="More Detailed Report")
    subjectivity_button=Button(master=top,fg="blue", bg="SpringGreen2",font="comicon 18 bold",command=subjectivity_cmd,text="Subjectivity")
    compare_p_button=Button(master=top, fg="blue", bg="SpringGreen2",font="comincon 18 bold",command=comp,text="Compare Polarity")

    get_x.place(x=230,y=40)
    get_y.place(x=720,y=40)
    detail_button1.place(x=150,y=80)
    detail_button2.place(x=650,y=80)
    subjectivity_button.place(x=150,y=600)
    compare_p_button.place(x=600,y=600)
    sa = SentimentAnalysis()
    sa.DownloadData()
    plotPieChart1()
    plotPieChart2()



if __name__== "__main__":
    gui = Tk()
    fondo = PhotoImage(file= r'C:\Users\Pawan Kumar\PycharmProjects\pythonProject1\img\b7.png')
    background_label = Label(gui, image=fondo)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    gui.geometry("900x463")
    gui.maxsize(900,463)
    gui.minsize(900,463)
    gui.title("Welcome to twitter Sentiment analysis")
    winsound.PlaySound('C:\\Users\\Pawan Kumar\\PycharmProjects\\pythonProject1\\img\\snd.wav', winsound.SND_ALIAS | winsound.SND_ASYNC)
    gui.iconbitmap("C:\\Users\\Pawan Kumar\\PycharmProjects\\pythonProject1\\img\\icoo.ico")
    title = Label(gui, text="Comparing Sentiments of Two Trends", fg="white", bg="pink1", font="comicon 25 bold").place(x=150,y=80)
    account1 = Label(gui, text="Enter the First \n Trend :", fg="red3", bg="white", font="comicon 15 bold").place(x=40,y=155)
    account2 = Label(gui, text="Enter the Second\n Trend :", fg="red3", bg="white", font="comicon 15 bold").place(x=450,y=155)
    entry_trend1 = Entry(gui, font="comicon 15 bold")
    entry_trend2= Entry(gui, font="comicon 15 bold")

    nooftweets = Label(gui, text="Number of Tweets   :", fg="red3", bg="white", font="comicon 15 bold").place(x=220,y=280)
    entry_nooftweets = Entry(gui, font="comicon 13 bold",width=10)
    submit_button = Button(gui, bg="red3",font="comicon 15 bold",borderwidth=3,command=open, height=1, width=4).place(x=385,y=340)
    #login_btn = PhotoImage(file="C:\\Users\\Pawan Kumar\\PycharmProjects\\pythonProject1\\img\\letgobutn4.png")
    #submit_button= Button(gui,text="LEts go", image=login_btn,command=open,borderwidth=2)
    #submit_button.place(x=145,y=220)
    #gui.protocol("WM_DELETE_WINDOW", quitar)

    entry_trend1.place(x=205,y=167)
    entry_trend2.place(x=645,y=167)
    entry_nooftweets.place(x=470,y=284)



    gui.mainloop()

