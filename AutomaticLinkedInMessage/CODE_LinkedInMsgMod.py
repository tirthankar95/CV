import json
import re 

if __name__=='__main__':
    file = open("TXT_LinkedInMsgMod.txt","r")
    file_json = open("JSON_LinkedInMsgMod.json","r")
    data = json.load(file_json)
    replace = {}
    for line in file:
        for word in line.split():
            if word[0] == '<':
                # print(f'KEY[{key}] -> {data[key]}')
                replace[word] = data[word[1:-1]]
    file_json.close()
    file.close()
    file = open("TXT_LinkedInMsgMod.txt","r")
    file_op = open("OP_LinkedInMsgMod.txt", "w")
    print(replace)
    for line in file:
        for k, v in replace.items():
            pattern = f'{k}'
            line = re.sub(pattern, v, line)
        file_op.write(line)
    file.close()
    file_op.close()