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
        self.assertEqual([1, 2, 3, 4], pagination_list['pagination'])

    def test_first_range_is_static_if_current_page_is_less_than_middle_page(self):  # noqa
        # Current page = 1
        # page_range = [1,2,3,4]
        pagination_list = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=1,
        )
        self.assertEqual([1, 2, 3, 4], pagination_list['pagination'])

        pagination_list = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=7,
        )
        self.assertEqual([6, 7, 8, 9], pagination_list['pagination'])

        # Current page = 3
        # page_range = [2,3,4,5]
        pagination_list = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=3,
        )
        self.assertEqual([2, 3, 4, 5], pagination_list['pagination'])

        # Current page = 17
        # page_range = [16, 17, 18, 19]
        pagination_list = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=17,
        )
        self.assertEqual([16, 17, 18, 19], pagination_list['pagination'])

        # Current page = 19
        # page_range = [17, 18, 19, 20]
        pagination_list = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=19,
        )
        self.assertEqual([17, 18, 19, 20], pagination_list['pagination'])

        # Current page = 20
        # page_range = [17, 18, 19, 20]
        pagination_list = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=20,
        )
        self.assertEqual([17, 18, 19, 20], pagination_list['pagination'])

    def test_make_pagination_range_is_static_when_last_page_is_next(self):  # noqa
        # Current page = 19
        # page_range = [17, 18, 19, 20]
        pagination_list = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=18,
        )
        self.assertEqual([17, 18, 19, 20], pagination_list['pagination'])

        # Current page = 19
        # page_range = [17, 18, 19, 20]
        pagination_list = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=19,
        )
        self.assertEqual([17, 18, 19, 20], pagination_list['pagination'])

        # Current page = 20
        # page_range = [17, 18, 19, 20]
        pagination_list = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=20,
        )
        self.assertEqual([17, 18, 19, 20], pagination_list['pagination'])

        # Current page = 21
        # page_range = [17, 18, 19, 20]
        pagination_list = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=21,
        )
        self.assertEqual([17, 18, 19, 20], pagination_list['pagination'])
