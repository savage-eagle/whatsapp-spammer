import time, json, random, sys

from whatsapp import WhatsApp
from datetime import datetime

import core.function as functions

users_sent = {}
users_json = "users_sent.json"

def loaded_previous_messages():
	with open(users_json, encoding="utf-8") as json_file:
		data = json_file.read()
		try:
			loaded = json.loads(data)
		except:
			print("Falha para carregar os arquivos")
			sys.exit(1)

		users_sent = loaded

def save_users_sent():
	with open(users_json, 'w', encoding="utf-8") as f:
		json.dump(users_sent, f, indent=4, ensure_ascii=False)

def main():
	users = None
	with open("users_phone.json", encoding="utf-8") as json_file:
		data = json_file.read()
		users = json.loads(data)
	
	if not users:
		print("Sem usuários")
		return False

	whatsapp = WhatsApp(30, session="project")
	count = 0
	for user in users:
		full_name = user["full_name"].lower()
		last_purchase = user["last_purchase"]
		
		explode_name = full_name.split(" ")
		try:
			first_name = explode_name[0].capitalize()
		except:
			first_name = full_name.capitalize()

		saved_contact_name = first_name + " " + last_purchase
		if users_sent.get(saved_contact_name):
			continue

		found_number = False

		start = int(datetime.now().timestamp())
		while True:
			if start + 5 < int(datetime.now().timestamp()):
				break
			
			whatsapp.clear_text_box()
			whatsapp.type_in_box(saved_contact_name)
			chat_name = whatsapp.get_user_chat_name()

			if chat_name == saved_contact_name:
				found_number = True
				break

			time.sleep(1)

		if not found_number:
			functions.printValues("O Chat não estava no nome de " + str(saved_contact_name) + " então saímos.")
			continue

		try:
			whatsapp.send_message(saved_contact_name, "gwerghwea")
		except:
			functions.printValues("Falha para enviar a mensagem para " + str(saved_contact_name) + ".")
			continue

		users_sent[saved_contact_name] = start

		count = count + 1
		functions.printValues("[MENSAGEM ENVIADA] - %s foi enviado a mensagem. Mensagem de número %d" % (saved_contact_name, count))
		save_users_sent()
		time.sleep(random.randint(5, 15))

functions.printValues("Robô iniciado")
loaded_previous_messages()
main()