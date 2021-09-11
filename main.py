###
# Copyright 2021 tomGER, git@tomger.eu
#
# Licensed under the EUPL, Version 1.2 or – as soon they will be approved by the European Commission - subsequent versions of the EUPL (the "Licence");
# You may not use this work except in compliance with theLicence.
#
# You may obtain a copy of the Licence at: https://joinup.ec.europa.eu/software/page/eupl
#
# Unless required by applicable law or agreed to in writing, software distributed under the Licence is distributed on an "AS IS" basis,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the Licence for the specific language governing permissions and limitations under the Licence.
###

import discord

import config

from discord.ext import commands
from dislash import InteractionClient, Option, OptionType

from clues import clues

bot = commands.Bot(command_prefix="!")
# test_guilds exists because I can't be bothered to have to wait 3 years for discord to accept slash-commands
inter_client = InteractionClient(bot, test_guilds=[335895133805477889, 364791892635811840])

desc = "Gives a clue for /r/game"
option = [Option("level", "Specify the level to give the hint for", OptionType.STRING, required=True)]

@inter_client.slash_command(description = desc, options = option)
async def hint(ctx, level):
    if level in clues.keys():
        message = clues[level]
    else:
        message = "Couldn't find the level you were searching for - Are you sure that you typed it correctly?"
    await ctx.send(message)
    
# Dislash doesn't support aliases yet - So sadly this is our current solution
@inter_client.slash_command(description = desc, options = option)
async def level(ctx, level):
    await hint(ctx, level)
    
bot.run(config.token)
