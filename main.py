def formatAs2Decimals(num: float) -> str:
    return "%.2f" % num
    #return "{:.2f}".format(num)

with open('particlearts/2.aff', 'r') as file1:
    with open('particlearts/2edited.aff', 'w') as file2:
        globalTimeFactor = 0.9
        for line in file1.readlines():
            
            if line.startswith('timing'): #当语句为timing语句时候
                line = line.replace('timing', '')
                line = line.replace(';', '')
                
                line = list(eval(line))

                line[0] = int(line[0]//globalTimeFactor) #timing开始时间
                line[1] = formatAs2Decimals((line[1]*globalTimeFactor)) #timing的bpm
                line[2] = "%.2f" % line[2] #timing每小节拍数

                line = 'timing'+str(tuple(line))+';\n'
                line = line.replace("'", "")
                line = line.replace(" ", "")

            elif line.startswith('hold'):#当前note为地面长条
                line = line.replace('hold', '')
                line = line.replace(';', '')
                line = list(eval(line))
                line[0] = line[0]//globalTimeFactor #hold开始时间
                line[1] = line[1]//globalTimeFactor #hold结束时间
                line[2] = line[2] #hold轨道，不动

                #convert everything in the list to int, as the hold notes are int
                for i in range(len(line)):
                    line[i] = int(line[i])

                line = 'hold'+str(tuple(line))+';\n'
                line = line.replace("'", "")
                line = line.replace(" ", "")


            file2.write(line)
            
            

        
        



    
