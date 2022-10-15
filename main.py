def get_costumers_groups(n_customers: int) -> dict:
    """

    :param n_customers: integer number of customers
    :return: dict: key:sum of id, value: list of id's with that sum
    """
    groups = {}
    for id in range(n_customers):
        id_sum = sum(map(int, str(id)))
        if id_sum in groups:
            groups[id_sum].append(id)
        else:
            groups[id_sum] = [id]
    return groups


def get_costumers_groups_for_range(n_customers: int, n_first_id: int) -> dict:
    """

    :param n_customers:  number of customers
    :param n_first_id: id of first customer
    :return: dict: key:sum of id, value: list of id's with that sum
    """
    groups = {}
    for id in range(n_first_id, n_first_id + n_customers):
        id_sum = sum(map(int, str(id)))
        if id_sum in groups:
            groups[id_sum].append(id)
        else:
            groups[id_sum] = [id]
    return groups


if __name__ == "__main__":
    from pprint import pprint

    pprint(get_costumers_groups(100))
    pprint(get_costumers_groups_for_range(100, 500))
