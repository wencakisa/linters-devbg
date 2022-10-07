import random
from utils import get_title
from datetime import datetime

tools = [
    'flake8', "isort", 'black']


selected_tool = random.choice(tools)

title = get_title()


def get_today(arg):
    today = datetime.now().date()
    return today


print(f'{title} - {selected_tool}')
