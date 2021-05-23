import discord


class SubmoduleHandler(discord.Client):
    def __init__(self, submodules):
        self.submodules = submodules

        super().__init__()

    async def on_connect(self):
        for module in self.submodules:
            await module.on_connect()

    async def on_shard_connect(self, shard_id):
        for module in self.submodules:
            await module.on_shard_connect(shard_id)

    async def on_disconnect(self):
        for module in self.submodules:
            await module.on_disconnect()

    async def on_shard_disconnect(self, shard_id):
        for module in self.submodules:
            await module.on_shard_disconnect(shard_id)

    async def on_ready(self):
        for module in self.submodules:
            await module.on_ready()

    async def on_shard_ready(self, shard_id):
        for module in self.submodules:
            await module.on_shard_ready(shard_id)

    async def on_resumed(self):
        for module in self.submodules:
            await module.on_resumed()

    async def on_shard_resumed(self, shard_id):
        for module in self.submodules:
            await module.on_shard_resumed(shard_id)

    async def on_socket_raw_receive(self, msg):
        for module in self.submodules:
            await module.on_socket_raw_receive(msg)

    async def on_socket_raw_send(self, payload):
        for module in self.submodules:
            await module.on_socket_raw_send(payload)

    async def on_typing(self, channel, user, when):
        for module in self.submodules:
            await module.on_typing(channel, user, when)

    async def on_message(self, msg: discord.Message):
        for module in self.submodules:
            await module.on_message(msg)

    async def on_message_delete(self, msg: discord.Message):
        for module in self.submodules:
            await module.on_message_delete(msg)

    async def on_bulk_message_delete(self, msgs: discord.Message):
        for module in self.submodules:
            await module.on_bulk_message_delete(msgs)

    async def on_raw_message_delete(self, payload):
        for module in self.submodules:
            await module.on_raw_message_delete(payload)

    async def on_raw_bulk_message_delete(self, payload):
        for module in self.submodules:
            await module.on_raw_bulk_message_delete(payload)

    async def on_message_edit(self, before: discord.Message, after: discord.Message):
        for module in self.submodules:
            await module.on_message_edit(before, after)

    async def on_raw_message_edit(self, payload):
        for module in self.submodules:
            await module.on_raw_message_edit(payload)

    async def on_reaction_add(self, reaction, user):
        for module in self.submodules:
            await module.on_reaction_add(reaction, user)

    async def on_raw_reaction_add(self, payload):
        for module in self.submodules:
            await module.on_raw_reaction_add(payload)

    async def on_reaction_remove(self, reaction, user):
        for module in self.submodules:
            await module.on_reaction_remove(reaction, user)

    async def on_raw_reaction_remove(self, payload):
        for module in self.submodules:
            await module.on_raw_reaction_remove(payload)

    async def on_reaction_clear(self, msg: discord.Message, reactions):
        for module in self.submodules:
            await module.on_reaction_clear(msg, reactions)

    async def on_raw_reaction_clear(self, payload):
        for module in self.submodules:
            await module.on_raw_reaction_clear(payload)

    async def on_reaction_clear_emoji(self, reaction):
        for module in self.submodules:
            await module.on_reaction_clear_emoji(reaction)

    async def on_raw_reaction_clear_emoji(self, payload):
        for module in self.submodules:
            await module.on_raw_reaction_clear_emoji(payload)

    async def on_private_channel_delete(self, channel):
        for module in self.submodules:
            await module.on_private_channel_delete(channel)

    async def on_private_channel_create(self, channel):
        for module in self.submodules:
            await module.on_private_channel_create(channel)

    async def on_private_channel_update(self, before, after):
        for module in self.submodules:
            await module.on_private_channel_update(before, after)

    async def on_private_channel_pins_update(self, channel, last_pin):
        for module in self.submodules:
            await module.on_private_channel_pins_update(channel, last_pin)

    async def on_guild_channel_delete(self, channel):
        for module in self.submodules:
            await module.on_guild_channel_delete(channel)

    async def on_guild_channel_create(self, channel):
        for module in self.submodules:
            await module.on_guild_channel_create(channel)

    async def on_guild_channel_update(self, before, after):
        for module in self.submodules:
            await module.on_guild_channel_update(before, after)

    async def on_guild_channel_pins_update(self, channel, last_pin):
        for module in self.submodules:
            await module.on_guild_channel_pins_update(channel, last_pin)

    async def on_guild_integrations_update(self, guild):
        for module in self.submodules:
            await module.on_guild_integrations_update(guild)

    async def on_webhooks_update(self, channel):
        for module in self.submodules:
            await module.on_webhooks_update(channel)

    async def on_member_join(self, member):
        for module in self.submodules:
            await module.on_member_join(member)

    async def on_member_remove(self, member):
        for module in self.submodules:
            await module.on_member_remove(member)

    async def on_member_update(self, before, after):
        for module in self.submodules:
            await module.on_member_update(before, after)

    async def on_user_update(self, before, after):
        for module in self.submodules:
            await module.on_user_update(before, after)

    async def on_guild_join(self, guild):
        for module in self.submodules:
            await module.on_guild_join(guild)

    async def on_guild_remove(self, guild):
        for module in self.submodules:
            await module.on_guild_remove(guild)

    async def on_guild_update(self, before, after):
        for module in self.submodules:
            await module.on_guild_update(before, after)

    async def on_guild_role_create(self, role):
        for module in self.submodules:
            await module.on_guild_role_create(role)

    async def on_guild_role_delete(self, role):
        for module in self.submodules:
            await module.on_guild_role_delete(role)

    async def on_guild_role_update(self, before, after):
        for module in self.submodules:
            await module.on_guild_role_update(before, after)

    async def on_guild_emojis_update(self, guild, before, after):
        for module in self.submodules:
            await module.on_guild_emojis_update(guild, before, after)

    async def on_guild_available(self, guild):
        for module in self.submodules:
            await module.on_guild_available(guild)

    async def on_guild_unavailable(self, guild):
        for module in self.submodules:
            await module.on_guild_unavailable(guild)

    async def on_voice_state_update(self, member, before, after):
        for module in self.submodules:
            await module.on_voice_state_update(member, before, after)

    async def on_member_ban(self, guild, user):
        for module in self.submodules:
            await module.on_member_ban(guild, user)

    async def on_member_unban(self, guild, user):
        for module in self.submodules:
            await module.on_member_unban(guild, user)

    async def on_invite_create(self, invite):
        for module in self.submodules:
            await module.on_invite_create(invite)

    async def on_invite_delete(self, invite):
        for module in self.submodules:
            await module.on_invite_delete(invite)

    async def on_group_join(self, channel, user):
        for module in self.submodules:
            await module.on_group_join(channel, user)

    async def on_group_remove(self, channel, user):
        for module in self.submodules:
            await module.on_group_remove(channel, user)

    async def on_relationship_add(self, relationship):
        for module in self.submodules:
            await module.on_relationship_add(relationship)

    async def on_relationship_remove(self, relationship):
        for module in self.submodules:
            await module.on_relationship_remove(relationship)

    async def on_relationship_update(self, before, after):
        for module in self.submodules:
            await module.on_relationship_update(before, after)


class BotModule:
    commands = {}
    aliases = {}

    @staticmethod
    def command(func):
        return command(func)

    def alias(self, command_name, alias):
        self.aliases[alias] = command_name

    def on_added(self):
        for attr_name in dir(self):
            attr = getattr(self, attr_name)
            if callable(attr) and hasattr(attr, "__discord_command"):
                self.commands[attr.__name__] = attr

    async def on_connect(self):
        pass

    async def on_shard_connect(self, shard_id):
        pass

    async def on_disconnect(self):
        pass

    async def on_shard_disconnect(self, shard_id):
        pass

    async def on_ready(self):
        pass

    async def on_shard_ready(self, shard_id):
        pass

    async def on_resumed(self):
        pass

    async def on_shard_resumed(self, shard_id):
        pass

    async def on_socket_raw_receive(self, msg):
        pass

    async def on_socket_raw_send(self, payload):
        pass

    async def on_typing(self, channel, user, when):
        pass

    async def on_message(self, msg: discord.Message):
        pass

    async def on_message_delete(self, msg: discord.Message):
        pass

    async def on_bulk_message_delete(self, msgs: discord.Message):
        pass

    async def on_raw_message_delete(self, payload):
        pass

    async def on_raw_bulk_message_delete(self, payload):
        pass

    async def on_message_edit(self, before: discord.Message, after: discord.Message):
        pass

    async def on_raw_message_edit(self, payload):
        pass

    async def on_reaction_add(self, reaction, user):
        pass

    async def on_raw_reaction_add(self, payload):
        pass

    async def on_reaction_remove(self, reaction, user):
        pass

    async def on_raw_reaction_remove(self, payload):
        pass

    async def on_reaction_clear(self, msg: discord.Message, reactions):
        pass

    async def on_raw_reaction_clear(self, payload):
        pass

    async def on_reaction_clear_emoji(self, reaction):
        pass

    async def on_raw_reaction_clear_emoji(self, payload):
        pass

    async def on_private_channel_delete(self, channel):
        pass

    async def on_private_channel_create(self, channel):
        pass

    async def on_private_channel_update(self, before, after):
        pass

    async def on_private_channel_pins_update(self, channel, last_pin):
        pass

    async def on_guild_channel_delete(self, channel):
        pass

    async def on_guild_channel_create(self, channel):
        pass

    async def on_guild_channel_update(self, before, after):
        pass

    async def on_guild_channel_pins_update(self, channel, last_pin):
        pass

    async def on_guild_integrations_update(self, guild):
        pass

    async def on_webhooks_update(self, channel):
        pass

    async def on_member_join(self, member):
        pass

    async def on_member_remove(self, member):
        pass

    async def on_member_update(self, before, after):
        pass

    async def on_user_update(self, before, after):
        pass

    async def on_guild_join(self, guild):
        pass

    async def on_guild_remove(self, guild):
        pass

    async def on_guild_update(self, before, after):
        pass

    async def on_guild_role_create(self, role):
        pass

    async def on_guild_role_delete(self, role):
        pass

    async def on_guild_role_update(self, before, after):
        pass

    async def on_guild_emojis_update(self, guild, before, after):
        pass

    async def on_guild_available(self, guild):
        pass

    async def on_guild_unavailable(self, guild):
        pass

    async def on_voice_state_update(self, member, before, after):
        pass

    async def on_member_ban(self, guild, user):
        pass

    async def on_member_unban(self, guild, user):
        pass

    async def on_invite_create(self, invite):
        pass

    async def on_invite_delete(self, invite):
        pass

    async def on_group_join(self, channel, user):
        pass

    async def on_group_remove(self, channel, user):
        pass

    async def on_relationship_add(self, relationship):
        pass

    async def on_relationship_remove(self, relationship):
        pass

    async def on_relationship_update(self, before, after):
        pass
