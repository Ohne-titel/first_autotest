from selene.support.shared import browser
from selene import be, have


def test_positive_chrome(browser_configs):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_open_chrome(browser_configs):
    browser.element('[class="gLFyf"]').click().type('shmekelbesh7mene5').press_enter()
    browser.element('[style="padding-top:.33em"]').should(have.text('Es wurden keine mit deiner Suchanfrage - '
                                                                    'shmekelbesh7mene5 - übereinstimmenden Dokumente '
                                                                    'gefunden.'))
