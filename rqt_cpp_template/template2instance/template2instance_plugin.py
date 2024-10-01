from re import sub
from template2instance import get_license_short_text

def camel_case(s):
    # Use regular expression substitution to replace underscores and hyphens with spaces,
    l = sub(r"(_|-|\.|\+|:|#)+", " ", s).split()
    # For each element in the list, if there is 2 consecutive letters capitalized
    # only capitalize the first one
    res = ""
    for x in l:
        w = ""
        w += x[0].upper()
        for i in range(1, len(x)):
            if i > 0 and x[i].isupper() and x[i-1].isupper():
                w += x[i].lower()
            else:
                w += x[i]
        res += w
    return res

def camel_case_package_name(vars: dict) -> str:
    return camel_case(vars['PACKAGE_NAME'])

def uncapitalize(s):
    return s[0].lower() + s[1:]


def uncapitalized_camel_case_package_name(vars: dict) -> str:
    return uncapitalize(camel_case_package_name(vars))

def upper_case_package_name(vars: dict) -> str:
    return vars['PACKAGE_NAME'].upper()

def current_year(_: dict) -> str:
    from datetime import datetime
    return int(datetime.now().year)


def license_reference(variables: dict) -> str:
    """
    This function returns the license reference for the project.

    Parameters
    ----------
    variables : dict
        The variables of the project
    
    Returns
    -------
    str
        The license reference for the project
    """
    return get_license_short_text(variables["PACKAGE_LICENSE"])
