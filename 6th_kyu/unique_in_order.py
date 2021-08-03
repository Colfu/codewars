def unique_in_order(list_of_args):
    """
    Turn a sequence into list without any same value elements next to each other, preserving the original order.

    :param: list_of_args: input is list of arguments, str or int
    :return: final_list_of_items
    """
    # If input is empty, return empty list
    if len(list_of_args) < 1: return []
    else:
        # Setup 1st item to compare 2nd against
        current_item = list_of_args[0]
        final_list_of_items = [list_of_args[0]]
        #  Go through each item, pass if same as current_item, otherwise add to final_list_of_items
        for item in list_of_args[1:]:
            if item == current_item:
                pass
            else:
                final_list_of_items.append(item)
                current_item = item
        return final_list_of_items
