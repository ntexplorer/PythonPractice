# import queue as Q
#
#
# class Skill(object):
#     def __init__(self, priority, description):
#         self.priority = priority
#         self.description = description
#
#     def __lt__(self, other):
#         return self.priority < other.priority
#
#     def __str__(self):
#         return '(' + str(self.priority) + ',\'' + self.description + '\')'
#
#
# def PriorityQueue_class():
#     que = Q.PriorityQueue()
#     que.put(Skill(7, 'proficient7'))
#     que.put(Skill(5, 'proficient5'))
#     que.put(Skill(6, 'proficient6'))
#     que.put(Skill(10, 'expert'))
#     que.put(Skill(1, 'novice'))
#     print('end')
#     while not que.empty():
#         print(que.get())
#
#
# PriorityQueue_class()
#
# '''
# 当队列的元素是自定义时，需要我们在元素的类中定义出比较规则
# '''


# def a(input):
#     if input:
#         return True
#     else:
#         return False
#
#
# print(a(1))
#

# import re
#
# input = "aA1234"
# __valid_count = 0
# __upper = re.compile(r'[A-Z]+')
# __lower = re.compile(r'[a-z]+')
# __number = re.compile(r'[0-9]+')
# __special = re.compile(r'[*&#@_-]+')
# x = __upper.search(input)
# y = __lower.search(input)
# z = __number.search(input)
# w = __special.search(input)
# if x:
#     __valid_count += 1
#     print(x)
#
# if y:
#     __valid_count += 1
#     print(y)
#
# if z:
#     __valid_count += 1
#     print(z)
#
# if w:
#     __valid_count += 1
#     print(w)
#
# if __valid_count >= 3:
#     print(True)

print(type(len("-s-s") // 2))
