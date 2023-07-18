class SingleNumber:

    def single_number(self, array):

        result = 0

        for i in range(len(array)):

            result = result ^ array[i]

        return result


object = SingleNumber()
array = list(map(int, input().split()))
print(object.single_number(array))