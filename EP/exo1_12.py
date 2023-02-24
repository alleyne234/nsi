def renverse(mot):
    """Renvoie la chaine en sens inverse
    :mot: str
    @return str
    """
    m_inv = ""
    for l in mot:
        m_inv = l + m_inv
    return m_inv
