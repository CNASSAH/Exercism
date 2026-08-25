"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*args):
    """Return a list of wagons, given an arbitrary amount of wagon numbers.

    Parameters:
        An arbitrary number of wagon numbers, unpacked.

    Returns:
        list: A list of wagon numbers.
    """
    return list(args)


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    Parameters:
        each_wagons_id (list[int]): The list of wagons.
        missing_wagons (list[int]): The list of missing wagons.

    Returns:
        list[int]: The corrected list of wagons.
    """
    locomotive_idx = each_wagons_id.index(1)
    after_locomotive = each_wagons_id[locomotive_idx + 1:]
    wagons_before_locomotive = each_wagons_id[:locomotive_idx]
    *combined_list, = *[each_wagons_id[locomotive_idx]],  *missing_wagons, *after_locomotive, *wagons_before_locomotive
    return combined_list
    


def add_missing_stops(route, **kwargs):
    """Add missing stops to route dict.

    Parameters:
        route (dict): The dict of routing information.
        (dict): An arbitrary number of stops.

    Returns:
        dict: The updated route dictionary.
    """
    full_itinerary = {}
    stops_list = []
    for value in kwargs.values():
        stops_list.append(value)
    full_itinerary = {**full_itinerary, **route, **{"stops": stops_list}}
    return full_itinerary


def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    Parameters:
        route (dict): The route information.
        more_route_information (dict): The extra route information.

    Returns:
        dict: The extended route information.
    """
    full_extended_route = {**route, **more_route_information}
    return full_extended_route


def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    Parameters:
        wagons_rows (list[list[tuple]]): The list of rows of wagons.

    Returns:
        list[list[tuple]]: the list of rows of wagons.
    """
    return [list(row) for row in zip(*wagons_rows)]
