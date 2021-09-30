"""
Copyright 2021 Onii-chan

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import logging
from typing import List

import aiohttp
import discord
from redbot.core import commands
from redbot.core.utils.chat_formatting import box


async def api_call(call_uri, returnObj=False):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{call_uri}") as response:
            response = await response.json()
            if returnObj == False:
                return response["url"]
            elif returnObj == True:
                return response
    await session.close()

log = logging.getLogger("red.onii.nsfw")


class Nsfw(commands.Cog):
    """
    Nsfw commands, proceed with caution.
    """

    __author__ = ["Onii-chan"]
    __version__ = "2.1.0"

    def __init__(self, bot):
        self.bot = bot

    def format_help_for_context(self, ctx: commands.Context) -> str:
        """Thanks Sinbad!"""
        pre_processed = super().format_help_for_context(ctx)
        return f"{pre_processed}\n\nAuthors: {', '.join(self.__author__)}\nCog Version: {self.__version__}"

    async def _version_msg(
        self,
        ctx: commands.Context,
        version: str,
        authors: List[str]
    ):
        """Cog version message."""
        msg = box(
            ("Nsfw cog version: {version}\nAuthors: {authors}").format(
                version=version, authors=", ".join(authors)
            ),
            lang="py",
        )
        return await ctx.send(msg)

    @commands.command()
    async def nsfwversion(self, ctx: commands.Context):
        """Get the version of the installed Nsfw cog."""

        await self._version_msg(ctx, self.__version__, self.__author__)

    @commands.group()
    @commands.is_nsfw()
    async def hentai(self, ctx: commands.Context):
        """Hentai Commands"""

    @commands.group()
    @commands.is_nsfw()
    async def real(self, ctx: commands.Context):
        """Real Porn"""

    @commands.cooldown(5, 7, commands.BucketType.user)
    @hentai.command()
    @commands.is_nsfw()
    @commands.guild_only()
    async def erok(self, ctx):
        """Eroctic!"""
        if ctx.channel.is_nsfw():
            embed = discord.Embed(
                title="Erok Kitsune !!!",
                color=ctx.message.author.color,
            )

            embed.set_footer(
                text=f"Requested by {ctx.message.author.display_name}",
                icon_url=ctx.message.author.avatar_url,
            )
            embed.set_author(
                name=self.bot.user.display_name,
                icon_url=self.bot.user.avatar_url
            )

            embed.set_image(
                url=await api_call(
                    "https://nekos.life/api/v2/img/erok"
                )
            )
            await ctx.reply(embed=embed, mention_author=False)
        else:
            await ctx.reply(
                "This command can only be used in a NSFW channel.",
                mention_author=False
            )

    @commands.cooldown(5, 7, commands.BucketType.user)
    @hentai.command()
    @commands.is_nsfw()
    @commands.guild_only()
    async def eroneko(self, ctx):
        """Eroctic nekos? what could be better?"""
        if ctx.channel.is_nsfw():
            embed = discord.Embed(
                title="***ERO*** NEKO!",
                color=ctx.message.author.color,
            )

            embed.set_footer(
                text=f"Requested by {ctx.message.author.display_name}",
                icon_url=ctx.message.author.avatar_url,
            )
            embed.set_author(
                name=self.bot.user.display_name,
                icon_url=self.bot.user.avatar_url
            )

            embed.set_image(
                url=await api_call(
                    "https://nekos.life/api/v2/img/erokemo"
                )
            )
            await ctx.reply(embed=embed, mention_author=False)
        else:
            await ctx.reply(
                "This command can only be used in a NSFW channel.",
                mention_author=False
            )

    @commands.cooldown(5, 7, commands.BucketType.user)
    @hentai.command(name="feet", aliases=["feetgif", "foot"])
    @commands.is_nsfw()
    @commands.guild_only()
    async def feet(self, ctx):
        """Tasty feet"""
        if ctx.channel.is_nsfw():
            embed = discord.Embed(
                title="***Feet***",
                color=ctx.message.author.color,
            )

            embed.set_footer(
                text=f"Requested by {ctx.message.author.display_name}",
                icon_url=ctx.message.author.avatar_url,
            )
            embed.set_author(
                name=self.bot.user.display_name,
                icon_url=self.bot.user.avatar_url
            )

            embed.set_image(
                url=await api_call(
                    "https://nekos.life/api/v2/img/feetg"
                )
            )
            await ctx.reply(embed=embed, mention_author=False)
        else:
            await ctx.reply(
                "This command can only be used in a NSFW channel.",
                mention_author=False
            )

    @commands.cooldown(5, 7, commands.BucketType.user)
    @hentai.command()
    @commands.guild_only()
    @commands.is_nsfw()
    async def cum(self, ctx):
        """Beautiful white cum"""
        if ctx.channel.is_nsfw():
            embed = discord.Embed(
                title="***Sticky white stuff!***",
                color=ctx.message.author.color,
            )
            embed.set_footer(
                text=f"Requested by {ctx.message.author.display_name}",
                icon_url=ctx.message.author.avatar_url,
            )
            embed.set_author(
                name=self.bot.user.display_name,
                icon_url=self.bot.user.avatar_url
            )
            embed.set_image(
                url=await api_call(
                    "https://nekos.life/api/v2/img/cum"
                    )
                )
            await ctx.reply(embed=embed, mention_author=False)
        else:
            await ctx.reply(
                "This command can only be used in a NSFW channel.",
                mention_author=False
            )

    @commands.cooldown(5, 7, commands.BucketType.user)
    @hentai.command(name="nekofuck", aliases=["nekosex", "nekogif"])
    @commands.is_nsfw()
    @commands.guild_only()
    async def nekofuck(self, ctx):
        """Fuck nekos!"""
        if ctx.channel.is_nsfw():
            embed = discord.Embed(
                title="Catgirls!!!!",
                color=ctx.message.author.color,
            )
            embed.set_footer(
                text=f"Requested by {ctx.message.author.display_name}",
                icon_url=ctx.message.author.avatar_url,
            )
            embed.set_author(
                name=self.bot.user.display_name,
                icon_url=self.bot.user.avatar_url
            )
            embed.set_image(
                url=await api_call(
                    "https://nekos.life/api/v2/img/nsfw_neko_gif"
                )
            )
            await ctx.reply(embed=embed, mention_author=False)
        else:
            await ctx.reply(
                "This command can only be used in a NSFW channel.",
                mention_author=False
            )

    @commands.cooldown(5, 7, commands.BucketType.user)
    @hentai.command(name="futanari")
    @commands.is_nsfw()
    @commands.guild_only()
    async def futanari(self, ctx):
        """Futanari stuff."""
        if ctx.channel.is_nsfw():
            embed = discord.Embed(
                title="",
                color=ctx.message.author.color,
            )
            embed.set_footer(
                text=f"Requested by {ctx.message.author.display_name}",
                icon_url=ctx.message.author.avatar_url,
            )
            embed.set_author(
                name=self.bot.user.display_name,
                icon_url=self.bot.user.avatar_url
            )
            embed.set_image(
                url=await api_call(
                    "https://nekos.life/api/v2/img/futanari"
                )
            )
            await ctx.reply(embed=embed, mention_author=False)
        else:
            await ctx.reply(
                "This command can only be used in a NSFW channel.",
                mention_author=False
            )

    @commands.cooldown(5, 7, commands.BucketType.user)
    @hentai.command(name="boobs", aliases=["boob"])
    @commands.is_nsfw()
    @commands.guild_only()
    async def boobs(self, ctx):
        """Juicy tits"""
        if ctx.channel.is_nsfw():
            embed = discord.Embed(
                title="**Titties**!!!!!",
                color=ctx.message.author.color,
            )
            embed.set_footer(
                text=f"Requested by {ctx.message.author.display_name}",
                icon_url=ctx.message.author.avatar_url,
            )
            embed.set_author(
                name=self.bot.user.display_name,
                icon_url=self.bot.user.avatar_url
            )
            embed.set_image(
                url=await api_call(
                    "https://nekos.life/api/v2/img/boobs"
                )
            )

            await ctx.reply(embed=embed, mention_author=False)
        else:
            await ctx.reply(
                "This command can only be used in a NSFW channel.",
                mention_author=False
            )

    @commands.cooldown(5, 7, commands.BucketType.user)
    @hentai.command(name="blowjob")
    @commands.is_nsfw()
    @commands.guild_only()
    async def blowjob(self, ctx):
        """Blowjobs"""
        if ctx.channel.is_nsfw():
            embed = discord.Embed(
                title="Oh shit!",
                color=ctx.message.author.color,
            )
            embed.set_footer(
                text=f"Requested by {ctx.message.author.display_name}",
                icon_url=ctx.message.author.avatar_url,
            )
            embed.set_author(
                name=self.bot.user.display_name,
                icon_url=self.bot.user.avatar_url
            )
            embed.set_image(
                url=await api_call(
                    "https://nekos.life/api/v2/img/blowjob"
                )
            )

            await ctx.reply(embed=embed, mention_author=False)
        else:
            await ctx.reply(
                "This command can only be used in a NSFW channel.",
                mention_author=False
            )

    @commands.cooldown(5, 7, commands.BucketType.user)
    @hentai.command()
    @commands.is_nsfw()
    @commands.guild_only()
    async def pussy(self, ctx: commands.Context):
        """Tight pussies"""
        if ctx.channel.is_nsfw():
            embed = discord.Embed(
                title="Dang!",
                color=ctx.message.author.color,
            )
            embed.set_footer(
                text=f"Requested by {ctx.message.author.display_name}",
                icon_url=ctx.message.author.avatar_url,
            )
            embed.set_author(
                name=self.bot.user.display_name,
                icon_url=self.bot.user.avatar_url
            )
            embed.set_image(
                url=await api_call(
                    "https://nekos.life/api/v2/img/pussy"
                )
            )

            await ctx.reply(embed=embed, mention_author=False)
        else:
            await ctx.reply(
                "This command can only be used in a NSFW channel.",
                mention_author=False
            )

    @commands.cooldown(5, 7, commands.BucketType.user)
    @hentai.command()
    @commands.guild_only()
    @commands.is_nsfw()
    async def spank(self, ctx, user: commands.Greedy[discord.Member] = None):
        """Spank somebody"""
        if ctx.channel.is_nsfw():
            if user is None:
                await ctx.message.reply(
                    "Please mention somebody to spank nex time."
                    )
                return
            spanked_users = "".join(f"{users.mention} " for users in user)
            embed = discord.Embed(
                title="Oooof!",
                description="{} got spanked by {}".format(
                    spanked_users,
                    ctx.author.mention,
                ),
                color=ctx.message.author.color,
            )
            embed.set_footer(
                text=f"Requested by {ctx.message.author.display_name}",
                icon_url=ctx.message.author.avatar_url,
            )
            embed.set_author(
                name=self.bot.user.display_name,
                icon_url=self.bot.user.avatar_url
            )
            embed.set_image(
                url=await api_call(
                    "https://nekos.life/api/v2/img/spank"
                )
            )
            await ctx.reply(embed=embed, mention_author=False)
        else:
            await ctx.reply(
                "This command can only be used in a NSFW channel.",
                mention_author=False
            )

    @commands.cooldown(5, 7, commands.BucketType.user)
    @hentai.command()
    @commands.is_nsfw()
    @commands.guild_only()
    async def lesbian(self, ctx):
        """Lesbian Hentai"""
        if ctx.channel.is_nsfw():
            embed = discord.Embed(color=ctx.message.author.color)
            embed.set_footer(
                text=f"Requested by {ctx.message.author.display_name}",
                icon_url=ctx.message.author.avatar_url,
            )
            embed.set_author(
                name=self.bot.user.display_name,
                icon_url=self.bot.user.avatar_url
            )
            embed.set_image(
                url=await api_call(
                    "https://nekos.life/api/v2/img/les"
                )
            )
            await ctx.reply(embed=embed, mention_author=False)
        else:
            await ctx.reply(
                "This command can only be used in a NSFW channel.",
                mention_author=False
            )

    @commands.cooldown(5, 7, commands.BucketType.user)
    @hentai.command()
    @commands.is_nsfw()
    @commands.guild_only()
    async def trap(self, ctx):
        """Trapped"""
        if ctx.channel.is_nsfw():
            embed = discord.Embed(color=ctx.message.author.color)
            embed.set_footer(
                text=f"Requested by {ctx.message.author.display_name}",
                icon_url=ctx.message.author.avatar_url,
            )
            embed.set_author(
                name=self.bot.user.display_name,
                icon_url=self.bot.user.avatar_url
            )
            embed.set_image(
                url=await api_call(
                    "https://nekos.life/api/v2/img/trap"
                )
            )
            await ctx.reply(embed=embed, mention_author=False)
        else:
            await ctx.reply(
                "This command can only be used in a NSFW channel.",
                mention_author=False
            )

    @commands.cooldown(5, 7, commands.BucketType.user)
    @hentai.command()
    @commands.is_nsfw()
    @commands.guild_only()
    async def hololewd(self, ctx):
        """hololewd stuff"""
        if ctx.channel.is_nsfw():
            embed = discord.Embed(color=ctx.message.author.color)
            embed.set_footer(
                text=f"Requested by {ctx.message.author.display_name}",
                icon_url=ctx.message.author.avatar_url,
            )
            embed.set_author(
                name=self.bot.user.display_name,
                icon_url=self.bot.user.avatar_url
            )
            embed.set_image(
                url=await api_call(
                    "https://nekos.life/api/v2/img/hololewd"
                )
            )
            await ctx.reply(embed=embed, mention_author=False)
        else:
            await ctx.reply(
                "This command can only be used in a NSFW channel.",
                mention_author=False
            )

    @commands.cooldown(1, 5, commands.BucketType.user)
    @hentai.command()
    @commands.is_nsfw()
    @commands.guild_only()
    async def foxgirl(self, ctx):
        """Foxgirls!"""
        if ctx.channel.is_nsfw():
            embed = discord.Embed(
                title="Foxy",
                color=ctx.message.author.color,
            )
            embed.set_footer(
                text=f"Requested by {ctx.message.author.display_name}",
                icon_url=ctx.message.author.avatar_url,
            )
            embed.set_author(
                name=self.bot.user.display_name,
                icon_url=self.bot.user.avatar_url
            )
            embed.set_image(
                url=await api_call(
                    "https://nekos.life/api/v2/img/fox_girl"
                )
            )

            await ctx.reply(embed=embed, mention_author=False)
        else:
            await ctx.reply(
                "This command can only be used in a NSFW channel.",
                mention_author=False
            )

    @commands.cooldown(1, 5, commands.BucketType.user)
    @hentai.command(name="lewdkitsune", aliases=["lewdk"])
    @commands.is_nsfw()
    @commands.guild_only()
    async def lewdkitsune(self, ctx):
        """Lewdkitsune hentai!"""
        if ctx.channel.is_nsfw():
            embed = discord.Embed(
                title="Lewddd",
                color=ctx.message.author.color,
            )
            embed.set_footer(
                text=f"Requested by {ctx.message.author.display_name}",
                icon_url=ctx.message.author.avatar_url,
            )
            embed.set_author(
                name=self.bot.user.display_name,
                icon_url=self.bot.user.avatar_url
            )
            embed.set_image(
                url=await api_call(
                    "https://nekos.life/api/v2/img/lewdk"
                )
            )

            await ctx.reply(embed=embed, mention_author=False)
        else:
            await ctx.reply(
                "This command can only be used in a NSFW channel.",
                mention_author=False
            )

    @commands.cooldown(1, 5, commands.BucketType.user)
    @hentai.command()
    @commands.guild_only()
    @commands.is_nsfw()
    async def kuni(self, ctx):
        """Kuni Hentai!"""
        if ctx.channel.is_nsfw():
            embed = discord.Embed(
                title="",
                color=ctx.message.author.color,
            )
            embed.set_footer(
                text=f"Requested by {ctx.message.author.display_name}",
                icon_url=ctx.message.author.avatar_url,
            )
            embed.set_author(
                name=self.bot.user.display_name,
                icon_url=self.bot.user.avatar_url
            )
            embed.set_image(
                url=await api_call(
                    "https://nekos.life/api/v2/img/kuni"
                )
            )

            await ctx.reply(embed=embed, mention_author=False)
        else:
            await ctx.reply(
                "This command can only be used in a NSFW channel.",
                mention_author=False
            )

    @commands.cooldown(1, 5, commands.BucketType.user)
    @hentai.command()
    @commands.guild_only()
    @commands.is_nsfw()
    async def femdom(self, ctx):
        """femdom hentai"""
        if ctx.channel.is_nsfw():
            embed = discord.Embed(
                title="",
                color=ctx.message.author.color,
            )
            embed.set_footer(
                text=f"Requested by {ctx.message.author.display_name}",
                icon_url=ctx.message.author.avatar_url,
            )
            embed.set_author(
                name=self.bot.user.display_name,
                icon_url=self.bot.user.avatar_url
            )
            embed.set_image(
                url=await api_call(
                    "https://nekos.life/api/v2/img/femdom"
                )
            )

            await ctx.reply(embed=embed, mention_author=False)
        else:
            await ctx.reply(
                "This command can only be used in a NSFW channel.",
                mention_author=False
            )

    @commands.cooldown(1, 5, commands.BucketType.user)
    @hentai.command()
    @commands.is_nsfw()
    @commands.guild_only()
    async def erofeet(self, ctx):
        """Erofeet 3"""
        if ctx.channel.is_nsfw():
            embed = discord.Embed(
                title="",
                color=ctx.message.author.color,
            )
            embed.set_footer(
                text=f"Requested by {ctx.message.author.display_name}",
                icon_url=ctx.message.author.avatar_url,
            )
            embed.set_author(
                name=self.bot.user.display_name,
                icon_url=self.bot.user.avatar_url
            )
            embed.set_image(
                url=await api_call(
                    "https://nekos.life/api/v2/img/erofeet"
                )
            )

            await ctx.reply(embed=embed, mention_author=False)
        else:
            await ctx.reply(
                "This command can only be used in a NSFW channel.",
                mention_author=False
            )

    @commands.cooldown(1, 5, commands.BucketType.user)
    @hentai.command()
    @commands.guild_only()
    @commands.is_nsfw()
    async def solo(self, ctx):
        """Solo Porn"""
        if ctx.channel.is_nsfw():
            embed = discord.Embed(
                title="",
                color=ctx.message.author.color,
            )
            embed.set_footer(
                text=f"Requested by {ctx.message.author.display_name}",
                icon_url=ctx.message.author.avatar_url,
            )
            embed.set_author(
                name=self.bot.user.display_name,
                icon_url=self.bot.user.avatar_url
            )
            embed.set_image(
                url=await api_call(
                    "https://nekos.life/api/v2/img/solog"
                    )
                )

            await ctx.reply(embed=embed, mention_author=False)
        else:
            await ctx.reply(
                "This command can only be used in a NSFW channel.",
                mention_author=False
            )

    @commands.cooldown(1, 5, commands.BucketType.user)
    @hentai.command(name="gasm", aliases=["orgasm", "orgy"])
    @commands.is_nsfw()
    @commands.guild_only()
    async def gasm(self, ctx):
        """Gasm Porn"""
        if ctx.channel.is_nsfw():
            embed = discord.Embed(
                title="",
                color=ctx.message.author.color,
            )
            embed.set_footer(
                text=f"Requested by {ctx.message.author.display_name}",
                icon_url=ctx.message.author.avatar_url,
            )
            embed.set_author(
                name=self.bot.user.display_name,
                icon_url=self.bot.user.avatar_url
            )
            embed.set_image(
                url=await api_call(
                    "https://nekos.life/api/v2/img/gasm"
                )
            )

            await ctx.reply(embed=embed, mention_author=False)
        else:
            await ctx.reply(
                "This command can only be used in a NSFW channel.",
                mention_author=False
            )

    @commands.cooldown(1, 5, commands.BucketType.user)
    @hentai.command()
    @commands.is_nsfw()
    @commands.guild_only()
    async def yuri(self, ctx):
        """Yuri Porn"""
        if ctx.channel.is_nsfw():
            embed = discord.Embed(
                title="",
                color=ctx.author.color,
            )
            embed.set_footer(
                text=f"Requested by {ctx.author.display_name}",
                icon_url=ctx.author.avatar_url,
            )
            embed.set_author(
                name=self.bot.user.display_name,
                icon_url=self.bot.user.avatar_url
            )
            embed.set_image(
                url=await api_call(
                    "https://nekos.life/api/v2/img/yuri"
                )
            )

            await ctx.reply(embed=embed, mention_author=False)
        else:
            await ctx.reply(
                "This command can only be used in a NSFW channel.",
                mention_author=False
            )

    @commands.cooldown(1, 5, commands.BucketType.user)
    @hentai.command()
    @commands.is_nsfw()
    @commands.guild_only()
    async def anal(self, ctx):
        """Anal Hentai"""
        if ctx.channel.is_nsfw():
            embed = discord.Embed(
                title="",
                color=ctx.author.color,
            )
            embed.set_footer(
                text=f"Requested by {ctx.author.display_name}",
                icon_url=ctx.author.avatar_url,
            )
            embed.set_author(
                name=self.bot.user.display_name,
                icon_url=self.bot.user.avatar_url
            )
            embed.set_image(
                url=await api_call(
                    "https://nekos.life/api/v2/img/anal"
                )
                )

            await ctx.reply(embed=embed, mention_author=False)
        else:
            await ctx.reply(
                "This command can only be used in a NSFW channel.",
                mention_author=False
            )

    @commands.cooldown(3, 7, commands.BucketType.user)
    @hentai.command(name="ass", aliases=["hentaiass", "hass"])
    @commands.is_nsfw()
    @commands.guild_only()
    async def ass(self, ctx):
        """Ass Hentai"""
        if ctx.channel.is_nsfw():
            response = await api_call(
                "https://nekobot.xyz/api/image?type=hass",
                True
                )
            embed = discord.Embed(
                title="Big ass",
                color=response["color"],
            )

            embed.set_footer(
                text=f"Requested by {ctx.author.display_name}",
                icon_url=ctx.author.avatar_url,
            )
            embed.set_author(
                name=self.bot.user.display_name,
                icon_url=self.bot.user.avatar_url
            )

            embed.set_image(url=response["message"])
            await ctx.reply(embed=embed, mention_author=False)
        else:
            await ctx.reply(
                "This command can only be used in a NSFW channel.",
                mention_author=False
            )

    @commands.cooldown(3, 7, commands.BucketType.user)
    @real.command(name="porn", aliases=["pgif"])
    @commands.is_nsfw()
    @commands.guild_only()
    async def porn(self, ctx):
        """Just Porn"""
        if ctx.channel.is_nsfw():
            response = await api_call(
                "https://nekobot.xyz/api/image?type=pgif",
                True
            )
            embed = discord.Embed(
                title="Real porn",
                color=response["color"],
            )

            embed.set_footer(
                text=f"Requested by {ctx.author.display_name}",
                icon_url=ctx.author.avatar_url,
            )
            embed.set_author(
                name=self.bot.user.display_name,
                icon_url=self.bot.user.avatar_url
            )

            embed.set_image(url=response["message"])
            await ctx.reply(embed=embed, mention_author=False)
        else:
            await ctx.reply(
                "This command can only be used in a NSFW channel.",
                mention_author=False
            )

    @commands.cooldown(3, 7, commands.BucketType.user)
    @real.command(name="4k")
    @commands.is_nsfw()
    @commands.guild_only()
    async def fourk(self, ctx):
        """4K Hentai"""
        if ctx.channel.is_nsfw():
            response = await api_call(
                "https://nekobot.xyz/api/image?type=4k",
                True
            )
            embed = discord.Embed(
                title="The best quality",
                color=response["color"],
            )

            embed.set_footer(
                text=f"Requested by {ctx.author.display_name}",
                icon_url=ctx.author.avatar_url,
            )
            embed.set_author(
                name=self.bot.user.display_name,
                icon_url=self.bot.user.avatar_url
            )

            embed.set_image(url=response["message"])
            await ctx.reply(embed=embed, mention_author=False)
        else:
            await ctx.reply(
                "This command can only be used in a NSFW channel.",
                mention_author=False
            )

    @commands.cooldown(3, 7, commands.BucketType.user)
    @hentai.command(name="yaoi")
    @commands.is_nsfw()
    @commands.guild_only()
    async def yaoi(self, ctx):
        """yaoi hentai"""
        if ctx.channel.is_nsfw():
            response = await api_call(
                "https://nekobot.xyz/api/image?type=yaoi",
                True
            )
            embed = discord.Embed(
                title="Yaoi",
                color=response["color"],
            )

            embed.set_footer(
                text=f"Requested by {ctx.author.display_name}",
                icon_url=ctx.author.avatar_url,
            )
            embed.set_author(
                name=self.bot.user.display_name,
                icon_url=self.bot.user.avatar_url
            )

            embed.set_image(url=response["message"])
            await ctx.reply(embed=embed, mention_author=False)
        else:
            await ctx.reply(
                "This command can only be used in a NSFW channel.",
                mention_author=False
            )

    @commands.cooldown(3, 7, commands.BucketType.user)
    @real.command(name="thigh", aliases=["thighs"])
    @commands.is_nsfw()
    @commands.guild_only()
    async def thigh(self, ctx):
        """Thigh Hentai"""
        if ctx.channel.is_nsfw():
            response = await api_call(
                "https://nekobot.xyz/api/image?type=thigh",
                True
            )
            embed = discord.Embed(
                title="Them thic thighs",
                color=response["color"],
            )

            embed.set_footer(
                text=f"Requested by {ctx.author.display_name}",
                icon_url=ctx.author.avatar_url,
            )
            embed.set_author(
                name=self.bot.user.display_name,
                icon_url=self.bot.user.avatar_url
            )

            embed.set_image(url=response["message"])
            await ctx.reply(embed=embed, mention_author=False)
        else:
            await ctx.reply(
                "This command can only be used in a NSFW channel.",
                mention_author=False
            )

#    @real.command()
#    @commands.guild_only()
#    @commands.cooldown(1, 5, commands.BucketType.user)
#    async def pussy(self, ctx: commands.Context):
#        """Shows some pussy images from reddit.
#
#        Images shown are taken from r/pussy.
#        """
#        async with aiohttp.ClientSession() as session:
#            async with session.get(
#                "https://api.martinebot.com/v1/images/subreddit?name=pussy"
#            ) as resp:
#                origin = await resp.json()
#                data = origin["data"]
#                title = data["title"]
#                url = data["image_url"]
#                link = data["post_url"]
#                ups = data["upvotes"]
#                comments = data["comments"]
#                downvotes = data["downvotes"]
#                created_at = data["created_at"]
#
#                if data["subreddit"]:
#                    subreddit = data["subreddit"]
#                    sub_name = subreddit["name"]
#                    sub_url = subreddit["url"]
#
#                else:
#                    subreddit = ""
#                    sub_name = "Unknown"
#                    sub_url = ""
#
#                if data["author"]:
#                    author = data["author"]
#                    r_author = author["name"]
#                    r_author_url = author["url"]
#
#                else:
#                    author = ""
#                    r_author = "Unknown"
#                    r_author_url = ""
#
#        embed = discord.Embed(
#            title="Here's a random image...:frame_photo:",
#            colour=discord.Colour.random(),
#            description=(
#                "**Post by:** [u/{}]({})\n"
#                "**From:** [r/{}]({})\n"
#                "**This post was created on:** <t:{}:F>\n"
#                "**Title:** [{}]({})"
#            ).format(
#                r_author,
#                r_author_url,
#                sub_name,
#                sub_url,
#                created_at,
#                title,
#                link,
#            ),
#        )
#        embed.set_image(url=url)
#        embed.set_footer(
#            text="👍  {} • 👎  {} • 💬  {} • martinebot.com API".format(
#                ups,
#                downvotes,
#                comments,
#            ),
#            icon_url=ctx.message.author.avatar_url,
#        )
#        await session.close()
#        await ctx.trigger_typing()
#        await ctx.reply(
#            embed=embed,
#            mention_author=False,
#        )
