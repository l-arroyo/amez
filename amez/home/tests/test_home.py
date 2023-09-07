from wagtail.test.utils import WagtailPageTestCase
from home.models import HomePage

class AboutUsTestCase(WagtailPageTestCase):
    def test_can_create_about_us(self):
        # Create a page
        page = HomePage(
            title='About Us',
            slug='about-us',
            path='000100010001',
            depth=4,
            numchild=0,)

        # Save it to the database
        page.save()
        self.assertTrue(HomePage.objects.filter(title='About Us').exists())