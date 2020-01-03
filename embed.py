import discord


class Rexembed:

    def __init__(self, title='', description='', colour=''):

        self.title = title
        self.description = description
        colour = colour.lower()
        if colour == 'red':
            self.colour = discord.Colour.red()
        elif colour == 'green':
            self.colour = discord.Colour.green()
        elif colour == 'blue':
            self.colour = discord.Colour.blue()


    def normal_embed(self):
        rembed = discord.Embed(
            title = self.title,
            description = self.description,
            colour = self.colour,
        )

        return rembed