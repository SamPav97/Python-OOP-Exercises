from project.team import Team
from unittest import TestCase, main


class TeamTest(TestCase):
    def SetUp(self) -> None:
        self.team = Team("CSKA")

    def test_init_happy_case(self):
        team = Team("CSKA")
        self.assertEqual("CSKA", team.name)
        self.assertEqual({}, team.members)

    def test_init_raises(self):
        with self.assertRaises(ValueError) as ex:
            team = Team("CSKA1948")
        self.assertEqual("Team Name can contain only letters!", str(ex.exception))

    def test_add_member(self):
        team = Team("CSKA")
        x = team.add_member(sami=24)
        self.assertEqual({"sami": 24}, team.members)
        self.assertEqual(f"Successfully added: sami", x)

    def test_remove_member_happy(self):
        team = Team("CSKA")
        team.add_member(sami=24)
        self.assertEqual({"sami": 24}, team.members)
        x = team.remove_member("sami")
        self.assertEqual({}, team.members)
        self.assertEqual(f"Member sami removed", x)

    def test_remove_member_raises(self):
        team = Team("CSKA")
        team.add_member(sami=24)
        self.assertEqual({"sami": 24}, team.members)
        x = team.remove_member("pedal")
        self.assertEqual(f"Member with name pedal does not exist", x)

    def test_gt(self):
        team = Team("CSKA")
        team2 = Team("lefski")
        team.add_member(sami=24)
        team.add_member(samcho=24)
        team2.add_member(kole=22)
        x = team > team2
        y = team < team2
        self.assertEqual(True, x)
        self.assertEqual(False, y)

    def test_len(self):
        team = Team("CSKA")
        team.add_member(sami=24)
        team.add_member(samcho=24)
        x = len(team)
        self.assertEqual(2, x)

    def test_add_together(self):
        team = Team("CSKA")
        team2 = Team("lefski")
        team.add_member(sami=24)
        team.add_member(samcho=24)
        team2.add_member(kole=22)
        new_team = team + team2
        self.assertEqual("CSKAlefski", new_team.name)
        self.assertEqual({"sami": 24, "samcho": 24, "kole": 22}, new_team.members)
        self.assertEqual(new_team, new_team)

    def test_str(self):
        team = Team("CSKA")
        team.add_member(sami=24)
        team.add_member(kole=22)
        x = str(team)
        self.assertEqual("Team name: CSKA\nMember: sami - 24-years old\nMember: kole - 22-years old", x)
