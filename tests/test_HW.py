import time
from selenium import webdriver


def test_first(browser):
    browser.get(browser.url)
    assert "Google" in browser.title

def test_second(browser):
    browser.get(browser.url)
    assert "Дзен" in browser.title