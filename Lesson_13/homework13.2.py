
class Mathematician:
    def square_nums(self, nums: list):
        return [item**2 for item in nums]

    def remove_positives(self, nums: list):
        return [item for item in nums if item <= 0]     

    def filter_leaps(self, nums:list):
        def is_leap_year(year):
            return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
        return [item for item in nums if is_leap_year(item)]



m = Mathematician()

assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]
assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]
assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]