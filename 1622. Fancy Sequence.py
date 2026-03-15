# 1622. Fancy Sequence

# [Hard]

# Write an API that generates fancy sequences using the append, addAll, and multAll operations.

# Implement the Fancy class:

# Fancy() Initializes the object with an empty sequence.
# void append(val) Appends an integer val to the end of the sequence.
# void addAll(inc) Increments all existing values in the sequence by an integer inc.
# void multAll(m) Multiplies all existing values in the sequence by an integer m.
# int getIndex(idx) Gets the current value at index idx (0-indexed) of the sequence modulo 109 + 7. If the index is greater or equal than the length of the sequence, return -1.
 

# Example 1:

# Input
# ["Fancy", "append", "addAll", "append", "multAll", "getIndex", "addAll", "append", "multAll", "getIndex", "getIndex", "getIndex"]
# [[], [2], [3], [7], [2], [0], [3], [10], [2], [0], [1], [2]]
# Output
# [null, null, null, null, null, 10, null, null, null, 26, 34, 20]

# Explanation
# Fancy fancy = new Fancy();
# fancy.append(2);   // fancy sequence: [2]
# fancy.addAll(3);   // fancy sequence: [2+3] -> [5]
# fancy.append(7);   // fancy sequence: [5, 7]
# fancy.multAll(2);  // fancy sequence: [5*2, 7*2] -> [10, 14]
# fancy.getIndex(0); // return 10
# fancy.addAll(3);   // fancy sequence: [10+3, 14+3] -> [13, 17]
# fancy.append(10);  // fancy sequence: [13, 17, 10]
# fancy.multAll(2);  // fancy sequence: [13*2, 17*2, 10*2] -> [26, 34, 20]
# fancy.getIndex(0); // return 26
# fancy.getIndex(1); // return 34
# fancy.getIndex(2); // return 20
 

# Constraints:

# 1 <= val, inc, m <= 100
# 0 <= idx <= 105
# At most 105 calls total will be made to append, addAll, multAll, and getIndex.

# Code: Python 3

# class Fancy:   

#     def __init__(self):
#         self.obj = []

#     def append(self, val: int) -> None:
#         self.obj.append(val)

#     def addAll(self, inc: int) -> None:
#         self.obj = [x+inc for x in self.obj]

#     def multAll(self, m: int) -> None:
#         self.obj = [x*m for x in self.obj]

#     def getIndex(self, idx: int) -> int:
#         MOD = 10**9 + 7
#         if idx > -1 and idx < len(self.obj):
#             return self.obj[idx] % MOD
#         else:
#             return -1

class Fancy:

    def __init__(self):
        self.mod = 10**9 + 7
        self.v = list()
        self.a = [1]
        self.b = [0]

    # fast exponentiation
    def quickmul(self, x: int, y: int) -> int:
        return pow(x, y, self.mod)

    # multiplicative inverse
    def inv(self, x: int) -> int:
        return self.quickmul(x, self.mod - 2)

    def append(self, val: int) -> None:
        self.v.append(val)
        self.a.append(self.a[-1])
        self.b.append(self.b[-1])

    def addAll(self, inc: int) -> None:
        self.b[-1] = (self.b[-1] + inc) % self.mod

    def multAll(self, m: int) -> None:
        self.a[-1] = self.a[-1] * m % self.mod
        self.b[-1] = self.b[-1] * m % self.mod

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.v):
            return -1
        ao = self.inv(self.a[idx]) * self.a[-1]
        bo = self.b[-1] - self.b[idx] * ao
        ans = (ao * self.v[idx] + bo) % self.mod
        return ans

# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)