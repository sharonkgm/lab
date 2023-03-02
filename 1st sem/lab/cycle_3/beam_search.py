from numpy import array
#function for beam 
def beam_search(distances, beta):
    paths_so_far = [[list(), 0]]
    for index, tier in enumerate(distances):
        if index > 0:
            print(f'Paths kept after tier {index-1}:')
            print(*paths_so_far, sep='\n')
        paths_at_tier = list()
        for i in range(len(paths_so_far)):
            path, distance = paths_so_far[i]
            for j in range(len(tier)):
                path_appended = [path + [j], distance + tier[j]]
                paths_at_tier.append(path_appended)
        paths_sorted = sorted(paths_at_tier, key=lambda element: element[1])
        paths_so_far = paths_sorted[:beta]
        print(f'\nPaths pruned after tier {index}: ')
        print(*paths_sorted[beta:], sep='\n')
        
    return paths_so_far


# Define a distance matrix 
distance = [[0, 4, 1, 3, 8],
         [9, 2, 5, 8, 6]]
distance = array(distance)
best_beta_paths = beam_search(distance, 3)
print('\nThe best beta paths:')
for beta_path in best_beta_paths:
    print(beta_path)