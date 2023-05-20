s = input("분석할 문장 입력: ")
rd={'병원':'명','불':'동','날씨':'명','많이':'부','풀리':'동','즐기':'동','묻':'동','선생님':'명','아프':'형','뛰':'동','나':'대관','학교':'명','가':'동','네':'대명','그':'대관','밥':'명','먹':'동','않':'동','이':'관','책':'명','어제':'부','읽':'동','날':'명','뛰어가':'동','어둡':'형','비':'명','오':'동','바람':'명','시원하':'형','불':'동','배':'명','의문':'명','풀리':'동','나':'대','사과':'명','네':'대','좋':'형'}
ad={'아서':'어','니':'어','ㄴ다':'어','ㅂ니다':'어','께':'조','으니':'어','에서부터':'조','부터':'조','은':'조','는':'조','이':'조','가':'조','을':'조','를':'조','지':'어','았':'선어','다':'어','습니다':'어','에서':'조','다가':'어','까지':'조','는데':'어','겠':'선어','었':'선어','게':'어','어서':'어','에':'조','는다':'어'}
words = s.split(" ")
for i in range(0,len(words)):
    print("-------------------------") 
    
   
    if("겼" in words[i]):
        words[i] = words[i].replace("겼","기었")
    elif("녔" in words[i]):
        words[i] = words[i].replace("녔","니었")
    elif("뎠" in words[i]):
        words[i] = words[i].replace("뎠","디었")
    elif("렸" in words[i]):
        words[i] = words[i].replace("렸","리었")
    elif("몄" in words[i]):
        words[i] = words[i].replace("몄","미었")
    elif("볐" in words[i]):
        words[i] = words[i].replace("볐","비었")
    elif("셨" in words[i]):
        words[i] = words[i].replace("셨","시었")
    elif("였" in words[i]):
        words[i] = words[i].replace("였","이었")
    elif("졌" in words[i]):
        words[i] = words[i].replace("졌","지었")
    elif("쳤" in words[i]):
        words[i] = words[i].replace("쳤","치었")
    elif("켰" in words[i]):
        words[i] = words[i].replace("켰","키었")
    elif("텼" in words[i]):
        words[i] = words[i].replace("텼","티었")
    elif("폈" in words[i]):
        words[i] = words[i].replace("폈","피었")
    elif("혔" in words[i]):
        words[i] = words[i].replace("혔","히었")

    if("붑니" in words[i]):
        words[i] = words[i].replace("붑니","불ㅂ니")

    if("간다" in words[i]):
        words[i] = words[i].replace("간다","가ㄴ다")

    if("물으" in words[i]):
        words[i] = words[i].replace("물으","묻")

    if("아파" in words[i]):
        words[i] = words[i].replace("아파","아프아")

    #어근 분리
    for j in range(len(words[i])-1,-1,-1):
        target = words[i][0:j+1]
        if(target in rd):
            print(target+" / "+rd[target])
            break
    last = j

    #어미 분리
    while(last < len(words[i])-1):
        for k in range(len(words[i])-1,last,-1):
            target = words[i][last+1:k+1]
            if(target in ad):
                print(target+" / "+ad[target])
                break
        last = k
