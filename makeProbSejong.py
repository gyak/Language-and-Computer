file = open("sejong_exam.txt","r")
x = file.read()
words = x.split("\n")
allCount = 0
tagCount = 0
tag = input("</태그> 입력: ")
d = {}
for i in range(0,len(words)):
    temp = words[i].split("\t")
    for j in range(0, len(temp)):
        if(j % 2 == 1):
            temp[j] = temp[j].replace(" ","")
            parts = temp[j].split("+")
            for k in range(0, len(parts)):
                if(tag in parts[k]):
                    tagCount = tagCount + 1
                allCount = allCount + 1
print("찾으려는 tag의 수: {}, 전체 tag의 수: {}". format(tagCount, allCount))
print("해당 tag는 전체 tag에서 {:.3f}%를 차지하고 있습니다.". format((tagCount*100)/allCount))
file.close()
