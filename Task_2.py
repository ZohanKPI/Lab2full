class FileWorker:

  @staticmethod
  def CreateAndFillFile():
    with open('myfile.txt', 'w') as f:
      f.write('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')

  @staticmethod
  def ReadFile():
    with open('myfile.txt', 'r') as f:
      print(f.read())

  @staticmethod
  def CountLetters():
    counter = 0

    with open('myfile.txt', 'r') as f:
      text = f.read()
      for i in text:
        if i != " " or i != "," or i != ".":
          counter += 1

    print("[RESULT] Letters in file: %s" % counter)

  @staticmethod
  def CountSentences():
    sentences = []

    with open('myfile.txt', 'r') as f:
      text = f.read()
      sentences = text.split(".")

    print("[RESULT] Sentences in file: %s" % len(sentences))

  @staticmethod
  def CountWords():
    words = []

    with open('myfile.txt', 'r') as f:
      text = f.read()
      words = text.split(" ")

    print("[RESULT] Words in file: %s" % len(words))


FileWorker.CreateAndFillFile()
FileWorker.ReadFile()
FileWorker.CountLetters()
FileWorker.CountWords()
FileWorker.CountSentences()