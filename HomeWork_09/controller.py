# -*- coding: cp1251 -*-

import view
import model
import text

def start():
    while True:
        choice = view.main_menu()

        match choice:
            case 1:

                model.open_pb()
                view.print_message(text.load_successful)

            case 2:

                model.save_pb()
                view.print_message(text.save_successful)

            case 3:

                pb = model.get_pb()
                view.print_contacts(pb, text.pb_empty)

            case 4:

                contact = view.input_contact(text.input_new_contact)
                name = model.add_contact(contact)
                view.print_message(text.new_contact_successfull(name))

            case 5:

                key_word = view.input_search(text.input_search)
                result = model.search_contact(key_word)
                view.print_contacts(result, text.empty_search(key_word))

            case 6:

                key_word = view.input_search(text.input_change)
                result = model.search_contact(key_word)
                if result:
                    if len(result) != 1:
                        view.print_contacts(result, '')
                        current_id = view.input_search(text.input_index)
                    else:
                        current_id = result[0].get('id')
                    view.print_contacts(result, '')
                    new_contact = view.input_contact(text.change_contact)
                    name = model.change_contact(new_contact, current_id)
                    view.print_message(text.change_succsessful(name))
                else:
                    view.print_message(text.empty_search(key_word))

            case 7:

                 key_word = view.input_search(text.input_delete)
                 result = model.search_contact(key_word)
                 if result:
                        if len(result) != 1:
                            view.print_contacts(result, '')
                            current_id = view.input_search(text.input_index)
                        else:
                            current_id = result[0].get('id')
                        view.print_contacts(result, '')                        
                        name = model.delete_contact(current_id)                    
                        view.print_message(text.delete_succsessful(name))
                 else:
                    view.print_message(text.empty_search(key_word))
                
            case 8:
                break
