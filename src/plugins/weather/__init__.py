from nonebot import on_command, CommandSession

from .data_source import get_weather_of_city
from .utils import Robot



@on_command('weather', aliases=('主题', '话题', '议题'), only_to_me=False)
async def weather(session: CommandSession):
    city = session.get('city', prompt='想生成的话题是什么？')
    weather_report = await get_weather_of_city(city)
    await session.send(weather_report)


@weather.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            robot = Robot()
            issue = robot.create_issue(stripped_arg)
            session.state['city'] = str(issue.number)
        return

    if not stripped_arg:
        session.pause('想生成的话题是什么，请重新输入')

    session.state[session.current_key] = stripped_arg


@on_command('comment', aliases=('#'), only_to_me=False)
async def comment(session: CommandSession):
    city = session.get('city', prompt='评论是什么')
    # await session.send("评论已经记录")


@comment.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            content = stripped_arg.split()
            issue_number = int(content[0])
            comment_content = "".join(content[1:]) 
            robot = Robot()
            issue = robot.create_comment_by_issue_number(issue_number,comment_content)
            session.state['city'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('想记录的东西是什么。')

    session.state[session.current_key] = stripped_arg