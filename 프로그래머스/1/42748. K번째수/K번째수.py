def solution(array, commands):
    answer = []
    for i in range(0,len(commands)):
        split_array = array[commands[i][0]-1:commands[i][1]]
        split_array.sort()
        print(split_array)
        answer.append(split_array[commands[i][2]-1])
    
    return answer
