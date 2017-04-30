import urllib.request
import datetime,threading
import xml.etree.ElementTree as ET
import sys


def checking():
    global flag, Curr_pair, target,query,check_high,check_low
    if (flag==1):
        set_values()
        flag=0
    url='http://rates.fxcm.com/RatesXML'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    tree=ET.ElementTree(file=urllib.request.urlopen(req))
    root=tree.getroot()
    #print (root)
    
    print("The current System time is: ",datetime.datetime.now())
    for rate in root:
        sym=rate.get('Symbol')
        b=rate.findtext('Bid')
        bid=float(b)
        dire=rate.findtext('Direction')
        last=rate.findtext('Last')
        # if Curr_pair in sym_list:
        if (sym==Curr_pair):
            if (target==bid):
                    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
                    print("TARGET RATE ACHIEVED")
                    print("Updated at: ",datetime.datetime.now())
                    print("Site Updated at: ",last)
                    print("The current Rate is: ",bid)
                    print("The direction of Bid is ",dire)
                    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
                    print("Press Enter to exit")
                    sys.exit()
                
            elif (target>bid):
                if (check_low==0):             
                    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
                    print("TARGET RATE ACHIEVED")
                    print("Updated at: ",datetime.datetime.now())
                    print("Site Updated at: ",last)
                    print("The current Rate is: ",bid)
                    print("The direction of Bid is ",dire)
                    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
                    print("Press Enter to exit")
                    sys.exit()
                    
                    '''here=True
                    while here:
                        print("Do you want to continue? Enter 'y' for Yes, 'n' for No.")
                        this_query=True
                        query=input().lower()
                        while this_query:
                            if not (query):
                                print("Empty String, Press 'y' for Yes,'n' for No")
                                query=input().lower()
                            
                            else:
                                this_query=False
                                if(query=='y'):
                                    set_flag()
                                    checking()
                                    here=False
                                if(query=='n'):
                                    here=False
                                    exit()
                                else:
                                    print("Invalid Input")'''
                else:
                    check_high=0;
                    print("The current Rate is:",bid)
                    print("Entered Target rate is greater than the Current rate")
                    print("Waiting for Bid to reach Target......")
                    print("=======================================================================")
                    
                threading.Timer(10,checking).start()
            else:
                
                if(check_high==0):
                    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
                    print("TARGET RATE ACHIEVED")
                    print("Updated at: ",datetime.datetime.now())
                    print("Site Updated at: ",last)
                    print("The current Rate is: ",bid)
                    print("The direction of Bid is ",dire)
                    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
                    print("Press Enter to exit")
                    sys.exit()
                    '''here=True
                    while here:
                        print("Do you want to continue? Enter 'y' for Yes, 'n' for No.")
                        this_query=True
                        query=input().lower()
                        while this_query:
                            if not (query):
                                print("Empty String, Press 'y' for Yes,'n' for No")
                                query=input().lower()
                            
                            else:
                                this_query=False
                                if(query=='y'):
                                    set_flag()
                                    checking()
                                    here=False
                                if(query=='n'):
                                    here=False
                                    exit()
                                else:
                                    print("Invalid Input")'''
                else:
                    check_low=0;
                    print("The current Rate is:",bid)
                    print("Entered Target rate is less than the Current rate")
                    print("Waiting for Bid to reach Target......")
                    print("=======================================================================")
                   
                threading.Timer(10,checking).start()

def set_flag():
    global flag ,Curr_pair,target,query,check_high,check_low
    check_high=1
    check_low=1
    flag = 1
    Curr_pair=''
    target=0
    query=''


def check_pair():
    url='http://rates.fxcm.com/RatesXML'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    tree=ET.ElementTree(file=urllib.request.urlopen(req))
    root=tree.getroot()
    #print (root)
    global Curr_pair
    sym_list=[]
    for rate in root:
        sym=rate.get('Symbol')
        sym_list.append(sym.upper())
    
    if Curr_pair in sym_list:
        return True
    else:
        return False

def set_values():
    global Curr_pair
    global target
    #Curr_pair="GBPNZD"   # HARD coded for now
    #target="1.82798"
    print("Enter the Currency Pair:")
    Curr_pair=input().upper()
    this_curr=True
    while this_curr:
        if not (Curr_pair):
            print("Empty String, Enter Currency Pair:")
            Curr_pair=input().upper()
        else:
            if(check_pair()):
                print("Currency Pair:",Curr_pair)
                this_curr=False
            else:
                print("Invalid Currency pair, Enter Currency Pair:")
                Curr_pair=input().upper()
    
    print("Enter the Target Rate:")
    
    this_tar=True
    tar=input()
    while this_tar:
        if not (tar):
            print("Empty String, Enter Target Rate:")
            tar=input()
        else:
            try:
                target=float(tar)
                this_tar=False
                print("Target Rate:",target)
            except ValueError:
                print("Please enter a valid float value")
                tar=input()






print("Welcome...")
set_flag()
checking()
