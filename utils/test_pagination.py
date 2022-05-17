from unittest import TestCase

from utils.pagination import make_pagination_range

'''
    1,2,3,4
    [1],2,3,4
    1,[2],3,4
    2,[3],4,5
    3,[4],5,6
'''


class PaginationTest(TestCase):
    def test_make_pagination_range_returns_a_pagination_range(self):
        # [1] 2 3 4 5 6 7 8 9  10
        # 1 [2] 3 4 5 6 7 8 9  10
        # 2 3 4 5 6 [7] 8 9 10 11
        pagination_list = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=1,
        )
        self.assertEqual([1, 2, 3, 4], pagination_list)

    def test_first_range_is_static_if_current_page_is_less_than_middle_page(self):  # noqa
        # Current page = 1
        # page_range = [1,2,3,4]
        pagination_list = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=1,
        )
        self.assertEqual([1, 2, 3, 4], pagination_list)

        pagination_list = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=7,
        )
        self.assertEqual([6, 7, 8, 9], pagination_list)

        # Current page = 3
        # page_range = [2,3,4,5]
        pagination_list = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=3,
        )
        self.assertEqual([2, 3, 4, 5], pagination_list)
