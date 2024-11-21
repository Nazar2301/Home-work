
import unittest
from runner_and_tournament import Runner, Tournament

class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = Runner("Усэйн", 10)
        self.andrey = Runner("Андрей", 9)
        self.nick = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            print(result)

    def test_usain_and_nick(self):
        tournament = Tournament(90, self.usain, self.nick)
        results = tournament.start()
        self.__class__.all_results["test_usain_and_nick"] = results
        self.assertTrue(results[max(results.keys())] == "Ник")

    def test_andrey_and_nick(self):
        tournament = Tournament(90, self.andrey, self.nick)
        results = tournament.start()
        self.__class__.all_results["test_andrey_and_nick"] = results
        self.assertTrue(results[max(results.keys())] == "Ник")

    def test_usain_andrey_and_nick(self):
        tournament = Tournament(90, self.usain, self.andrey, self.nick)
        results = tournament.start()
        self.__class__.all_results["test_usain_andrey_and_nick"] = results
        self.assertTrue(results[max(results.keys())] == "Ник")

if __name__ == "__main__":
    unittest.main()