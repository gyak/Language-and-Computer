#소나기 텍스트를 "소녀"를 "소년으로, "소년"을 "소녀"로 바꿔 출력하라
#단, 소년, 소녀 뒤에 붙는 조사들도 이에 알맞게 바꿔야 한다.
file = open("sonagi.txt","r")
x = file.read()
words = x.split("\n")
i = 0
while(1):
    if(("소년" in words[i]) or ("소녀" in words[i])):
        words[i] = words[i].replace("소년이", "@@가")
        words[i] = words[i].replace("소년을", "@@를")        
        words[i] = words[i].replace("소년은", "@@는")        
        words[i] = words[i].replace("소년과", "@@와")
        words[i] = words[i].replace("소년", "@@")
        words[i] = words[i].replace("소녀가", "!!이")
        words[i] = words[i].replace("소녀를", "!!을")        
        words[i] = words[i].replace("소녀는", "!!은")        
        words[i] = words[i].replace("소녀와", "!!과")
        words[i] = words[i].replace("소녀", "!!")
        words[i] = words[i].replace("@@", "소녀")
        words[i] = words[i].replace("!!", "소년")        
    print(words[i])
    i = i + 1
    if (i == len(words)):
        break
    
