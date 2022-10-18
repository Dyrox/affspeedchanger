import easygui
import os
import shutil
import sox
#import json

def formatAs2Decimals(num: float) -> str:
    return f'{num:.2f}'

def apostropheSpaceRemove(s: str) -> str:
    return (s.replace("'", "")).replace(" ", "")

def lineChangeSpeed(line,globalTimeFactor):
    line = line.strip()
    if line == '-':
        line = line + '\n'

    if line.startswith("AudioOffset"):
        line = "AudioOffset:" + str(int(int(line.split(':')[1]) // globalTimeFactor)) + '\n'

    elif line.startswith('timing') and not 'group' in line: #当语句为timing语句时候
        line = line.replace('timing', '')
        line = line.replace(';', '')
        
        line = list(eval(line))

        line[0] = int(line[0]//globalTimeFactor) #timing开始时间
        line[1] = formatAs2Decimals((line[1]*globalTimeFactor)) #timing的bpm
        line[2] = formatAs2Decimals(line[2]) #timing每小节拍数

        line = 'timing'+str(tuple(line))+';\n'
        line = apostropheSpaceRemove(line)


    elif 'hold' in line:#当前note为地面长条
        line = line.replace('hold', '')
        line = line.replace(';', '')
        line = list(eval(line)) #hold
        line[0] = line[0]//globalTimeFactor #hold开始时间
        line[1] = line[1]//globalTimeFactor #hold结束时间
        line[2] = line[2] #hold轨道，不动

        #convert everything in the list to int, as the hold notes are int
        for i in range(len(line)):
            line[i] = int(line[i])

        line = 'hold'+str(tuple(line))+';\n'
        line = apostropheSpaceRemove(line)
    
    elif line.startswith('('):#当前note为地面tap
        line = line.replace(';', '')
        line = list(eval(line))
        line[0] = line[0]//globalTimeFactor #tap开始时间
        line[1] = line[1] #tap轨道，不动

        for i in range(len(line)):
            line[i] = int(line[i])

        line = str(tuple(line))+';\n'
        line = apostropheSpaceRemove(line)

    elif line.startswith('arc'): #当语句为arc语句时候
        if 'arctap' in line: arctapBool = True
        else: arctapBool = False

        if arctapBool: #把蛇和天键的部分给拆分开来
            arcLine = line[:line.find('[')]
            arcTapLine = line[line.find('['):-1]
        else:
            arcLine = line[:-1]
            arcTapLine = ''
        
        ####蛇处理####
        arcLine = arcLine.replace('arc','').replace('(','').replace(')','').replace(';','')
        arcLine = (arcLine.split(','))
        for i in range(0,1+1): #蛇起始结束时间, in ms
            arcLine[i] = int(arcLine[i])
            arcLine[i] = int(arcLine[i]//globalTimeFactor)

        for i in range(2,6+1): #蛇x1,x2,y1,y2坐标
            if i == 4:
                pass
            else:
                arcLine[i] = float(arcLine[i])
                arcLine[i] = formatAs2Decimals(arcLine[i])

        arcLine[4] = str(arcLine[4]) #蛇形状, eg: b, s, si so
        arcLine[8] = str(arcLine[8]) #蛇custom hitsound
        arcLine[9] = str(arcLine[9]) #是黑线? bool
        arcLine = 'arc'+str(tuple(arcLine))
        arcLine = apostropheSpaceRemove(arcLine)
        
        ####下面是天键处理####

        arcTapAmount = arcTapLine.count('arctap')#一个蛇中天键个数
        arcTapLine = arcTapLine.replace('[','').replace(']','')
        arcTapLine = arcTapLine.split(',')
        for i in range(arcTapAmount): 
            arcTapLine[i] = int(''.join(filter(str.isdigit,arcTapLine[i])))
            arcTapLine[i] = int(arcTapLine[i] // globalTimeFactor)
            arcTapLine[i] = 'arctap('+ str(arcTapLine[i])+')'

        
        arcTapLine = str(tuple(arcTapLine))
        arcTapLine = arcTapLine[:-1] + ''
        arcTapLine = arcTapLine[1:] + ''
        arcTapLine = apostropheSpaceRemove(arcTapLine)
        arcTapLine = '['+ arcTapLine + '];'

        if arcTapAmount == 1:
            arcTapLine = arcTapLine.replace(',','')
            
        ####蛇和天键合并####

        if arctapBool:
            line = arcLine + arcTapLine + '\n'
        
        else:
            line = arcLine + ';\n'

    elif line.startswith('timinggroup'): #为timinggroup语句
        line = line + '\n'
    elif line == '};':
        line = line + '\n' 

    elif line.startswith('scenecontrol'): #scenecontrol语句
        line = line.replace('scenecontrol', '')
        line = line.replace(';', '')
        line = list(eval(line))

        line[0] = int(line[0]//globalTimeFactor) #timing开始时间
        line[2] = formatAs2Decimals((line[2]//globalTimeFactor)) #timing的bpm

        line = 'scenecontrol'+str(tuple(line))+';\n'
        line = apostropheSpaceRemove(line)
    return line

globalTimeFactor = 0.85

enwidencamera = 'enwidencamera'
enwidenlanes = 'enwidenlanes'
hidegroup = 'hidegroup'

aff_filepath = easygui.fileopenbox()

songid = (aff_filepath.split('/'))[-2]
filename = (aff_filepath.split('/'))[-1]
changedtempo_songid = songid + f'{globalTimeFactor:.2f}'.replace('.','')
newaff_filepath = aff_filepath.replace(songid,songid+'/'+changedtempo_songid)
os.chdir(aff_filepath.replace('/'+filename,''))

if not os.path.exists(changedtempo_songid):
    os.mkdir(changedtempo_songid)

for file in os.listdir():
    if file == 'base.jpg' or file == 'base_256.jpg':
        shutil.copy(file,changedtempo_songid)
    elif file == 'base.ogg':
        sox.Transformer().tempo(globalTimeFactor).build_file('base.ogg', changedtempo_songid + '/' + 'base.ogg')
    elif file.endswith('.wav'):
        sox.Transformer().tempo(globalTimeFactor).build_file(file, changedtempo_songid + '/' + file)


with open(aff_filepath, 'r') as file1:
    with open(newaff_filepath, 'w') as file2:
        
        for line in file1.readlines():

            changedLine = lineChangeSpeed(line,globalTimeFactor)

            file2.write(changedLine)
            

        

