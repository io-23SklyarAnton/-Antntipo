from math import ceil


class PaginationHelper:
    """This class allows to work with pages"""

    @staticmethod
    def page_counting(symbols_len, symbols_per_page):
        return ceil(symbols_len/symbols_per_page)
    def __init__(self, collection, items_per_page):
        self.__collection = collection
        self.__items_per_page = items_per_page
        self.__prop_flag = True

    def item_count(self) -> int:
        return len(self.__collection)

    def page_count(self) -> int:
        return self.page_counting(self.item_count(), self.__items_per_page)

    def page_item_count(self, page_index: int) -> int:

        if not 0 < page_index + 1 <= self.page_count():
            return -1

        # finding out the remainder of symbols
        elif self.item_count() - (page_index * self.__items_per_page) >= self.__items_per_page:
            return self.__items_per_page

        else:
            return self.item_count() - page_index * self.__items_per_page

    def page_index(self, item_index: int) -> int:
        if not 0 <= item_index < self.item_count():
            return -1
        else:
            return int(item_index/self.__items_per_page)