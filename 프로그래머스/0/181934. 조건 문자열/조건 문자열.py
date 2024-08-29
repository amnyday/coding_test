def solution(ineq, eq, n, m):
    if eq == '!' and (ineq == '<' or ineq == '>'):
        s = ineq
    else:
        s = ineq +eq
        
    if eval(f'{n} {s} {m}'):
        return 1
    else:
        return 0