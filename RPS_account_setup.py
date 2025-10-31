print("------------------------------------------")
print("🤘rock,", "✋paper,", "✂scissor,", "🧾Account,", "🛠setup")
print("------------------------------------------")
while True:
  username = input("Pick your username: ")
  password = input("Pick your password: ")
  password_confirm = input("Confirm your password: ")
  if password != password_confirm:
      print("Passwords do not match. Please try again.")
  if password == password_confirm:
      print("Account created successfully!")
      text_file = open("accounts.txt", "a")
      # text_file.write(",")
      # text_file.write(username)
      # text_file.write(",")
      # text_file.write(password)
      # text_file.write("\n")
      text_file.write(username + "\n" + password + "\n")
      text_file.close()
      break
