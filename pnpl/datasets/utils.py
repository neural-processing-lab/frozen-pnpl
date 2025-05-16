import warnings


def check_include_and_exclude_ids(include_ids, exclude_ids, all_ids):
    if (set(include_ids) & set(exclude_ids)):
        raise ValueError(
            f"IDs cannot be both included and excluded: {set(include_ids) & set(exclude_ids)}")
    if (set(exclude_ids) - set(all_ids)):
        warnings.warn(
            f"Trying to exclude subjects that are not part of the dataset: {set(exclude_ids) - set(all_ids)}")


def include_exclude_ids(include_ids, exclude_ids, all_ids):
    if include_ids:
        ids = include_ids
    else:
        ids = all_ids
    if exclude_ids:
        ids = [id for id in ids if id not in exclude_ids]
    return ids
