import unittest
import logging
from rt_with_exceptions import Runner

is_frozen = False


class RunnerTest(unittest.TestCase):
    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        try:
            walk_test_runner = Runner('Вася', -5)
            for _ in range(10):
                walk_test_runner.walk()
            self.assertEqual(walk_test_runner.distance, 50)
            logging.info(f'"test_walk" выполнен успешно')
        except ValueError:
            logging.warning("Неверная скорость для Runner", exc_info=True)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run(self):
        try:
            run_test_runner = Runner(True)
            for _ in range(10):
                run_test_runner.run()
            self.assertEqual(run_test_runner.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError:
            logging.warning("Неверный тип данных для объекта Runner", exc_info=True)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_challenge(self):
        challenge_test_runner_1 = Runner('Илья')
        challenge_test_runner_2 = Runner('Арсен')
        for _ in range(10):
            challenge_test_runner_1.run()
            challenge_test_runner_2.walk()
        self.assertNotEqual(challenge_test_runner_1.distance, challenge_test_runner_2.distance)


logging.basicConfig(
    level=logging.INFO,
    filename="runner_tests.log",
    filemode="w",
    encoding="utf-8",
    format="%(asctime)s | %(levelname)s | %(message)s"
)

if __name__ == "__main__":
    unittest.main()