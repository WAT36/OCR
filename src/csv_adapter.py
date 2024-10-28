import sys
import os
import re

args = sys.argv

if len(args) != 4:
    print("Error: Usage: {0} (Input left-txt file) (Input right-txt file) (Output csv file)".format(args[0]))
    sys.exit(1)

left_txt_file = args[1]
right_txt_file = args[2]
output_csv_file = args[3]

if(not os.path.isfile(left_txt_file)):
    print("Error: {0} is not found.".format(left_txt_file))
    sys.exit(1)
elif(not os.path.isfile(right_txt_file)):
    print("Error: {0} is not found.".format(right_txt_file))
    sys.exit(1)

empty_phrase = '-{3,20}'

output_txt = []

# reading left file
with open(left_txt_file) as f:
    question={'sentense': '','option':[]}
    sentense = ''
    for line in f:
        if(re.search('-{3,20}',line)):
            # 問題文データを登録
            sentense=line+' '
        elif(re.search(r'\([ABCD]',line)):
            # 選択肢の場合
            question['option'].append(re.sub(r'\([ABCD].* +','',line).replace('\n', ''))
            if re.search(r'\(D',line):
                #  (D)の場合はここで問題データ登録して初期化
                output_txt.append(question['sentense']+','+','.join(question['option']))
                sentense=''
                question={'sentense': '','option':[]}
        elif(line.strip() == ''):
            # 空行の場合
            if sentense != '':
                # 問題文にデータがあるときは問題文を登録
                question['sentense'] = sentense.replace('\n', '')
                sentense = ''
            continue
        else:
            sentense += line + ' '

# reading right file
with open(right_txt_file) as f:
    question_count=0
    statements=[]
    for line in f:
        if(line.strip() == ''):
            if(len(statements)>0):
                #答え,解説　で登録
                output_txt[question_count]=(output_txt[question_count]+(','+statements[0].strip()[-1]+','+''.join(statements[1:]))).replace('\n', '')
                question_count+=1
                statements=[]
        else:
            reline=re.sub(r' ([\(\)a-zA-Z]+)','@\\1',line)
            reline=re.sub(r'([\(\)a-zA-Z]+) ','\\1@',reline)
            reline=reline.replace(' ','').replace('@',' ').replace(',','、')
            statements.append(reline)

# csvファイルに書き込み
with open(output_csv_file, mode='w') as f:
    f.write('\n'.join(output_txt))

