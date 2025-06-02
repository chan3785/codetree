m, d = map(int, input().split())

# Please write your code here.
def is_날짜있음(m, d):
    if d > 31 or m > 12:
        return "No"
    if m > 7:
        if m % 2 == 0:
            if d <= 31:
                return "Yes"
        else:
            if d <= 30:
                return "Yes"
    elif m <= 7:
        if m == 2:
            if d <= 28:
                return "Yes"
        elif m % 2 == 0:
            if d <= 30:
                return "Yes"
        else:
            if d <= 31:
                return "Yes"
    return "No"

print(is_날짜있음(m,d))