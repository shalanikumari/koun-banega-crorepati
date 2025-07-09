print("Welcome to KBC!")
questions = [
    ["1. Which programming language was used to craete facebook ?","Python","HTML","Javascript","PHP","C++",4],
    ["2. When is Windows 10 end of support by Microsoft ?","2026 - Nov","2025 - June","2025 - oct","2034 - May","2024 - Dec",3],
    ["3. Which one is not a web browser ?","Chrome","Linux","Firefox","Safari","Edge",2],
    ["4. What is HTTP used for ?","Email","gaming","Coding","Browsing","Calling",4],
    ["5. Which is a social media platform ?","Facebook","Python","ChatGPT","Excel","Capcut",1],
    ["6. Which comapany owns Youtube ?","Meta","Apple","google","Microsoft","Amazon",3],
    ["7. WHat does VPN protects ?","Ads","Privacy","Speed","Viruses","User",2],
    ["8. which is a search engine ?","Bing","Whatsapp","Photoshop","Discord","Copilot",1],
    ["9. What does a firewall do ?","Boost speed","Delete files","Block Access","Open sites","Burn data",3],
    ["10. what is 'WWW' short for ?","World wide web","web world wide","Wonder wide web","World wide well","Wonderfull world's Web",1 ],
    ["11. Which keyboard key is used to refresh ?","Ctrl","R","Esc","F5","/",4],
    ["12. Which device connects to wifi ?","CPU","Router","printer","DVD","TV",2],
    ["13. What is 'Google' knkown as ?","Search engine","Social media","Operating system","Chatbox","Photo Editor",1],
    ["14. Which is a file type for images ?",'PDF',"TXT","JPG","MP4","EXE",3],
    ["15. What is 'CTRL + X' is used for ?","Copy","Cut","Paste","Undo","Redo",2],
    ["16. What is youtube used for ?","VIdeo Sharing","Search engine","Code Editor","Vide Editor",1],   
]
levels = [1000,2000,3000,4000,5000,10000,20000,40000,80000,160000,320000,1250000,2500000,5000000,7500000,10000000,75000000]
money = 0
for i in range(0,len(questions)):
    question = questions[i]
    print("")
    print(question[0])
    print(f"Question for Rs. {levels[i]}")
    print(f"1.{question[1]}   2.{question[2]}")
    print(f"3.{question[3]}   4.{question[4]}")
    reply = int(input("Enter Your Answer 1-4: "))
    if reply == question[-1]:
        print(f"Correct Answer! You won Rs. {levels[i]}")
        if(i == 4):
            money = 1000
        elif (i == 9):
            money = 320000
        elif (i == 14):
            money = 7500000    
        elif (i == 16):
            money = 75000000
    else:
        print(f"The money you are taking home is {money}!")            

