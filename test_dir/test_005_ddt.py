import seldom
from seldom import data


class DDTTest(seldom.TestCase):
    """
    数据驱动
    """

    @data([
        ('case1', 'seldom'),
        ('case2', 'selenium'),
        ('case3', 'unittest'),
    ])
    def test_baidu(self, _, search_key):
        """
         used parameterized test
        :param _: case name
        :param search_key: search keyword
        """
        self.open("https://cn.bing.com/")
        self.type(id_="sb_form_q", text=search_key, enter=True)
        self.assertInTitle(search_key)


if __name__ == '__main__':
    seldom.main(debug=True)
