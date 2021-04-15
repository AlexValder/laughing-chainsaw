# noinspection PyPep8Naming
def main() -> None:
    tn_1: float = 6.0 * 10**(-2)
    tn_2: float = 3.5 * 10**(-2)
    m1: int = 18
    m2: int = 30
    n1: int = 6
    n2: int = 5
    T: int = 8
    N1: int = 56
    N: int = 126

    Pr_1: float = tn_1 * m1 / T
    Pr_2: float = tn_2 * m2 / T
    Pn_1: float = tn_1 * n1
    Pn_2: float = tn_2 * n2
    P_n1: float = Pn_1 * Pr_1
    P_n2: float = Pn_2 * Pr_2
    Pn2: float = P_n2 + P_n1 - P_n2 * P_n1
    P_nn: float = N1 * Pn2 / N
    print(f'P^r_1 = {Pr_1}')
    print(f'P^r_2 = {Pr_2}')
    print(f'P^n_1 = {Pn_1}')
    print(f'P^n_2 = {Pn_2}')
    print(f'P_n_1 = {P_n1}')
    print(f'P_n_2 = {P_n2}')
    print(f'P_n(2) = {Pn2}')
    print(f'P_nn = {P_nn}')
