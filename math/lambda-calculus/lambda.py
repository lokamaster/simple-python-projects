# True and false
TRUE = lambda x: lambda y: x
FALSE = lambda x: lambda y: y

# Basic operators
OR = lambda x: lambda y: x(x)(y)
AND = lambda x: lambda y: x(y)(x)

# Derived operators
NOT = lambda x: x(FALSE)(TRUE)
NOR = lambda x: lambda y: NOT(OR(x)(y))
NAND = lambda x: lambda y: NOT(AND(x)(y))
XOR = lambda x: lambda y: x(NOT(y))(y)
XNOR = lambda x: lambda y: NOT(XOR(x)(y))
IMPLICATION = lambda x: lambda y: OR(NOT(x))(y)


def test() -> None:
    # Test OR
    assert OR(FALSE)(FALSE) == FALSE
    assert OR(FALSE)(TRUE) == TRUE
    assert OR(TRUE)(FALSE) == TRUE
    assert OR(TRUE)(TRUE) == TRUE

    # Test AND
    assert AND(FALSE)(FALSE) == FALSE
    assert AND(FALSE)(TRUE) == FALSE
    assert AND(TRUE)(FALSE) == FALSE
    assert AND(TRUE)(TRUE) == TRUE

    # Test XOR
    assert XOR(FALSE)(FALSE) == FALSE
    assert XOR(FALSE)(TRUE) == TRUE
    assert XOR(TRUE)(FALSE) == TRUE
    assert XOR(TRUE)(TRUE) == FALSE

    # Test IMPLICATION
    assert IMPLICATION(FALSE)(FALSE) == TRUE
    assert IMPLICATION(FALSE)(TRUE) == TRUE
    assert IMPLICATION(TRUE)(FALSE) == FALSE
    assert IMPLICATION(TRUE)(TRUE) == TRUE


def main() -> None:
    test()
    print("All test passed!")


if __name__ == "__main__":
    main()

