from random import randint

def test_tri():
    """Test la fonction tri
    @return (bool)
    """
    l1 = [randint(0,100) for _ in range(10)]
    l2 = l1[:]
    l3 = tri(l1)
    for i in range(len(l3) - 1):
        assert l3[i] <= l3[i + 1], "La liste n'est pas correctement triée"
    for nb in l3:
        assert nb in l2, "Les valeurs ne sont pas identiques"
    return True
