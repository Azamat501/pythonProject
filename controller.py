import text
import view
import model


def start():
    while True:
       choice = view.main_menu()
       match choice:
           case 1:
              model.open_pb()
              view.print_message(text.load_successful)





