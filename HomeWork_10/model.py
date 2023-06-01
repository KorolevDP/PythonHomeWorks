class PhoneBook:
    
    def __init__(self, path: str = 'phones.txt'):
        self._phone_book: list[dict[str, str]] = []
        self._path = path
        self._last_id = 0
                 

    def open(self):        
        with open(self._path, 'r', encoding = 'UTF-8') as file:
            data = file.readlines()
        for contact in data:
            contact = contact.strip().split(';')
            new = {'id': contact[0], 'name': contact[1], 'phone': contact[2], 'comment': contact[3]}
            self._phone_book.append(new)

    def save(self):        
        data = []
        for contact in self._phone_book:
            data.append('; '.join([value for value in contact.values()]))
        data = '\n'.join(data)
        with open(self._path, 'w', encoding = 'UTF-8') as file:
            file.write(data)

    def load(self):
        return self._phone_book

    def add(self, new: dict[str, str]) -> str:
        self._last_id += 1
        new['id'] = str(self._last_id)        
        self._phone_book.append(new)
        return new.get('name')

    def search(self, word: str) -> list[dict[str, str]]:
        result: list[dict[str, str]] = []
        for contact in self._phone_book:
            for field in contact.values():
                if word.lower() in field.lower():
                    result.append(contact)
                    break
        return result

    def change(self, new: dict, index: int | str) -> str:
        for contact in self._phone_book:
            if index == contact.get('id'):            
                contact['name'] = new.get('name', contact.get('name'))
                contact['phone'] = new.get('phone', contact.get('phone'))
                contact['comment'] = new.get('comment', contact.get('comment'))
                return contact.get('name')

    def delete_contact( index: int) -> list[dict[str, str]]:
        global phone_book    

        del phone_book[index]
        return phone_book[index]

   
 #def add_contact(new: dict[str, str]) -> str:
 #   global phone_book
 #   new_id = int(phone_book[-1].get('id')) + 1
 #   new['id'] = str(new_id)
 #   phone_book.append(new)
 #   return new.get('name')