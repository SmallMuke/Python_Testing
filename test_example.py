

class TestExample:
    def test_example(self,set_up_browser):
        driver = set_up_browser
        driver.get("https://skillbox.ru")
        # здесь можно писать любую проверку
        assert 'NO' == driver.title

    def test_example_2(self,set_up_browser):
        driver = set_up_browser
        driver.get("https://skillbox.ru")
        # здесь можно писать любую проверку
        assert 'NO' == driver.title

    def test_example_3(self,set_up_browser):
        driver = set_up_browser
        driver.get("https://skillbox.ru")
        # здесь можно писать любую проверку
        assert 'NO' == driver.title

    def test_example_4(self,set_up_browser):
        driver = set_up_browser
        driver.get("https://skillbox.ru")
        # здесь можно писать любую проверку
        assert 'Skillbox – образовательная платформа с онлайн-курсами' == driver.title
