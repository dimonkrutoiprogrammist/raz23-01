def gas_station(dis, gas): 
    #Функция для возврата списка индексов заправок, где нужно заправиться
    """
    dis - расстояния между заправками
    gas - Ход на полном баке
    """
    n = len(dis) 
    fuel = gas 
    stops = [] 

    # Координаты
    coord = [0]
    for d in dis:
        coord.append(coord[-1] + d)

    #Вывод
    print("=" * 60)
    print("Маршрут СПБ - Москва")
    print("==" * 60)
    print(f"Общее расстояние: {coord[-1]} km")
    print(f"Запас хода на полном баке: {gas} km")
    print("\nКоординаты заправок от Петербурга - ")

    for i, c in enumerate(coord):
        if i == 0:
            print(f"  Петербург: {c} km")
        elif i == len(coord) - 1:
            print(f"  Москва: {c} km")
        else:
            print(f"  Заправка {i}: {c} km")

    print("\n" + "==" * 60)
    print("Начало поездки из СПБ до МоСК")
    print("==" * 60)

    pos = 0  #Текущ
    i = 0  #nomer

    while i < n:    
        #Цикл        
        to_next = dis[i]    
        #Расстояние

        print(f"\nПозиция: {pos} km")
        print(f"До следующей точки: {to_next} km")      
        print(f"Остаток топлива: {fuel} km")

       
        if to_next > fuel:
            print(f"Мало топлива! Нужна заправка.")

            # Заправка
            if pos > 0:  
                stops.append(i)  #nomer 
                fuel = gas
                print(f"Заправляемся на заправке №{i}")
                print(f"Бак заполнен до {fuel} km")
            else:   #Иначе
                print("Уже заправлены в SPB")
                
                if to_next > gas: 
                    return "Нету машрута!"

       
        fuel -= to_next 
        pos += to_next  
        i += 1  

    print("\n" + "==" * 60)
    print("В МСК!")
    print("==" * 60)

    return stops



dis = [200, 150, 300, 250, 100]
gas = 400   


result = gas_station(dis, gas)
#Вывод
print(f"\nНужно заправиться на заправках: {[x + 1 for x in result]} (нумерация с 1)")
print(f"Всего заправок: {len(result)}")

