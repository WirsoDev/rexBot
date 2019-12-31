# test color and embed for dscord bot

@client.command()
async def test(ctx, *args):
    retStr = str("""```css\nThis is some colored Text```""")
    embed = discord.Embed(title="Random test")
    embed.add_field(name="Name field can't be colored as it seems",value=retStr)
    await ctx.send(embed=embed)