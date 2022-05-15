from unittest import TestCase, main

from project.hero import Hero


class HeroTest(TestCase):
    def setUp(self) -> None:
        self.hero = Hero("Warrior", 10, 100, 50)
        self.enemy = Hero("Knight", 10, 100, 50)

    def test_init(self):
        hero = Hero("username", 7, 90.5, 10.0)
        self.assertEqual("username", hero.username)
        self.assertEqual(7, hero.level)
        self.assertEqual(90.5, hero.health)
        self.assertEqual(10.0, hero.damage)

    def test_battle_if_enemy_username_same_as_yours_raises(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_if_self_health_se_zero_raises(self):
        for health in [0, -2]:
            with self.assertRaises(Exception) as ex:
                self.hero.health = health
                self.hero.battle(self.enemy)
            self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_battle_if_enemy_health_se_zero_raises(self):
        for health in [0, -2]:
            with self.assertRaises(Exception) as ex:
                self.enemy.health = health
                self.hero.battle(self.enemy)
            self.assertEqual(f"You cannot fight {self.enemy.username}. He needs to rest", str(ex.exception))

    def test_if_battle_is_draw(self):
        x = self.hero.battle(self.enemy)
        self.assertEqual("Draw", x)

    def test_if_you_win(self):
        self.hero.health = 600
        x = self.hero.battle(self.enemy)
        self.assertEqual("You win", x)
        self.assertEqual(11, self.hero.level)
        self.assertEqual(105, self.hero.health)
        self.assertEqual(55, self.hero.damage)

    def test_if_you_lose(self):
        self.enemy.health = 600
        x = self.hero.battle(self.enemy)
        self.assertEqual("You lose", x)
        self.assertEqual(11, self.enemy.level)
        self.assertEqual(105, self.enemy.health)
        self.assertEqual(55, self.enemy.damage)

    def test_string_method(self):
        self.assertEqual(f"Hero {self.hero.username}: {self.hero.level} lvl\nHealth: {self.hero.health}\nDamage: {self.hero.damage}\n", str(self.hero))

