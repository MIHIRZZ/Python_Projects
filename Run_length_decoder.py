
class Solution:
   def solve(self, s):
      output = ""
      num = ""
      for i in s:
         if i.isalpha():
            output+=i*int(num)
            num=""
         else:
            num+=i
      return output

ob = Solution()
print(ob.solve("4B3A2D1C2B"))
"""
ok so this program is for decoding the run-length encoding

for that in input you have a number (means you need to read that many lines), then lines for each pattern (in these lines you have # or . and some numbers. i.e. # 4 3 5 7 3)
here, each lines summation is same, if it is not same then you need to return "Error decoding image"

for output you need to decode the numbers as following:
# 4 3 5 7 2  =>  ####...#####.......##
. 4 3 5 7 3  =>  ....###.....#######...


"""