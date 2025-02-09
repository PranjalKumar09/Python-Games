class Game:
    def __init__(self, game_id):
        self.player1_has_played = False
        self.player2_has_played = False
        self.ready = False
        self.id = game_id
        self.moves = [None, None]
        self.player_wins = [0, 0]
        self.ties = 0

    def get_player_move(self, player):
        """
        Get the move of the specified player.

        :param player: Player index (0 or 1)
        :return: Move (e.g., "Rock", "Paper", "Scissors")
        """
        return self.moves[player]

    def play(self, player, move):
        """
        Record the move made by a player.

        :param player: Player index (0 or 1)
        :param move: Move made by the player (e.g., "Rock", "Paper", "Scissors")
        """
        self.moves[player] = move
        if player == 0:
            self.player1_has_played = True
        else:
            self.player2_has_played = True

    def connected(self):
        """
        Check if both players are connected and ready to play.

        :return: True if both players are connected and ready, False otherwise
        """
        return self.ready

    def both_players_played(self):
        """
        Check if both players have made their moves.

        :return: True if both players have played, False otherwise
        """
        return self.player1_has_played and self.player2_has_played

    def determine_winner(self):
        """
        Determine the winner based on the moves of both players.

        :return: Index of the winning player (0 or 1) or -1 for a tie
        """
        player1_move = self.moves[0].upper()[0]
        player2_move = self.moves[1].upper()[0]

        winner = -1
        if (player1_move == "R" and player2_move == "S") or (player1_move == "P" and player2_move == "R") or ( player1_move == "S" and player2_move == "P"):
            winner = 0
        elif (player1_move == "S" and player2_move == "R") or (player1_move == "R" and player2_move == "P") or (player1_move == "P" and player2_move == "S"):
            winner = 1
        return winner

    def reset_play_status(self):
        """
        Reset the play status of both players.
        """
        self.player1_has_played = False
        self.player2_has_played = False
