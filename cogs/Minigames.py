import discord, random
from discord.ext import commands

# TODO: Tic Tac Toe game is currently not working, so had to pull down this Cog.

kiwi = discord.Colour.from_rgb(0, 200, 118)
    
class minigames(commands.Cog):
    def __init__(self, client):
        self.client = client

    player1 = ""
    player2 = ""
    turn = ""
    gameOver = True
    board = []
    winningConditions = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    @commands.command()
    async def tictactoe(self, ctx, p1: discord.Member, p2: discord.Member):
        global count
        global player1
        global player2
        global turn
        global gameOver
        if gameOver:
            global board
            board = [":white_large_square:", ":white_large_square:", ":white_large_square:",
                    ":white_large_square:", ":white_large_square:", ":white_large_square:",
                    ":white_large_square:", ":white_large_square:", ":white_large_square:"]
            turn = ""
            gameOver = False
            count = 0
            player1 = p1
            player2 = p2
            
            line = ""
            for x in range(len(board)):
                if x == 2 or x == 5 or x == 8:
                    line += " " + board[x]
                    await ctx.send(line); line = ""
                else:
                    line += " " + board[x]

            num = random.randint(1, 2)
            if num == 1:
                turn = player1
                await ctx.send("It's <@" + str(player1.id) + ">'s turn.")
            elif num == 2:
                turn = player2
                await ctx.send("It's <@" + str(player2.id) + ">'s turn.")
        else:
            await ctx.send("There is already a game in progress! Finish the game before starting a new one.")

    @commands.command()
    async def place(self, ctx, pos: int):
        global turn
        global player1
        global player2
        global board
        global count
        global gameOver
        if not gameOver:
            mark = ""
            if turn == ctx.author:
                if turn == player1:
                    mark = ":regional_indicator_x:"
                elif turn == player2:
                    mark = ":o2:"
                if 0 < pos < 10 and board[pos - 1] == ":white_large_square:" :
                    board[pos - 1] = mark
                    count += 1

                    line = ""
                    for x in range(len(board)):
                        if x == 2 or x == 5 or x == 8:
                            line += " " + board[x]
                            await ctx.send(line)
                            line = ""
                        else:
                            line += " " + board[x]

                    checkWinner(winningConditions, mark)
                    if gameOver == True:
                        await ctx.send(mark + " wins!")
                    elif count >= 9:
                        gameOver = True
                        await ctx.send("It's a tie!")

                    if turn == player1:
                        turn = player2
                    elif turn == player2:
                        turn = player1
                else:
                    await ctx.send("Make sure you've written a whole number from 1 to 9 that has not been filled in the board.")
            else:
                await ctx.send("Hey! It's not your turn yet!")
        else:
            await ctx.send("Please start a new game by typing !tictactoe")
    def checkWinner(self, winningConditions, mark):
        global gameOver
        for condition in winningConditions:
            if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
                gameOver = True

    @tictactoe.error
    async def tictactoe_error(self, ctx, error):
        print(error)
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please mention 2 players to start the game.")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("Make sure you tag the players (i.e. @Kiwi).")

    @place.error
    async def place_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please type the position you want to mark.")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("Make sure to type a whole number.")

    @commands.command(brief = "Rock, paper, or scissors. Do you not know this game?")
    async def rps(self, ctx, arg):
        """Type this command and one of the 3 options, Kiwi will randomly answer and tell you who won."""
        options = ["rock", "paper", "scissors"]
        botAnswer = random.choice(options)
        if arg in options:
            if arg == "rock":
                if botAnswer == "rock":
                    await ctx.send(":rock: vs. :rock: It's a tie!")
                elif botAnswer == "paper":
                    await ctx.send(":rock: vs. :roll_of_paper: Kiwi wins!")
                elif botAnswer == "scissors":
                    await ctx.send(":rock: vs. :scissors: You win!")
            elif arg == "paper":
                if botAnswer == "rock":
                    await ctx.send(":roll_of_paper: vs. :rock: You win!")
                elif botAnswer == "paper":
                    await ctx.send(":roll_of_paper: vs. :roll_of_paper: It's a tie!")
                elif botAnswer == "scissors":
                    await ctx.send(":roll_of_paper: vs. :scissors: Kiwi wins!")
            elif arg == "scissors":
                if botAnswer == "rock":
                    await ctx.send(":scissors: vs. :rock: Kiwi wins!")
                elif botAnswer == "paper":
                    await ctx.send(":scissors: vs. :roll_of_paper: You win!")
                elif botAnswer == "scissors":
                    await ctx.send(":scissors: vs. :scissors: It's a tie!")

def setup(client):
    client.add_cog(minigames(client))