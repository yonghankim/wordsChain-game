print("Loading Word Chain Game ...")

import time, sys
from utils import humanEg, computerEg, defaultEg

dicData = [] #사전목록
useData = [] #이미사용된 단어 저장
time.sleep(1)

try:
    f = open("db/word_dictionary_kor.txt","r")
except:
    print("[Error] word_dictionary_kor.txt file not found")
    print("[Fail] Loading word_dictionary_kor.txt")
    time.sleep(3)
    sys.exit()

while True:
    data = f.readline().rstrip('\r\n')
    dicData.append(data)
    if data == "":
        break

#스타트 엔진
print("Please enter a word")
lastChar = ""
f = open("db/word_dictionary_kor.txt","r")

while True:
    hmWord = humanEg.humanInput(lastChar) #사람이 단어를 입력함
    hmWord = humanEg.humanConnectChar(hmWord,lastChar) #사람이 입력 한 단어를 가공함
    hmCanUse = humanEg.humanWordDefine(hmWord,dicData) #사람이 입력한 단어가 있는지 확인

    if hmCanUse:
        #word_dictionary_kor DB에 구성되지 않은 단어 일 경우, add_words DB 추가
        print("[Error] word_dictionary_kor db에 구성되지 않은 단어입니다.")
        print("'{}'가 추가되었습니다.".format(hmWord))
        f = open("db/add_words.txt", 'a')
        f.write(hmWord + '\n')
        f.close()
        continue
    isuse = humanEg.humanUseWord(hmWord,useData)

    if isuse:
        continue
    else:
        useData.append(hmWord)

    #사람이 입력할것이 완료됨
    #컴퓨터의 시작
    lastChar = defaultEg.getLastChar(hmWord)
    comWord = computerEg.useWord(lastChar,dicData)
    if comWord == []:
        print("[Error] word_dictionary_kor db에 구성된 단어가 없을 경우 종료됩니다.")
        time.sleep(3)
        print("Ending Word Chain Game ...")
        time.sleep(1)
        sys.exit()

    comWord = computerEg.useAgain(comWord,useData)

    if comWord == []:
        print("Word Chain Game Ending...")
        time.sleep(5)
        sys.exit()

    #comWord  변수에 총 사용가능한 단어들이 모여있습니다.
    computerUse = computerEg.selectWord(comWord)
    print("COM : ", computerUse)
    useData.append(computerUse)
    lastChar = defaultEg.getLastChar(computerUse)
