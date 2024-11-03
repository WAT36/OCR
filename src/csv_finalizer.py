import sys
import os
import re

args = sys.argv

if len(args) != 3:
    print("Error: Usage: {0} (Input csv file) (Output csv file)".format(args[0]))
    sys.exit(1)

input_csv_file = args[1]
output_csv_file = args[2]

if(not os.path.isfile(input_csv_file)):
    print("Error: {0} is not found.".format(input_csv_file))
    sys.exit(1)

output_txt = []
# reading left file
index=1
with open(input_csv_file) as f:
    for line in f:
        #csvデータをバラす(この時点では問題文,選択肢1,選択肢2,選択肢3,選択肢4,答え(仮で@),解説)
        csv_data=line.split(',')
        # 答え更新されていなかったら終了
        if(len(csv_data)<7):
            print("Error: Csv line data is not formatted. {0}:{1}".format(index,csv_data))
            sys.exit(1)
        if(csv_data[5]=='@'):
            print("Error: Answer is not renewed. {0}".format(csv_data))
            sys.exit(1)
        #答えの記号からcsvデータを書き換える
        #解説　正解の場合は書き換えず消した方が良さげ？？
        if(csv_data[5]=='A'):
            csv_data.pop(5)
            csv_data[-1]=csv_data[-1].replace('(A)',' ').replace('(A',' ').replace('A)',' ').replace('(B)',r'{d1} ').replace('(B',r'{d1} ').replace('B)',r'{d1} ').replace('(C)',r'{d2} ').replace('(C',r'{d2} ').replace('C)',r'{d2} ').replace('(D)',r'{d3} ').replace('(D',r'{d3} ').replace('D)',r'{d3} ')
        elif(csv_data[5]=='B'):
            csv_data.pop(5)
            answer=csv_data.pop(2)
            csv_data.insert(1,answer)
            csv_data[-1]=csv_data[-1].replace('(B)',' ').replace('(B',' ').replace('B)',' ').replace('(A)',r'{d1} ').replace('(A',r'{d1} ').replace('A)',r'{d1} ').replace('(C)',r'{d2} ').replace('(C',r'{d2} ').replace('C)',r'{d2} ').replace('(D)',r'{d3} ').replace('(D',r'{d3} ').replace('D)',r'{d3} ')
        elif(csv_data[5]=='C'):
            csv_data.pop(5)
            answer=csv_data.pop(3)
            csv_data.insert(1,answer)
            csv_data[-1]=csv_data[-1].replace('(C)',' ').replace('(C',' ').replace('C)',' ').replace('(A)',r'{d1} ').replace('(A',r'{d1} ').replace('A)',r'{d1} ').replace('(B)',r'{d2} ').replace('(B',r'{d2} ').replace('B)',r'{d2} ').replace('(D)',r'{d3} ').replace('(D',r'{d3} ').replace('D)',r'{d3} ')
        elif(csv_data[5]=='D'):
            csv_data.pop(5)
            answer=csv_data.pop(4)
            csv_data.insert(1,answer)
            csv_data[-1]=csv_data[-1].replace('(D)',' ').replace('(D',' ').replace('D)',' ').replace('(A)',r'{d1} ').replace('(A',r'{d1} ').replace('A)',r'{d1} ').replace('(B)',r'{d2} ').replace('(B',r'{d2} ').replace('B)',r'{d2} ').replace('(C)',r'{d3} ').replace('(C',r'{d3} ').replace('C)',r'{d3} ')
        else:
            print("Error: Answer is not inproper value. {0}".format(csv_data[5]))
            sys.exit(1)
        # 問題ファイルIDを先頭に添える
        csv_data.insert(0,'8')
        output_txt.append(','.join(csv_data))
        index+=1

# csvファイルに書き込み(問題文,答え文,ダミー選択肢1,ダミー選択肢2,ダミー選択肢3,解説)
with open(output_csv_file, mode='w') as f:
    f.write(''.join(output_txt))



