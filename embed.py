# personal discord embed for rex 


import discord

class Rexembed:

    def __init__(self, title='', description='', colour='', thumbnail=''):

        self.title = title
        self.description = description
        self.thumbnail = thumbnail
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
        
        rembed.set_thumbnail(url=self.thumbnail)
        #rembed.set_image(url=self.image)
        #rembed.set_footer(text=self.footer)

        return rembed

'''
class Rexembed:

    def __init__(self, title='', description='', colour='', thumbnail='', image='', footer=''):

        self.title = title
        self.description = description
        self.thumbnail = thumbnail
        self.image = image
        self.footer = footer
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
        
        rembed.set_thumbnail(url=self.thumbnail)
        rembed.set_image(url=self.image)
        rembed.set_footer(text=self.footer)

        return rembed
'''