def formatAs2Decimals(num: float) -> str:
    return "%.2f" % num
    #return "{:.2f}".format(num)

def apostropheSpaceRemove(s: str) -> str:
    return (s.replace("'", "")).replace(" ", "")

with open('particlearts/2.aff', 'r') as file1:
    with open('particlearts/2edited.aff', 'w') as file2:
        globalTimeFactor = 0.9
        for line in file1.readlines():

            if line.startswith("AudioOffset"):
                line = "AudioOffset:" + str(int(int(line.split(':')[1]) // globalTimeFactor)) + '\n'

            elif line.startswith('timing'): #当语句为timing语句时候
                line = line.replace('timing', '')
                line = line.replace(';', '')
                
                line = list(eval(line))

                line[0] = int(line[0]//globalTimeFactor) #timing开始时间
                line[1] = formatAs2Decimals((line[1]*globalTimeFactor)) #timing的bpm
                line[2] = formatAs2Decimals(line[2]) #timing每小节拍数

                line = 'timing'+str(tuple(line))+';\n'
                line = apostropheSpaceRemove(line)


            elif line.startswith('hold'):#当前note为地面长条
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

            if line.startswith('arc'): #当语句为arc语句时候
                arctapBool = False

                if 'arctap' in line:
                    arctapBool = True
                else:
                    pass

                line = line.replace('arc', '')
                line = line.replace(';', '')
                line = line.replace('(','').replace(')','')
                line = (line.split(','))
                
                for i in range(0,1+1):
                    line[i] = int(line[i])
                    line[i] = int(line[i]//globalTimeFactor)
                    
                    
                for i in range(2,6+1):
                    if i == 4:
                        pass
                    else:
                        line[i] = float(line[i])
                        line[i] = formatAs2Decimals(line[i])
                    
        
                line[4] = str(line[4])
                line[8] = str(line[8])
                line[9] = str(line[9])
            
                if arctapBool == False:
                    line = 'arc'+str(tuple(line))+';\n'
                else:
                    pass

                
                line = apostropheSpaceRemove(line)

        
            file2.write(line)
            

