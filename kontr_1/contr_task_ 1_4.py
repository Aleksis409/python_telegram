# задача 4 (контрольная 1)
class FunnyList(list):

    def append(self, element):
        """ метод добавляет элемент в начало списка"""
        super().insert(0, element)

        
# # проверка
# funny_list=FunnyList()
# funny_list.append(10)
# funny_list.append(11)
# funny_list.append(12)
# print(*funny_list)
# print(*sorted(funny_list))
# print(*FunnyList([1,2,3]))