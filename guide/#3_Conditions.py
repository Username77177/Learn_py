#Conditions (Условия)

#First Condition IF
#Первое условие IF (если)

#Let's learn it on example
#Давайте выучим что-такое условие if на примере


a = 10
b = 200
#       Операции сравнения
# == - равно (equal)
# != - не равно (not equal)
# > - больше (bigger)
# < - меньше (smaller)
# => - больше или равно (bigger or equal)
# =< - меньше или равно (smaller or equal)

if a>b:        
   
   #if(condition) || if(условие)
    print("This text will not appear, because in our case a<b")
    print("Это сообщение не появится, потому что a<b")

elif b == a:
    print("If if condition false, and condition of elif true, programm will enter in elif(else if)")
    print("Если условие if не подтверждено, а условие elif верно, программа войдет в elif (Остальное если)")

else:
    print("If a not bigger than b, than programm enter in else, if else existing")
    print("Если a не больше чем b, тогда программа войдет в else(остальное), если else вообще существует")

#Else always without condition
#Else всегда без условия

#       Логические операции
#   1. and - возращает True, если оба вырадения равны
if 2 == 2 and 3 == 3:
    print("2 = 2 and 3 = 3")
    