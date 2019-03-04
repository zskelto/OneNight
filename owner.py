from discord.ext import commands

class OwnerCog:
    def __init__(self, bot):
        self.bot = bot

    def isowner(ctx):
        return ctx.message.author.server_permissions.administrator

    @commands.command(name='load', hidden=True)
    @commands.check(isowner)
    async def cog_load(self, ctx, *, cog: str):
        """"Command which loads a module"""

        try:
            self.bot.load_extension(cog)
        except Exception as e:
            await self.bot.say(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await self.bot.say('**`SUCCESS`**')

    @commands.command(name='unload', hidden=True)
    @commands.check(isowner)
    async def cog_unload(self, ctx, *, cog: str):
        """Command which Unloads a module."""

        try:
            self.bot.unload_extension(cog)
        except Exception as e:
            await self.bot.say(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await self.bot.say('**`SUCCESS`**')

    @commands.command(name='reload', hidden=True)
    @commands.check(isowner)
    async def cog_reload(self, ctx, *, cog: str):
        """Command which Reloads a Module."""

        try:
            self.bot.unload_extension(cog)
            self.bot.load_extension(cog)
        except Exception as e:
            await self.bot.say(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await self.bot.say('**`SUCCESS`**')

    @commands.command(name='quit', hidden=True)
    @commands.check(isowner)
    async def bot_quit(self):
        await self.bot.logout()

def setup(bot):
    bot.add_cog(OwnerCog(bot))
