from gis.settings import DEBUG
from bot.models import Usersbot, Konfbot

def user(mess):
    if mess.chat.type == 'private':
        users = mess.from_user
        a = Usersbot.objects.filter(id = users.id)
        if len(a) == 0:
            temp = Usersbot(id = users.id, username = users.username,
                            last_name = users.last_name, first_name = users.first_name)
            temp.save()
            b = ['reg', temp.role]
        else:
            b = ['exist', a[0].role]
        return b
    else:
        konf = mess.chat
        a = Konfbot.objects.filter(id = konf.id)
        if len(a) == 0:
            temp = Konfbot(id = konf.id, name = konf.title)
            temp.save()
            b = ['reg', temp.role]
        else:
            b = ['exist', a[0].role]
        return b
