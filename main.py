import logging
import ssl

from aiohttp import web
from aiogram import executor, types
from handlers import login

from handlers import announcement

from handlers import choose_poll
from handlers import poll_view
from handlers import poll_announcement
from handlers import choose_announcement
from handlers import poll_delete

from handlers import disciplines
from handlers import tests
from handlers import marks, add_marks as t_marks

from handlers.register_dir import admin_register
from handlers.register_dir import teacher_register
from handlers.register_dir import student_register

from handlers.teacher_material_dir import add_material as t_add
from handlers.teacher_material_dir import add_additional_material as t_add_additional
from handlers.teacher_material_dir.announcement_add_material import send_message
from handlers.teacher_material_dir import edit_material as t_edit
from handlers.teacher_material_dir import delete_material as t_delete
from handlers.teacher_material_dir import view_material as t_view

from handlers.teacher_task_dir import view_task as t_view_task, add_task as t_add_task, delete_task as t_delete_task, edit_task as t_edit_task

from handlers.student_material_dir import add_material as s_add
from handlers.student_material_dir import edit_material as s_edit
from handlers.student_material_dir import delete_material as s_delete
from handlers.student_material_dir import view_material as s_view

from bot_create import dp, TOKEN_API, bot
from keyboard import first_keyboard
from user_role_files import teacher, student


###
import aioschedule
import asyncio

###
# teacher material
t_add.register_handlers_files(dp)
t_add_additional.register_handlers_files(dp)
t_edit.register_handlers_files(dp)
t_delete.register_handlers_files(dp)
t_view.register_handlers_files(dp)
# teacher tasks
t_add_task.register_handlers_tasks(dp)
t_view_task.register_handlers_tasks(dp)
t_delete_task.register_handlers_tasks(dp)
t_edit_task.register_handlers_tasks(dp)
#student tasks

# student material
s_add.register_handlers_files(dp)
s_edit.register_handlers_files(dp)
s_delete.register_handlers_files(dp)
s_view.register_handlers_files(dp)
# login and register
login.register_handlers_login(dp)
student_register.register_handlers_student_register(dp)
teacher_register.register_handlers_teacher_register(dp)
admin_register.register_handlers_admin_register(dp)
teacher.register_handlers_teacher(dp)
student.register_handlers_teacher(dp)

announcement.register_handlers_announcement(dp)
poll_announcement.register_handlers_poll_announcement(dp)
choose_announcement.register_handlers_choose_announcement(dp)
choose_poll.register_handlers_choose_poll(dp)
poll_view.register_handlers_poll_view(dp)
poll_delete.register_handlers_files(dp)

disciplines.register_handlers_disciplines(dp)
tests.register_handlers_tests(dp)
marks.register_handlers_marks(dp)
t_marks.register_handlers_marks(dp)

logging.basicConfig(level=logging.INFO)

WEBHOOK_HOST = '130.211.226.27'
WEBHOOK_PORT = 8443  # 443, 80, 88 or 8443 (port need to be 'open')
WEBHOOK_LISTEN = '0.0.0.0'  # In some VPS you may need to put here the IP addr

WEBHOOK_SSL_CERT = '../url_cert.pem'  # Path to the ssl certificate
WEBHOOK_SSL_PRIV = '../url_private.key'  # Path to the ssl private key


@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    await message.answer("Ласкаво прошу до StudyBot!", reply_markup=first_keyboard)


async def scheduler():
    aioschedule.every(60).seconds.do(send_message)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)


async def on_startup(_):
    asyncio.create_task(scheduler())

# if __name__ == '__main__':
#     executor.start_polling(dp, skip_updates=False, on_startup=on_startup)








# Quick'n'dirty SSL certificate generation:
#
# openssl genrsa -out webhook_pkey.pem 2048
# openssl req -new -x509 -days 3650 -key webhook_pkey.pem -out webhook_cert.pem
#
# When asked for "Common Name (e.g. server FQDN or YOUR name)" you should reply
# with the same value in you put in WEBHOOK_HOST

WEBHOOK_URL_BASE = "https://{}:{}".format(WEBHOOK_HOST, WEBHOOK_PORT)
WEBHOOK_URL_PATH = "/{}/".format(TOKEN_API)


app = web.Application()


# Process webhook calls
async def handle(request):
    # await on_startup()
    if request.match_info.get('token') == bot.token:
        request_body_dict = await request.json()
        update = types.Update.de_json(request_body_dict)
        bot.process_new_updates([update])
        return web.Response()
    else:
        return web.Response(status=403)


app.router.add_post('/{token}/', handle)



# Remove webhook, it fails sometimes the set if there is a previous webhook
# bot.remove_webhook()
# bot.delete_webhook()
#
# # Set webhook
# bot.set_webhook(url=WEBHOOK_URL_BASE + WEBHOOK_URL_PATH,
#                 certificate=open(WEBHOOK_SSL_CERT, 'r'))

# Build ssl context
context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_3)
context.load_cert_chain(WEBHOOK_SSL_CERT, WEBHOOK_SSL_PRIV)

# Start aiohttp server
web.run_app(
    app,
    host=WEBHOOK_LISTEN,
    port=WEBHOOK_PORT,
    ssl_context=context,
)