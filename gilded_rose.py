# -*- coding: utf-8 -*-


class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class GildedRose(object):

    def __init__(self, items: list[Item]):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == "Sulfuras, Hand of Ragnaros":
                continue  # Sulfuras does not degrade or decrease in sell_in

            degrade_rate = 1
            if item.name.startswith("Conjured"):  # Conjured items degrade twice as fast
                degrade_rate *= 2

            # handle quality increase for Aged Brie, Backstage passes before adjusting sell_in
            if item.name == "Aged Brie":
                item.quality += 1 if item.quality < 50 else 0
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                if item.sell_in <= 0:
                    item.quality = 0
                elif item.sell_in <= 5:
                    item.quality += 3
                elif item.sell_in <= 10:
                    item.quality += 2
                else:
                    item.quality += 1

            # decrease sell_in
            item.sell_in -= 1

            # handle quality decrease for all items except "Sulfuras", "Aged Brie", and "Backstage passes"
            # after potentially adjusting their quality above
            if item.sell_in < 0:
                if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
                    if item.name.startswith("Conjured"):
                        item.quality -= degrade_rate * 2
                    else:
                        item.quality -= degrade_rate
            elif item.name not in ["Aged Brie", "Backstage passes to a TAFKAL80ETC concert", "Sulfuras, Hand of Ragnaros"]:
                item.quality -= degrade_rate

            # ensure quality does not fall below 0 or rise above 50
            item.quality = max(0, min(item.quality, 50))
