class Solution:
    def reverse(self, x: int) -> int:
        max_ = 2 ** 31 - 1
        min_ = -2 ** 31
        if x < min_:
            return 0
        if x > max_:
            return 0
        list_ = []
        negative_flag = 0 if x > 0 else 1
        x = x if x > 0 else -x
        while x:
            list_.append(x % 10)
            x = x // 10
        sum = 0
        for i in range(len(list_)):
            sum += 10 ** (len(list_) - i - 1) * list_[i]
        sum = -sum if negative_flag else sum
        return sum


if __name__ == '__main__':
    x = 1534236469
    print(Solution().reverse(x))
