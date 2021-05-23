import asyncio
import discord

from modules import SubmoduleHandler, BotModule


def command(func):
    setattr(func, "__discord_command", True)
    return func


class DiscordBot(SubmoduleHandler):
    def __init__(self, prefix, *args, **kwargs):
        self.prefix = prefix
        self.module = BotModule()
        self.modules = [self.module]

        self.commands = {}
        self.aliases = {}

        super().__init__(self.modules)

    def add(self, module_or_name):
        if type(module_or_name) is str:
            module_name = module_or_name
            raw_module = __import__(module_name)
            assert hasattr(raw_module, "__all__"), f"{module_name} it not a valid discordlib module"
            for module_attr in raw_module.__all__:
                if issubclass(module_attr, BotModule) or isinstance(module_attr, BotModule):
                    module = module_attr
                    break
            else:
                raise AssertionError(f"{module_name} is not a valid discordlib module")
        else:
            module_or_module_class = module_or_name
            if module_or_module_class.__class__ is type:
                module = module_or_module_class()
            else:
                module = module_or_module_class

        module: BotModule
        module.bot = self
        module.on_added()

        self.modules.append(module)

        self.commands |= module.commands
        self.aliases |= module.aliases

    def event(self, coro):
        setattr(self.module, coro.__name__, coro)
        assert asyncio.iscoroutinefunction(coro), "event registered must be a coroutine function"
        return coro

    def command(self, func):
        return self.module.command(func)

    def alias(self, command_name, alias):
        self.module.alias(command_name, alias)

    async def on_message(self, msg: discord.Message):
        if msg.content.startswith(self.prefix):
            await self.handle_command_content(msg, msg.content[len(self.prefix):])

        await super().on_message(msg)

    async def handle_command_content(self, msg: discord.Message, command_content):
        command_name, *space_separated_args = command_content.split(" ")
        # raw_args = " ".join(space_separated_args)

        if command_name in self.commands:
            await self.commands[command_name](msg, space_separated_args)

