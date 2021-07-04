# import numpy as np

# # rng = np.random.RandomState(1)
# # X = np.sort(5 * rng.rand(80, 2), axis=0)		#4 hang, moi hang co 2 cot
# # print(X)
# # y = np.sin(X).ravel()   #ravel(): tat ca cac gia tri se duoc dc ve mang 1 chieu
# # y[::5] += 3 * (0.5 - rng.rand(16))

# A = np.array([[1,2],[3,4],[5,6],[7,8], [9,10], [2,1],[4,3],[6,5]])
# # B = [1,2,3,4,5,6,7,8,9]
# # print(A[::1])
# print(A)
# print(A[:, 0])
# # A.sort()
# sorted_list = sorted(A, key=lambda x:x[0])
# B = np.stack( sorted_list, axis=0 )
# print(B)


# def breadth_first_search_graph(problem):
#     "[Figure 3.11]"
    
#     # we use these two variables at the time of visualisations
#     iterations = 0
#     all_node_colors = []
#     node_colors = {k : 'white' for k in problem.graph.nodes()}
    
#     node = Node(problem.initial)
    
#     node_colors[node.state] = "red"
#     iterations += 1
#     all_node_colors.append(dict(node_colors))
      
#     if problem.goal_test(node.state):
#         node_colors[node.state] = "green"
#         iterations += 1
#         all_node_colors.append(dict(node_colors))
#         return(iterations, all_node_colors, node)
    
#     frontier = deque([node])
    
#     # modify the color of frontier nodes to blue
#     node_colors[node.state] = "orange"
#     iterations += 1
#     all_node_colors.append(dict(node_colors))
        
#     explored = set()
#     while frontier:
#         node = frontier.popleft()
#         node_colors[node.state] = "red"
#         iterations += 1
#         all_node_colors.append(dict(node_colors))
        
#         explored.add(node.state)     
        
#         for child in node.expand(problem):
#             if child.state not in explored and child not in frontier:
#                 if problem.goal_test(child.state):
#                     node_colors[child.state] = "green"
#                     iterations += 1
#                     all_node_colors.append(dict(node_colors))
#                     return(iterations, all_node_colors, child)
#                 frontier.append(child)

#                 node_colors[child.state] = "orange"
#                 iterations += 1
#                 all_node_colors.append(dict(node_colors))
                    
#         node_colors[node.state] = "gray"
#         iterations += 1
#         all_node_colors.append(dict(node_colors))
#     return None



# all_node_colors = []
# romania_problem = GraphProblem('Arad', 'Bucharest', romania_map)
# display_visual(romania_graph_data, user_input=False, 
#                algorithm=breadth_first_search_graph, 
#                problem=romania_problem)

from PIL import Image, ImageDraw, ImageFilter
import cv2
# ROI_195.jpg
im1 = Image.open('ROI_195.jpg').crop((120, 160, 173, 265))
img = cv2.imread("ROI_195.jpg")[160:265, 120:173]
# area = (160, 120, (265-160), (173-120))
im = im1.crop((120, 160, 173, 265))
# img2 = img.paste(img1, (108, 169))
# img.format = "PNG"
im1.show()
cv2.imshow('adv',img)
cv2.waitKey()