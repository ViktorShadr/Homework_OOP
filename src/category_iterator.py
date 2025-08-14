class CategoryIterator:

    def __init__(self, category):
        self._products = category.products_list
        self.index = 0


    def __repr__(self):
        return f"{self.__class__.__name__}({self._products})"


    def __iter__(self):
        return self


    def __next__(self):
        if self.index < len(self._products):
            product = self._products[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration