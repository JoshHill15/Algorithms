var rockPaperScissors = function (numOfRounds) {
    var options = ['rock', 'paper', 'scissors'];
    var allPossibilities = [];

    var roundChoice = function (round, roundNumber) {
        for (var i = 0; i < options.length; i++) {
            round.push(options[i]);
            if (roundNumber === numOfRounds) {
                allPossibilities.push(round.slice());
            } else {
                roundChoice(round, roundNumber + 1);
            }
            round.pop();
        }
    }
    roundChoice([], 1);
    return allPossibilities;
}
console.log(rockPaperScissors(1))