import pytest


# @pytest.mark.parametrize("url,title", [
#     ("https://yandex.ru", "Яндекс"),
#     ("https://google.ru", "Google")
# ])
def test_title(browser, base_url):
    browser.get(base_url)
    current_title = browser.title
    #import pdb; pdb.set_trace()
    assert "OpenCart" in current_title

def test_login(browser, admin_url):
    browser.get(admin_url)


