import time


class Tablet:
    """
    This is a tablet class that is used by the pepper class.
    To load in tablet functions from the pepper API.
    """
    session = tablet_service = None

    def __init__(self, session):
        self.session = session
        self.tablet_service = session.service("ALTabletService")

        self.tablet_service.enableWifi()
        self.tablet_service.showWebview("https://oege.ie.hva.nl/~niewols/website/tablet.html")

    """
    Show website view on tablet.
    """
    def show_website(self):
        try:
            # Display a web page on the tablet
            self.tablet_service.showWebview("https://oege.ie.hva.nl/~niewols/website/tablet.html")

        except Exception, e:
            print "Error was: ", e

    """
    Hide the website view on tablet
    """
    def hide_website(self):
        self.tablet_service.hideWebview()
