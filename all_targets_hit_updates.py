def all_targets_hit_upgrade(attempts: list) -> bool:
    return any([any(target) for target in targets_list])


targets_list = [[False], [True, True], [False, True, True]]
print(all_targets_hit_upgrade(targets_list))