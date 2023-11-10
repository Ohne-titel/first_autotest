from selene.support.shared import browser
from selene import be, have


def test_open_chrome(browser_configs):
    browser.element('[class="gLFyf"]').click().type('shmekelbesh7mene5').press_enter()
    browser.element('[style="padding-top:.33em"]').should(have.text('Es wurden keine mit deiner Suchanfrage - '
                                                                    'shmekelbesh7mene5 - übereinstimmenden Dokumente '
                                                                    'gefunden.'))