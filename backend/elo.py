class Rating:
    """
    A class that represents an implementation of the Elo Rating System
    Reference - https://metinmediamath.wordpress.com/2013/11/27/how-to-calculate-the-elo-rating-including-example
    """

    def __init__(self, attacker_rating: object, defender_rating: object, attacker_outcome: object) -> object:  # constructor
        """
        :rtype: object
        """
        self.attacker_rating = attacker_rating
        self.defender_rating = defender_rating
        self.attacker_outcome = attacker_outcome

    def find_rating(self):
        # Step 1: Find expected score of Player A (Attacker) & B (Defender)
        expected_attacker_score = self.expected_rating(self.attacker_rating, self.defender_rating)
        expected_defender_score = self.expected_rating(self.defender_rating, self.attacker_rating)

        # Step 2: Now we wait for the war to finish and set the actual score of the player A & B
        if self.attacker_outcome == "win":
            attacker_score = 1.0
            defender_score = 0.0
        elif self.attacker_outcome == "loss":
            attacker_score = 0.0
            defender_score = 1.0
        # K-Factor is a cap on how many Elo points a player can win or lose from a single match.
        # K-Factor is a critical part of maintaining an accurate rating.
        # In chess the ICC uses a value of K = 32

        k_factor = 32

        # Step 3: Update elo rating for each player
        new_attacker_rating = self.attacker_rating + k_factor * (attacker_score-expected_attacker_score)
        new_defender_rating = self.defender_rating + k_factor * (defender_score-expected_defender_score)

        return new_attacker_rating,new_defender_rating

    @staticmethod
    def expected_rating(player1_rating, player2_rating):
        exp = player2_rating - player1_rating
        return (1 + 10 ** (exp / 400.0)) ** -1


