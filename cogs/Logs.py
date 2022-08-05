from discord.ext import commands
import discord


class Logs(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        print('Module {} is loaded'.format(self.__class__.__name__))

    @commands.Cog.listener()
    async def on_member_join(self, member):
        msg = f"{id.member} подключился к серверу."
        # You must specify the id of the channel for the logs
        await self.bot.get_channel("963841079143178351").send(msg)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        msg = f"{id.member} отлючился от сервера."
        # You must specify the id of the channel for the logs
        await self.bot.get_channel("963841079143178351").send(msg)

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        msg = f"Message before changes {before.content}\n" \
              f"Message after changes {after.content}"
        # You must specify the id of the channel for the logs
        await self.bot.get_channel("963841079143178351").send(msg)

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        msg = f"Deleted message: {message.content}\n"
        # You must specify the id of the channel for the logs
        await self.bot.get_channel("963841079143178351").send(msg)

    @commands.Cog.listener()
    async def on_voice_state_update(self, member: discord.Member, before: discord.VoiceState,
                                    after: discord.VoiceState):
        if before.channel is None:
            msg = f"{id.member} покдлючился к каналу {after.channel.mention}"
            # You must specify the id of the channel for the logs
            await self.bot.get_channel("963841079143178351").send(msg)
        elif after.channel is None:
            msg = f"{id.member} отключился от канала {before.channel.mention}"
            # You must specify the id of the channel for the logs
            await self.bot.get_channel("963841079143178351").send(msg)
        elif before.channel != after.channel:
            msg = f"{id.member} перешёл из канала {before.channel.mention}" \
                  f" into the channel {after.channel.mention}"
            # You must specify the id of the channel for the logs
            await self.bot.get_channel("963841079143178351").send(msg)


def setup(bot):
    bot.add_cog(Logs(bot))
