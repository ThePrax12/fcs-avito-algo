class HashTable:
    """
    Собственная реализация хеш-таблицы на основе списков.

    Атрибуты:
        size (int): количество бакетов в таблице.
        count (int): текущее количество элементов.
        buckets (list[list]): список бакетов, каждый бакет — список пар [key, value].
        _load_factor (float): текущая нагрузка таблицы.

    Методы:
        add(key, value): добавляет пару ключ-значение в таблицу или обновляет значение, если ключ уже существует.
        get(key): возвращает значение по ключу или None, если ключ отсутствует.
        delete(key): удаляет элемент по ключу и возвращает его значение, или None, если ключа нет.
        __len__(): возвращает количество элементов в таблице.
        __str__(): возвращает строковое представление всех пар ключ-значение в таблице.
    """

    def __init__(self, size=16):
        self.size = size
        self.count = 0
        self.buckets = [[] for _ in range(self.size)]
        self._load_factor = 0

    def add(self, key, value, rehash_flg=False):
        """
        Добавляет пару ключ-значение в таблицу.
        Если ключ уже существует, обновляет значение.
        Автоматически выполняет rehash при превышении load factor > 0.7.

        Args:
            key: хешируемый объект, используемый как ключ.
            value: значение, связанное с ключом.
            rehash_flg: флаг того, что сейчас делаем рехеш, чтобы не считать лишнее
        """
        try:
            i = hash(key) % self.size
        except TypeError:
            raise TypeError(f"Ключ {key} не хешируемый")

        for j, el in enumerate(self.buckets[i]):
            if el[0] == key:
                self.buckets[i][j] = [key, value]
                break
        else:
            self.buckets[i].append([key, value])
            if not rehash_flg:
                self.count += 1
                self._load_factor = self.count / self.size
                if self._load_factor > 0.7:
                    self._rehash()

    def _rehash(self):
        """
        Увеличивает размер таблицы в 2 раза и перераспределяет все существующие элементы.
        """
        self.size *= 2
        self.count = 0
        buckets_old = self.buckets
        self.buckets = [[] for _ in range(self.size)]
        for bucket in buckets_old:
            for k, v in bucket:
                self.add(k, v, rehash_flg=True)
        del buckets_old

    def get(self, key):
        """
        Возвращает значение, связанное с ключом.

        Args:
            key: ключ для поиска.

        Returns:
            Значение, связанное с ключом, или None, если ключ отсутствует.
        """
        i = hash(key) % self.size
        for el in self.buckets[i]:
            if el[0] == key:
                return el[1]
        return None

    def delete(self, key):
        """
        Удаляет элемент по ключу.

        Args:
            key: ключ элемента, который нужно удалить.

        Returns:
            Значение удалённого элемента, или None, если ключа нет.
        """
        i = hash(key) % self.size
        for j, el in enumerate(self.buckets[i]):
            if el[0] == key:
                self.count -= 1
                self._load_factor = self.count / self.size
                return self.buckets[i].pop(j)[1]
        return None

    def __len__(self):
        return self.count

    def __str__(self):
        return str([(k, v) for bucket in self.buckets for k, v in bucket])
