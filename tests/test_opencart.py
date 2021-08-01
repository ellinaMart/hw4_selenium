import pytest


# @pytest.mark.parametrize("url,title", [
#     ("https://yandex.ru", "Яндекс"),
#     ("https://google.ru", "Google")
# ])
def test_title(browser, base_url, title):
    browser.get(base_url)
    current_title = browser.title
    import pdb; pdb.set_trace()
    assert current_title == "OpenCart"