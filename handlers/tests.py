from aiogram.dispatcher.filters import Text
from aiogram import types, Dispatcher
from handlers import test_json_decoder
from handlers.login import UserRoles
user_data = {}
user_task = {}
user_answersave = {}
answerstring = ""
question = []
numofquestions = []
question_value = []
answervarA = []
answervarB = []
answervarC = []
answervarD = []

def get_keyboard(num: int, line):
    if test_json_decoder.MyClass.num2 == 0:
        if num == 0:
            buttons = [types.InlineKeyboardButton(text="Choose", callback_data="ans_Ch1"),
                       types.InlineKeyboardButton(text="->", callback_data="ans_Next")]
            keyboard = types.InlineKeyboardMarkup(row_width=2)
            keyboard.add(*buttons)
            return keyboard
        elif num != test_json_decoder.MyClass.num3:
            buttons = [types.InlineKeyboardButton(text="<-", callback_data="ans_Previous"),
                       types.InlineKeyboardButton(text="Choose", callback_data="ans_Ch1"),
                       types.InlineKeyboardButton(text="->", callback_data="ans_Next")]
            keyboard = types.InlineKeyboardMarkup(row_width=3)
            keyboard.add(*buttons)
            return keyboard
        else:
            buttons = [types.InlineKeyboardButton(text="<-", callback_data="ans_Previous"),
                       types.InlineKeyboardButton(text="Choose", callback_data="ans_Ch1")]
            keyboard = types.InlineKeyboardMarkup(row_width=2)
            keyboard.add(*buttons)
            return keyboard
    elif test_json_decoder.MyClass.num2 == 1:
        if num == 0:
            buttons = [types.InlineKeyboardButton(text="Choose", callback_data="ans_Ch2"),
                       types.InlineKeyboardButton(text="->", callback_data="ans_Next")]
            keyboard = types.InlineKeyboardMarkup(row_width=2)
            keyboard.add(*buttons)
            return keyboard
        elif num != test_json_decoder.MyClass.num3:
            buttons = [types.InlineKeyboardButton(text="<-", callback_data="ans_Previous"),
                       types.InlineKeyboardButton(text="Choose", callback_data="ans_Ch2"),
                       types.InlineKeyboardButton(text="->", callback_data="ans_Next")]
            keyboard = types.InlineKeyboardMarkup(row_width=3)
            keyboard.add(*buttons)
            return keyboard
        else:
            buttons = [types.InlineKeyboardButton(text="<-", callback_data="ans_Previous"),
                       types.InlineKeyboardButton(text="Choose", callback_data="ans_Ch2")]
            keyboard = types.InlineKeyboardMarkup(row_width=2)
            keyboard.add(*buttons)
            return keyboard
    elif test_json_decoder.MyClass.num2 == 5:
        buttons = [types.InlineKeyboardButton(text="Choose", callback_data="ans_Ch2")]
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(*buttons)
        return keyboard
    else:
        if str(line)[num] == '_':
            if num == 0:
                if numofquestions[0] == 2:
                    buttons = [types.InlineKeyboardButton(text="A", callback_data="ans_A"),
                               types.InlineKeyboardButton(text="B", callback_data="ans_B"),
                               types.InlineKeyboardButton(text="Next", callback_data="ans_Next")]
                    keyboard = types.InlineKeyboardMarkup(row_width=2)
                    keyboard.add(*buttons)
                    return keyboard
                elif numofquestions[0] == 3:
                    buttons = [types.InlineKeyboardButton(text="A", callback_data="ans_A"),
                               types.InlineKeyboardButton(text="B", callback_data="ans_B"),
                               types.InlineKeyboardButton(text="C", callback_data="ans_C"),
                               types.InlineKeyboardButton(text="Next", callback_data="ans_Next")]
                    keyboard = types.InlineKeyboardMarkup(row_width=3)
                    keyboard.add(*buttons)
                    return keyboard
                else:
                    buttons = [types.InlineKeyboardButton(text="A", callback_data="ans_A"),
                               types.InlineKeyboardButton(text="B", callback_data="ans_B"),
                               types.InlineKeyboardButton(text="C", callback_data="ans_C"),
                               types.InlineKeyboardButton(text="D", callback_data="ans_D"),
                               types.InlineKeyboardButton(text="Next", callback_data="ans_Next")]
                    keyboard = types.InlineKeyboardMarkup(row_width=4)
                    keyboard.add(*buttons)
                    return keyboard
            elif num != len(answerstring) - 1:
                if numofquestions[num] == 2:
                    buttons = [types.InlineKeyboardButton(text="A", callback_data="ans_A"),
                               types.InlineKeyboardButton(text="B", callback_data="ans_B"),
                               types.InlineKeyboardButton(text="Previous", callback_data="ans_Previous"),
                               types.InlineKeyboardButton(text="Next", callback_data="ans_Next")]
                    keyboard = types.InlineKeyboardMarkup(row_width=2)
                    keyboard.add(*buttons)
                    return keyboard
                elif numofquestions[num] == 3:
                    buttons = [types.InlineKeyboardButton(text="A", callback_data="ans_A"),
                               types.InlineKeyboardButton(text="B", callback_data="ans_B"),
                               types.InlineKeyboardButton(text="C", callback_data="ans_C"),
                               types.InlineKeyboardButton(text="Previous", callback_data="ans_Previous"),
                               types.InlineKeyboardButton(text="Next", callback_data="ans_Next")]
                    keyboard = types.InlineKeyboardMarkup(row_width=3)
                    keyboard.add(*buttons)
                    return keyboard
                else:
                    buttons = [types.InlineKeyboardButton(text="A", callback_data="ans_A"),
                               types.InlineKeyboardButton(text="B", callback_data="ans_B"),
                               types.InlineKeyboardButton(text="C", callback_data="ans_C"),
                               types.InlineKeyboardButton(text="D", callback_data="ans_D"),
                               types.InlineKeyboardButton(text="Previous", callback_data="ans_Previous"),
                               types.InlineKeyboardButton(text="Next", callback_data="ans_Next")]
                    keyboard = types.InlineKeyboardMarkup(row_width=4)
                    keyboard.add(*buttons)
                    return keyboard
            else:
                if numofquestions[num] == 2:
                    buttons = [types.InlineKeyboardButton(text="A", callback_data="ans_A"),
                               types.InlineKeyboardButton(text="B", callback_data="ans_B"),
                               types.InlineKeyboardButton(text="Previous", callback_data="ans_Previous"),
                               types.InlineKeyboardButton(text="End", callback_data="ans_End")]
                    keyboard = types.InlineKeyboardMarkup(row_width=2)
                    keyboard.add(*buttons)
                    return keyboard
                elif numofquestions[num] == 3:
                    buttons = [types.InlineKeyboardButton(text="A", callback_data="ans_A"),
                               types.InlineKeyboardButton(text="B", callback_data="ans_B"),
                               types.InlineKeyboardButton(text="C", callback_data="ans_C"),
                               types.InlineKeyboardButton(text="Previous", callback_data="ans_Previous"),
                               types.InlineKeyboardButton(text="End", callback_data="ans_End")]
                    keyboard = types.InlineKeyboardMarkup(row_width=3)
                    keyboard.add(*buttons)
                    return keyboard
                else:
                    buttons = [types.InlineKeyboardButton(text="A", callback_data="ans_A"),
                               types.InlineKeyboardButton(text="B", callback_data="ans_B"),
                               types.InlineKeyboardButton(text="C", callback_data="ans_C"),
                               types.InlineKeyboardButton(text="D", callback_data="ans_D"),
                               types.InlineKeyboardButton(text="Previous", callback_data="ans_Previous"),
                               types.InlineKeyboardButton(text="End", callback_data="ans_End")]
                    keyboard = types.InlineKeyboardMarkup(row_width=4)
                    keyboard.add(*buttons)
                    return keyboard
        else:
            if num == 0:
                buttons = [types.InlineKeyboardButton(text="Change answer", callback_data="ans_Change"),
                           types.InlineKeyboardButton(text="Next", callback_data="ans_Next")]
                keyboard = types.InlineKeyboardMarkup(row_width=2)
                keyboard.add(*buttons)
                return keyboard
            elif num != len(answerstring) - 1:
                buttons = [types.InlineKeyboardButton(text="Change answer", callback_data="ans_Change"),
                           types.InlineKeyboardButton(text="Previous", callback_data="ans_Previous"),
                           types.InlineKeyboardButton(text="Next", callback_data="ans_Next")]
                keyboard = types.InlineKeyboardMarkup(row_width=3)
                keyboard.add(*buttons)
                return keyboard
            else:
                buttons = [types.InlineKeyboardButton(text="Change answer", callback_data="ans_Change"),
                           types.InlineKeyboardButton(text="Previous", callback_data="ans_Previous"),
                           types.InlineKeyboardButton(text="End", callback_data="ans_End")]
                keyboard = types.InlineKeyboardMarkup(row_width=3)
                keyboard.add(*buttons)
                return keyboard

async def cmd_numbers(message: types.Message):
    user_data[message.from_user.id] = 0
    user_task[message.from_user.id] = 0
    stringstr = ""
    user_answersave[message.from_user.id] = stringstr
    test_json_decoder.MyClass.num3 = len(test_json_decoder.subject_list) - 1
    await message.answer("Оберіть назву предмета\n" + "\nПоточний предмет: " + test_json_decoder.subject_list[0], reply_markup=get_keyboard(0, stringstr))

async def update_num_text(message: types.Message, task_number: int, user_savedans):
    #Оновлення тексту питань
    if test_json_decoder.MyClass.num2 == 0:
        await message.edit_text("Оберіть назву предмета\n" + "\nПоточний предмет: " + test_json_decoder.subject_list[task_number], reply_markup=get_keyboard(task_number, user_savedans))
    elif test_json_decoder.MyClass.num2 == 1 or test_json_decoder.MyClass.num2 == 5:
        await message.edit_text("Оберіть номер тесту\n" + "\nПоточний тест: " + str(task_number + 1), reply_markup=get_keyboard(task_number, user_savedans))
    elif numofquestions[task_number] == 2:
        await message.edit_text("Питання " + str(task_number + 1) + "\n" + question[task_number] + "\nОберіть відповідь: \n" + answervarA[task_number] + "\n" + answervarB[task_number], reply_markup=get_keyboard(task_number, user_savedans))
    elif numofquestions[task_number] == 3:
        await message.edit_text("Питання " + str(task_number + 1) + "\n" + question[task_number] + "\nОберіть відповідь: \n" + answervarA[task_number] + "\n" + answervarB[task_number] + "\n" + answervarC[task_number], reply_markup=get_keyboard(task_number, user_savedans))
    else:
        await message.edit_text("Питання " + str(task_number + 1) + "\n" + question[task_number] + "\nОберіть відповідь: \n" + answervarA[task_number] + "\n" + answervarB[task_number] + "\n" + answervarC[task_number] + "\n" + answervarD[task_number], reply_markup=get_keyboard(task_number, user_savedans))

async def callbacks_num(call: types.CallbackQuery):
    user_value = user_data.get(call.from_user.id, 0)
    user_tasknumber = user_task.get(call.from_user.id, 0)
    user_savedans = user_answersave.get(call.from_user.id, 0)
    action = call.data.split("_")[1]
    if action == "Ch1":
        test_json_decoder.MyClass.num2 = int(1)
        test_json_decoder.MyClass.subject = str(test_json_decoder.subject_list[user_tasknumber])
        user_task[call.from_user.id] = 0
        await test_json_decoder.count_tests(test_json_decoder.MyClass.subject)
        if (test_json_decoder.MyClass.numoftests == 1):
            test_json_decoder.MyClass.num2 = int(5)
        else:
            test_json_decoder.MyClass.num3 = int(test_json_decoder.MyClass.numoftests) - 1
        await update_num_text(call.message, 0, user_savedans)
    elif action == "Ch2":
        test_json_decoder.MyClass.num2 = int(2)
        test_json_decoder.MyClass.numoftest = user_tasknumber
        user_task[call.from_user.id] = 0
        await test_json_decoder.get_info()
        stringstr = ""
        for i in range(0, len(answerstring)):
            stringstr = stringstr + "_"
        user_answersave[call.from_user.id] = stringstr
        await update_num_text(call.message, 0, stringstr)
    elif action == "A" or action == "B" or action == "C" or action == "D":
        stringstr = user_savedans
        stringstr = stringstr[:user_tasknumber] + str(action) + stringstr[user_tasknumber + 1:]
        user_answersave[call.from_user.id] = stringstr
        await update_num_text(call.message, user_tasknumber, stringstr)
    elif action == "Next":
        user_task[call.from_user.id] = user_tasknumber + 1
        await update_num_text(call.message, user_tasknumber + 1, user_savedans)
    elif action == "Previous":
        user_task[call.from_user.id] = user_tasknumber - 1
        await update_num_text(call.message, user_tasknumber - 1, user_savedans)
    elif action == "Change":
        stringstr = user_savedans
        stringstr = stringstr[:user_tasknumber] + "_" + stringstr[user_tasknumber + 1:]
        user_answersave[call.from_user.id] = stringstr
        await update_num_text(call.message, user_tasknumber, stringstr)
    else:
        for i in range(0, len(answerstring)):
            if user_savedans[i] == answerstring[i]:
                user_value = user_value + question_value[i]
        await call.message.edit_text(f"Сума балів: {user_value}")
    await call.answer()




def register_handlers_tests(dp: Dispatcher):
    dp.register_message_handler(cmd_numbers, lambda message: message.text == "Тести", state=UserRoles.teacher)
    # dp.register_message_handler(cmd_numbers, commands="choose")
    dp.register_callback_query_handler(callbacks_num, Text(startswith="ans_"))