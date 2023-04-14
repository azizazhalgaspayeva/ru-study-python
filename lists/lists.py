class ListExercise:
    @staticmethod
    def replace(input_list: list[int]) -> list[int]:
        """
        Заменить все положительные элементы целочисленного списка на максимальное значение
        элементов списка.

        :param input_list: Исходный список
        :return: Список с замененными элементами
        """
        res = []
        if input_list:
            maxx = input_list[0]
            for element in input_list:
                if element > maxx:
                    maxx = element               
            res = [maxx if x > 0 else x for x in input_list]
        return res

    @staticmethod
    def search(input_list: list[int], query: int) -> int:
        """
        Реализовать двоичный поиск
        Функция должна возвращать индекс элемента

        :param input_list: Исходный список
        :param query: Искомый элемент
        :return: Номер элемента
        """
        def binary_search(input_list, left, right, query):
            if left > right:
                return -1
            
            mid = (left + right) // 2
            if input_list[mid] == query:
                return mid
            if query < input_list[mid]:
                return binary_search(input_list, left, mid - 1, query)
            else:
                return binary_search(input_list, mid + 1, right, query)
        
        
        left = 0
        right = len(input_list) - 1
        return binary_search(input_list, left, right, query)
