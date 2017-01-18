
def assert_valid_dict(to_validate, known_contents={}, known_types={}, excluded_fields=[]):
    """
    Take a dict to_validate and validate all known known + unknown fields,
    while skipping any excluded_fields

    Details of inputs:
      - known_contents is a dict with the exact key/value pairs expected in to_validate
      - known_types is a dict of the exact key combined with the *type* of value that is expected
      - excluded fields is a list of the fields who value type is unknown

    """
    assert type(to_validate) is dict, to_validate
    assert type(known_contents) is dict, known_contents
    assert type(known_types) is dict, known_types
    assert type(excluded_fields) in (list, set, tuple), excluded_fields

    # Be sure we're not missing any fields
    to_validate_keys_set = set(to_validate.keys())
    known_contents_set = set(known_contents.keys())
    unknown_fields_set = set(known_types.keys())
    excluded_fields_set = set(excluded_fields)
    missing_keys_set = to_validate_keys_set - unknown_fields_set - excluded_fields_set - known_contents_set
    if missing_keys_set:
        err_msg = 'Keys for {missing_keys_dict} not in '
        err_msg += 'known_contents keys ({known_contents}), '
        err_msg += 'known_types keys ({known_types}), '
        err_msg += 'nor excluded_fields ({excluded_fields}).'
        err_msg = err_msg.format(
            missing_keys_dict={x: to_validate[x] for x in missing_keys_set},
            known_contents=list(known_contents_set),
            known_types=list(unknown_fields_set),
            excluded_fields=list(excluded_fields_set),
        )
        raise KeyError(err_msg)

    excluded_fields_not_in_original_dict = excluded_fields_set - to_validate_keys_set
    if excluded_fields_not_in_original_dict:
        err_msg = '{} not in {}'.format(excluded_fields_not_in_original_dict, excluded_fields)
        raise KeyError(err_msg)

    # Be sure every field we're expecting we get back correctly
    for known_field_to_return, known_value_to_return in known_contents.items():
        if known_field_to_return not in to_validate:
            err_msg = 'Expected field `{known_field_to_return}` (`{known_value_to_return}`)'
            err_msg += ' not in dict: {to_validate}'
            err_msg = err_msg.format(
                known_field_to_return=known_field_to_return,
                known_value_to_return=known_value_to_return,
                to_validate=to_validate,
            )
            raise KeyError(err_msg)
        if known_value_to_return != to_validate[known_field_to_return]:
            err_msg = 'Expected `{known_value_to_return}` as value for key '
            err_msg += '`{known_field_to_return}` but got `{supplied_dict_field}`'
            err_msg += '\n to_validate: {to_validate}'
            err_msg += '\n known_contents: {known_contents}'
            err_msg = err_msg.format(
                known_value_to_return=known_value_to_return,
                known_field_to_return=known_field_to_return,
                supplied_dict_field=to_validate[known_field_to_return],
                to_validate=to_validate,
                known_contents=known_contents,
            )
            raise ValueError(err_msg)

    # Be sure the fields we don't know are of the correct types
    for field_to_return, field_type in known_types.items():

        # required fields must be a type (TODO: support more general plugins)
        if type(field_type) is not type:
            raise TypeError('{} is not of type'.format(field_type))

        if field_to_return not in to_validate:
            err_msg = '{} not in {}'.format(field_to_return, to_validate)
            raise KeyError(err_msg)

        # Check the type of the field returned
        if type(to_validate[field_to_return]) is not field_type:
            err_msg = '{} is not {}:\n{} in {}'.format(
                type(to_validate[field_to_return]),
                field_type,
                field_to_return,
                to_validate,
            )
            raise ValueError(err_msg)


def assert_valid_fields(dict_to_validate, known_contents={},
                        unknown_contents={}, fields_not_required=[]):
    return assert_valid_dict(
        to_validate=dict_to_validate,
        known_contents=known_fields_dict,
        known_types=unknown_contents,
        excluded_fields=fields_not_required,
    )
