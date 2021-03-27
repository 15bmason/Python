await message.channel.send("How many seconds would you like to countdown from?")

        def check(reaction, user):
            return user == message.author and str(reaction.emoji) == '👍'

        msg = await client.wait_for(int)

        x = 0

        while x != msg:

            y = message.content - x

            await message.channel.send(y)

            x += 1 
