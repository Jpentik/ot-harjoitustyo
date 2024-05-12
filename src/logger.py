import datetime

class Logger:
    """Class to save game result to log"""
    def logger(self):
        """Reads a log file, adds the current game to it, and rewrites the updated log.

        Args:
            self: Finished game, a list of lists. Every value is symbol "X" or "0" at this point
        """
        with open("tictactoe_log.txt", 'a', encoding="utf-8") as game_log:
            game_log.write("\n")
            game_log.write("Time of game " + str(datetime.datetime.now()) + "\n")
            for _ in range(0, int(len(self))):
                game_log.write(str(self[_]) + "\n") # pylint: disable=unsubscriptable-object
            return True
