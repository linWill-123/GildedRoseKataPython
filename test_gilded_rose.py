# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)

    def test_vest_item_should_decrease_after_one_day(self):
        vest = "+5 Dexterity Vest"
        items = [Item(vest, 1, 2), Item(vest, 9, 19), Item(vest, 4, 6)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        expected = [Item(vest, 0, 1), Item(vest, 8, 18), Item(vest, 3, 5)]
        for i, item in enumerate(expected):
            self.assertEqual(str(items[i]), str(item))

    def testConjuredItemQualityDegradesTwiceAsFastBeforeSellIn(self):
        items = [Item(name="Conjured Mana Cake", sell_in=10, quality=20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        assert items[0].quality == 18, "Quality should decrease by 2 for Conjured items before SellIn"

    def testConjuredItemQualityDegradesTwiceAsFastAfterSellIn(self):
        items = [Item(name="Conjured Mana Cake", sell_in=0, quality=10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        expected_quality = 10 - 4
        self.assertEqual(items[0].quality, expected_quality, "Quality of Conjured item did not degrade twice as fast after SellIn")

    def testConjuredItemQualityNeverNegative(self):
        items = [Item(name="Conjured Mana Cake", sell_in=1, quality=1)]
        gilded_rose = GildedRose(items)

        for _ in range(5):
            gilded_rose.update_quality()

        self.assertTrue(items[0].quality >= 0, "Quality of Conjured item is negative")
        self.assertEqual(items[0].quality, 0, "Quality of Conjured item did not stop at 0")

    def testBackstagePassesQualityIncreasesBy2When10DaysOrLess(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 20)]
        gildedRose = GildedRose(items)
        gildedRose.update_quality()
        self.assertEqual(22, items[0].quality, "Backstage passes quality did not increase by 2 when there are 10 days or less")

    def testBackstagePassesQualityIncreasesBy3When5DaysOrLess(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 20)]
        gildedRose = GildedRose(items)
        gildedRose.update_quality()
        self.assertEqual(23, items[0].quality, "Backstage passes quality did not increase by 3 when there are 5 days or less")

    def testBackstagePassesQualityDropsTo0AfterConcert(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 20)]
        gildedRose = GildedRose(items)
        gildedRose.update_quality()
        self.assertEqual(0, items[0].quality, "Backstage passes quality did not drop to 0 after the concert")

if __name__ == '__main__':
    unittest.main()
