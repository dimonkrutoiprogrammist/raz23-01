def greedy_meetings(meetings):  
    #Функция для выбора максимального количества непересекающихся заседаний
    """
    meetings: список (начало, конец)
    """
   
    sorted_meet = sorted(meetings, key=lambda x: x[1])

    selected = []   
    last_end = -1   

    for start, end in sorted_meet:  
        if start >= last_end:              
            selected.append((start, end))  
            last_end = end

    return selected                         
    #выбранные заседания


meetings = [(9, 10), (10, 12), (11, 13), (12, 14), (13, 15)] #Заседания

#Вывод
print("\nЭвристика: выбор заседаний")
print("Все заседания - ", meetings)
print("Максимум можно посетить:", greedy_meetings(meetings))
