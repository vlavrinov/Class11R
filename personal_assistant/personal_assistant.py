import json
import csv
import os
import datetime
import re

class Note:
    def __init__(self, id, title, content="", timestamp=None):
        self.id = id
        self.title = title
        self.content = content
        self.timestamp = timestamp or datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")

class Task:
    def __init__(self, id, title, description="", done=False, priority="Средний", due_date=None):
        self.id = id
        self.title = title
        self.description = description
        self.done = done
        self.priority = priority
        self.due_date = due_date

class Contact:
    def __init__(self, id, name, phone="", email=""):
        self.id = id
        self.name = name
        self.phone = phone
        self.email = email

class FinanceRecord:
    def __init__(self, id, amount, category, date, description=""):
        self.id = id
        self.amount = amount
        self.category = category
        self.date = date
        self.description = description


class PersonalAssistant:
    def __init__(self):
        self.notes = self.load_data("notes.json", Note)
        self.tasks = self.load_data("tasks.json", Task)
        self.contacts = self.load_data("contacts.json", Contact)
        self.finances = self.load_data("finance.json", FinanceRecord)
        self.next_note_id = 1 if not self.notes else max(note.id for note in self.notes) + 1
        self.next_task_id = 1 if not self.tasks else max(task.id for task in self.tasks) + 1
        self.next_contact_id = 1 if not self.contacts else max(contact.id for contact in self.contacts) + 1
        self.next_finance_id = 1 if not self.finances else max(finance.id for finance in self.finances) + 1


    def load_data(self, filename, data_class):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                data = json.load(f)
                return [data_class(**item) for item in data]
        except FileNotFoundError:
            return []

    def save_data(self, filename, data):
        with open(filename, "w", encoding="utf-8") as f:
            json.dump([vars(item) for item in data], f, indent=4, ensure_ascii=False)



    def main_menu(self):
        while True:
            print("\nДобро пожаловать в Персональный помощник!")
            print("Выберите действие:")
            print("1. Управление заметками")
            print("2. Управление задачами")
            print("3. Управление контактами")
            print("4. Управление финансовыми записями")
            print("5. Калькулятор")
            print("6. Выход")

            choice = input("Ваш выбор: ")

            if choice == '1':
                self.notes_menu()
            elif choice == '2':
                self.tasks_menu()
            elif choice == '3':
                self.contacts_menu()
            elif choice == '4':
                self.finance_menu()
            elif choice == '5':
                self.calculator()
            elif choice == '6':
                print("До свидания!")
                break
            else:
                print("Неверный выбор. Попробуйте снова.")

    def notes_menu(self):
        while True:
            print("\nУправление заметками:")
            print("1. Создать заметку")
            print("2. Просмотреть заметки")
            print("3. Редактировать заметку")
            print("4. Удалить заметку")
            print("5. Импорт из CSV")
            print("6. Экспорт в CSV")
            print("7. Назад")

            choice = input("Ваш выбор: ")
            if choice == '1':
                self.add_note()
            elif choice == '2':
                self.view_notes()
            elif choice == '3':
                self.edit_note()
            elif choice == '4':
                self.delete_note()
            elif choice == '5':
                self.import_notes_csv()
            elif choice == '6':
                self.export_notes_csv()

            if choice == '7':
                break


    def tasks_menu(self):
         while True:
            print("\nУправление задачами:")
            print("1. Добавить задачу")
            print("2. Просмотреть задачи")
            print("3. Отметить задачу как выполненную")
            print("4. Редактировать задачу")
            print("5. Удалить задачу")
            print("6. Экспорт в CSV")
            print("7. Импорт из CSV")
            print("8. Назад")

            choice = input("Ваш выбор: ")
            if choice == '1':
                self.add_task()
            elif choice == '2':
                self.view_tasks()
            elif choice == '3':
                self.mark_task_done()
            elif choice == '4':
                self.edit_task()
            elif choice == '5':
                self.delete_task()
            elif choice == '6':
                self.export_tasks_csv()
            elif choice == '7':
                self.import_tasks_csv()

            if choice == '8':
                break

    def contacts_menu(self):
        while True:
            print("\nУправление контактами:")
            print("1. Добавить контакт")
            print("2. Поиск контакта")  # Add search functionality
            print("3. Редактировать контакт")
            print("4. Удалить контакт")
            print("5. Экспорт в CSV")
            print("6. Импорт из CSV")
            print("7. Назад")

            choice = input("Ваш выбор: ")
            if choice == '1':
                self.add_contact()
            elif choice == '2':
                self.search_contact()
            elif choice == '3':
                self.edit_contact()
            elif choice == '4':
                self.delete_contact()
            elif choice == '5':
                self.export_contacts_csv()
            elif choice == '6':
                self.import_contacts_csv()

            if choice == '7':
                break


    def finance_menu(self):
         while True:
            print("\nУправление финансами:")
            print("1. Добавить запись")
            print("2. Просмотреть записи")
            print("3. Сгенерировать отчет")
            print("4. Удалить запись")
            print("5. Экспорт в CSV")
            print("6. Импорт из CSV")
            print("7. Назад")

            choice = input("Ваш выбор: ")
            if choice == '1':
                self.add_finance_record()
            elif choice == '2':
                self.view_finance_records()
            elif choice == '3':
                self.generate_report()
            elif choice == '4':
                self.delete_finance_record()
            elif choice == '5':
                self.export_finances_csv()
            elif choice == '6':
                self.import_finances_csv()

            if choice == '7':
                break

    def calculator(self):
        try:
            expression = input("Введите выражение: ")
            result = eval(expression) # Use eval() carefully. Consider safer alternatives for user input.
            print("Результат:", result)
        except (ValueError, ZeroDivisionError, SyntaxError) as e:
            print(f"Ошибка: {e}")
        except Exception as e:  # Catching other potential errors
            print(f"Непредвиденная ошибка: {e}")

    def export_notes_csv(self):
        if not self.notes:
            print("Нет заметок для экспорта.")
            return

        with open("notes.csv", "w", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["id", "title", "content", "timestamp"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for note in self.notes:
                writer.writerow({
                    "id": note.id,
                    "title": note.title,
                    "content": note.content,
                    "timestamp": note.timestamp
                })
        print("Заметки экспортированы в notes.csv")

    def import_notes_csv(self):
        try:
            with open("notes.csv", "r", encoding="utf-8") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    note = Note(int(row["id"]), row["title"], row["content"], row["timestamp"])
                    self.notes.append(note)
                    self.next_note_id = max(self.next_note_id, int(row["id"]) + 1)
            self.save_data("notes.json", self.notes)
            print("Заметки импортированы из notes.csv")
        except FileNotFoundError:
            print("Файл notes.csv не найден.")
        except Exception as e:
            print(f"Ошибка при импорте: {e}")

    def view_notes(self):
        if not self.notes:
            print("Нет заметок.")
            return
        for note in self.notes:
            print(f"ID: {note.id}, Заголовок: {note.title}, Дата: {note.timestamp}")
            print(f"Текст: {note.content}\n")

    def edit_note(self):
        self.view_notes()
        try:
            note_id = int(input("Введите ID заметки для редактирования: "))
            note = next((note for note in self.notes if note.id == note_id), None)
            if note:
                new_title = input("Введите новый заголовок заметки: ")
                new_content = input("Введите новый текст заметки: ")
                note.title = new_title
                note.content = new_content
                note.timestamp = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                self.save_data("notes.json", self.notes)
                print("Заметка отредактирована!")
            else:                print("Заметка с таким ID не найдена.")
        except ValueError:
            print("Неверный формат ID. Попробуйте снова.")
    def delete_note(self):
        self.view_notes()
        try:
            note_id = int(input("Введите ID заметки для удаления: "))
            note = next((note for note in self.notes if note.id == note_id), None)
            if note:
                self.notes.remove(note)
                self.save_data("notes.json", self.notes)
                print("Заметка удалена!")
            else:
                print("Заметка с таким ID не найдена.")
        except ValueError:
            print("Неверный формат ID. Попробуйте снова.")

    def add_task(self):
        title = input("Введите название задачи: ")
        description = input("Введите описание задачи: ")
        priority = input("Введите приоритет задачи (Высокий, Средний, Низкий): ")
        due_date_str = input("Введите срок выполнения задачи (ДД-ММ-ГГГГ): ")
        try:
            due_date = datetime.datetime.strptime(due_date_str, "%d-%m-%Y").strftime("%d-%m-%Y")
        except ValueError:
            due_date = None
            print("Неверный формат даты. Дата не будет сохранена.")
        task = Task(self.next_task_id, title, description, False, priority, due_date)
        self.tasks.append(task)
        self.next_task_id += 1
        self.save_data("tasks.json", self.tasks)
        print("Задача добавлена!")

    def view_tasks(self):
        if not self.tasks:
            print("Нет задач.")
            return
        for task in self.tasks:
            status = "Выполнено" if task.done else "Не выполнено"
            print(f"ID: {task.id}, Заголовок: {task.title}, Статус: {status}, Приоритет: {task.priority}")
            if task.due_date:
                print(f"Срок: {task.due_date}")
            print(f"Описание: {task.description}\n")

    def mark_task_done(self):
        self.view_tasks()
        try:
            task_id = int(input("Введите ID задачи для выполнения: "))
            task = next((task for task in self.tasks if task.id == task_id), None)
            if task:
                task.done = True                
                self.save_data("tasks.json", self.tasks)
                print("Задача отмечена как выполненная!")
            else:
                print("Задача с таким ID не найдена.")
        except ValueError:
            print("Неверный формат ID. Попробуйте снова.")

    def edit_task(self):
        self.view_tasks()
        try:
            task_id = int(input("Введите ID задачи для редактирования: "))
            task = next((task for task in self.tasks if task.id == task_id), None)
            if task:
                new_title = input("Введите новый заголовок задачи: ")
                new_description = input("Введите новое описание задачи: ")
                new_priority = input("Введите новый приоритет задачи (Высокий, Средний, Низкий): ")
                new_due_date_str = input("Введите новый срок выполнения задачи (ДД-ММ-ГГГГ): ")
                try:
                    new_due_date = datetime.datetime.strptime(new_due_date_str, "%d-%m-%Y").strftime("%d-%m-%Y")
                except ValueError:
                    new_due_date = None
                    print("Неверный формат даты. Дата не будет изменена.")
                task.title = new_title
                task.description = new_description
                task.priority = new_priority
                task.due_date = new_due_date
                self.save_data("tasks.json", self.tasks)
                print("Задача отредактирована!")
            else:
                print("Задача с таким ID не найдена.")
        except ValueError:
            print("Неверный формат ID. Попробуйте снова.")

    def delete_task(self):
        self.view_tasks()
        try:
            task_id = int(input("Введите ID задачи для удаления: "))
            task = next((task for task in self.tasks if task.id == task_id), None)
            if task:
                self.tasks.remove(task)
                self.save_data("tasks.json", self.tasks)
                print("Задача удалена!")
            else:
                print("Задача с таким ID не найдена.")
        except ValueError:
            print("Неверный формат ID. Попробуйте снова.")

    def add_contact(self):
        name = input("Введите имя контакта: ")
        phone = input("Введите номер телефона: ")
        email = input("Введите email: ")
        contact = Contact(self.next_contact_id, name, phone, email)
        self.contacts.append(contact)
        self.next_contact_id += 1
        self.save_data("contacts.json", self.contacts)
        print("Контакт добавлен!")

    def search_contact(self):
        search_term = input("Введите имя или часть имени контакта для поиска: ")
        results = [contact for contact in self.contacts if search_term.lower() in contact.name.lower()]
        if results:
            for contact in results:
                print(f"ID: {contact.id}, Имя: {contact.name}, Телефон: {contact.phone}, Email: {contact.email}")
        else:
            print("Контакты не найдены.")

    def edit_contact(self):
        self.view_contacts()
        try:
            contact_id = int(input("Введите ID контакта для редактирования: "))
            contact = next((contact for contact in self.contacts if contact.id == contact_id), None)
            if contact:
                new_name = input("Введите новое имя контакта: ")
                new_phone = input("Введите новый номер телефона: ")
                new_email = input("Введите новый email: ")
                contact.name = new_name
                contact.phone = new_phone
                contact.email = new_email
                self.save_data("contacts.json", self.contacts)
                print("Контакт отредактирован!")
            else:
                print("Контакт с таким ID не найден.")
        except ValueError:
            print("Неверный формат ID. Попробуйте снова.")

    def delete_contact(self):
        self.view_contacts()
        try:
            contact_id = int(input("Введите ID контакта для удаления: "))
            contact = next((contact for contact in self.contacts if contact.id == contact_id), None)
            if contact:
                self.contacts.remove(contact)
                self.save_data("contacts.json", self.contacts)
                print("Контакт удален!")
            else:
                print("Контакт с таким ID не найден.")
        except ValueError:
            print("Неверный формат ID. Попробуйте снова.")

    def view_contacts(self):
        if not self.contacts:
            print("Нет контактов.")
            return
        for contact in self.contacts:
            print(f"ID: {contact.id}, Имя: {contact.name}, Телефон: {contact.phone}, Email: {contact.email}")

    def add_finance_record(self):
        amount = float(input("Введите сумму: "))
        category = input("Введите категорию: ")
        date_str = input("Введите дату (ДД-ММ-ГГГГ): ")
        description = input("Введите описание (необязательно): ")
        try:
            date = datetime.datetime.strptime(date_str, "%d-%m-%Y").strftime("%d-%m-%Y")
        except ValueError:
            print("Неверный формат даты. Используйте формат ДД-ММ-ГГГГ.")
            return
        record = FinanceRecord(self.next_finance_id, amount, category, date, description)
        self.finances.append(record)
        self.next_finance_id += 1
        self.save_data("finance.json", self.finances)
        print("Финансовая запись добавлена!")

    def view_finance_records(self):
        if not self.finances:
            print("Нет финансовых записей.")
            return
        for record in self.finances:
            print(f"ID: {record.id}, Сумма: {record.amount}, Категория: {record.category}, Дата: {record.date}, Описание: {record.description}")

    def generate_report(self):
        if not self.finances:
            print("Нет финансовых записей для генерации отчета.")
            return
        total_expenses = sum(record.amount for record in self.finances)
        print(f"\nОбщая сумма расходов: {total_expenses}")
        categories = {}
        for record in self.finances:
            category = record.category
            amount = record.amount
            if category not in categories:
                categories[category] = 0
            categories[category] += amount
        print("\nРасходы по категориям:")
        for category, amount in categories.items():
            print(f"{category}: {amount}")


    def delete_finance_record(self):
        self.view_finance_records()
        try:
            record_id = int(input("Введите ID записи для удаления: "))
            record = next((record for record in self.finances if record.id == record_id), None)
            if record:
                self.finances.remove(record)
                self.save_data("finance.json", self.finances)
                print("Финансовая запись удалена!")
            else:
                print("Запись с таким ID не найдена.")
        except ValueError:
            print("Неверный формат ID. Попробуйте снова.")

    def export_finances_csv(self):
        if not self.finances:
            print("Нет финансовых записей для экспорта.")
            return

        with open("finances.csv", "w", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["id", "amount", "category", "date", "description"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for record in self.finances:
                writer.writerow({
                    "id": record.id,
                    "amount": record.amount,
                    "category": record.category,
                    "date": record.date,
                    "description": record.description
                })
        print("Финансовые записи экспортированы в finances.csv")

    def import_finances_csv(self):
        try:
            with open("finances.csv", "r", encoding="utf-8") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    record = FinanceRecord(int(row["id"]), float(row["amount"]), row["category"], row["date"], row["description"])
                    self.finances.append(record)
                    self.next_finance_id = max(self.next_finance_id, int(row["id"]) + 1)
            self.save_data("finance.json", self.finances)
            print("Финансовые записи импортированы из finances.csv")
        except FileNotFoundError:
            print("Файл finances.csv не найден.")
        except Exception as e:
            print(f"Ошибка при импорте: {e}")

    def export_tasks_csv(self):
        if not self.tasks:
            print("Нет задач для экспорта.")
            return

        with open("tasks.csv", "w", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["id", "title", "description", "done", "priority", "due_date"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for task in self.tasks:
                writer.writerow({
                    "id": task.id,
                    "title": task.title,
                    "description": task.description,
                    "done": task.done,
                    "priority": task.priority,
                    "due_date": task.due_date
                })
        print("Задачи экспортированы в tasks.csv")

    def import_tasks_csv(self):
        try:
            with open("tasks.csv", "r", encoding="utf-8") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    task = Task(int(row["id"]), row["title"], row["description"], row["done"] == "True", row["priority"], row["due_date"])
                    self.tasks.append(task)
                    self.next_task_id = max(self.next_task_id, int(row["id"]) + 1)
            self.save_data("tasks.json", self.tasks)
            print("Задачи импортированы из tasks.csv")
        except FileNotFoundError:
            print("Файл tasks.csv не найден.")
        except Exception as e:
            print(f"Ошибка при импорте: {e}")

    def export_contacts_csv(self):
        if not self.contacts:
            print("Нет контактов для экспорта.")
            return

        with open("contacts.csv", "w", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["id", "name", "phone", "email"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for contact in self.contacts:
                writer.writerow({
                    "id": contact.id,
                    "name": contact.name,
                    "phone": contact.phone,
                    "email": contact.email
                })
        print("Контакты экспортированы в contacts.csv")

    def import_contacts_csv(self):
        try:
            with open("contacts.csv", "r", encoding="utf-8") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    contact = Contact(int(row["id"]), row["name"], row["phone"], row["email"])
                    self.contacts.append(contact)
                    self.next_contact_id = max(self.next_contact_id, int(row["id"]) + 1)
            self.save_data("contacts.json", self.contacts)
            print("Контакты импортированы из contacts.csv")
        except FileNotFoundError:
            print("Файл contacts.csv не найден.")
        except Exception as e:
            print(f"Ошибка при импорте: {e}")

    def add_note(self):
        title = input("Введите заголовок заметки: ")
        content = input("Введите текст заметки: ")
        note = Note(self.next_note_id, title, content)
        self.notes.append(note)
        self.next_note_id += 1
        self.save_data("notes.json", self.notes)
        print("Заметка добавлена!")
        
    def run(self):
        self.main_menu()




    
if __name__ == "__main__":
    assistant = PersonalAssistant()
    assistant.run()
