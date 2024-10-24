# function to check the given date is a valid one or not
def compare_dates(y, m, d, given_date):
    given_date = [int(x) for x in given_date]
    if given_date[0] >= y:
        if given_date[0] == y:
            if given_date[1] >= m:
                if given_date[1] == m:
                    if given_date[2] > d:
                        return True
                    return False
                return True
            return False
        return True
    return False