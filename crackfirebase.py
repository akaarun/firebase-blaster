import names
import urllib3
from py_random_words import RandomWords
import random
import subprocess
import sys


subprocess.run('cls',shell=True)


def sendrequest(url):
    try: 
        http = urllib3.PoolManager()
        url_response = http.request('GET',url)
        url_response_status = url_response.status
        return url_response_status
    except KeyboardInterrupt:
        sys.exit()
   

def withwordlist(wordlist):
    try:
        with open(wordlist, "r") as a_file:
                for line in a_file:
                    stripped_line = line.strip()
                    lower_case_word = stripped_line.lower()
                    addingurl = "https://"+lower_case_word+"."+"firebaseio.com/.json"
                    start_func = sendrequest(addingurl)
                    try: 
                        if start_func == 200:
                        # newfile = open("writefirebase.txt","a")
                        # newfile.write(addingurl)
                            print("  "+addingurl)
                            vulnerable_df = open("Firebase_Vulnerable_database.txt","a")
                            vulnerable_df.write(addingurl+"\n")
                    except KeyboardInterrupt:
                        sys.exit()
    except:
        pass                
    
                

def  withoutwordlist():
        try:
            while True:
                real_names = names.get_first_name()
                lowercase_real_name = real_names.lower()
                rnd_word = RandomWords()
                real_rnd_word = rnd_word.get_word()
                atuple = (real_rnd_word,lowercase_real_name)
                choosingrandom = random.choice(atuple)
                addingurl = "https://"+choosingrandom+"."+"firebaseio.com/.json"
                start_func = sendrequest(addingurl)
                try: 
                    if start_func == 200:
                        print("  "+addingurl)
                        vulnerable_df = open("Firebase_Vulnerable_database.txt","a")
                        vulnerable_df.write(addingurl+ "\n")
                    # else:
                    #     print(addingurl)
                except:
                    pass
        except:
            pass       




print('\n')
print('                              |=== ==|==  |\\   |===  |\\     /\\    ---- |===    |\\   |         /\\    ----  =====  |===  |\\')
print('                              |===   |    | \\  |===  |/    /  \\   \\    |===    |/   |        /  \\   \\       |    |===  | \\')
print('                              |      |    |/   |     |\\   /___ \\   \\   |       |\\   |       /___ \\   \\      |    |     |/')
print('                              |    ==|==  |\\   |===  |/  /      \\ _/   |===    |/   |____  /      \\ _/      |    |===  |\\')


print('\n')
print('                                         Made By')
print('                                                 /\\   |\\   |   |  |\\   |   ----  ______  |\\   |  |       |  |' )
print('                                                /  \\  |_\\  |   |  | \\  |   \\       ||    | \\  |  |       |__|')
print('                                               /____\\ |\\   |   |  |  \\ |    \\      ||    |  \\ |  | /--|  |  |')
print('                                              /      \\| \\  |___|  |   \\|  __/    ======  |   \\|  |/   |  |  |')





        

print('\n')

print('''  Disclaimer: Usage of Firebase Blaster for attacking databases without prior mutual consent is illegal. 
  It is the end user's responsibility to obey all applicable local, state and federal laws. 
  Developers assume no liability and are not responsible for any misuse or damage caused by this program.''')

print('\n')

print('''  Select Below Options
  1. Use Wordlist.
  2. Without Wordlist.''')
print("\n")
userinput = input("  Select Opition >> ")
print('\n')

if userinput == "1":
    print("  Give Your Wordlist Path")
    wordlist_path_input = input("  >> ")
    print("  Now it is time to hack, it can take some time :)")
    print('\n')
    print('''  Vulnerable Database 
  ||||||||||||||||||
  \/\/\/\/\/\/\/\/\/
''')

    withwordlist(wordlist_path_input)

elif userinput == "2":
    print("  Ok, We are going to hack, it will take some time :)")
    print('\n')
    print('''  Vulnerable Database 
  ||||||||||||||||||
  \/\/\/\/\/\/\/\/\/
''')
    withoutwordlist()
else:
    print("  Please select one options")
    exit



