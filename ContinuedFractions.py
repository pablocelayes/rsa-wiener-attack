'''
Created on Dec 14, 2011

@author: pablocelayes
    
'''
# Types
CFListT = list[int]  # CF coefficients
CVListT = list[tuple[int, int]]  # Convergents at each coefficient level

def rational_to_contfrac(x: int, y: int) -> tuple[CFListT, CVListT]:
    """
    Converts a rational x/y fraction into
    a list of partial coefficients [a0, ..., an], and
    a list of convergents at each coefficient level [(n0, d0), (n1, d1), ...]

    The algorithm of computing the convergents from left to right is available
    in Section 9.1 of https://r-knott.surrey.ac.uk/Fibonacci/cfINTRO.html#CFtofract

    Args:
        x (int): numerator of the given rational number
        y (int): denominator of the given rational number

    Returns:
        tuple[CFListT, CVListT]: a tuple of coefficients and convergents at each
        coefficient level
    """
    a = x // y
    cflist = [a]
    cvlist = [(a, 1)]
    ppn, ppd = 1, 0  # pre-pre numerator and denominator of convergent
    pn, pd = a, 1  # pre numerator and denominator of convergent
    while a * y != x:
        x, y = y, x - a * y
        a = x // y
        cflist.append(a)
        cn, cd = a * pn + ppn, a * pd + ppd
        cvlist.append((cn, cd))
        ppn, ppd = pn, pd
        pn, pd = cn, cd
    return cflist, cvlist
