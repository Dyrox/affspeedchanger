with open('particlearts/2.aff', 'r') as file1:
    with open('particlearts/2edited.aff', 'w') as file2:
        factor = 0.9
        for line in file1.readlines():
            
            if line.startswith('timing'): #当语句为timing语句时候
                line = line.replace('timing', '')
                line = line.replace(';', '')
                line = list(eval(line))

                line[0] = int(line[0]*factor)
                line[1] = "%.2f" % (line[1]*factor)
                line[2] = "%.2f" % line[2]

                line = 'timing'+str(tuple(line))+';\n'
                line = line.replace("'", "")
                line = line.replace(" ", "")

            elif line.startswith('hold'):#当前note为地面长条


            file2.write(line)
            
            

        
        



    
