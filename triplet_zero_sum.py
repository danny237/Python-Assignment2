"""  Program to find three elements that sum to zero from given list """


class Triplet:
    """
    Class for calculation the three elements sum to zero
    """
    def __init__(self, list1):
        """constructor"""
        self.list1 = list1


    def three_sum(self):
        """function to return the result list"""
        sorted_list = sorted(self.list1)
        new_list = []
        length = len(sorted_list)
        i = 0
        while i < length-2:
            L, R = i + 1, length - 1
            while(L < R):
                if sorted_list[i] + sorted_list[L] + sorted_list[R] == 0:
                    new_list.append([sorted_list[i], sorted_list[L], sorted_list[R]])
                    L, R = L + 1, R - 1
                    while L < R and sorted_list[L] == sorted_list[L - 1]:
                        L += 1
                    while L < R and sorted_list[R] == sorted_list[R + 1]:
                        R -= 1
                if sorted_list[i] + sorted_list[L] + sorted_list[R] < 0:
                    L += 1
                elif sorted_list[i] + sorted_list[L] + sorted_list[R] > 0:
                    R -= 1
            i += 1
            while i < length - 2 and sorted_list[i] == sorted_list[i - 1]:
                i += 1
        return new_list

obj = Triplet([10,-5,0,1,5,4,3,6,-40,-10,3,5])
print(obj.three_sum())