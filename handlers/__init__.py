from handlers import login
from handlers.teacher_material_dir import announcement_add_material, add_material, add_additional_material, \
    delete_material, view_material, edit_material
from handlers.teacher_task_dir import view_task, add_task, delete_task, edit_task
from handlers.student_material_dir import add_material, delete_material, view_material, edit_material

from handlers import choose_announcement
from handlers import announcement

from handlers import disciplines
from handlers import tests
from handlers import marks
from handlers.register_dir import teacher_register, student_register, admin_register
from handlers.tests import test_json_decoder

from handlers import poll_delete
from handlers import poll_view
from handlers import choose_poll
from handlers import poll_announcement

