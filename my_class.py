class MyList(list):
    def __add__(self: list, other: list) -> list:
        min_len = min(len(self), len(other))
        max_len = max(len(self), len(other))

        result = MyList()

        for i in range(min_len):
            result.append(self[i] + other[i])

        for i in range(min_len, max_len):
            if max_len == len(self):
                result.append(self[i])
            else:
                result.append(other[i])

        return result

    def __sub__(self: list, other: list) -> list:
        min_len = min(len(self), len(other))
        max_len = max(len(self), len(other))

        result = MyList()

        for i in range(min_len):
            result.append(self[i] - other[i])

        for i in range(min_len, max_len):
            if max_len == len(self):
                result.append(self[i])
            else:
                result.append(0 - other[i])

        return result

    def __lt__(self: list, other: list) -> bool:
        sum_self, sum_other = self.get_sum_self_other(other)
        return sum_self < sum_other

    def __le__(self: list, other: list) -> bool:
        sum_self, sum_other = self.get_sum_self_other(other)
        return sum_self <= sum_other

    def __eq__(self: list, other: list) -> bool:
        sum_self, sum_other = self.get_sum_self_other(other)
        return sum_self == sum_other

    def __ne__(self: list, other: list) -> bool:
        sum_self, sum_other = self.get_sum_self_other(other)
        return sum_self != sum_other

    def __gt__(self: list, other: list) -> bool:
        sum_self, sum_other = self.get_sum_self_other(other)
        return sum_self > sum_other

    def __ge__(self: list, other: list) -> bool:
        sum_self, sum_other = self.get_sum_self_other(other)
        return sum_self >= sum_other

    def get_sum_self_other(self: list, other: list) -> tuple:
        sum_self = 0
        sum_other = 0

        for i in self:
            sum_self += i

        for i in other:
            sum_other += i

        return sum_self, sum_other
