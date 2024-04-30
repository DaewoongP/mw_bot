import time
import All
import random


def init_question(questions):
    with open('fiveseconds.txt', 'r') as file:
        for line in file:
            sentence = line.strip().split('\n')
            questions.append(sentence)


def start(client, commands, discord):
    five_list = dict()  # map과 같은 동작
    questions = list()  # 문제 리스트

    @client.hybrid_command(name="5초준다", with_app_command=True, description="5초준다 참여")
    async def fiveseconds(ctx: commands.Context):
        embed = discord.Embed(title='🎉 ```5초준다 참여!```', color=random.choice(All.colors))
        embed.set_thumbnail(
            url='https://cdn.discordapp.com/attachments/957612748978683914/960483064197296168/unknown_2.png')
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar)
        embed.add_field(name='등록완료!', value=f'<@{ctx.message.author.id}>', inline=False)
        await ctx.send(embed=embed)

        five_list[f'{ctx.message.author.display_name}'] = 0

        for key, value in five_list.items():
            print(key, value)

    @client.hybrid_command(name="5초등록", with_app_command=True, description="5초준다 등록")
    async def fiveregist(ctx: commands.Context, *, question):
        with open('fiveseconds.txt', 'a') as f:
            f.write(question + '\n')

        init_question(questions)

    @client.hybrid_command(name="5초문제", with_app_command=True, description="5초준다 시작")
    async def fivestart(ctx: commands.Context):
        await ctx.message.delete()

        if len(questions) == 0:
            init_question(questions)

        embed = discord.Embed(title='```3가지를 작성!```', color=random.choice(All.colors))
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar)
        embed.add_field(name=random.choice(questions), value='', inline=False)
        question_embed = await ctx.send(embed=embed)

        check_second = 5
        second_edit = await ctx.send(f'남은시간 : {check_second}초')
        for i in range(5):
            content_string = f'남은시간 : {check_second - i - 1}초'
            await second_edit.edit(content=content_string)
            time.sleep(1)

        await question_embed.delete()
        await second_edit.delete()

    @client.hybrid_command(name="점수증가", with_app_command=True, description="5초준다 참여")
    async def up(ctx: commands.Context):
        five_list[f'{ctx.message.author.display_name}'] += 1
