import unittest
import shapes


class TestShapes(unittest.TestCase):

    def test_rectangle_area(self):
        # given
        rect = shapes.Rectangle(2, 4)
        expected_area = 8
        # when
        actual_area = rect.area()
        # then
        self.assertEquals(expected_area, actual_area)

    def test_rectangle_perimeter(self):
        # given
        rect = shapes.Rectangle(2, 4)
        expected_perimeter = 12
        # when
        actual_perimeter = rect.perimeter()
        # then
        self.assertEquals(expected_perimeter, actual_perimeter)

    def test_square_area(self):
        # given
        square = shapes.Square(4)
        expected_area = 16
        # when
        actual_area = square.area()
        # then
        self.assertEquals(expected_area, actual_area)

    def test_square_perimeter(self):
        # given
        square = shapes.Square(4)
        expected_perimeter = 16
        # when
        actual_perimeter = square.perimeter()
        # then
        self.assertEquals(expected_perimeter, actual_perimeter)
