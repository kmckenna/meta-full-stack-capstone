from django.test import TestCase
from restaurant.models import MenuItem
from django.urls import reverse

class MenuItemListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create 13 menuitems for pagination tests
        number_of_menuitems = 4

        for menuitem_id in range(number_of_menuitems):
            MenuItem.objects.create(
                title=f'Yummy Menu Item: {menuitem_id}',
                price=menuitem_id * 3.00,
                inventory=menuitem_id,
            )


    def test_getall(self):
        pass

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/menu/')
        self.assertEqual(response.status_code, 200)
    #
    # def test_view_url_accessible_by_name(self):
    #     response = self.client.get(reverse('menuitems'))
    #     self.assertEqual(response.status_code, 200)
    #
    # def test_view_uses_correct_template(self):
    #     response = self.client.get(reverse('menuitems'))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'catalog/menuitem_list.html')
    #
    # def test_pagination_is_ten(self):
    #     response = self.client.get(reverse('menuitems'))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTrue('is_paginated' in response.context)
    #     self.assertTrue(response.context['is_paginated'] == True)
    #     self.assertEqual(len(response.context['menuitem_list']), 10)
    #
    # def test_lists_all_menuitems(self):
    #     # Get second page and confirm it has (exactly) remaining 3 items
    #     response = self.client.get(reverse('menuitems')+'?page=2')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTrue('is_paginated' in response.context)
    #     self.assertTrue(response.context['is_paginated'] == True)
    #     self.assertEqual(len(response.context['menuitem_list']), 3)
    #