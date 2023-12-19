# n = int(input())
# m = int(input())
# a = []
# for i in range(n):
#     a.append([])
#     for j in range(m):
#         if i == 0 or j ==0:
#             a[i].append(int('1'))
#         else:
#             g = a[i-1][j] + a[i][j-1]
#             a[i].append(g)
#
# for i in range(n):
#     for j in range(m):
#         print(a[i][j], end='\t')
#     print('\n')
