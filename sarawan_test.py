def n_elements(n):
    """
    принимает n - количество элементов последовательности
    """
    start = 1
    seq = ""

    def get_elements(seq, start):
        """
        генерирует последовательность и возвращает n элементов
        последовательности где каждое следующее число numb
        повторяется numb раз: 122333444455555...
        """
        seq += str(start) * start
        if len(seq) >= n:
            return seq[:n]
        return get_elements(seq, start + 1)

    return get_elements(seq, start)


if __name__ == "__main__":
    print(n_elements(5))
