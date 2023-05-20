file = open("sejong_exam.txt","r")
x = file.read()
words = x.split("\n")
tag = input("<형태/태그> 입력: ")
d = {}
for i in range(0,len(words)):
    temp = words[i].split("\t")
    for j in range(0, len(temp)):
        if(j%2 == 1):
            temp[j] = temp[j].replace(" ","")
            parts = temp[j].split("+")
            for k in range(0, len(parts)):
                if((i == 0 and j == 0 and k == 0) != 1 and tag in parts[k]):
                    slash = lastParts.find('/')
                    if(slash == 0):
                        partpart[0] = "/"
                        partpart[1] = "SP"
                    else:
                        partpart = lastParts.split("/")
                    target = partpart[1]
                    if(target in d):
                        d[target] = d[target] + 1
                    else:
                        d[target] = 1
                lastParts = parts[k]
lt = d.items()
lt = sorted(d.items(), key=lambda x: (-x[1], x[0]))
print('[{}]에 선행하는 <태그>의 유형별 빈도'. format(tag))
for t in range(0, len(lt)):
    print(lt[t][0], lt[t][1])
file.close()
